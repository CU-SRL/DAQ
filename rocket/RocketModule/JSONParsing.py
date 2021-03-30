import json
import os
import pathlib

class Configuration():

    def __init__(self, filename): #Function called upon "Configuration" object instantiation
        self.filename = filename
        self.rawJSON = dict()
        self.thermocoupleDict = dict()
        self.ducerDict = dict()
        self.loadCellDict = dict()
        self.servoDict = dict()
        self.buttonDict = dict()
        self.ducerOffset = 0 #Amount of index offset for correctly creating the ducer dictionary
        self.loadCellOffset = 0 #Amount of index offset for correctly creating the load cell dictionary
        
    def ingestJSON(self, configType): #Ingest JSON function, flags which parts of the raw JSON dictionary should be unpacked into dictionaries
        with open(self.filename) as f:
            self.rawJSON = json.load(f)
        if configType == "IO": #If the object is of type input/output
            self.thermoUnpack = 1
            self.ducerUnpack = 1
            self.loadUnpack = 1
            self.servoUnpack = 1
            self.buttonUnpack = 0
        elif configType == "buttons": #If the object is of type buttons
            self.thermoUnpack = 0
            self.ducerUnpack = 0
            self.loadUnpack = 0
            self.servoUnpack = 0
            self.buttonUnpack = 1
        
    def thermocouples(self): #Create a thermocouple dictionary or ignore the thermocouple entries if the object is of type buttons
        if self.thermoUnpack == 1:
            for i in range(len(self.rawJSON['inputs'])): #Loop through every input entry
                if self.rawJSON['inputs'][i]['type'] == "ADS1115Thermo": #If the input is a thermocouple
                    self.thermocoupleDict[i] = self.rawJSON['inputs'][i] #Add to the library
            return self.thermocoupleDict #Return the library
        else:
            return #Do nothing

    def ducers(self): #Create a ducer dictionary or ignore the ducer entries if the object is of type buttons
        if self.ducerUnpack == 1:
            for i in range(len(self.rawJSON['inputs'])):
                if(self.rawJSON['inputs'][i-1]['type'] == "ADS1115Thermo"): #If the previous input is a thermocouple
                    self.ducerOffset = i #Set the ducer offset (if offset not created, raw JSON index and dictionary index won't start at 0) 
                if self.rawJSON['inputs'][i]['type'] == "ADS1115Ducer":
                    self.ducerDict[i-self.ducerOffset] = self.rawJSON['inputs'][i] #Subtract the ducer offset to make sure the dictionary starts at index 0
            return self.ducerDict
        else:
            return 

    def loadCell(self): #Create a load cell dictionary or ignore the load cell entries if the object is of type buttons
        if self.loadUnpack == 1:
            for i in range(len(self.rawJSON['inputs'])):
                if(self.rawJSON['inputs'][i-1]['type'] == "ADS1115Ducer"):
                    self.loadCellOffset = i
                if self.rawJSON['inputs'][i]['type'] == "HX711":
                    self.loadCellDict[i-self.loadCellOffset] = self.rawJSON['inputs'][i]
            return self.loadCellDict
        else:
            return

    def servos(self): #Create a servo dictionary or ignore the servo entries if the object is of type buttons
        if self.servoUnpack == 1:
            for i in range(len(self.rawJSON['outputs'])):
                if self.rawJSON['outputs'][i]['type'] == "PCA9685":
                    self.servoDict[i] = self.rawJSON['outputs'][i]
            return self.servoDict
        else:
            return
        

    def buttons(self): #Create a button dictionary or ignore the button entries if the object is of type IO
        if self.buttonUnpack == 1:
            for i in range(len(self.rawJSON)):
                self.buttonDict[i] = self.rawJSON[i]
            return self.buttonDict
        else:
            return

    def run(self):
        self.thermocoupleDict = self.thermocouples() #Create the thermocouple dictionary
        self.ducerDict = self.ducers() #Create the ducer dictionary
        self.loadCellDict = self.loadCell() #Create the load cell dictionary
        self.servoDict = self.servos() #Create the servo dictionary
        self.buttonDict = self.buttons() #Create the button dictionary

# INCLUDE THIS BLOCK OF CODE TO INGEST JSON, CHANGE FILE PATHING AS NECESSARY



# IOConfig = Configuration(os.path.join(os.path.dirname( __file__ ), '..','..','configurations','IO.json'))
# buttonConfig = Configuration(os.path.join(os.path.dirname( __file__ ), '..','..','configurations','IO.json'))


# # ! old stuff for Ian's computer. Should be fine without it now
# #// IOConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/IO.json') #Create an input/output configuration object based on the IO.json file
# #//  buttonConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/buttons.json') #Create a button configuration object based on the buttons.json file

# IOConfig.ingestJSON("IO")
# IOConfig.run()
# buttonConfig.ingestJSON("buttons")
# buttonConfig.run()

# END OF NECESSARY CODE


if __name__ == "__main__":

    IOConfig = Configuration(os.path.join(os.path.dirname( __file__ ),'..','..','configurations','IO.json'))
    buttonConfig = Configuration(os.path.join(os.path.dirname( __file__ ),'..','..','configurations','buttons.json'))

    IOConfig.ingestJSON("IO")
    IOConfig.run()
    buttonConfig.ingestJSON("buttons")
    buttonConfig.run()


    for i in range(len(IOConfig.thermocoupleDict)):
        print(IOConfig.thermocoupleDict[i]['name'])

    for i in range(len(IOConfig.ducerDict)):
        print(IOConfig.ducerDict[i]['name'])

    for i in range(len(IOConfig.loadCellDict)):
        print(IOConfig.loadCellDict[i]['name'])

    for i in range(len(IOConfig.servoDict)):
        print(IOConfig.servoDict[i]['name'])

    for i in range(len(buttonConfig.buttonDict)):
        print(buttonConfig.buttonDict[i]['name'])

else:
    IOConfig = Configuration(os.path.join(os.path.dirname( __file__ ), '..','..','configurations','IO.json'))
    buttonConfig = Configuration(os.path.join(os.path.dirname( __file__ ), '..','..','configurations','buttons.json'))

    IOConfig.ingestJSON("IO")
    IOConfig.run()
    buttonConfig.ingestJSON("buttons")
    buttonConfig.run()
    
    print("JSON Has been parsed")


