# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.162851, -0.162851, -0.162851, -0.162851, -0.162851, -0.162851, -0.162851, -0.162851])

names.append("HeadYaw")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0, 0, 0, 0, 0, 0, 0, 0])

names.append("LAnklePitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.0837433, 0.0837433, 0.0837433, 0.0837433, 0.0837433, 0.0837433, 0.0837433, 0.0837433])

names.append("LAnkleRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.106134, -0.106134, -0.106134, -0.106134, -0.106134, -0.106134, -0.106134, -0.106134])

names.append("LElbowRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.414821, -0.414821, -0.414821, -0.414821, -0.414821, -0.414821, -0.414821, -0.414821])

names.append("LElbowYaw")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-1.19838, -1.19838, -1.19838, -1.19838, -1.19838, -1.19838, -1.19838, -1.19838])

names.append("LHand")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.298236, 0.298236, 0.298236, 0.298236, 0.298236, 0.298236, 0.298236, 0.298236])

names.append("LHipPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.122061, 0.122061, 0.122061, 0.122061, 0.122061, 0.122061, 0.122061, 0.122061])

names.append("LHipRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141])

names.append("LHipYawPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.16286, -0.16286, -0.16286, -0.16286, -0.16286, -0.16286, -0.16286, -0.16286])

names.append("LKneePitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454])

names.append("LShoulderPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([1.43487, 1.43487, 1.43487, 1.43487, 1.43487, 1.43487, 1.43487, 1.43487])

names.append("LShoulderRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.220831, 0.220831, 0.220831, 0.220831, 0.220831, 0.220831, 0.220831, 0.220831])

names.append("LWristYaw")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.0928924])

names.append("RAnklePitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.0837432, 0.0837432, 0.0837432, 0.0837432, 0.0837432, 0.0837432, 0.0837432, 0.0837432])

names.append("RAnkleRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.10613, 0.10613, 0.10613, 0.10613, 0.10613, 0.10613, 0.10613, 0.10613])

names.append("RElbowRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.0446726, 0.0446726, 0.0446726, 0.0446726, 0.0446726, 0.0446726, 0.0446726, 0.4259])

names.append("RElbowYaw")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.256213, -0.256213, -0.256213, -0.256213, -0.256213, -0.256213, -0.256213, 1.22677])

names.append("RHand")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.888956, 0.888956, 0.888956, 0.888956, 0.888956, 0.888956, 0.888956, 0.270533])

names.append("RHipPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.122061, 0.122061, 0.122061, 0.122061, 0.122061, 0.122061, 0.122061, 0.122061])

names.append("RHipRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.114094, -0.114094, -0.114094, -0.114094, -0.114094, -0.114094, -0.114094, -0.114094])

names.append("RHipYawPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.16286, -0.16286, -0.16286, -0.16286, -0.16286, -0.16286, -0.16286, -0.16286])

names.append("RKneePitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454, -0.0884454])

names.append("RShoulderPitch")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-1.29359, -1.29359, -1.29359, -1.29359, -1.29359, -1.29359, -1.29359, 1.44898])

names.append("RShoulderRoll")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([-0.798616, -0.0487493, -0.654052, -0.032705, -0.732316, -0.00405653, -0.765795, -0.224374])

names.append("RWristYaw")
times.append([0.36, 0.76, 1.16, 1.56, 1.92, 2.28, 2.68, 3.04])
keys.append([0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.0928924, 0.389392])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
