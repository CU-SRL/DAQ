import tkinter as tk
import os
import time
import json
import threading
import socket
import sys


# ! treating rocket/raspberryPi as server
class recieveConfig():

    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT):
        self.initialRecvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pilotIP = pilotIP
        self.pilotPort = pilotPORT
        self.rocketIP = rocketIP
        self.rocketPORT = rocketPORT

        

    def run(self):
        self.initialRecvSocket.bind((self.rocketIP,self.rocketPORT))
        print("bound")

        while(True):
            self.initialRecvSocket.listen()
            print("listended")
            conn, addr = self.initialRecvSocket.accept()
            print("accepted")
            print(addr)
            print((self.rocketIP, self.rocketPORT))

            if (addr == (self.pilotIP, self.pilotPort)):
                with conn:

                    print(addr)
                    data = conn.recv(1024)
                    # print(data)
                    conn.sendall(b"all good -rocket")


                    self.initialRecvSocket.close()
                    return data
            else:
                print("Attempted connection from non-pilot address")


