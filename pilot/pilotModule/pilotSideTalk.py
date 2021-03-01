import tkinter as tk
import os
import time
import json
import threading
import socket
import sys


class pilotSideTalk:
    
    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT):
        self.talkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pilotAddress = (pilotIP, pilotPORT)
        self.rocketAddress = (rocketIP, rocketPORT)

    def run(self):
        while True:
            message = b"<message from pilot>"
            # ! find some sort of non-blocking solution that works without MSG_DONTWAIT
            self.talkSocket.sendto(message, self.rocketAddress)
            time.sleep(.5)
           