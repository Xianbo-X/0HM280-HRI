import nao_nocv_2_1 as nao

def InitNao():
    IP = "127.0.0.1" # IP address of the (Webots) simulator
    # IP="192.168.0.117" #Bender
    nao.InitProxy(IP, ) # Initialize motion proxy
    nao.InitSonar() # Initialize front-left and front-right sonar
   
def MoveRobot(forward_distance, sideward_distance, angle):
    # Keeps taking steps until a new Move command is given
    #
    # Nao can move forward, sideward and turn simultaneously in one step
    # forward_distance  = Nao forward distance of one step in meter
    # sideward_distance = Nao sideward distance of one step in meter
    # angle             = Nao turn angle of one step in degrees
    #
    # StandUp() needs to be run once before this command works
    frequency = 10 # nr of steps per second
    nao.Move(forward_distance, sideward_distance, angle, frequency)       

def RotateHead(yaw, pitch, speed):
    # RotateHead: turns head for the specified amount of radians and then stops
    # yaw   = horizontal angle in radians
    # pitch = vertical angle in radians
    # speed = speed of angular change in radians / second 
    # angle_is_absolute =
    #   if True:  yaw and pitch are absolute (in space)
    #   if False: yaw and pitch are only the change in radians
    angle_is_absolute  = False
    nao.MoveHead(yaw, pitch, angle_is_absolute) 

def StandUp():
    # StandUp: Robot stands up, and gets ready to move
    nao.InitPose()    

def Crouch():
    # Crouch: Robot sits down
    # In real robots it also relaxes the motors
    nao.Crouch()

def MoveForward():
    # MoveForward: keep moving straight forwards
    # will continue until a new Move command is given
    MoveRobot(1.0, 0.0, 0.0)       
          
def MoveBackward():
    # MoveForward: keep moving straight backwards
    # will continue until a new Move command is given
    MoveRobot(-1.0, 0.0, 0.0)

def MoveLeft():
    # MoveLeft: keep moving to the left
    # will continue until a new Move command is given
    MoveRobot(0.0, 1.0, 0.0)

def MoveRight():
    # MoveRight: keep moving to the left
    # will continue until a new Move command is given
    MoveRobot(0.0, -1.0, 0.0)

def TurnLeft():
    # TurnLeft: rotate (on the spot) to the left
    # will continue until a new Move command is given
    MoveRobot(0.0, 0.0, 0.4)

def TurnRight():
    # TurnRight: rotate (on the spot) to the right
    # will continue until a new Move command is given
    MoveRobot(0.0, 0.0, -0.4)

def StopRobot():
    # StopRobot: stop the robot from moving or turning
    MoveRobot(0.0, 0.0, 0.0)

def TurnHeadLeft():
    # TurnHeadLeft: turn head left for 0.1 radians (~6 deg)
    RotateHead(0.1, 0.0, 0.1)

def TurnHeadRight():
    # TurnHeadRight: turn head right for 0.1 radians (~6 deg)
    RotateHead(-0.1, 0.0, 0.1)

def TurnHeadUp():
    # TurnHeadUp: turn head up for 0.1 radians (~6 deg)
    RotateHead(0.0, -0.1, 0.1)

def TurnHeadDown():
    # TurnHeadDown: turn head down for 0.1 radians (~6 deg)
    RotateHead(0.0, 0.1, 0.1)

def RunGesture(file_name):
    # RunGesture: run module from folder 'gestures'
    # only .py files and .ges files will work
    # folder 'gestures' must be in the same folder as this module
    nao.RunMovement(file_name)

def ShowAllGestures():
    # GetAllGestures: returns all available gesture files
    # from folder 'gestures'
    gestures = nao.GetAvailableGestures()
    for gesture in gestures:
        print(gesture)

def ReadSonar():
    # ReadSonar: returns averages of left and right sonar
    return nao.ReadSonar()

def ShowCommands():
    print("")
    print(" NAO remote control commands:")
    print(" su: Stand Up")
    print(" cr: Crouch Pose")
    print(" mf: Move Forward ")
    print(" mb: Move Back ")
    print(" ml: Move Left ")
    print(" mr: Move Right")
    print(" tl: Turn Left on spot")
    print(" tr: Turn Right on spot")
    print(" sr: Stop the Robot")
    print(" hl: turn Head Left")
    print(" hr: turn Head Right")
    print(" hu: turn Head Up")
    print(" hd: turn Head Down")
    print(" rg: Run Gesture movement")
    print(" gl: List available Gestures")
    print(" rs: Read Sonar")
    print(" ?: Show help")
    print(" q: Quit")      

def RunCommand(cmd):
    # decide the action to be taken on input cmd
    if cmd == 'su':
        print('Standing up ...')
        StandUp()

    elif cmd == 'cr':
        print('Crouching ...')
        Crouch()

    elif cmd == "mf":
        print('Moving forward ...')
        MoveForward()

    elif cmd == "mb":
        print('Moving backward ...')
        MoveBackward()

    elif cmd == "ml":
        print('Moving left ...')
        MoveLeft()
        
    elif cmd == "mr":
        print('Moving right ...')
        MoveRight()

    elif cmd == "tl":
        print('Turning left ...')
        TurnLeft()

    elif cmd == "tr":
        print('Turning right ...')
        TurnRight()

    elif cmd =="sr":
        print('Stopping robot ...')
        StopRobot()

    elif cmd == 'hl':
        print('Turning head left ...')
        TurnHeadLeft()

    elif cmd == 'hr':
        print('Turning head right ...')
        TurnHeadRight()

    elif cmd == 'hu':
        print('Turning head up ...')
        TurnHeadUp()

    elif cmd == 'hd':
        print('Turning head down ...')
        TurnHeadDown()

    elif cmd =='rg':
        gesture_name = raw_input("Enter file name of gesture: ")
        nao.RunMovement(gesture_name)

    elif cmd =='gl':
        print('Available Gestures: ')
        ShowAllGestures()

    elif cmd =="rs":
        print('Read Sonar: ')
        distance = nao.ReadSonar()
        print(distance[0] + distance[1]) / 2.0
    elif cmd =='?':
        print("Show help")
        ShowCommands()

    else:
        print("unknown remote control command '" + cmd+ "'")
        ShowCommands()

def TestCommands():
    # first time: show all available RC commands
    ShowCommands()

    # main menu
    cmd = ""
    while (cmd != "q"):
        cmd = raw_input("rc command ('?' for help): ")
        RunCommand(cmd)

def main():
    # initialize communications with simulated robot
    # the webots simulation must run for this to work
    InitNao()
    
    StandUp() # prepare the Nao for moving

    TestCommands()

    Crouch()  # bring the Nao in a 'relaxed' sitting state

# this module can be both run and imported as a module with this little 'trick'
if __name__ == '__main__':
    main()



