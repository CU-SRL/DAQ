import threading
import queue
import RocketModule
import os
import time
import json
import socket
import sys
from enum import Enum

# Instantiate all queues
sensorQueue = queue.Queue()
tlmQueue = queue.Queue() 
cmdQueue = queue.Queue()
# TODO Define rest of the queue objects

class rocketState(Enum):
    START_UP      = 1
    GET_CONFIG    = 2
    START_LISTEN  = 3
    START_TALK    = 4
    RUNNING       = 5



################### STATE MACHINE ###################

# * on startup we want to wait for a connection from the pilot laptop

currentState = rocketState.START_UP

while(True):

    if(currentState == rocketState.START_UP):
        print("State ", rocketState.START_UP, " -- Starting Hypervisor")

        # Instantiate classes to execute thread functionality
        hypervisor = RocketModule.Hypervisor(sensorQueue, tlmQueue, cmdQueue)
        # TODO Instantiate classes and pass corresponding queues

        # Instantiate all threads
        # Declare as daemons so threads stop if the main process stops
        # ? Do we want hypervisor as daemon or as main thread?
        hypervisorThread = threading.Thread(target=hypervisor.threadRun, daemon=True)
        # TODO The rest of the threads

        # Run all threads
        hypervisorThread.start()

        currentState = rocketState.GET_CONFIG

    if(currentState == rocketState.GET_CONFIG):
        print("State ", rocketState.GET_CONFIG, " -- Getting config from DAQ")

        initialRecvConfig = RocketModule.recieveConfig('127.0.0.1', 50000, '127.0.0.1', 50001)
        initialRecvConfig.run()

        currentState = rocketState.START_LISTEN


    if(currentState == rocketState.START_LISTEN):
        print("State ", rocketState.START_LISTEN, " -- Starting Listening to Rocket")

        rocketListen_obj = RocketModule.rocketSideListen('127.0.0.1', 50000, '127.0.0.1', 50001)
        listenThread = threading.Thread(target=rocketListen_obj.run)
        listenThread.start()

        currentState = rocketState.START_TALK

    if(currentState == rocketState.START_TALK):
        print("State ", rocketState.START_TALK, " -- Starting talking to Rocket")

        rocketTalk_obj = RocketModule.rocketSideTalk('127.0.0.1', 50000, '127.0.0.1', 50001)
        talkThread = threading.Thread(target=rocketTalk_obj.run)
        talkThread.start()

        currentState = rocketState.RUNNING

    if (currentState == rocketState.RUNNING):
        print("State ", rocketState.RUNNING, " -- Running")

    time.sleep(.1) # rocket main loop time









# # Instantiate classes to execute thread functionality
# hypervisor = RocketModule.Hypervisor(sensorQueue, tlmQueue, cmdQueue)
# # TODO Instantiate classes and pass corresponding queues

# # Instantiate all threads
# # Declare as daemons so threads stop if the main process stops
# # ? Do we want hypervisor as daemon or as main thread?
# hypervisorThread = threading.Thread(target=hypervisor.threadRun, daemon=True)
# # TODO The rest of the threads

# # Run all threads
# hypervisorThread.start()



# if __name__ == "__main__":
    
#     rocketTalk_obj = rocketSideTalk('127.0.0.1', 50000, '127.0.0.1', 50001)
#     rocketListen_obj = rocketSideListen('127.0.0.1', 50000, '127.0.0.1', 50001)

#     talkThread = threading.Thread(target=rocketTalk_obj.run)
#     talkThread.start()

#     listenThread = threading.Thread(target=rocketListen_obj.run)
#     listenThread.start()


# while(True):
#     pass
