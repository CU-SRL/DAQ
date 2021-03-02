import json



def ingestJSON(filename):
    with open(filename) as f:
        spiceShuttleJSON = json.load(f)

    return spiceShuttleJSON


configJSON = ingestJSON('pilotModule/spiceShuttle.json')

dataLabels_list = []
for i in range(len(configJSON["devices"])):

    for j in range(len(configJSON["devices"][i])):

        print(configJSON["devices"][i]["name"])


# print(dataLabels_list)

