import Rpi.GPIO as GPIO
import Adafruit_ADS1x15
from hx711 import HX711

# This section for testing only
import json

def ingestJSON(filename):
    with open(filename) as f:
        spiceShuttleJSON = json.load(f)

    return spiceShuttleJSON
#Above section for testing only

GPIO.setmode(GPIO.bcm)

#JSON Injestion
JSONDict = ingestJSON('spiceShuttle.json')

#Devices
adc0 = JSONDict['devices'][0]['name']
adc1 = JSONDict['devices'][1]['name']
adc2 = JSONDict['devices'][2]['name']
adc3 = JSONDict['devices'][3]['name']
loadCell = JSONDict['devices'][4]['name']

adc0 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][0]['address'],busnum=1)
adc1 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][1]['address'],busnum=1)
adc2 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][2]['address'],busnum=1)
adc3 = Adafruit_ADS1x15.ADS1115(address=JSONDict['devices'][3]['address'],busnum=1)
loadCell = HX711(dout_pin=JSONDict['devices'][4]['DOUT'], pd_sck_pin=JSONDict['devices'][4]['CLK'])

#Scales
ADCScale = [JSONDict['devices'][0]['scaleADCtoVoltage'], JSONDict['devices'][1]['scaleADCtoVoltage'], JSONDict['devices'][2]['scaleADCtoVoltage'], JSONDict['devices'][3]['scaleADCtoVoltage']]
ADCGain = [JSONDict['devices'][0]['gain'], JSONDict['devices'][1]['gain'], JSONDict['devices'][2]['gain'], JSONDict['devices'][3]['gain']]
ducerPressureScale1 = [JSONDict['devices'][2]['transducers'][0]['scaleVoltagetoPressure'],JSONDict['devices'][2]['transducers'][1]['scaleVoltagetoPressure'],JSONDict['devices'][2]['transducers'][2]['scaleVoltagetoPressure'],JSONDict['devices'][2]['transducers'][3]['scaleVoltagetoPressure']]
ducerPressureScale2 = [JSONDict['devices'][3]['transducers'][0]['scaleVoltagetoPressure'],JSONDict['devices'][3]['transducers'][1]['scaleVoltagetoPressure'],JSONDict['devices'][3]['transducers'][2]['scaleVoltagetoPressure'],JSONDict['devices'][3]['transducers'][3]['scaleVoltagetoPressure']]
loadCell.set_scale_ratio(JSONDict['devices'][4]['loadCell']['scale'])

#Thermocouple coefficients (0-500 degC, type K)
d0 = 0
d1 = 2.508355*(10**1)
d2 = 7.860106*(10**-2)
d3 = -2.503131*(10**-1)
d4 = 8.315270*(10**-2)
d5 = -1.228034*(10**-2)
d6 = 9.804036*(10**-4)
d7 = -4.413030*(10**-5)
d8 = 1.057734*(10**-6)
d9 = -1.052755*(10**-8)

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

    #load cell
    thrust = loadCell.get_weight()

    #Voltage to degC / psi conversion
    temp0 = d0 + d1*tempVolt0 + d2*(tempVolt0**2) + d3*(tempVolt0**3) + d4*(tempVolt0**4) + d5*(tempVolt0**5) + d6*(tempVolt0**6) + d7*(tempVolt0**7) + d8*(tempVolt0**8) + d9*(tempVolt0**9)
    temp1 = d0 + d1*tempVolt1 + d2*(tempVolt1**2) + d3*(tempVolt1**3) + d4*(tempVolt1**4) + d5*(tempVolt1**5) + d6*(tempVolt1**6) + d7*(tempVolt1**7) + d8*(tempVolt1**8) + d9*(tempVolt1**9)
    temp2 = d0 + d1*tempVolt2 + d2*(tempVolt2**2) + d3*(tempVolt2**3) + d4*(tempVolt2**4) + d5*(tempVolt2**5) + d6*(tempVolt2**6) + d7*(tempVolt2**7) + d8*(tempVolt2**8) + d9*(tempVolt2**9)
    temp3 = d0 + d1*tempVolt3 + d2*(tempVolt3**2) + d3*(tempVolt3**3) + d4*(tempVolt3**4) + d5*(tempVolt3**5) + d6*(tempVolt3**6) + d7*(tempVolt3**7) + d8*(tempVolt3**8) + d9*(tempVolt3**9)
    temp4 = d0 + d1*tempVolt4 + d2*(tempVolt4**2) + d3*(tempVolt4**3) + d4*(tempVolt4**4) + d5*(tempVolt4**5) + d6*(tempVolt4**6) + d7*(tempVolt4**7) + d8*(tempVolt4**8) + d9*(tempVolt4**9)
    temp5 = d0 + d1*tempVolt5 + d2*(tempVolt5**2) + d3*(tempVolt5**3) + d4*(tempVolt5**4) + d5*(tempVolt5**5) + d6*(tempVolt5**6) + d7*(tempVolt5**7) + d8*(tempVolt5**8) + d9*(tempVolt5**9)
    temp6 = d0 + d1*tempVolt6 + d2*(tempVolt6**2) + d3*(tempVolt6**3) + d4*(tempVolt6**4) + d5*(tempVolt6**5) + d6*(tempVolt6**6) + d7*(tempVolt6**7) + d8*(tempVolt6**8) + d9*(tempVolt6**9)
    temp7 = d0 + d1*tempVolt7 + d2*(tempVolt7**2) + d3*(tempVolt7**3) + d4*(tempVolt7**4) + d5*(tempVolt7**5) + d6*(tempVolt7**6) + d7*(tempVolt7**7) + d8*(tempVolt7**8) + d9*(tempVolt7**9)
    pressure0 = pressureVolt0*ducerPressureScale1[0]
    pressure1 = pressureVolt1*ducerPressureScale1[1]
    pressure2 = pressureVolt2*ducerPressureScale1[2]
    pressure3 = pressureVolt3*ducerPressureScale1[3]
    pressure4 = pressureVolt4*ducerPressureScale2[0]
    pressure5 = pressureVolt5*ducerPressureScale2[1]
    pressure6 = pressureVolt6*ducerPressureScale2[2]
    pressure7 = pressureVolt7*ducerPressureScale2[3]

    sensorData = [thrust, temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7, pressure0, pressure1, pressure2, pressure3, pressure4, pressure5, pressure6, pressure7]

    return sensorData