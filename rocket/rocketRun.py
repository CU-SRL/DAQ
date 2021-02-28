import threading
import queue
import RocketModule
# Instantiate all queues
sensorQueue = queue.Queue()
tlmQueue = queue.Queue() 
cmdQueue = queue.Queue()
# TODO Define rest of the queue objects




################### STATE MACHINE ###################

# * on startup we want to wait for a connection from the pilot laptop

initialRecvConfig = RocketModule.recieveConfig('127.0.0.1', 50000, '127.0.0.1', 50001)

initialRecvConfig.run()














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
