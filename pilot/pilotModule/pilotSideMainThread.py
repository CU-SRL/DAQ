import tkinter as tk
import os
import time
import json
import threading
import socket
import sys
import pilotModule.button as buttonModule
import pilotModule.telemetryDisplay as telemetryDisplayModule
import pilotModule.JSONParsing as JSONParsing
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


        # ************ Loaded Dictionary ************
        configJSON = JSONParsing.ingestJSON("pilotModule/spiceShuttle.json")

        # ************ Button creation ************
        buttonName_list = []
        for i in range(len(configJSON["buttons"])):
            buttonName_list.append(buttonModule.button(self.frm1,configJSON["buttons"][i]["name"]))

            #! We will initialize the interface with some sort of "inactive" button handler
        for instance in buttonName_list:
            instance.btn.bind("<Button-1>", self.defaultHandler)

        # ************ Data Display ************
        dataLabels_list = []

        for i in range(10):
            dataLabels_list.append(telemetryDisplayModule.telemetryDisplay(self.frm2,"Cheems Baby!\nbruh\n\n"))


        self.frm1.pack(side = tk.LEFT)
        self.frm2.pack(side = tk.RIGHT)


        

# ************ Main function of main thread ************
    def run(self):
        while (True):
            self.window.update()
            self.window.update_idletasks()
            time.sleep(.1)
