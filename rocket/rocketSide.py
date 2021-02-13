import socket
import sys
import time




class rocketSideTalk(): 
    

    def __init__(self, rocketIP, rocketPORT, pilotIP, pilotPORT): #constructor
        self.talkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.pilotAddress = (pilotIP, pilotPORT)


    def run(self):
        while True:

            message = b"<message from rocket>"
            self.talkSocket.sendto(message, self.pilotAddress)
            time.sleep(.5)





    # def printTalking(self): #place holder function
    #         lstng = "\rtalking"
    #         elip = "."
    #         for i in range(4):
    #             sys.stdout.write(lstng + ((i) * elip))
    #             time.sleep(1)
    #             sys.stdout.write("\r             ") #line ends
    #             sys.stdout.flush


class rocketSideListen():
    

    def __init__(self, rocketIP, rocketPORT, pilotIP, pilotPORT):
        self.listenSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.pilotAddress = (pilotIP, pilotPORT)

        self.listenSocket.bind(self.rocketAddress)


    def run(self):

        while True:

            data = self.listenSocket.recv(1024)
            print("recieved from pilot: %s" % data)

            

        
    # def run(self): #place holder function
    #     while True:
    #         lstng = "\rlistening"
    #         elip = "."
    #         for i in range(4):
    #             sys.stdout.write(lstng + ((i) * elip))
    #             time.sleep(1)
    #             sys.stdout.write("\r             ") #line ends
    #             sys.stdout.flush


