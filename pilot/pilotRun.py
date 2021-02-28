import tkinter as tk
import os
import time
import json
import threading
import socket
import sys
from enum import Enum

import pilotModule 




class pilotState(Enum):
    START_UP      = 1
    FIND_ROCKET   = 2
    START_LISTEN  = 3
    START_COMMAND = 4
    START_UI      = 5
    RUNNING       = 6


    






currentState = pilotState.FIND_ROCKET

if __name__ == "__main__":
    while(True):

        if(currentState == pilotState.FIND_ROCKET):

            print("State 1 -- config with rocket")

            intitialSendConfig = pilotModule.sendConfig('127.0.0.1', 50000, '127.0.0.1', 50001, "pilotModule/spiceShuttle.json")
            goodStart = intitialSendConfig.run()

            currentState = pilotState.RUNNING


        if(currentState == pilotState.RUNNING):

            print("Running")


        









#     pilotTalk_obj = pilotSideTalk('127.0.0.1', 50000, '127.0.0.1', 50001)
#     pilotListen_obj = pilotSideListen('127.0.0.1', 50000, '127.0.0.1', 50001)

#     talkThread = threading.Thread(target=pilotTalk_obj.run)
#     talkThread.start()

#     listenThread = threading.Thread(target=pilotListen_obj.run)
#     listenThread.start()

#     mainThread = pilotSide()
#     mainThread.run()


