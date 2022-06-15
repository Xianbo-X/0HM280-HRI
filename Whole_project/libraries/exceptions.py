import libraries.nao_nocv_2_1 as nao
from nao_remote_control import TestCommands,StopRobot

class BatteryLowException(Exception):
    def __init__(self, message):
        super(BatteryLowException,self).__init__(message)
        self.message = "Battery low"

class NoResponseException(Exception):
    def __init__(self, message):
        super(NoResponseException,self).__init__(message)
        self.message = "No response"

class BatteryLowHandler():
    def __init__(self):
        pass
    def __call__(cls):
        nao.Say("Battery low")
        return 0

class NoResponseHandler():
    def __init__(self):
        pass

    def __call__(cls):
        nao.Say("No response from custom, Go back to StandBy Mode")
        return 1

class GeneralHandler():
    def __init__(self):
        pass
    
    def __call__(cls):
        nao.Say("Unexpected error, remote control on")
        TestCommands()
        StopRobot()
        nao.Say("Remote control off")
        return 1
        
if __name__=="__main__":
    print(BatteryLowException("20"))
    print(NoResponseException("Service"))