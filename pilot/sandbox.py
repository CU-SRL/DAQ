# import json


# # buttonConfig = json.load(open("spiceShuttle.json"))

# # # for i in range(3):
# # #     print(buttonConfig["buttons"][i]["buttonLabel"])

# # for button in buttonConfig:
# #     print(button)

# print("bruh", flush = True)


import sys 
import time 
  
# for i in range(10): 
#     print(i, end =' ') 
#     sys.stdout.flush() 
#     time.sleep(1) 

while True:
    lstng = "\rlistening"
    elip = "."
    for i in range(4):
        string = lstng + elip
        sys.stdout.write(lstng + ((i) * elip))
        time.sleep(1)
        sys.stdout.write("\r             ")
        sys.stdout.flush

        # sys.stdout.write("\rlistening")
        # time.sleep(1)
        # sys.stdout.flush()
        # sys.stdout.write(" ")
        # sys.stdout.write("\rlistening.")
        # time.sleep(1)
        # sys.stdout.flush()
        # sys.stdout.write(" ")
        # sys.stdout.write("\rlistening..")
        # time.sleep(1)
        # sys.stdout.flush()
        # sys.stdout.write(" ")
        # sys.stdout.write("\rlistening...")
        # time.sleep(1)
        # sys.stdout.flush()

    # sys.stdout.write("\rbruh")
    # time.sleep(1)

    # sys.stdout.flush()

    # sys.stdout.write("\r   ")
    # time.sleep(1)

    




    # ! this one works

    # def printTalking(self): #place holder function
    #         lstng = "\rtalking"
    #         elip = "."
    #         for i in range(4):
    #             sys.stdout.write(lstng + ((i) * elip))
    #             time.sleep(1)
    #             sys.stdout.write("\r             ") #line ends
    #             sys.stdout.flush
