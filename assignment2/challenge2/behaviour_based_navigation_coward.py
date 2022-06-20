import math
import random
import numpy as np

degree = math.pi/180.0 # radians per degree
# MAX_VELOCITY=10
MAX_VELOCITY=10
# MAX_DISTANCE=100
MAX_DISTANCE=50
MIN_DISTANCE=0.5
WHEEL_LENGTH=0.09

def FTarget(target_distance, target_angle):

    #do something useful here
    Ftar=0

    # if target_angle > 0:
    #     Ftar += target_distance * 0.1 #target on the left, increase turn rate
    # elif target_angle < 0:
    #     Ftar -= target_distance * 0.1 # target on the right, decrease turn rate

    return Ftar

def FObstacle(obs_distance, obs_angle):
    too_far=10 #cm

    if obs_distance < too_far:
        #do something useful here
        Fobs=0 # needs replacing !
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

def positive_power(sonar_distance,max_velocity,max_distance,min_distance):
    vel=(50/sonar_distance)/(max_distance-min_distance)*max_velocity*10
    # vel=sonar_distance
    if sonar_distance>max_distance: vel = max_velocity
    # pr=np.random.uniform(0,1)
    # if pr<0.1:
    #     vel+=np.random.randn()*max_velocity/100
    if sonar_distance<min_distance: vel = 0.0
    return vel

def compute_velocity(sonar_distance_left, sonar_distance_right):
    max_velocity = MAX_VELOCITY
    max_distance = MAX_DISTANCE #m
    # min_distance = 0.2 #m
    min_distance = MIN_DISTANCE #m
    right_velocity=positive_power(sonar_distance_left,max_velocity,max_distance,min_distance)
    left_velocity=positive_power(sonar_distance_right,max_velocity,max_distance,min_distance)
    
    return (left_velocity+right_velocity)/2

def compute_turnrate(target_dist, target_angle, sonar_distance_left, sonar_distance_right):
    """
    Differential Drive Kinematics 
    """
    max_velocity = MAX_VELOCITY
    max_distance = MAX_DISTANCE #m
    min_distance = MIN_DISTANCE #m

    left_velocity=positive_power(sonar_distance_left,max_velocity,max_distance,min_distance)
    right_velocity=positive_power(sonar_distance_right,max_velocity,max_distance,min_distance)
    
    return (right_velocity-left_velocity)/WHEEL_LENGTH

if __name__=="__main__":
    pass