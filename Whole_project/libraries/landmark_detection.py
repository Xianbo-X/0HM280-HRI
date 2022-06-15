import nao_nocv_2_1 as nao
import numpy as np
DEBUG=True


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
                        return detected, markerInfo
    nao.MoveHead(yaw_val = 0, pitch_val=0, isAbsolute =True)
    return False, None