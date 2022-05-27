import math
import random

degree = math.pi/180.0 # radians per degree

def FTarget(target_distance, target_angle):

    #do something useful here
    Ftar=-math.sin(-target_angle)#*math.exp(-target_distance)
    print ("Ftar", Ftar)
    return Ftar

def FObstacle(obs_distance, obs_angle):
    # too_far=10 #cm
    too_far=5 #cm
    sigma_obs=100 #cm, large sigma_obs make forces due to angle large
    beta_1=50
    beta_2=100 # large beta_2 makes the obstacle force is large
    if obs_distance < too_far:
        #do something useful here
        Fobs=math.exp(-(obs_angle)**2/(2*sigma_obs*sigma_obs))*(-obs_angle)*math.exp(-obs_distance/beta_2)
    else:
        Fobs=0
    return beta_1*Fobs

def FStochastic():
    """FStochastic adds noise to the turnrate force. This is just to make the simulation more realistic by adding some noie something useful here"""
    mu=0
    sigma=0.5
    Fstoch=random.gauss(mu,sigma)
    return Fstoch

def FOrienting(target_distance,orientation_angle):
    #do something useful here
    Forient=0 # In our case, out objcet don't have a orientation. So, we don't add forces here.
    Forient=-math.exp(-target_distance)*math.sin(-orientation_angle)
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
    velocity=(math.tanh(0.03*((sonar_distance_left+sonar_distance_right)/2-(max_distance+min_distance)/2))+1)*max_velocity
    # hand-designed velocity function to make the speed changes with the distance of obstacles.

    
    return velocity

def compute_turnrate(target_dist, target_angle, sonar_distance_left, sonar_distance_right):
    max_turnrate = 0.349 #rad/s # may need adjustment!
    # max_turnrate = 3.145926 /2  #rad/s # may need adjustment!

    delta_t = 0.1 # may need adjustment!
    sonar_angle_left = 30 *  degree
    sonar_angle_right = -30 * degree

    Fobs_left =(sonar_distance_left/(sonar_distance_left+sonar_distance_right))*FObstacle(sonar_distance_left, sonar_angle_left)
    Fobs_right =(sonar_distance_right/(sonar_distance_left+sonar_distance_right))* FObstacle(sonar_distance_right, sonar_angle_right)
    # Weighted left force and right force based on the corresponding obstacle distance. It can help our robot avoid obstacles.
    print("Fobs_left",Fobs_left)
    print("Fobs_right",Fobs_right)
    # THRESHOLD=0.1
    # MAX_SONAR_DISTANCE=10
    # if (abs(sonar_distance_left-sonar_distance_right)<THRESHOLD and sonar_distance_left<MAX_SONAR_DISTANCE): # Within THRESHOLD, we see the two distances are the same
    #     print("True")
    #     Fobs_left=Fobs_left*1.5 # Deal with cases that the obstablce is exactly in fornt of the robot. To make robot turn left in this case.

    print("Fobs_left2",Fobs_left)
    print("Fobs_right2",Fobs_right)
    FTotal = 0.5*FTarget(target_dist, target_angle) + \
             1.01*Fobs_left + \
             Fobs_right + \
             FOrienting(target_dist,target_angle) + \
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
