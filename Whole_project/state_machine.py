import libraries.nao_nocv_2_1 as nao
from time import sleep
from libraries.audio import speech_recog
from libraries.battery import detect_low_battery
from libraries.exceptions import *
import logging
from landmark_detection import search_landmark
from behavior_based_navigation_ch4 import moveToTarget
import math

DEBUG=True
logging.basicConfig(level=logging.INFO)


class StateMachine():
    def __init__(self):
        pass
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.ROBOT_IP=ROBOT_IP
        self.ROBOT_PORT=ROBOT_PORT
        # self.nao=nao
    #     pass
    def enter(self,*args,**kwargs):
        pass
    def exit(self,*args,**kwargs):
        pass

    def run(self,states_dict,**kwargs):
        return {"next":0}
    def __call__(self,states_dict,**kwargs):
        return self.run(states_dict,**kwargs)

class Blank(StateMachine):
    pass
class Wait(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.deteced=False
        if DEBUG:
            self.deteced=True
        pass
    def enter(self, *args, **kwargs):
        #TODO: face detection(while loop)
        return True
    def exit(self, *args, **kwargs):
        # return state
        if self.deteced:
            return {"next":2}
        else:
            return {"next":1}
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()

def do_posture_once(do_posture,base_posture,sleep_time=0.1):
    try:
        nao.GoToPosture(do_posture)
        nao.motionProxy.waitUntilMoveIsFinished()        
        nao.GoToPosture(base_posture)
        nao.motionProxy.waitUntilMoveIsFinished()
    except Exception,e:
        logging.debug("Exception: %s"%e)
        raise e
class Greeting(StateMachine):
    def __init__(self, ROBOT_IP, ROBOT_PORT, nao):
        self.ROBOT_IP=ROBOT_IP
        self.ROBOT_PORT=ROBOT_PORT

    def enter(self):
        logging.debug("State_2(GreetingMode): enter")
        pass

    def body(self,*args,**kwargs):
        nao.Say("Hello! Dear cusomer.")
        selection=None
        while(selection is None or selection=="NoResult"):
            self.show_selection()
            selection=self.get_selection()
        return selection

    def show_selection(self):
        nao.Say("May I offer you any service?")
        nao.Say("Yes or No?")
        do_posture_once("StandZero","Crouch")

    def get_selection(self):
        selection=None
        worldList=["Yes","No"]
        selection=speech_recog(worldList,10,"greeting")
        return selection

    def exit(self, *args, **kwargs):
        # Set the state machine to inital state
        self.selection=None

    def run(self,state_dict,**kwargs):
        self.enter()
        selection=self.body()
        print "robot:get selection: %s"%selection
        battery_low_level=detect_low_battery(self.ROBOT_IP,self.ROBOT_PORT)
        self.exit()
        if battery_low_level: raise BatteryLowException("20")
        if selection.upper() in ["YES"]: return {"next":3}
        if selection.upper() in ["NO"]:
            nao.Say("Thank you! Enjoy your day!")
            return {"next":1}
        raise NoResponseException("Greeting")


class Service_Selection(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.wordlist = ["Check in", "Check out", "other services"]
        self.nextphase = 0
        self.retry = 5
        
    def enter(self, *args, **kwargs):
        nao.Say("Which service would you like me to offer? Check in, Check out or other services")
        try:
            answer = speech_recog(self.wordlist)
            if answer == "NoResult":
                cnt = 0
                # try to get customer's selection again
                while cnt<self.retry and answer == "NoResult":
                    cnt += 1
                    nao.Say("Sorry, I can't understand what you said, could you repeat your selection again?")
                    answer = speech_recog(self.wordlist)
                if cnt==self.retry:
                    raise NoResponseException("check in")
            self.nextphase = self.wordlist.index(answer) + 4 # checkin:4 checkout:5 other:6
        except Exception,e:
            logging.error("State(Service Selection): Error: %s"%e)
            raise e
    def exit(self, *args, **kwargs):
        # return state
        if self.nextphase == 8:
            return {"next":self.nextphase, "error":"NoResponse"}
        return {"next":self.nextphase}
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()
        
class CheckIn(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.wordlist = ["done", "yes", "no"]
        self.nextphase = 0
        self.retry = 5
    def enter(self, *args, **kwargs):
        nao.Say("Please give me your personal ID, and when you done please say done to me.")
        try:
            answer = speech_recog(self.wordlist)
            # if answer == "NoResult" or not self.wordlist.index(answer) == 0:
            cnt = 0
            # try to get customer's selection again
            while (cnt<self.retry) and (answer == "NoResult" or not self.wordlist.index(answer) == 0):
                cnt += 1
                nao.Say("Sorry, I can't understand what you said, could you repeat your selection again?")
                answer = speech_recog(self.wordlist)
            if cnt==self.retry:
                raise NoResponseException("check in")
            if self.wordlist.index(answer) == 0:
                nao.Say("Please wait...Thank you! The Check in process is done, enjoy your room!")
            # for further service
            nao.Say("Still need other service?")
            answer = speech_recog(self.wordlist)
            if answer == "NoResult":
                cnt=0
                # try to get customer's selection again
                while cnt<self.retry and answer == "NoResult":
                    cnt += 1
                    answer = speech_recog(self.wordlist)
                if cnt==self.retry:
                    raise NoResponseException("check in")
            if self.wordlist.index(answer) == 1:
                self.nextphase = 6
            elif self.wordlist.index(answer) == 2:
                self.nextphase = 1
        except Exception,e:
            logging.error("State(CheckIn): Error: %s"%e)
            raise(e)
            # if DEBUG:
                # nao.Say("Please wait...Thank you! The Check in process is done, enjoy your room!")
                # nao.Say("Still need other service?")
                # self.nextphase = 6
                # return "Yes" #TODO: Changed in the development version
            # else:
                # self.nextphase = 8
                # return "NoResponse"
        return
    def exit(self, *args, **kwargs):
        # return state
        if self.nextphase == 8:
            return {"next":self.nextphase, "error":"NoResponse"}
        return {"next":self.nextphase}
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()
    
class CheckOut(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.nextphase = 0
    def enter(self, *args, **kwargs):
        nao.Say("Thanks for choosing our hotel! Have a nice day")
        self.nextphase = 1
    def exit(self, *args, **kwargs):
        # return state
        return {"next":self.nextphase}
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()

class OtherService(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.nextphase = 0
        self.wordlist = ["Gudie", "Alarm", "Taxi", "Reserve", "Nearby", "Info", "No", "Again"]
        self.retry = 5
        
    def ask_more_service(self):
        nao.Say("Still need other service?")
        optionlist = ["yes", "no"]
        try:
            answer = speech_recog(optionlist)
            if answer == "NoResult":
                cnt=0
                # try to get customer's selection again
                while cnt<self.retry and answer == "NoResult":
                    cnt += 1
                    answer = speech_recog(optionlist)
                if cnt==self.retry:
                    raise NoResponseException("other service")
            if answer == "yes":
                self.nextphase = 6
                return
            elif answer == "no":
                self.nextphase = 1
                return
        except Exception,e:
            logging.error("State(other serivce): Error: %s"%e)
            raise(e)

    def enter(self, *args, **kwargs):
        nao.Say("Dear customer, I can guide you to the elevator, set the alarm for tommorow, call a taxi, \
                reverve an available front desk, offer hotel info, share nearby attraction place")
        answer = speech_recog(self.wordlist)

        if answer == "No":
            nao.Say("Have a nice day!")
            self.nextphase = 1
            return
        if answer == "Again":
            self.nextphase=6
            return
        if answer == "Guide":
            self.nextphase=7
            return
        if answer == "Alarm":
            nao.Say("I have already set 7:00 at tommorow morning.")
            self.ask_more_service()
            return
        if answer == "Taxi":
            nao.Say("I have already called a taxi for you, please wait infront of the hotel gate.")
            self.nextphase=1
            return
        if answer == "Reserve":
            nao.Say("Number one front desk is available now")
            self.nextphase=1
            return
        if answer == "Nearby":
            nao.Say("I recommend you to visit Eindhoven JumpSquare!") # could use random sentence list
            self.ask_more_service()
            return
        if answer == "Info":
            nao.Say("We have GYM at 5th floor, Swimming pool on the roof.")
            self.ask_more_service()
            return
            
    def exit(self, *args, **kwargs):
        # return state
        return {"next":self.nextphase}
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()

class Guide(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.nextphase = 0
        self.wordlist = ["yes", "no"]
        self.retry = 5

    def navigation():
        nao.InitPose()
        nao.InitSonar()

        # find landmark
        try:
            find_landmark, markinfo = search_landmark(nao)
        except Exception,e:
            find_landmark = True
            nao.Walk(0,0, 0.3)
            nao.MoveHead(yaw_val = 0, pitch_val=0, isAbsolute =True)
        reach_landmark=False
        while (not reach_landmark):
            if(find_landmark):
                #print markinfo[0][3]
                moveToTarget(nao,5,0)
                [SL, SR]=nao.ReadSonar()
                if(SL < 1 and SR < 1):
                    reach_landmark = True
            else:
                nao.InitSonar(True)
                [SL, SR]=nao.ReadSonar()
                print SL, SR
                if(SL > 1 and SR > 1):
                    nao.Stiffen() # turns all motors on
                    moveToTarget(nao,0.5,0)
                    # nao.Walk(0.5, 0, 0) # move forward to find the landmark
                else:
            #         nao.Walk(0,0,math.pi) # turn around
                    while(SL<1 or SR<1):
                        nao.Move(0,0,0.349)
                        [SL, SR]=nao.ReadSonar()
                    moveToTarget(nao,0.5,0)
                    # nao.Walk(0.5, 0, 0)
                find_landmark, markinfo = search_landmark(nao)
                if(find_landmark==False):
            #         speaker = ALProxy(IP="marvin.local", proxy=[0], PORT = 9559) # may need to changed
                    nao.Say("I cannot find landmark!")
                    print "I cannot find landmark!"

    

    def enter(self, *args, **kwargs):
        nao.Say("Please follow me!")
        # navigation to landmark
        self.navigation()
        try:
            nao.Say("Still need other service?")
            answer = speech_recog(self.wordlist)
            if answer == "NoResult":
                cnt=0
                # try to get customer's selection again
                while cnt<self.retry and answer == "NoResult":
                    cnt += 1
                    nao.Say("Sorry, I can't understand what you said, could you repeat your selection again?")
                    answer = speech_recog(self.wordlist)
                if cnt == self.retry:
                    raise NoResponseException("guide")
            if answer=="yes":
                self.nextphase = 3
                return
            elif answer=="no":
                nao.Say("Have a nice day!")
                self.nextphase = 1
                return
        except Exception,e:
            logging.error("State(Guide): Error: %s"%e)
            raise(e)
    def exit(self, *args, **kwargs):
        # return state
        return {"next":self.nextphase}
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()

class Unexpected(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.nextphase = 0
        self.enterinfo = ""
        self.wordlist=["yes","no"]
    def enter(self, *args, **kwargs):
        if self.enterinfo == "NoResponse":
            nao.Say("Would you still like to ask for a service from me?")
            try:
                answer = speech_recog(self.wordlist)
                if answer == "NoResult":
                    cnt=0
                    # try to get customer's selection again
                    while cnt<self.retry and answer == "NoResult":
                        cnt += 1
                        nao.Say("Sorry, I can't understand what you said, could you repeat your selection again?")
                        answer = speech_recog(self.wordlist)
                if answer=="yes":
                    self.nextphase = 3
                elif answer=="no":
                    nao.Say("Have a nice day!")
                    self.nextphase = 1
                return
            except Exception,e:
                logging.error("State(Guide): Error: %s"%e)
                raise e
                
        if self.enterinfo == "LowBattery":
            nao.Say("Sorry dear coustomer, I need charge now.")
            self.nextphase = 0
            return

    def exit(self, *args, **kwargs):
        # return state
        pass
    def run(self,state_dict,**kwargs):
        return {"next":0}


__all__=[Blank,Wait,Greeting,Service_Selection,CheckIn,CheckOut,OtherService,Guide,Unexpected]