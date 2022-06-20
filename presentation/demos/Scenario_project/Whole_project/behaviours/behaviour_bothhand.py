# Choregraphe simplified export in Python.
from naoqi import ALProxy
import nao_nocv_2_1 as nao

def behaviour_bothhand():
  names = list()
  times = list()
  keys = list()

  names.append("HeadPitch")
  times.append([0.56, 0.84, 1.28, 1.8])
  keys.append([0.0904641, 0.169297, -0.169297, -0.0276539])

  names.append("HeadYaw")
  times.append([0.56, 0.84, 1.28, 1.8])
  keys.append([0.032172, 0.032172, 0.032172, 0.032172])

  names.append("LAnklePitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.036858, 0.032172, -4.19617e-05, -0.00157595])

  names.append("LAnkleRoll")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.0889301, -0.0889301, -0.095066, -0.0904641])

  names.append("LElbowRoll")
  times.append([0.52, 0.96, 1.24, 1.84])
  keys.append([-1.33761, -0.897349, -0.981718, -1.05995])

  names.append("LElbowYaw")
  times.append([0.52, 0.96, 1.24, 1.84])
  keys.append([-1.22724, -1.62148, -1.51563, -1.49723])

  names.append("LHand")
  times.append([0.52, 0.96, 1.24, 1.84])
  keys.append([0.1012, 0.8596, 0.6988, 0.5484])

  names.append("LHipPitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([0.395814, 0.273093, 0.306841, 0.322183])

  names.append("LHipRoll")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([0.0813439, 0.0828778, 0.0798099, 0.0782759])

  names.append("LHipYawPitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.141086, -0.154892, -0.147222, -0.148756])

  names.append("LKneePitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.0859461, -0.0859461, -0.0859461, -0.0859461])

  names.append("LShoulderPitch")
  times.append([0.52, 0.96, 1.24, 1.84])
  keys.append([1.37135, 1.47567, 1.48487, 1.4772])

  names.append("LShoulderRoll")
  times.append([0.52, 0.96, 1.24, 1.84])
  keys.append([0.0122299, 0.0705221, 0.0398422, 0.0444441])

  names.append("LWristYaw")
  times.append([0.52, 0.96, 1.24, 1.84])
  keys.append([-0.737896, -0.70108, -0.730227, -0.72409])

  names.append("RAnklePitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.0260359, 0.039926, 0.0245859, 0.00924586])

  names.append("RAnkleRoll")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([0.162646, 0.14884, 0.147306, 0.147306])

  names.append("RElbowRoll")
  times.append([0.44, 0.92, 1.2, 1.8])
  keys.append([1.43587, 0.941918, 1.02782, 1.1214])

  names.append("RElbowYaw")
  times.append([0.44, 0.92, 1.2, 1.8])
  keys.append([1.2425, 1.54623, 1.47106, 1.46186])

  names.append("RHand")
  times.append([0.44, 0.92, 1.2, 1.8])
  keys.append([0.1084, 0.8564, 0.6984, 0.5428])

  names.append("RHipPitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([0.398797, 0.268407, 0.294486, 0.31903])

  names.append("RHipRoll")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.185572, -0.151824, -0.15796, -0.164096])

  names.append("RHipYawPitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.141086, -0.154892, -0.147222, -0.148756])

  names.append("RKneePitch")
  times.append([0.52, 0.88, 1.16, 1.76])
  keys.append([-0.0843279, -0.0843279, -0.0843279, -0.0843279])

  names.append("RShoulderPitch")
  times.append([0.44, 0.92, 1.2, 1.8])
  keys.append([1.40979, 1.51257, 1.5187, 1.51563])

  names.append("RShoulderRoll")
  times.append([0.44, 0.92, 1.2, 1.8])
  keys.append([-0.092082, -0.0890141, -0.0844118, -0.0782759])

  names.append("RWristYaw")
  times.append([0.44, 0.92, 1.2, 1.8])
  keys.append([0.791502, 0.868202, 0.89428, 0.891212])

  try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    # motion = ALProxy("ALMotion", IP, 9559)
    # motion = ALProxy("ALMotion")
    motion=nao.motionProxy
    motion.angleInterpolation(names, keys, times, True)
  except BaseException, err:
    print err
