import socket
import sys
import time
import threading





class rocketSideTalk():
    
    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT):  # constructor
        self.talkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.pilotAddress = (pilotIP, pilotPORT)

    def run(self):
        while True:
            message = b"<message from rocket>"
            # ! find some sort of non-blocking solution that works without MSG_DONTWAIT
            self.talkSocket.sendto(message, self.pilotAddress)
            time.sleep(.5)

