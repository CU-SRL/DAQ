import socket
import sys
import time




class rocketSideTalk(): 
    
<<<<<<< HEAD
    def __init__(self, rocketIP, rocketPORT, pilotIP, pilotPORT): #constructor
        self.talkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.pilotAddress = (pilotIP, pilotPORT)

=======
    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as talkSocket:

            message = None
            
            talkSocket.sendto()
>>>>>>> 10e3d3ded0d1678e4c543c6bffddb58660828d78


    def run(self):
        while True:
<<<<<<< HEAD

            message = b"<message from rocket>"
            self.talkSocket.sendto(message, self.pilotAddress)
            time.sleep(.5)





    # def printTalking(self): #place holder function
    #         lstng = "\rtalking"
    #         elip = "."
    #         for i in range(4):
    #             sys.stdout.write(lstng + ((i) * elip))
    #             time.sleep(1)
    #             sys.stdout.write("\r             ") #line ends
    #             sys.stdout.flush
=======
        lstng = "\rtalking"
        elip = "."
        for i in range(4):
            sys.stdout.write(lstng + ((i) * elip))
            time.sleep(1)
            sys.stdout.write("\r             ")
            sys.stdout.flush
>>>>>>> 10e3d3ded0d1678e4c543c6bffddb58660828d78


class rocketSideListen():
    

<<<<<<< HEAD
    def __init__(self, rocketIP, rocketPORT, pilotIP, pilotPORT):
        self.listenSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rocketAddress = (rocketIP, rocketPORT)
        self.pilotAddress = (pilotIP, pilotPORT)

        self.listenSocket.bind(self.rocketAddress)


    def run(self):

        while True:

            data = self.listenSocket.recv(1024)
            print("recieved from pilot: %s" % data)

            

        
    # def run(self): #place holder function
    #     while True:
    #         lstng = "\rlistening"
    #         elip = "."
    #         for i in range(4):
    #             sys.stdout.write(lstng + ((i) * elip))
    #             time.sleep(1)
    #             sys.stdout.write("\r             ") #line ends
    #             sys.stdout.flush

=======

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
>>>>>>> 10e3d3ded0d1678e4c543c6bffddb58660828d78
