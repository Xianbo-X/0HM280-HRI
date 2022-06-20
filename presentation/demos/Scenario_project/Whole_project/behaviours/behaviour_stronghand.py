# Choregraphe simplified export in Python.
from naoqi import ALProxy
import nao_nocv_2_1 as nao


def behaviour_stronghand():
  names = list()
  times = list()
  keys = list()

  names.append("HeadPitch")
  times.append([0.76, 1.4, 2.04])
  keys.append([0.251327, -0.400415, -0.351328])

  names.append("HeadYaw")
  times.append([0.2, 0.48, 0.76, 1, 1.2, 1.4, 1.64, 2.04])
  keys.append([-0.137881, 0.441568, -0.106465, 0.350811, -0.137881, 0.350811, 0.137881, 0.197222])

  names.append("LAnklePitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([-0.214803, -0.282298, -0.306841])

  names.append("LAnkleRoll")
  times.append([0.64, 1.36, 1.96])
  keys.append([-0.0873961, -0.00302602, -0.0367741])

  names.append("LElbowRoll")
  times.append([0.8, 1.44, 2.08])
  keys.append([-1.52322, -1.20875, -1.26704])

  names.append("LElbowYaw")
  times.append([0.8, 1.44, 2.08])
  keys.append([-1.03323, -2.08567, -1.89607])

  names.append("LHand")
  times.append([0.8, 1.44, 2.08])
  keys.append([0, 0.7544, 0.552])

  names.append("LHipPitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([0.101286, -0.671851, -0.424876])

  names.append("LHipRoll")
  times.append([0.64, 1.36, 1.96])
  keys.append([0.092082, 0.036858, 0.0429941])

  names.append("LHipYawPitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([-0.254602, -0.309826, -0.300622])

  names.append("LKneePitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([0.352778, 0.938765, 0.742414])

  names.append("LShoulderPitch")
  times.append([0.8, 1.44, 2.08])
  keys.append([0.765425, 1.0845, 1.05995])

  names.append("LShoulderRoll")
  times.append([0.8, 1.44, 2.08])
  keys.append([0.328234, 0.299088, 0.289883])

  names.append("LWristYaw")
  times.append([0.8, 1.44, 2.08])
  keys.append([0.022968, -1.44814, -1.07691])

  names.append("RAnklePitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([-0.121144, 0.030722, -0.056716])

  names.append("RAnkleRoll")
  times.append([0.64, 1.36, 1.96])
  keys.append([0.159578, 0.168782, 0.150374])

  names.append("RElbowRoll")
  times.append([0.72, 1.28, 2])
  keys.append([1.52637, 1.31775, 1.34843])

  names.append("RElbowYaw")
  times.append([0.72, 1.28, 2])
  keys.append([0.916298, 1.93433, 1.78401])

  names.append("RHand")
  times.append([0.72, 1.28, 2])
  keys.append([0, 0.6016, 0.446])

  names.append("RHipPitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([0.116542, -0.535408, -0.323717])

  names.append("RHipRoll")
  times.append([0.64, 1.36, 1.96])
  keys.append([-0.159494, -0.0367741, -0.0705221])

  names.append("RHipYawPitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([-0.254602, -0.309826, -0.300622])

  names.append("RKneePitch")
  times.append([0.64, 1.36, 1.96])
  keys.append([0.245482, 0.520068, 0.423426])

  names.append("RShoulderPitch")
  times.append([0.72, 1.28, 2])
  keys.append([1.03856, 1.17815, 1.17815])

  names.append("RShoulderRoll")
  times.append([0.72, 1.28, 2])
  keys.append([-0.107422, -4.19617e-05, 0.00302602])

  names.append("RWristYaw")
  times.append([0.72, 1.28, 2])
  keys.append([-0.0429941, 1.43271, 1.13358])

  try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    # IP = "127.0.0.1"
    # motion = ALProxy("ALMotion", IP, 9559)
    # motion = ALProxy("ALMotion")
    motion=nao.motionProxy
    motion.angleInterpolation(names, keys, times, True)
  except BaseException, err:
    print err
