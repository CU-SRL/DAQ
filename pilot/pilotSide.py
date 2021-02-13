import tkinter as tk
import os
import time
import json
import threading
import socket
import sys


class pilotSide:

    # ********* Button handler functions ************
    def defaultHandler(self, event):
        print("Epstien didn't kill himself")


    def __init__(self):
        self.window = tk.Tk()
        self.frm1 = tk.Frame()

        # for certain set's of hardware we should have corresponing json config files
        #TODO (TICKET 1) clean up json ingestions
            #TODO let's make it easy for the user to pass in the filename that they'd like
            #TODO come up with some easy format for the json that's easy for prop teams to write and for us to use
                # I think we're going to need different flavors of button (on/off, servos)


        #TODO (TICKET 2) fix button background color for MAC
            #TODO currently all buttons have a white background for MAC
            #TODO we need to fix this to according to Owen's spec that this is easy to read in high stress situations (req. 1.1)

        # ************ Button creation ************
        buttonConfig = json.load(open("spiceShuttle.json"))
        buttonList = []
        for i in range(buttonConfig["numOfButtons"]):
            buttonList.append(button(self.frm1, buttonConfig["buttons"][i]["buttonLabel"]))

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





class pilotSideListen:

    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT):
        self.listenSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pilotAddress = (pilotIP, pilotPORT)
        self.rocketAddress = (rocketIP, rocketPORT)

        self.listenSocket.bind(self.pilotAddress)

    def run(self):
        while True:
            data = self.listenSocket.recv(1024)
            print("Message recieved from rocket: %s" % data)
            time.sleep(.4)


class pilotSideTalk:
    
    def __init__(self, pilotIP, pilotPORT, rocketIP, rocketPORT):
        self.talkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pilotAddress = (pilotIP, pilotPORT)
        self.rocketAddress = (rocketIP, rocketPORT)

    def run(self):
        while True:
            message = b"<message from pilot>"
            self.talkSocket.sendto(message, socket.MSG_DONTWAIT, self.rocketAddress)
            time.sleep(.5)
           






if __name__ == "__main__":

    pilotTalk_obj = pilotSideTalk('127.0.0.1', 50000, '127.0.0.1', 50001)
    pilotListen_obj = pilotSideListen('127.0.0.1', 50000, '127.0.0.1', 50001)

    talkThread = threading.Thread(target=pilotTalk_obj.run)
    talkThread.start()

    listenThread = threading.Thread(target=pilotListen_obj.run)
    listenThread.start()

    mainThread = pilotSide()
    mainThread.run()


