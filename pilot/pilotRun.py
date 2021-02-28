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


    



intitialSendConfig = pilotModule.sendConfig('127.0.0.1', 50000, '127.0.0.1', 50001, "pilotModule/spiceShuttle.json")
intitialSendConfig.run()


# currentState = pilotState.START_UP

# if __name__ == "__main__":

#     if(currentState == pilotState.START_UP):
        









#     pilotTalk_obj = pilotSideTalk('127.0.0.1', 50000, '127.0.0.1', 50001)
#     pilotListen_obj = pilotSideListen('127.0.0.1', 50000, '127.0.0.1', 50001)

#     talkThread = threading.Thread(target=pilotTalk_obj.run)
#     talkThread.start()

#     listenThread = threading.Thread(target=pilotListen_obj.run)
#     listenThread.start()

#     mainThread = pilotSide()
#     mainThread.run()


