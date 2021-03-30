#Import necessary libraries and files
import RPi.GPIO as GPIO #Raspberry Pi GPIO library
import Adafruit_ADS1x15 #ADS1115 library
from hx711 import HX711 #HX711 library
import JSONParsing 
import os

GPIO.setmode(GPIO.bcm)

class sensorRead():
    def __init__(self): #Initialization function, parses JSON and creates device objects and data variables
        #JSON Ingestion
        self.IOConfig = JSONParsing.Configuration(os.path.join(os.path.dirname( __file__ ),'..','..','configurations','IO.json'))
        self.IOConfig.ingestJSON("IO")
        self.IOConfig.run()
        self.adc0 = Adafruit_ADS1x15.ADS1115(address=self.IOConfig.thermocoupleDict[0]['address'],busnum=1)
        self.adc1 = Adafruit_ADS1x15.ADS1115(address=self.IOConfig.thermocoupleDict[4]['address'],busnum=1)
        self.adc2 = Adafruit_ADS1x15.ADS1115(address=self.IOConfig.ducerDict[0]['address'],busnum=1)
        self.adc3 = Adafruit_ADS1x15.ADS1115(address=self.IOConfig.ducerDict[4]['address'],busnum=1)
        self.loadCell = HX711(dout_pin=self.IOConfig.loadCellDict['DOUT'], pd_sck_pin=IOConfig.loadCellDict['CLK'])
        self.ADCScaleThermo = dict()
        self.ADCScaleDucer = dict()
        self.ADCGainThermo = dict()
        self.ADCGainDucer = dict()
        self.ducerPressureScale = dict()
        self.thermoVolt = dict()
        self.thermocoupleData = dict()
        self.ducerVolt = dict()
        self.ducerData = dict()
        self.loadCellData = dict()
        
        #Thermocouple voltage to temperature coefficients (0-500 degC, type K)
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

    def scales(self): #Scaling function, gets scaling data from the JSON file
        for i in range(len(self.IOConfig.thermocoupleDict)):
            self.ADCScaleThermo[i] = self.IOConfig.thermocoupleDict[i]['scaleADCtoVoltage']
        for i in range(len(self.IOConfig.ducerDict)):
            self.ADCScaleDucer[i] = self.IOConfig.ducerDict[i]['scaleADCtoVoltage']
        for i in range(len(self.IOConfig.thermocoupleDict)):
            self.ADCGainThermo[i] = self.IOConfig.thermocoupleDict[i]['gain']
        for i in range(len(self.IOConfig.ducerDict)):
            self.ADCGainDucer[i] = self.IOConfig.thermocoupleDict[i]['gain']
        for i in range(len(self.IOConfig.ducerDict)):
            self.ducerPressureScale[i] = self.IOConfig.ducerDict[i]['scaleVoltagetoPressure']
        self.loadCell.set_scale_ratio(sensors.IOConfig.loadCellDict['scale'])

    def readThermocouples(self): #Thermocouple reading function, checks if the object is a thermocouple and calculates the voltage output, then converts it to a temperature using the thermocouple equation
        for i in range(len(self.IOConfig.thermocoupleDict)):
            if (i < 4 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                self.thermoVolt[i] = self.adc0.read(i,self.ADCGainThermo[i])*self.ADCScaleThermo[i]
            elif (i >= 4 and i < 8 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                self.thermoVolt[i] = self.adc0.read(i-4,self.ADCGainThermo[i])*self.ADCScaleThermo[i]
            elif (i >=8 and i < 12 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                self.thermoVolt[i] = self.adc1.read(i-8,self.ADCGainThermo[i])*self.ADCScaleThermo[i]
            elif (i >= 12 and i < 16 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                self.thermoVolt[i] = self.adc1.read(i-12,self.ADCGainThermo[i])*self.ADCScaleThermo[i]
            else:
                return
            self.thermocopleData[i] = d0 + d1*thermoVolt[i] + d2*(thermoVolt[i]**2) + d3*(thermoVolt[i]**3) + d4*(thermoVolt[i]**4) + d5*(thermoVolt[i]**5) + d6*(thermoVolt[i]**6) + d7*(thermoVolt[i]**7) + d8*(thermoVolt[i]**8) + d9*(thermoVolt[i]**9)
        return self.thermocoupleData

    def readDucers(self): #Pressure transducer reading function, checks if the object is a transducer and calculates the voltage output, then converts it into a pressure reading using the scale defined in the JSON file
        for i in range(len(self.IOConfig.ducerDict)):
            if (i < 4 and self.IOConfig.ducerDict[i]['type'] == "ADS1115Ducer"):
                self.ducerVolt[i] = self.adc2.read(i,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            elif (i >= 4 and i < 8 and self.IOConfig.ducerDict[i]['type'] == "ADS1115Ducer"):
                self.ducerVolt[i] = self.adc2.read(i-4,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            elif (i >=8 and i < 12 and self.IOConfig.ducerDict[i]['type'] == "ADS1115Ducer"):
                self.ducerVolt[i] = self.adc3.read(i-8,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            elif (i >= 12 and i < 16 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Ducer"):
                self.ducerVolt[i] = self.adc3.read(i-12,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            else:
                return
            self.ducerData[i] = ducervolt[i]*ducerPressureScale[i]
        return self.thermocoupleData

    def readLoadCell(self): #Load cell reading function, uses the "get_weight()" function from the HX711 library to get thrust data
        self.loadCellData = self.loadCell.get_weight()
        return self.loadCellData

    def run(self): #Main running function, collects data from all devices after setting the scale
        self.scales()
        self.thermocoupleData = self.readThermocouples()
        self.ducerData = self.readDucers()
        self.loadCellData = self.readLoadCell()
    

sensors = sensorRead()
sensors.run()
