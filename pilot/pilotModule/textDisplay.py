import tkinter as tk 
import os
import time
import json
import threading
import socket
import sys
from pilotModule.JSONParsing import *
from pilotModule.button import * 

class textDisplay:
    def __init__(self, frame, title):
        self.value = ""
        self.message = title + self.value
        self.title = title        
        self.textBox = tk.Label(
                master = frame,
                text = self.message,
                width = 15,
                height = 2,
                bg = "blue",
                fg = "red",
                relief = tk.SUNKEN)


        self.textBox.pack(side = tk.TOP)




