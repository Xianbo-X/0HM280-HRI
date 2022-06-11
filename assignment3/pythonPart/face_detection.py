import nao_nocv_2_1 as nao
import numpy as np
from start_dialog import config_audio,start_dialog
from naoqi import ALProxy

ip_addr="192.168.0.112" #
DIALOG_PATH= "/home/nao/group_08/mydialog_enu.top"  # Absolute path of the dialog topic file (on the robot).

def detect_face(nao):
    """
    Detect the human face then face to it

    Return 
    -----
    Boolean : whether the nao detect the face or not
    """
    face_detected = False

    detect_cnt = 50
    # head move range -119.5 ~ 119.5 deg
    head_mov_range = np.linspace(-1.086017,1.086017,10)
    nao.InitTrack()
    for rad in head_mov_range:
        nao.MoveHead(yaw_val=rad, pitch_val=0, isAbsolute=True)
        
        for cnt in range(detect_cnt):
            face_detected, _, location = nao.DetectFace()
            if face_detected:
                # change eye color
                nao.EyeLED([0,255,0])

                nao.EndTrack()
                return face_detected
    return face_detected


def onFindFace(nao):
    """onFindFace actions
    Params:
    --------
    nao: module of nao_nocv_2_1
    """
    nao.Say("Hi, there. Whilecome to the nice hotel.")
    nao.Say("What can I help you?")

    
    
def start_dialog(nao, topf_path,threshold=0.4):
    dialog_p = ALProxy('ALDialog',ip_addr , 9559)
    # dialog_p = nao.dialogProxy 
    dialog_p.setLanguage("English")
    dialog_p.setASRConfidenceThreshold(threshold)
    # Load topic - absolute path is required
    topf_path = topf_path.decode('utf-8')
    topic = dialog_p.loadTopic(topf_path.encode('utf-8'))

    # Start dialog
    dialog_p.subscribe('myModule') # "myModule" is the name for the subscriber, it's fine to write any other names.

    # Activate dialog
    dialog_p.activateTopic(topic)

    raw_input(u"Press 'Enter' to exit.")

    # Deactivate topic
    dialog_p.deactivateTopic(topic)

    # Unload topic
    dialog_p.unloadTopic(topic)

    # Stop dialog
    dialog_p.unsubscribe('myModule')


def control_flow(nao):
    while not detect_face(nao):
        pass
    print("Find face")
    onFindFace(nao)
    start_dialog(nao,DIALOG_PATH,0.3)
    nao.Say("Bye")

if __name__=="__main__":
    ip_addr="192.168.0.112" #
    # ip_addr="192.168.0.112" #
    # ip_addr="192.168.0.119" #EVE
    nao.InitProxy(ip_addr)
    # initial camera
    nao.InitVideo(1) #resolution 320*240 
    
    nao.EyeLED([255,0,0])
    control_flow(nao)