from urllib import response
import nao_nocv_2_1 as nao
from config import ROBOT_IP,ROBOT_PORT,SPEECH_SENSITIVITY,DIALOG_TOPICS
import logging
from start_dialog import start_dialog_on_multitopics
from time import sleep
MAX_SERVICE_TIMES=100
logging.basicConfig(level=logging.INFO)

def initNao():
    nao.InitProxy(ROBOT_IP,PORT=ROBOT_PORT)
    nao.EyeLED([0,0,255]) # Turn eye to blue to show that it is initalizing. 
    nao.InitSonar()
    nao.EyeLED([0,255,0]) # Turn eye to green to show that it is online
    return True

def active():
    try:
        nao.Say("Hi, I am nao. I am happy to see the beautiful world.")
        nao.Say("I am ready to help people!")
    except Exception,e:
        logging.error(str(e))
        nao.EyeLED([255,0,0])
        

def idle():
    nao.Say("I am idle.")

def wait():
    while not findFace(): 
        idle()


def findFace():
    """Provide actions during findface and result of whether find a face
    """
    nao.Say("Hi, if any one want my help, please come to me")
    return nao.FindFace()
        
def onFindFace():
    """Provide actions that Nao find a face
    """
    try:
        nao.ALTrack(True)
    except Exception,e:
        nao.Say("Oh, no. I can't start my face tracker.")
    finally:
        nao.Say("Hello, welcome to this nice hotel!")
        nao.Say("What can I help you? Or you can just start a small talk with me")
        return True


def start_conversation():
    reponse=start_dialog_on_multitopics(ROBOT_IP,ROBOT_PORT,DIALOG_TOPICS,SPEECH_SENSITIVITY) # start dialog, currently only support all dialog start together
    return response

def processing(exec_function):
    try:
        nao.EyeLED([0,0,255])
        exec_function()
        nao.EyeLED([0,255,0])
    except Exception,e:
        nao.EyeLED([255,0,0])
        nao.Say("I met a error, please contact the tech support team")
        nao.EndTrack()
        nao.Crouch()

def greeting_mode():
    nao.Say("Hello! Dear customer. May I offer you any service?")
    nao.GoToPosture("StandZero") #TODO: Change to a suitable posture
    sleep(0.1)
    return start_conversation()

def service_selection():
    #TODO: Set focus topic
    response=start_conversation()
    return response

def checkin_out():
    #TODO: Set focus topic
    response=start_conversation()
    return response

def control_flow():
    initNao()
    active()
    service_times=0
    while service_times<MAX_SERVICE_TIMES:
        service_times+=1
        wait()
        # detect human fo to Greeting. State 2
        onFindFace() #Transition actions
        response=greeting_mode() # State 2
        # TODO: if not checkbattery():  GoState7()
        if response =="NO": # GoTOState1
            continue
        if response =="YES": 
            reponse=service_selection()
        if response=="CHECKIN":
            checkin_out()
        nao.Say("Still in progress")
    
if __name__=="__main__":
    control_flow()