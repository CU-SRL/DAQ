import tkinter as tk
import os
import time
import json
import threading
import socket
import sys



class sendConfig():

    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT, configFile):
        self.initialSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.initialSocket.bind((pilotIP, pilotPORT))

        self.pilotIP = pilotIP
        self.pilotPort = pilotPORT
        self.rocketIP = rocketIP
        self.rocketPORT = rocketPORT

        self.configJson = json.load(open(configFile))

    def run(self):
        self.initialSocket.connect((self.rocketIP, self.rocketPORT))
        print("connected")

        self.initialSocket.sendall(json.dumps(self.configJson).encode('utf-8'))
        print("sent")

        data, recvAddress = self.initialSocket.recvfrom(1024)
        print("data received")
        if(recvAddress == (self.rocketIP, self.rocketPORT)):
            print("good handshake with rocket")

        print(data.decode('utf-8'))

        
        self.initialSocket.close()

