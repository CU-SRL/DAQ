import json

## no more than 2 lists in json

class Configuration():

    def __init__(self,filename):
        self.filename = filename

    def ingestJSON(self,filename):
        with open(self.filename) as f:
            RawJSON = json.load(f) 
        
        return RawJSON

IOConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/IO.json')
ButtonConfig = Configuration('c:/Users/ianmf/Documents/SRLDAQRepo/configurations/buttons.json')

IODict = IOConfig.ingestJSON('IO.json')
ButtonDict = ButtonConfig.ingestJSON('buttons.json')

print(IODict['inputs'][2]['name'])
print(ButtonDict[1]['name'])

# print([spiceShuttleDict['devices'][i]['address'] for i in range(len(spiceShuttleDict['devices'])) if spiceShuttleDict['devices'][i]['type'] == 'ADS1115Ducer'])
