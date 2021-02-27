"""init script for rocket-side code execution

CU Souding Rocket Lab
Team Lead: Ian Faber
Team Members: Carter Mak, Lyon Foster

"""

from rocket.RocketModule.Hypervisor import *
from rocket.RocketModule.ControlWrite import *
from rocket.RocketModule.SensorRead import *
from rocket.RocketModule.RocketSideListen import *
from rocket.RocketModule.RocketSideTalk import *
import threading
import queue


# TODO Define queue objects
# TODO Instantiate classes and pass corresponding queues

# Instantiate all queues
sensorQueue = queue.Queue()
tlmQueue = queue.Queue()
cmdQueue = queue.Queue()

# Instantiate classes to execute thread functionality
hypervisor = Hypervisor(sensorQueue,tlmQueue,cmdQueue)

# Instantiate all threads
hypervisorThread = threading.Thread(target=hypervisor.threadRun,daemon=True)

# Run all threads
hypervisorThread.start()