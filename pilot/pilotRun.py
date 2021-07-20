import tkinter as tk
import os
import time
import json
import threading
import socket
import sys
from enum import IntEnum
import queue
import signal

#from pilotModule import *
import pilotModule

cmdQ = queue.Queue(maxsize=100)
telemQ = queue.Queue(maxsize=100)
displayQ = queue.Queue(maxsize=100)

class pilotState(IntEnum):
    START_UP      = 1
    FIND_ROCKET   = 2
    START_LISTEN  = 3
    START_TALK    = 4
    START_UI      = 5
    RUNNING       = 6
    EXIT          = 7



currentState = pilotState.START_UP


if __name__ == "__main__":
    
    while(True):
        try:
            if(currentState == pilotState.START_UP):
                print("State ", int(pilotState.START_UP),  "-- Starting Up")

                loggingObj = pilotModule.loggingTelem(telemQ)
                loggingThread = threading.Thread(target = loggingObj.logTelem) 
                loggingThread.start()

                currentState = pilotState.FIND_ROCKET

            if(currentState == pilotState.FIND_ROCKET):

                print("State ", int(pilotState.FIND_ROCKET), " -- Find Rocket")

                #This pulls the filename member from the JSONParsing Configuration class so I don't have to do more file path nonsense
                configFileName = pilotModule.IOConfig.filename

                intitialSendConfig = pilotModule.sendConfig('127.0.0.1', 50000, '127.0.0.1', 50001, configFileName)
                goodStart = intitialSendConfig.run()

                currentState = pilotState.START_LISTEN

            if(currentState == pilotState.START_LISTEN):
                print("State ", pilotState.START_LISTEN, " -- Starting Listening to Rocket")

                pilotListen_obj = pilotModule.pilotSideListen('127.0.0.1', 50000, '127.0.0.1', 50001, telemQ, displayQ)
                listenThread = threading.Thread(target=pilotListen_obj.run)
                listenThread.daemon = True
                listenThread.start()

                currentState = pilotState.START_TALK

            if(currentState == pilotState.START_TALK):
                print("State ", pilotState.START_TALK, " -- Starting Talking to Rocket")

                pilotTalk_obj = pilotModule.pilotSideTalk('127.0.0.1', 50000, '127.0.0.1', 50001, cmdQ)
                talkThread = threading.Thread(target=pilotTalk_obj.run)
                talkThread.daemon = True
                talkThread.start()

                currentState = pilotState.START_UI

            if(currentState == pilotState.START_UI):
                #This is where we will assign the correct button handles and recolor  
                print("State ", pilotState.START_UI, " -- Starting UI")
                mainThread = pilotModule.pilotSide(displayQ, cmdQ)
                mainThread.run()

            if(currentState == pilotState.RUNNING):

                print("State ", pilotState.RUNNING, " -- Running")
                time.sleep(1)

            # State machine run frequency
            time.sleep(.25)

        except KeyboardInterrupt:
            # Print Shutdown statement
            print("Shutting Down Pilot! ...")

            loggingObj.run_flag.set()
            loggingThread.join()

            # Close csv gracefully
            loggingObj.close_csv()

            break

    exit()

    
