# ! might be deprecating this and replacing with rocker/run.py




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


