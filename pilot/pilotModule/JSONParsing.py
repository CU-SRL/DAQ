import json

class Configuration():

    def __init__(self, filename):
        self.filename = filename
        self.rawJSON = dict()
        self.thermocoupleDict = dict()
        self.ducerDict = dict()
        self.loadCellDict = dict()
        self.servoDict = dict()
        self.buttonDict = dict()
        self.ducerOffset = 0
        self.loadCellOffset = 0
        
    def ingestJSON(self, configType):
        with open(self.filename) as f:
            self.rawJSON = json.load(f)
        if configType == "IO":
            self.thermoUnpack = 1
            self.ducerUnpack = 1
            self.loadUnpack = 1
            self.servoUnpack = 1
            self.buttonUnpack = 0
        elif configType == "buttons":
            self.thermoUnpack = 0
            self.ducerUnpack = 0
            self.loadUnpack = 0
            self.servoUnpack = 0
            self.buttonUnpack = 1
        
    def thermocouples(self):
        if self.thermoUnpack == 1:
            for i in range(len(self.rawJSON['inputs'])):
                if self.rawJSON['inputs'][i]['type'] == "ADS1115Thermo":
                    self.thermocoupleDict[i] = self.rawJSON['inputs'][i]
            return self.thermocoupleDict
        else:
            return 

    def ducers(self):
        if self.ducerUnpack == 1:
            for i in range(len(self.rawJSON['inputs'])):
                if(self.rawJSON['inputs'][i-1]['type'] == "ADS1115Thermo"):
                    self.ducerOffset = i
                if self.rawJSON['inputs'][i]['type'] == "ADS1115Ducer":
                    self.ducerDict[i-self.ducerOffset] = self.rawJSON['inputs'][i]
            return self.ducerDict
        else:
            return 

    def loadCell(self):
        if self.loadUnpack == 1:
            for i in range(len(self.rawJSON['inputs'])):
                if(self.rawJSON['inputs'][i-1]['type'] == "ADS1115Ducer"):
                    self.loadCellOffset = i
                if self.rawJSON['inputs'][i]['type'] == "HX711":
                    self.loadCellDict[i-self.loadCellOffset] = self.rawJSON['inputs'][i]
            return self.loadCellDict
        else:
            return

    def servos(self):
        if self.servoUnpack == 1:
            for i in range(len(self.rawJSON['outputs'])):
                if self.rawJSON['outputs'][i]['type'] == "PCA9685":
                    self.servoDict[i] = self.rawJSON['outputs'][i]
            return self.servoDict
        else:
            return
        

    def buttons(self):
        if self.buttonUnpack == 1:
            for i in range(len(self.rawJSON)):
                self.buttonDict[i] = self.rawJSON[i]
            return self.buttonDict
        else:
            return

    def run(self):
        self.thermocoupleDict = self.thermocouples()
        self.ducerDict = self.ducers()
        self.loadCellDict = self.loadCell()
        self.servoDict = self.servos()
        self.buttonDict = self.buttons()
 
IOConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/IO.json')
buttonConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/buttons.json')

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

# print([spiceShuttleDict['devices'][i]['address'] for i in range(len(spiceShuttleDict['devices'])) if spiceShuttleDict['devices'][i]['type'] == 'ADS1115Ducer'])
# from sys import platform
# if platform == "linux" or platform == "linux2":
#     # linux
# elif platform == "darwin":
#     # OS X
# elif platform == "win32":
#     # Windows...
