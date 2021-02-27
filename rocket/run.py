import threading
import queue
import RocketModule
# Instantiate all queues
sensorQueue = queue.Queue()
tlmQueue = queue.Queue()
cmdQueue = queue.Queue()
# TODO Define rest of the queue objects

# Instantiate classes to execute thread functionality
hypervisor = RocketModule.Hypervisor(sensorQueue, tlmQueue, cmdQueue)
# TODO Instantiate classes and pass corresponding queues

# Instantiate all threads
# Declare as daemons so threads stop if the main process stops
hypervisorThread = threading.Thread(target=hypervisor.threadRun, daemon=True)
# TODO The rest of the threads

# Run all threads
hypervisorThread.start()
