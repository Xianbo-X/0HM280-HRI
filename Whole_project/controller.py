from libraries import nao_nocv_2_1 as nao
from config import ROBOT_IP,ROBOT_PORT,SPEECH_SENSITIVITY
from libraries.exceptions import BatteryLowException, NavigationException, NoResponseException,BatteryLowHandler,GeneralHandler, NoResponseHandler,NavigationHandler
import state_machine as sm
from time import sleep

class Handler():
    def __init__(self):
        self.batterylowHandler=BatteryLowHandler()
        self.noResponseHandler=NoResponseHandler()
        self.generalHandler=GeneralHandler()
        self.navigationHandler=NavigationHandler()
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
                next=self.returned_info["next"]
                if self.returned_info["next"]==0:
                    break
            except BatteryLowException,e:
                next=self.handler.batterylowHandler()
            except NoResponseException,e:
                next=self.handler.noResponseHandler()
            except NavigationException,e:
                self.handler.generalHandler()
                next=e.next
                print(next)
                self.returned_info={
                    "next":e.next,
                    "skip_navigation":True
                }
            except Exception,e:
                print(e)
                next=self.handler.generalHandler()
                # raise e
            finally:
                print "State_machine next: ",next
                self.set_current_state(self.get_next_state(next))
                # sleep(0.5)
            
def init_nao():
    nao.InitProxy(ROBOT_IP,PORT=ROBOT_PORT)
    # nao.ALTrack(False)
    # nao.EndTrack()
    nao.InitPose()

def init_controller():
    all_state_machine=[state_machine(ROBOT_IP,ROBOT_PORT,nao) for state_machine in sm.__all__]
    controller=FiniteMachineController(all_state_machine)
    return controller

if __name__=="__main__":
    init_nao()
    controller=init_controller()
    controller.start()