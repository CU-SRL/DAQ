"""hypervisor thread to execute control law based on sensor data and commands

CU Souding Rocket Lab
Team Lead: Ian Faber
Team Members: Carter Mak, Lyon Foster

"""

import threading
import queue

"""Collected functionality for hypervisor thread execution

Can be inherited and the threadRun() method can be overwritten
"""


class Hypervisor:
    def __init__(self, sensorQueue, tlmQueue, cmdQueue):
        self.sensorQueue = sensorQueue
        self.tlmQueue = tlmQueue
        self.cmdQueue = cmdQueue

    def threadRun(self):
        # TODO Do the things
        print('Hypervisor thread executing')
        return
