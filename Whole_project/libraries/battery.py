import logging
from matplotlib.style import library


from libraries import nao_nocv_2_1 as nao
from naoqi import ALProxy
DEBUG=True

def detect_low_battery(ROBOT_IP,ROBOT_PORT):
    if DEBUG: return False
    try:
        battery_proxy=ALProxy("ALBatteryProxy")
        battery_level=battery_proxy.getBatteryCharge()
        if battery_level<=20:
            return True
        return False
    except Exception,e:
        logging.debug("Battery: Exception: %s"%e)
        raise e