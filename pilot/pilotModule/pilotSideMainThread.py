import tkinter as tk
import os
import time
import json
import threading
import socket
import sys
from JSONParsing import *
from button import * 
#from pilotModule import *
# from pilotModule.button import *

class pilotSide:
    
    # ********* Button handler functions ************
    def defaultHandler(self, event):
        print("Epstein didn't kill himself")

    def buttonInnactive(self, event):
        print("button inactive")


    def __init__(self):
        self.window = tk.Tk()
        self.frm1 = tk.Frame()


        #TODO (TICKET 2) fix button background color for MAC
            #TODO currently all buttons have a white background for MAC
            #TODO we need to fix this to according to Owen's spec that this is easy to read in high stress situations (req. 1.1)

        # ************ Button creation ************
        # buttonConfig = json.load(open("pilotModule/spiceShuttle.json"))
        # buttonList = []
        # # for i in range(buttonConfig["numOfButtons"]):
        # #     buttonList.append(button(self.frm1, buttonConfig["buttons"][i]["buttonLabel"]))

        #print(buttonConfig.buttonDict())

        
        #TODO Ian put the config json stuff in here
        buttonList = []

        
        for i in range(len(JSONParsing.buttonConfig.buttonDict)):
            buttonList.append(button(self.frm1.JSONParsing.buttonConfig.buttonDict[i]['name']))
        # ************ Assign button handlers ************
            #! We will initialize the interface with some sort of "inactive" button handler
        for instance in buttonList:
            instance.btn.bind("<Button-1>", self.defaultHandler)

        self.frm1.pack(side = tk.LEFT)


        

# ************ Main function of main thread ************
    def run(self):
        while (True):
            self.window.update()
            self.window.update_idletasks()
            time.sleep(.1)
