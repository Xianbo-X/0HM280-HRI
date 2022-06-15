from libraries import nao_nocv_2_1 as nao
from config import ROBOT_IP,ROBOT_PORT,SPEECH_SENSITIVITY
from libraries.exceptions import BatteryLowException, NoResponseException,BatteryLowHandler,GeneralHandler, NoResponseHandler
import state_machine as sm

class Handler():
    def __init__(self):
        self.batterylowHandler=BatteryLowHandler()
        self.noResponseHandler=NoResponseHandler()
        self.generalHandler=GeneralHandler()
class FiniteMachineController():
    def __init__(self,all_states):
        """"
        Params:
        ------
        all_states: dict(int,StateMachine)
            a dict of all states
        """
        self.all_states=all_states
        self.handler=Handler()

    def set_current_state(self, cur_state):
        self.current_state=cur_state
    
    def get_next_state(self,next):
        """
        Params:
        ------
        next: int
            the next state code in the all states dict.
        """
        return self.all_states[next]
    
    def start(self):
        self.set_current_state(self.get_next_state(1))
        self.returned_info={"NoInfo":None}
        self.run()

    def run(self):
        while(True):
            try:
                self.returned_info=self.current_state(self.returned_info)
                print "State_machine next: ",self.returned_info["next"]
                next=self.returned_info["next"]
                if self.returned_info["next"]==0:
                    break
            except BatteryLowException,e:
                next=self.handler.batterylowHandler()
            except NoResponseException,e:
                next=self.handler.noResponseHandler()
            except Exception,e:
                print(e)
                next=self.handler.generalHandler()
            finally:
                self.set_current_state(self.get_next_state(next))
            
def init_nao():
    nao.InitProxy(ROBOT_IP,PORT=ROBOT_PORT)

def init_controller():
    all_state_machine=[state_machine(ROBOT_IP,ROBOT_PORT,nao) for state_machine in sm.__all__]
    controller=FiniteMachineController(all_state_machine)
    return controller

if __name__=="__main__":
    init_nao()
    controller=init_controller()
    controller.start()