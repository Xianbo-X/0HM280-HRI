import logging
from matplotlib.style import library


from libraries import nao_nocv_2_1 as nao
from naoqi import ALProxy
def detect_low_battery(ROBOT_IP,ROBOT_PORT):
    try:
        battery_proxy=ALProxy("ALBatteryProxy")
        battery_level=battery_proxy.getBatteryCharge()
        if battery_level<=20:
            return True
        return False
    except Exception,e:
        logging.debug("Battery: Exception: %s"%e)
        return False