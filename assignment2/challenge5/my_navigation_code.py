import math
import numpy as np
import behaviour_based_navigation as bn
from definitions import *
from kalmanfilter import kalmanfilter

A=np.matrix(np.identity(2))
B=np.matrix(np.array([[np.sqrt(3)/2,np.sqrt(3)/2]]).T*0.01)
C=np.matrix(np.identity(2))
R=np.matrix(1*np.identity(2)) # epsilon noise (process noise)
Q=np.matrix(1*np.identity(2)) # delta noise (measurement noise)
mu_s=[]
sigma_s=[np.matrix([0,0,0,0]).reshape(2,2)]
all_sonars_original=[]
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


def scan_world(robot, allobstacles, alltargets):
    [sonar_left, sonar_right] = robot.sonar(allobstacles)
    all_sonars_original.append(np.matrix([[sonar_left,sonar_right]]).T)
    if len(mu_s)==0: mu_s.append(np.matrix([[sonar_left,sonar_right]]).T)
    mu,sigma=kalmanfilter(mu_s[-1],sigma_s[-1],bn.compute_velocity(mu_s[-1][0,0],mu_s[-1][1,0]),np.matrix([[sonar_left,sonar_right]]).T,A,B,C,R,Q)
    mu_s.append(mu)
    sigma_s.append(sigma)
    sonar_left=mu_s[-1][0,0]
    sonar_right=mu_s[-1][1,0]

    target_distance, target_angle = compute_target_location(robot, alltargets)  # The angle is with respect to the world frame
    # print sonar_left, sonar_right, target_distance, target_angle
    target_angle_robot = target_angle - robot.phi  # This is the angle relative to the heading direction of the robot.

    print("sonar left",sonar_left)
    print("sonar right",sonar_right)
    turn_rate = bn.compute_turnrate(target_distance, target_angle_robot, sonar_left, sonar_right)
    velocity = bn.compute_velocity(sonar_left, sonar_right)
    print("turnrate: ",turn_rate)
    print("velocity: ",velocity)
    # sleep(1)
    robot.set_vel(velocity, turn_rate) # the simulated robot does not sidestep

def save_infors():
    np.save("mu_s",mu_s)
    np.save("sigma_s",sigma_s)
    np.save("sonar_info",all_sonars_original)