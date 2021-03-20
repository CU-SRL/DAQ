import json

class Configuration():

    def __init__(self, filename):
        self.filename = filename
        self.rawJSON = dict()
        self.thermocoupleDict = dict()
        self.ducerDict = dict()
        
    def ingestJSON(self):
        with open(self.filename) as f:
            self.rawJSON = json.load(f)
        
    def thermocouples(self):
        for i in range(len(self.rawJSON['inputs'])):
            if self.rawJSON['inputs'][i]['type'] == "ADS1115Thermo":
                self.thermocoupleDict[i] = self.rawJSON['inputs'][i]
        return self.thermocoupleDict

    def ducers(self):
        for i in range(len(self.rawJSON['inputs'])):
            if self.rawJSON['inputs'][i]['type'] == "ADS1115Ducer":
                self.ducerDict[i] = self.rawJSON['inputs'][i]
        return self.ducerDict

    def run(self):
        self.thermocoupleDict = self.thermocouples()
        self.ducerDict = self.ducers()
 
IOConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/IO.json')
buttonConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/buttons.json')

IOConfig.ingestJSON()
IOConfig.run()

for i in range(len(IOConfig.thermocoupleDict)):
    print(IOConfig.thermocoupleDict[i]['name'])

# for i in range(len(IOConfig.ducerDict)):
#     print(IOConfig.ducerDict[i]['name'])

# print(IODict['inputs'][2]['name'])
# print(ButtonDict[1]['name'])

# print([spiceShuttleDict['devices'][i]['address'] for i in range(len(spiceShuttleDict['devices'])) if spiceShuttleDict['devices'][i]['type'] == 'ADS1115Ducer'])
# from sys import platform
# if platform == "linux" or platform == "linux2":
#     # linux
# elif platform == "darwin":
#     # OS X
# elif platform == "win32":
#     # Windows...
