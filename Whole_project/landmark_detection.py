import nao_nocv_2_1 as nao
import numpy as np
from behavior_based_navigation_ch4 import moveToTarget
import math

def search_landmark():
    """
    Return
    -----
    [Detect result, landmark angle(Yaw)]
    """
    # head move range -119.5 ~ 119.5 deg
    head_mov_range = np.linspace(-1.086017,1.086017,10)
    # detect landmark times
    detect_cnt = 100
    for rad in head_mov_range:
        nao.InitTrack()
        nao.MoveHead(yaw_val = rad, pitch_val=0, isAbsolute=True)
#         time.sleep(0.2)
        nao.InitVideo(1) # resolution 320*240
        nao.InitLandMark()
        # detect landmark and return info
        for cnt in range(detect_cnt):
            detected, timestamp, markerInfo=nao.DetectLandMark()
            if(detected):
                if(marker_ID != markerInfo[0][0]):
                    marker_ID = markerInfo[0][0]
                    detect_threshhold = 0
                else:
                    detect_threshhold += 1
                # detected 10 times as confidence threshold
                if(detect_threshhold>=10):
                        nao.Say("Oh! I found the landmark!")
                        # directly face to landmark
                        print "Head Yaw:", nao.GetYaw(), " land mark angle: ", markerInfo[0][5]
                        #nao.MoveHead(yaw_va = markerInfo[0][5], pitch_val=0, isAbsolute=True)
                        nao.MoveHead(yaw_val = markerInfo[0][1]+rad, pitch_val=0, isAbsolute=True)
                        nao.Walk(0,0,markerInfo[0][1]+rad)
                        nao.MoveHead(yaw_val = 0, pitch_val=0, isAbsolute =True)
                        return detected, markerInfo[0][1]+rad
    nao.MoveHead(yaw_val = 0, pitch_val=0, isAbsolute =True)
    return False, None

def reach2target():
    _, markinfo=search_landmark(nao)
    #markerinfo[0][3] #sizeX
    if(markinfo[0][3]>100):
        return True
    else: return False

def navigation():
        nao.InitPose()
        nao.InitSonar()
        
        nao.Walk(0,0, math.pi/2)
        turn_back = - math.pi/2
        # find landmark
        try:
            find_landmark, turn_ang = search_landmark(nao)
        except Exception,e:
            find_landmark = True
            nao.Walk(0,0, 0.3)
            nao.MoveHead(yaw_val = 0, pitch_val=0, isAbsolute =True)
        turn_back -= turn_ang
        reach_landmark=False
        while (not reach_landmark):
            if(find_landmark):
                #print markinfo[0][3]
                moveToTarget(nao,5,0)
                #reach_landmark = reach2target() # depends on x size of landmark image
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
        # face to customer again
        nao.Walk(0,0,turn_back)