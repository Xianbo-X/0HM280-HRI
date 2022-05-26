import math
import random

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
    min_distance = 0.2 #m

    # if sonar_distance_left>max_distance and sonar_distance_right > max_distance:
        # velocity = max_velocity
    # elif sonar_distance_left<min_distance or sonar_distance_right < min_distance:
        # velocity = 0.0
    # elif sonar_distance_left<sonar_distance_right:
        # velocity = max_velocity*sonar_distance_left/max_distance
    # else:
        # velocity = max_velocity*sonar_distance_right/max_distance
    # else:
        # velocity=max_velocity*(sonar_distance_left+sonar_distance_right)/2
    velocity=math.tanh(0.03*((sonar_distance_left+sonar_distance_right)/2-(max_distance+min_distance)/2))+1

    
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
    
    print("Fobs_left",Fobs_left)
    print("Fobs_right",Fobs_right)
    FTotal = 0.5*FTarget(target_dist, target_angle) + \
             1.01*Fobs_left + \
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

if __name__=="__main__":
    pass
