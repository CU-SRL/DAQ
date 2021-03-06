import tkinter as tk
import os
import time
import json
import threading
import socket
import sys
import io
import csv
import queue

class pilotSideListen:

    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT, telemQ):
        self.listenSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pilotAddress = (pilotIP, pilotPORT)
        self.rocketAddress = (rocketIP, rocketPORT)

        self.listenSocket.bind(self.pilotAddress)
        self.telemetryQueue = telemQ

    def run(self):
        while True:
            data = self.listenSocket.recv(1024)
            print("Message recieved from rocket: %s" % data)
            self.telemetryQueue.put(json.loads(data))
            time.sleep(.4)

        
