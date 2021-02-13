import socket
import sys
import time




class rocketSideTalk(): 
    
    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as talkSocket:

            message = None
            
            talkSocket.sendto()


    def run(self):
        while True:
        lstng = "\rtalking"
        elip = "."
        for i in range(4):
            sys.stdout.write(lstng + ((i) * elip))
            time.sleep(1)
            sys.stdout.write("\r             ")
            sys.stdout.flush


class rocketSideListen():
    


    def run(self):
        while True:
            lstng = "\rlistening"
            elip = "."
            for i in range(4):
                sys.stdout.write(lstng + ((i) * elip))
                time.sleep(1)
                sys.stdout.write("\r             ")
                sys.stdout.flush



bruh = rocketSideListen()

bruh.run()