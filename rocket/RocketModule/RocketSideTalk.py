import socket
import sys
import time
import threading
import queue
import datetime
import json



class rocketSideTalk():
    
    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT):  # constructor
        self.talkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.pilotAddress = (pilotIP, pilotPORT)
        #telemetryQueue = queue.Queue(maxsize = 100)


    def run(self):
        while True:
            #message = b"<message from rocket>"
            # ! find some sort of non-blocking solution that works without MSG_DONTWAIT
            message =json.dumps([str(datetime.datetime.now()), "bru1", "kenny","ian put date here"]).encode('utf-8')

            self.talkSocket.sendto(message, self.pilotAddress)
            time.sleep(.5)

