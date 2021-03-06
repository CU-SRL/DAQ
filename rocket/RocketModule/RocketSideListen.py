import socket
import sys
import time
import threading


# Thread for recieving data and commands from the groundstation

class rocketSideListen():
    
    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT):
        self.listenSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.pilotAddress = (pilotIP, pilotPORT)

        self.listenSocket.bind(self.rocketAddress)

    def run(self):
        while True:
            data = self.listenSocket.recv(1024)
            print("recieved from pilot: %s" % data)
            time.sleep(.4)



