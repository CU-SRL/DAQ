from adafruit_servokit import ServoKit
import os
import JSONParsing

class Servo():
    def __init__(self, IOConfig):
        self.controller = ServoKit(channels = 16)
        self.IOConfig = IOConfig
        self.servoList = dict()
        for i in range(len(self.IOConfig.servoDict)):
            self.servoList[i] = self.IOConfig.servoDict[i]['channel']
        
    def writeServo(self, servoIndex, angle):
        self.controller.servo[servoIndex].angle = angle
        print(self.IOConfig.servoDict[servoIndex]['purpose'], " is at ", angle, " degrees")

if __name__ == "__main__":
    servos = Servo(JSONParsing.IOConfig)
    servos.writeServo(servos.servoList[0], 0)
    servos.writeServo(servos.servoList[1], 15)
    servos.writeServo(servos.servoList[2], 30)
    servos.writeServo(servos.servoList[3], 45)
    servos.writeServo(servos.servoList[4], 60)
    servos.writeServo(servos.servoList[0], 75)
    servos.writeServo(servos.servoList[1], 90)
else:
    servos = Servo(JSONParsing.IOConfig)




