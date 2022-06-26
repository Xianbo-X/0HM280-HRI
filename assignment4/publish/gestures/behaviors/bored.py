# Choregraphe simplified export in Python.
from naoqi import ALProxy
import nao_nocv_2_1 as nao

# def behaviour_bored():
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1.24, 2.44, 4.2, 5.76])
keys.append([0.0260361, 0.53379, 0.53379, 0.05825])

names.append("HeadYaw")
times.append([1.24, 2.44, 4.2, 5.76])
keys.append([0.0260361, 0.141086, 0.249999, -0.0521979])

names.append("LAnklePitch")
times.append([2.2, 3.96, 5.52])
keys.append([0.0523599, 0.0252329, -0.0349066])

names.append("LAnkleRoll")
times.append([2.2, 3.96, 5.52])
keys.append([-0.0523599, -0.0223779, -0.0960099])

names.append("LElbowRoll")
times.append([1.08, 2.28, 4.04, 5.6])
keys.append([-0.955639, -0.406468, -0.260738, -0.58748])

names.append("LElbowYaw")
times.append([1.08, 2.28, 4.04, 5.6])
keys.append([-0.771643, -1.17509, -1.27633, -0.811527])

names.append("LHand")
times.append([2.28, 4.04, 5.6])
keys.append([0.268389, 0.261844, 0.270207])

names.append("LHipPitch")
times.append([2.2, 3.96, 5.52])
keys.append([-0.38724, -0.414853, 0.0975039])

names.append("LHipRoll")
times.append([2.2, 3.96, 5.52])
keys.append([0, -0.0283302, 0.118934])

names.append("LHipYawPitch")
times.append([2.2, 3.96, 5.52])
keys.append([-0.33112, -0.36947, -0.291236])

names.append("LKneePitch")
times.append([2.2, 3.96, 5.52])
keys.append([0.331613, 0.380916, 0.176894])

names.append("LShoulderPitch")
times.append([1.08, 2.28, 4.04, 5.6])
keys.append([1.41584, 1.36675, 1.36522, 1.49101])

names.append("LShoulderRoll")
times.append([1.08, 2.28, 4.04, 5.6])
keys.append([0.124212, 0.133416, 0.210117, 0.1733])

names.append("LWristYaw")
times.append([2.28, 4.04, 5.6])
keys.append([-0.721022, -0.705682, -0.704148])

names.append("RAnklePitch")
times.append([2.2, 3.96, 5.52])
keys.append([-0.0174533, -0.0435446, -0.0349066])

names.append("RAnkleRoll")
times.append([2.2, 3.96, 5.52])
keys.append([0.0349066, 0.00379691, 0.0174533])

names.append("RElbowRoll")
times.append([0.92, 2.12, 3.88, 5.44])
keys.append([0.814596, 0.30224, 0.130432, 0.61671])

names.append("RElbowYaw")
times.append([0.92, 2.12, 3.88, 5.44])
keys.append([0.714801, 0.829852, 0.94797, 0.839057])

names.append("RHand")
times.append([2.12, 3.88, 5.44])
keys.append([0.359298, 0.350207, 0.364025])

names.append("RHipPitch")
times.append([2.2, 3.96, 5.52])
keys.append([-0.31899, -0.358873, 0.0691124])

names.append("RHipRoll")
times.append([2.2, 3.96, 5.52])
keys.append([0.039986, 0.076802, -0.0349066])

names.append("RKneePitch")
times.append([2.2, 3.96, 5.52])
keys.append([0.328391, 0.365207, 0.168854])

names.append("RShoulderPitch")
times.append([0.92, 2.12, 3.88, 5.44])
keys.append([1.34076, 1.25792, 1.284, 1.47575])

names.append("RShoulderRoll")
times.append([0.92, 2.12, 3.88, 5.44])
keys.append([-0.119694, -0.116626, -0.144238, -0.224006])

names.append("RWristYaw")
times.append([2.12, 3.88, 5.44])
keys.append([0.961776, 0.958708, 0.957173])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  # motion = nao.motionProxy
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
