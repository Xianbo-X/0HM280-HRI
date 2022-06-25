# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.6, 0.8, 1.32])
keys.append([-0.118682, 0.0872665, 0])

names.append("LAnklePitch")
times.append([0.72])
keys.append([-0.0496523])

names.append("LAnkleRoll")
times.append([0.72])
keys.append([0.0770189])

names.append("LElbowRoll")
times.append([0.92])
keys.append([-0.876155])

names.append("LElbowYaw")
times.append([0.92])
keys.append([-1.89019])

names.append("LHand")
times.append([0.92])
keys.append([1])

names.append("LHipPitch")
times.append([0.72])
keys.append([0.359314])

names.append("LHipRoll")
times.append([0.72])
keys.append([-0.133255])

names.append("LHipYawPitch")
times.append([0.72])
keys.append([-0.236319])

names.append("LKneePitch")
times.append([0.72])
keys.append([-0.0833201])

names.append("LShoulderPitch")
times.append([0.48, 0.92])
keys.append([0.555015, 0.79587])

names.append("RAnklePitch")
times.append([0.72])
keys.append([0.0519679])

names.append("RAnkleRoll")
times.append([0.72])
keys.append([0.245997])

names.append("RElbowRoll")
times.append([0.92])
keys.append([0.319395])

names.append("RHand")
times.append([0.92])
keys.append([0.65])

names.append("RHipPitch")
times.append([0.72])
keys.append([0.30692])

names.append("RHipRoll")
times.append([0.72])
keys.append([-0.297483])

names.append("RHipYawPitch")
times.append([0.72])
keys.append([-0.236319])

names.append("RKneePitch")
times.append([0.72])
keys.append([-0.0917307])

names.append("RShoulderPitch")
times.append([0.92])
keys.append([1.4556])

names.append("RShoulderRoll")
times.append([0.92])
keys.append([0.0959931])

names.append("RWristYaw")
times.append([0.92])
keys.append([-0.221657])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
