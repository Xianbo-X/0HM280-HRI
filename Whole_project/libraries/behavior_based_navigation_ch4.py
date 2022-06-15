import math
import random
import numpy as np

degree = math.pi/180.0 # radians per degree

def FTarget(target_distance, target_angle):

    #do something useful here
    Ftar=0
    Ftar=-math.sin(-target_angle)# Force to turn the robot face to the target
    # print ("Ftar", Ftar)
    return Ftar

def FObstacle(obs_distance, obs_angle):
    # too_far=10 #cm
    too_far=5 #cm
    sigma_obs=100 #cm? large sigma_obs make forces due to angle large
    beta_2=100 #? large beta_2 makes the obstacle force is large
    if obs_distance < too_far:
        #do something useful here
        Fobs=math.exp(-(obs_angle)**2/(2*sigma_obs*sigma_obs))*(-obs_angle)*math.exp(-obs_distance/beta_2)
    else:
        Fobs=0
    return Fobs
def FStochastic():
    """FStochastic adds noise to the turnrate force. This is just to make the simulation more realistic by adding some noie something useful here"""
    Kstoch=0.03
    
    Fstoch =Kstoch*random.randint(1,100)/100.0
    return Fstoch

def FOrienting():
    #do something useful here
    Forient=0 # In our case, out objcet don't have a orientation. So, we don't add forces here.
    return Forient

def compute_velocity(sonar_distance_left, sonar_distance_right):
    max_velocity = 1.0
    max_distance = 0.5 #m
    min_distance = 0.3 #m The distance is set based on the specification of the sonar sensor of the robot.

    if sonar_distance_left>max_distance and sonar_distance_right > max_distance:
        velocity = max_velocity
    elif sonar_distance_left<min_distance or sonar_distance_right < min_distance:
        velocity = 0.0
    elif sonar_distance_left<sonar_distance_right:
        velocity = max_velocity*sonar_distance_left/max_distance
    else:
        velocity = max_velocity*sonar_distance_right/max_distance

    
    return velocity

def compute_turnrate(target_dist, target_angle, sonar_distance_left, sonar_distance_right):
    max_turnrate = 0.349 #rad/s # may need adjustment!

    delta_t = 0.05 # may need adjustment!
    sonar_angle_left = 30 * degree
    sonar_angle_right = -30 * degree
    beta_1=20
    Fobs_left =beta_1*(sonar_distance_left/(sonar_distance_left+sonar_distance_right))*FObstacle(sonar_distance_left, sonar_angle_left)
    Fobs_right =beta_1*(sonar_distance_right/(sonar_distance_left+sonar_distance_right))* FObstacle(sonar_distance_right, sonar_angle_right)
    # Weighted left force and right force based on the corresponding obstacle distance. It can help our robot avoid obstacles.
    THRESHOLD=0.0001
    MAX_SONAR_DISTANCE=2.5
    if (abs(sonar_distance_left-sonar_distance_right)<THRESHOLD and sonar_distance_left<MAX_SONAR_DISTANCE): # Within THRESHOLD, we see the two distances are the same
        Fobs_left*=1.01 # Deal with cases that the obstablce is exactly in fornt of the robot. To make robot turn left in this case.
    # print(sonar_distance_left)    
    # print(sonar_distance_right)
    
    # print("Fobs_left",Fobs_left)
    # print("Fobs_right",Fobs_right)
    FTotal = 0.5*FTarget(target_dist, target_angle) + \
             Fobs_left + \
             Fobs_right + \
             FOrienting() + \
             FStochastic()
             
    # turnrate: d phi(t) / dt = sum( forces ) 
    turnrate =  FTotal*delta_t
    
    #normalise turnrate value
    if turnrate>max_turnrate:
        turnrate=1.0
    else:
        turnrate=turnrate/max_turnrate

    return turnrate

def compute_target_location(robot, alltargets):
    """This function computes the distance to the target and the angle relative to the robot in world coordinates"""
    dist = []
    angle = []
    for tar in alltargets:
        dx = tar.x - robot.x
        dy = tar.y - robot.y
        dist.append(np.linalg.norm([dx, dy])) # Eucliden distance
        angle.append(math.atan2(dy, dx))
    i = np.argmin(dist)
    return dist[i], angle[i]


def scan_world(robot, target_distance,target_angle):
    ''' This function computes the velocity and turnrate based on robot position and sonar information and target postiion. 
    The velocity and turnrate will help the robot avoid obstacles and move to the target
    '''

    [sonar_left, sonar_right] = robot.ReadSonar() # Get obstacle distances
    # print("sonar_left",sonar_left)
    # print("sonar_right",sonar_right)
    target_angle_robot=target_angle

    turn_rate = compute_turnrate(target_distance, target_angle_robot, sonar_left, sonar_right)
    velocity = compute_velocity(sonar_left, sonar_right)
    return velocity,turn_rate

delta_t=0.1
def moveToTarget(nao,target_distance,target_angle):
    """This function will let robot move the target and avoid obstacles.
    Params:
    ---------
    target_distance: the distance between robot and target
    target_angle: relative angle of the target and the face direction of robot. If target is in the left side of robots, the angle will be positive. 

    Returns:
    ---------
    dx: distance moved by the robot in forward direction.  x_axis
    dy: distance moved by the rotot in the left side direction. y_axis
    dtheta: The direciton of face changed of the robot.

    """
    vel,turnrate=scan_world(nao,target_distance,target_angle) # Get the velocity and the angular velocity 
    # Assume the robot move in constant velocity, and face to the d_theta direction
    d_theta=-turnrate*delta_t  # Obey the sign defination of angles for the Walk function
    dx=vel*delta_t*math.cos(d_theta)
    dy=vel*delta_t*math.sin(d_theta)
    nao.Walk(dx,dy,d_theta)
    nao.motionProxy.waitUntilMoveIsFinished() # Wait motion finish to avoid send instruction too fast.
    return dx,dy,d_theta