import tkinter as tk
import os
import time
import json
import threading
import socket
import sys

class button:
    def __init__(self, frame, buttonLabel):
        self.btn = tk.Button(
            master = frame,
            text= buttonLabel,
            width=15,
            height=4,
            bg="blue",
            fg="blue",
            relief = tk.RAISED)

        self.btn.pack(side = tk.TOP)


