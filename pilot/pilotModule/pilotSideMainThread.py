import tkinter as tk
import os
import time
import json
import threading
import socket
import sys
from pilotModule.JSONParsing import *
from pilotModule.button import * 
from pilotModule.textDisplay import *
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
        self.frm2 = tk.Frame()
        self.frm3 = tk.Frame()


        #TODO (TICKET 2) fix button background color for MAC
            #TODO currently all buttons have a white background for MAC
            #TODO we need to fix this to according to Owen's spec that this is easy to read in high stress situations (req. 1.1)


        # ************ Button creation ************
        # Buttons from the configuration file
        buttonList = []
        
        for i in range(len(buttonConfig.buttonDict)):
            buttonList.append(button(self.frm1, buttonConfig.buttonDict[i]['name']))
        # ************ Assign button handlers ************
            #! We will initialize the interface with some sort of "inactive" button handler
            #The buttons will get an actuall callback once the state machine deems it necessary
        for instance in buttonList:
            instance.btn.bind("<Button-1>", self.defaultHandler)

        self.frm1.pack(side = tk.LEFT)
        
        # Buttons for scamble and run test

        scrambleButton = button(self.frm2, "SCRAMBLE")
        runTestButton = button(self.frm2, "Run Test")

        scrambleButton.btn.bind("<Button-1>", self.defaultHandler)
        runTestButton.btn.bind("<Button-1>", self.defaultHandler)
        self.frm2.pack(side = tk.LEFT)
        

        #Text Box
        self.textList = []

        # Import the button names from the config json

        for i in range(len(IOConfig.thermocoupleDict)):
            self.textList.append(textDisplay(self.frm3, IOConfig.thermocoupleDict[i]['name']))

        for i in range(len(IOConfig.ducerDict)):
            self.textList.append(textDisplay(self.frm3, IOConfig.ducerDict[i]['name']))

        for i in range(len(IOConfig.loadCellDict)):
            self.textList.append(textDisplay(self.frm3, IOConfig.loadCellDict[i]['name']))

        for i in range(len(IOConfig.servoDict)):
            self.textList.append(textDisplay(self.frm3, IOConfig.servoDict[i]['name']))

        
        self.frm3.pack(side = tk.RIGHT)






    def pilotUpdate(self):

        #This function will handle poping from the TLM queue and pushing commands to the CMD queue
        #I can't be fucked to do this rn so for now the text will just be the word "bruh"

       
        for instance in self.textList:
            instance.textBox.configure(text = instance.title + "\n" + "bruh") 


# ************ Main function of main thread ************
    def run(self):
        while (True):
            self.window.update()
            self.window.update_idletasks()
            self.pilotUpdate()
            time.sleep(.1)
