import tkinter as tk
import os
import time
import json
import threading
import socket
import sys


class telemetryDisplay:

    def __init__(self, frame, label):
        self.defaultText = "NAN"
        self.telemetry_label = label    
        self.frame = frame

        self.display = tk.Label(master = frame, text = label)
        self.display.pack(side = tk.TOP)




