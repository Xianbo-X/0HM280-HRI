import math
import numpy as np
import behaviour_based_navigation_aggressive as bn
from definitions import *


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

def sensor_position(robot):
    pos=[]
    for sensor in range(len(robot.sensor_positions)):
        pos.append(np.array([robot.x + robot.sensor_positions[sensor][0] * math.cos(robot.sensor_positions[sensor][1] + robot.phi),
        robot.y + robot.sensor_positions[sensor][0] * math.sin(robot.sensor_positions[sensor][1] + robot.phi)]))
    return pos

def compute_sensor_distange(robot,alltargets,max_detect_distance=None):
    """
    Parameters:
    ------------
    robot: (object) robot,
    alltargets: (object) alltargets,
    max_detect_distance: (int>=0|None|-1) 
        None: use robote.max_detection
        -1  : No max detect distance limits, np.inf
        int : max detect distance is the non-negative number

    returns:
    -----------
    left,right: left detected distance, right detected distance
    """

    if max_detect_distance is None: max_detect_distance=robot.max_distance
    if max_detect_distance is -1: max_detect_distance=np.inf
    pos=sensor_position(robot)
    target=alltargets.sprites()[0]
    left=min(np.linalg.norm(pos[0]-np.array([target.x,target.y]),2),max_detect_distance)
    right=min(np.linalg.norm(pos[1]-np.array([target.x,target.y]),2),max_detect_distance)
    return left,right
    


def scan_world(robot, allobstacles, alltargets):
    # [sonar_left, sonar_right] = robot.sonar(allobstacles)
    [sonar_left, sonar_right] = compute_sensor_distange(robot,alltargets,-1)
    print([sonar_left,sonar_right])
    target_distance, target_angle = compute_target_location(robot, alltargets)  # The angle is with respect to the world frame
    # print sonar_left, sonar_right, target_distance, target_angle
    target_angle_robot = target_angle - robot.phi  # This is the angle relative to the heading direction of the robot.

    turn_rate = bn.compute_turnrate(target_distance, target_angle_robot, sonar_left, sonar_right)
    velocity = bn.compute_velocity(sonar_left, sonar_right)
    print("velocity ",velocity)
    print("turnrate:",turn_rate)
    robot.set_vel(velocity, turn_rate) # the simulated robot does not sidestep

