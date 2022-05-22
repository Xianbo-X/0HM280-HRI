import math
import random
import numpy as np

degree = math.pi/180.0 # radians per degree

def FTarget(target_distance, target_angle):

    #do something useful here
    Ftar=0
    Ftar=-math.sin(-target_angle)#*math.exp(-target_distance)
    print ("Ftar", Ftar)
    return Ftar

def FObstacle(obs_distance, obs_angle):
    # too_far=10 #cm
    too_far=5 #cm
    sigma_obs=100 #cm?
    beta_2=100 #?
    if obs_distance < too_far:
        #do something useful here
        Fobs=0 # needs replacing !
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
    Forient=0
    return Forient

def compute_velocity(sonar_distance_left, sonar_distance_right):
    max_velocity = 1.0
    max_distance = 0.5 #m
    min_distance = 0.3 #m

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
    # max_turnrate = 3.145926 /2  #rad/s # may need adjustment!

    delta_t = 0.05 # may need adjustment!
    sonar_angle_left = 30 * degree
    sonar_angle_right = -30 * degree
    beta_1=20
    Fobs_left =beta_1*(sonar_distance_left/(sonar_distance_left+sonar_distance_right))*FObstacle(sonar_distance_left, sonar_angle_left)
    Fobs_right =beta_1*(sonar_distance_right/(sonar_distance_left+sonar_distance_right))* FObstacle(sonar_distance_right, sonar_angle_right)
    THRESHOLD=0.0001
    MAX_SONAR_DISTANCE=2.5
    if (abs(sonar_distance_left-sonar_angle_right)<THRESHOLD and sonar_distance_left<MAX_SONAR_DISTANCE):
        Fobs_left*=1.01
    print(sonar_distance_left)    
    print(sonar_distance_right)
    
    print("Fobs_left",Fobs_left)
    print("Fobs_right",Fobs_right)
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
        dist.append(np.linalg.norm([dx, dy]))
        angle.append(math.atan2(dy, dx))
    i = np.argmin(dist)
    return dist[i], angle[i]


def scan_world(robot, target_distance,target_angle):
    [sonar_left, sonar_right] = robot.ReadSonar()
    # target_distance, target_angle = compute_target_location(cur_pos, alltargets)  # The angle is with respect to the world frame
    # print sonar_left, sonar_right, target_distance, target_angle
    # target_angle_robot = target_angle - cur_pos.theta  # This is the angle relative to the heading direction of the robot.
    target_angle_robot=target_angle

    turn_rate = compute_turnrate(target_distance, target_angle_robot, sonar_left, sonar_right)
    velocity = compute_velocity(sonar_left, sonar_right)
    return velocity,turn_rate

delta_t=0.1
def moveToTarget(nao,target_distance,target_angle):
    vel,turnrate=scan_world(nao,target_distance,target_angle)
    d_theta=-turnrate*delta_t
    # print("d_theta",d_theta)
    dx=vel*delta_t*math.cos(d_theta)
    dy=vel*delta_t*math.sin(d_theta)
    nao.Walk(dx,dy,d_theta)
    nao.motionProxy.waitUntilMoveIsFinished()
    return dx,dy,d_theta