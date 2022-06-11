from face_detection import detect_face,onFindFace
from start_dialog import start_dialog_on_multitopics
import nao_nocv_2_1 as nao
from config import ROBOT_IP,ROBOT_PORT,SPEECH_SENSITIVITY,DIALOG_TOPICS


def meet_customer(nao):
    while not detect_face(nao):
        # Wait until our robot find a person
        pass
    onFindFace(nao) # Execuate finding face actions
    try:
        start_dialog_on_multitopics(ROBOT_IP,ROBOT_PORT,DIALOG_TOPICS,SPEECH_SENSITIVITY)
    except Exception,e:
        print "Failed to start dialog ",e


def control_flow(nao):
    meet_customer(nao)

if __name__=="__main__":
    nao.InitProxy(ROBOT_IP)
    control_flow(nao)