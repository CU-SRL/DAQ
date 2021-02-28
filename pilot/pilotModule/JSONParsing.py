import json



def ingestJSON(filename):
    with open(filename) as f:
        spiceShuttleJSON = json.load(f)

    return spiceShuttleJSON


# spiceShuttleDict = ingestJSON('spiceShuttle.json')

# print([spiceShuttleDict['devices'][i]['address'] for i in range(len(spiceShuttleDict['devices'])) if spiceShuttleDict['devices'][i]['type'] == 'ADS1115Ducer'])
