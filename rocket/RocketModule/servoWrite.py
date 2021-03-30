from adafruit_servokit import ServoKit
import os
import JSONParsing

class servo():
    def __init__(self):
        self.controller = ServoKit(channels = 16)
        self.IOConfig = JSONParsing.Configuration(os.path.join(os.path.dirname( __file__ ),'..','..','configurations','IO.json'))
        self.IOConfig.ingestJSON("IO")
        self.IOConfig.run()
        self.servoList = dict()
        for i in range(len(self.IOConfig.servoDict)):
            self.servoList[i] = self.IOConfig.servoDict[i]['channel']
        
    def writeServo(self, servoIndex, angle):
        self.controller.servo[servoIndex].angle = angle
        print(self.IOConfig.servoDict[servoIndex]['purpose'], " is at ", angle, " degrees")

    def openServo(self, servoIndex):
        self.controller.servo[servoIndex].angle = self.IOConfig.servoDict[servoIndex]['fullOpen']
        print(self.IOConfig.servoDict[servoIndex]['purpose'], " is at ", self.IOConfig.servoDict[servoIndex]['fullOpen'], " degrees")

    def openServoHalf(self, servoIndex):
        self.controller.servo[servoIndex].angle = self.IOConfig.servoDict[servoIndex]['partialOpen']
        print(self.IOConfig.servoDict[servoIndex]['purpose'], " is at ", self.IOConfig.servoDict[servoIndex]['partialOpen'], " degrees")

    def closeServo(self, servoIndex):
        self.controller.servo[servoIndex].angle = self.IOConfig.servoDict[servoIndex]['fullClose']
        print(self.IOConfig.servoDict[servoIndex]['purpose'], " is at ", self.IOConfig.servoDict[servoIndex]['fullClose'], " degrees")

servos = servo()
servos.writeServo(servos.servoList[0], 30)
servos.openServo(servos.servoList[1])
servos.openServoHalf(servos.servoList[2])
servos.closeServo(servos.servoList[3])
