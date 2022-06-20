import time
from naoqi import ALProxy

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tracker = ALProxy( "ALTracker" )

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.maxSpeed = 0.5

        self.useWholeBody = False
        self.frame = 0 #FRAME TORSO

    def onLoad(self):
        self.BIND_PYTHON(self.getName(), "setParameter")

    def onUnload(self):
        pass

    def onInput_onStart(self):
        self.x = self.getParameter("X (m)")
        self.y = self.getParameter("Y (m)")
        self.z = self.getParameter("Z (m)")

        self.maxSpeed = self.getParameter("Speed (%)") / 100.0
        self.useWholeBody = self.getParameter("WholeBody")

        frameStr = self.getParameter("Frame")
        if frameStr == "Torso":
            self.frame = 0
        elif frameStr == "World":
            self.frame = 1
        elif frameStr == "Robot":
            self.frame = 2

        self.tracker.lookAt([self.x, self.y, self.z], self.frame, self.maxSpeed, self.useWholeBody)
        self.onStopped()

    def onInput_onStop(self):
        self.onUnload()
        pass

    def setParameter(self, parameterName, newValue):
        GeneratedClass.setParameter(self, parameterName, newValue)

        if (parameterName == "X (m)"):
            self.x = newValue
            self.tracker.lookAt([self.x, self.y, self.z], self.frame, self.maxSpeed, self.useWholeBody)
            self.onStopped()
            return

        if (parameterName == "Y (m)"):
            self.y = newValue
            self.tracker.lookAt([self.x, self.y, self.z], self.frame, self.maxSpeed, self.useWholeBody)
            self.onStopped()
            return

        if (parameterName == "Z (m)"):
            self.z = newValue
            self.tracker.lookAt([self.x, self.y, self.z], self.frame, self.maxSpeed, self.useWholeBody)
            self.onStopped()
            return

        if (parameterName == "Speed (%)"):
            self.maxSpeed = newValue / 100.0
            return

        if (parameterName == "WholeBody"):
            self.useWholeBody = newValue
            return

        if (parameterName == "Frame"):
            if(newValue == "Torso"):
                self.frame = 0
            elif newValue == "World":
                self.frame = 1
            elif newValue == "Robot":
                self.frame = 2