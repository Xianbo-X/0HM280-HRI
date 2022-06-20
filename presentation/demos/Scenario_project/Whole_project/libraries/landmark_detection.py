import nao_nocv_2_1 as nao
import numpy as np
from libraries.exceptions import *
from threading import Thread,Event
DEBUG=False

from behavior_based_navigation_ch4 import moveToTarget
import math

def search_landmark(nums=5):
    """
    Return
    -----
    [Detect result, landmark angle(Yaw)]
    """
    # head move range -119.5 ~ 119.5 deg
    head_mov_range = np.linspace(-1.086017,1.086017,nums)
    # detect landmark times
    detect_cnt = 100
    marker_ID=0
    for rad in head_mov_range:
        nao.InitTrack()
        nao.MoveHead(yaw_val = rad, pitch_val=0, isAbsolute=True)
#         time.sleep(0.2)
        nao.InitVideo(1) # resolution 320*240
        if not DEBUG:
            nao.InitLandMark()
        # detect landmark and return info
        for cnt in range(detect_cnt):
            if DEBUG: detected=False
            else:
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
    return False, 0

def reach2target():
    _, markinfo=search_landmark()
    #markerinfo[0][3] #sizeX
    if(markinfo[0][3]>100):
        return True
    else: return False

def action_no_landmark():
    print("Look around")
    nao.InitSonar()
    find,markInfo=search_landmark()
    max_retry=5
    total_retry=0
    while (not find and total_retry<max_retry):
        print "\r Retry:"+str(total_retry)
        total_retry+=1
        for i in range(4):
            moveToTarget(nao,5,0) # Move around
            nao.motionProxy.waitUntilMoveIsFinished() # Wait motion finish to avoid send instruction too fast.
        find,markInfo=search_landmark()
        nao.Walk(0,0,0)
    return find,markInfo

def navigation():
        nao.InitPose()
        nao.InitSonar()
        
        nao.Walk(0,0, math.pi/2)
        turn_back = - math.pi/2
        # find landmark
        
        find_landmark, turn_ang = search_landmark()
        
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
                    # moveToTarget(nao,0.5,0) # move forward to find the landmark
                else:
            #         nao.Walk(0,0,math.pi) # turn around
                    while(SL<1 or SR<1):
                        nao.Move(0,0,0.349)
                        [SL, SR]=nao.ReadSonar()
                    # moveToTarget(nao,0.5,0)
                find_landmark,markinfo=action_no_landmark()
                    # nao.Walk(0.5, 0, 0)
                # find_landmark, markinfo = search_landmark() 
                if(find_landmark==False):
            #         speaker = ALProxy(IP="marvin.local", proxy=[0], PORT = 9559) # may need to changed
                    nao.Say("I cannot find landmark!")
                    print "I cannot find landmark!"
                    raise NavigationException("Guide",8)
        # face to customer again
        nao.Walk(0,0,turn_back)
        