import Adafruit_ADS1x15

# This section for testing only
import json

def ingestJSON(filename):
    with open(filename) as f:
        spiceShuttleJSON = json.load(f)

    return spiceShuttleJSON
#Above section for testing only

JSONDict = ingestJSON('spiceShuttle.json')
adc0 = JSONDict['devices'][0]['name']
adc1 = JSONDict['devices'][1]['name']
adc2 = JSONDict['devices'][2]['name']
adc3 = JSONDict['devices'][3]['name']
ADCScale = [JSONDict['devices'][0]['scaleADCtoVoltage'], JSONDict['devices'][1]['scaleADCtoVoltage'], JSONDict['devices'][2]['scaleADCtoVoltage'], JSONDict['devices'][3]['scaleADCtoVoltage']]
ADCGain = [JSONDict['devices'][0]['gain'], JSONDict['devices'][1]['gain'], JSONDict['devices'][2]['gain'], JSONDict['devices'][3]['gain']]
ducerPressureScale1 = [JSONDict['devices'][2]['transducers'][0]['scaleVoltagetoPressure'],JSONDict['devices'][2]['transducers'][1]['scaleVoltagetoPressure'],JSONDict['devices'][2]['transducers'][2]['scaleVoltagetoPressure'],JSONDict['devices'][2]['transducers'][3]['scaleVoltagetoPressure']]
ducerPressureScale2 = [JSONDict['devices'][3]['transducers'][0]['scaleVoltagetoPressure'],JSONDict['devices'][3]['transducers'][1]['scaleVoltagetoPressure'],JSONDict['devices'][3]['transducers'][2]['scaleVoltagetoPressure'],JSONDict['devices'][3]['transducers'][3]['scaleVoltagetoPressure']]

adc0 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][0]['address'],busnum=1)
adc1 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][1]['address'],busnum=1)
adc2 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][2]['address'],busnum=1)
adc3 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][3]['address'],busnum=1)

def readSensors():
    #First ADS1115
    if(JSONDict['devices'][0]['thermocouples'][0]['purpose'] != "N/A"):
        tempVolt0 = adc0.read(0,ADCGain[0])*ADCScale[0]
    else:
        tempVolt0 = 0

    if(JSONDict['devices'][0]['thermocouples'][1]['purpose'] != "N/A"):
        tempVolt1 = adc0.read(1,ADCGain[0])*ADCScale[0]
    else:
        tempVolt1 = 0
    
    if(JSONDict['devices'][0]['thermocouples'][2]['purpose'] != "N/A"):
        tempVolt2 = adc0.read(2,ADCGain[0])*ADCScale[0]
    else:
        tempVolt2 = 0

    if(JSONDict['devices'][0]['thermocouples'][3]['purpose'] != "N/A"):
        tempVolt3 = adc0.read(3,ADCGain[0])*ADCScale[0]
    else:
        tempVolt3 = 0

    #Second ADS1115
    if(JSONDict['devices'][1]['thermocouples'][0]['purpose'] != "N/A"):
        tempVolt4 = adc0.read(0,ADCGain[1])*ADCScale[1]
    else:
        tempVolt4 = 0

    if(JSONDict['devices'][1]['thermocouples'][1]['purpose'] != "N/A"):
        tempVolt5 = adc0.read(1,ADCGain[1])*ADCScale[1]
    else:
        tempVolt5 = 0
    
    if(JSONDict['devices'][1]['thermocouples'][2]['purpose'] != "N/A"):
        tempVolt6 = adc0.read(2,ADCGain[1])*ADCScale[1]
    else:
        tempVolt6 = 0

    if(JSONDict['devices'][1]['thermocouples'][3]['purpose'] != "N/A"):
        tempVolt7 = adc0.read(3,ADCGain[1])*ADCScale[1]
    else:
        tempVolt7 = 0

    #Third ADS1115
    if(JSONDict['devices'][2]['transducers'][0]['purpose'] != "N/A"):
        pressureVolt0 = adc0.read(0,ADCGain[2])*ADCScale[2]
    else:
        pressureVolt0 = 0

    if(JSONDict['devices'][2]['transducers'][1]['purpose'] != "N/A"):
        pressureVolt1 = adc0.read(1,ADCGain[2])*ADCScale[2]
    else:
        pressureVolt1 = 0
    
    if(JSONDict['devices'][2]['tranducers'][2]['purpose'] != "N/A"):
        pressureVolt2 = adc0.read(2,ADCGain[2])*ADCScale[2]
    else:
        pressureVolt2 = 0

    if(JSONDict['devices'][2]['transducers'][3]['purpose'] != "N/A"):
        pressureVolt3 = adc0.read(3,ADCGain[2])*ADCScale[2]
    else:
        pressureVolt3 = 0

    #Fourth ADS1115
    if(JSONDict['devices'][3]['transducers'][0]['purpose'] != "N/A"):
        pressureVolt4 = adc0.read(0,ADCGain[3])*ADCScale[3]
    else:
        pressureVolt4 = 0

    if(JSONDict['devices'][3]['transducers'][1]['purpose'] != "N/A"):
        pressureVolt5 = adc0.read(1,ADCGain[3])*ADCScale[3]
    else:
        pressureVolt5 = 0
    
    if(JSONDict['devices'][3]['tranducers'][2]['purpose'] != "N/A"):
        pressureVolt6 = adc0.read(2,ADCGain[3])*ADCScale[3]
    else:
        pressureVolt6 = 0

    if(JSONDict['devices'][3]['transducers'][3]['purpose'] != "N/A"):
        pressureVolt7 = adc0.read(3,ADCGain[3])*ADCScale[3]
    else:
        pressureVolt7 = 0

    pressure0 = pressureVolt0*ducerPressureScale1[0]
    pressure1 = pressureVolt1*ducerPressureScale1[1]
    pressure2 = pressureVolt2*ducerPressureScale1[2]
    pressure3 = pressureVolt3*ducerPressureScale1[3]
    pressure4 = pressureVolt4*ducerPressureScale2[0]
    pressure5 = pressureVolt5*ducerPressureScale2[1]
    pressure6 = pressureVolt6*ducerPressureScale2[2]
    pressure7 = pressureVolt7*ducerPressureScale2[3]