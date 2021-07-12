import tkinter as tk
import os
import time
import json
import threading
import socket
import sys


class pilotSideTalk:
    
    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT, cmdQ):
        self.talkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pilotAddress = (pilotIP, pilotPORT)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.commandQueue = cmdQ

    def run(self):
        while True:
            if(self.commandQueue.empty()):
                message = b"no command"
            else:
                message = commandQueue.get()
            # ! find some sort of non-blocking solution that works without MSG_DONTWAIT
            self.talkSocket.sendto(message, self.rocketAddress)
            time.sleep(.5)
           
