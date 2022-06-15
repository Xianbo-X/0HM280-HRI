import libraries.nao_nocv_2_1 as nao
from time import sleep
from libraries.audio import speech_recog
from libraries.battery import detect_low_battery
import logging
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
        nao.GotoPosture(do_posture)
        sleep(sleep_time)
        nao.GotoPosture(base_posture)
    except Exception,e:
        logging.debug("Exception: %s"%e)
        pass
class Greeting(StateMachine):
        
    def __init__(self, ROBOT_IP, ROBOT_PORT, nao):
        self.selection=None
        self.ROBOT_IP=ROBOT_IP
        self.ROBOT_PORT=ROBOT_PORT

    def enter(self):
        logging.debug("State_2(GreetingMode): enter")
        pass

    def body(self,*args,**kwargs):
        nao.Say("Hello! Dear cusomer.")
        selection=None
        try:
            while(selection is None or selection=="NoResult"):
                self.show_selection()
                selection=self.get_selection()
        except Exception,e:
            logging.error("State_2(GreetingMode): Error: %s"%e)
            if DEBUG:
                # selection="Yes" #TODO: Changed in the development version
                selection=input("Please choose weather get a service") #TODO: Changed in the development version
            else:
                selection="NoResponse"
        return selection

    def show_selection(self):
        nao.Say("May I offer you any service?")
        nao.Say("Yes or No?")
        do_posture_once("StandZero","Crouch")

    def get_selection(self):
        selection=None
        worldList=["Yes","No","Sure"]
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
        if battery_low_level:
            return {"next":8,"error":"LowBattery"}
        if selection=="Yes":
            return {"next":3}
        if selection in ["No","NoResponse"]:
            nao.Say("Thank you! Enjoy your day!")
            return {"next":1}
        return{"next":1} # Error


class Service_Selection(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.wordlist = ["Check in" "Check out" "other services"]
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
                else:
                    self.nextphase = 8
            self.nextphase = self.wordlist.index(answer) + 4 # checkin:4 checkout:5 other:6
        except Exception,e:
            logging.error("State(Service Selection): Error: %s"%e)
            if DEBUG:
                self.nextphase = 4
                return "Yes" #TODO: Changed in the development version
            else:
                self.nextphase = 8
                return "NoResponse"
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
            if answer == "NoResult" and not self.wordlist.index(answer) == 0:
                cnt = 0
                # try to get customer's selection again
                while cnt<self.retry and answer == "NoResult" and not self.wordlist.index(answer) == 0:
                    cnt += 1
                    nao.Say("Sorry, I can't understand what you said, could you repeat your selection again?")
                    answer = speech_recog(self.wordlist)
                else:
                    self.nextphase = 8
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
            if self.wordlist.index(answer) == 1:
                self.nextphase = 6
            elif self.wordlist.index(answer) == 2:
                self.nextphase = 1
        except Exception,e:
            logging.error("State(CheckIn): Error: %s"%e)
            if DEBUG:
                nao.Say("Please wait...Thank you! The Check in process is done, enjoy your room!")
                nao.Say("Still need other service?")
                self.nextphase = 6
                return "Yes" #TODO: Changed in the development version
            else:
                self.nextphase = 8
                return "NoResponse"
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
        return self.nextphase
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()

class OtherService(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.nextphase = 0
    def enter(self, *args, **kwargs):
        pass
    def exit(self, *args, **kwargs):
        # return state
        self.nextphase = 1
        return {"next":self.nextphase}
    def run(self,state_dict,**kwargs):
        self.enter()
        return self.exit()

class Guide(StateMachine):
    def __init__(self,ROBOT_IP,ROBOT_PORT,nao):
        self.nextphase = 0
        self.wordlist = ["yes", "no"]

    def enter(self, *args, **kwargs):
        nao.Say("Please follow me!")
        # navigation to landmark

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
            if answer=="yes":
                self.nextphase = 3
            elif answer=="no":
                nao.Say("Have a nice day!")
                self.nextphase = 1
        except Exception,e:
            logging.error("State(Guide): Error: %s"%e)
            if DEBUG:
                nao.Say("Please wait...Thank you! The Check in process is done, enjoy your room!")
                nao.Say("Still need other service?")
                self.nextphase = 6
                return "Yes" #TODO: Changed in the development version
            else:
                self.nextphase = 8
                return "NoResponse"
        return
    def exit(self, *args, **kwargs):
        # return state
        if self.nextphase == 8:
            return {"next":self.nextphase, "error":"NoResponse"}
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
                if DEBUG:
                    nao.Say("Please wait...Thank you! The Check in process is done, enjoy your room!")
                    nao.Say("Still need other service?")
                    self.nextphase = 3
                    return "Yes" #TODO: Changed in the development version
                else:
                    self.nextphase = 1
                    return "NoResponse"

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