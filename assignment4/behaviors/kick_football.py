# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LHipYawPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.96, 2.36, 2.76])
keys.append([-0.225548, -0.225548, -0.225548, -0.225548, -0.225548, -0.225548, -0.225548])

names.append("RAnklePitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.96, 2.36, 2.76])
keys.append([0.0724396, 0.0724396, 0.0724396, 0.0724396, 0.0724396, 0.0724396, 0.0724396])

names.append("RAnkleRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.96, 2.36, 2.76])
keys.append([0.110624, 0.110624, 0.110624, 0.110624, 0.110624, 0.110624, 0.110624])

names.append("RHipPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.96, 2.36, 2.76])
keys.append([-0.536597, -0.536597, -0.536597, -0.536597, -0.536597, -0.536597, -0.0567959])

names.append("RHipRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.96, 2.36, 2.76])
keys.append([-0.133209, -0.133209, -0.133209, -0.133209, -0.133209, -0.133209, -0.133209])

names.append("RHipYawPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.96, 2.36, 2.76])
keys.append([-0.225548, -0.225548, -0.225548, -0.225548, -0.225548, -0.225548, -0.225548])

names.append("RKneePitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.96, 2.36, 2.76])
keys.append([0.628818, 0.282473, 0.766248, 0.250669, 0.791651, 0.195731, 0.195731])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
