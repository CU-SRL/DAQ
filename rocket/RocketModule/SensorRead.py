#Import necessary libraries and files
import RPi.GPIO as GPIO #Raspberry Pi GPIO library
import adafruit_ads1x15.ads1115 as ADS #ADS1115 library
from adafruit_ads1x15.analog_in import AnalogIn
from hx711 import HX711 #HX711 library
import board
import busio
import JSONParsing 
import os
import time

GPIO.setmode(GPIO.BCM)
i2c = busio.I2C(board.SCL, board.SDA)

class SensorRead():
    def __init__(self): #Initialization function, parses JSON and creates device objects and data variables
        #JSON Ingestion
        self.IOConfig = JSONParsing.IOConfig
        #Devices
        self.adc0 = ADS.ADS1115(i2c, gain=self.IOConfig.thermocoupleDict[0]['gain'], data_rate = 860, address=self.IOConfig.ADSDict[0]['address'])
        self.adc0chan = [AnalogIn(self.adc0,ADS.P0), AnalogIn(self.adc0,ADS.P1), AnalogIn(self.adc0,ADS.P2),AnalogIn(self.adc0,ADS.P3)]
        #self.adc1 = ADS.ADS1115(i2c, gain=self.IOConfig.thermocoupleDict[1]['gain'], data_rate = 860, address=self.IOConfig.ADSDict[1]['address'])
        #self.adc1chan = [AnalogIn(self.adc0,ADS.P0), AnalogIn(self.adc1,ADS.P1), AnalogIn(self.adc1,ADS.P2),AnalogIn(self.adc1,ADS.P3)]
        #self.adc2 = ADS.ADS1115(i2c, gain=self.IOConfig.thermocoupleDict[2]['gain'], data_rate = 860, address=self.IOConfig.ADSDict[2]['address'])
        #self.adc2chan = [AnalogIn(self.adc0,ADS.P0), AnalogIn(slf.adc2,ADS.P1), AnalogIn(self.adc2,ADS.P2),AnalogIn(self.adc2,ADS.P3)]
        #self.adc3 = ADS.ADS1115(i2c, gain=self.IOConfig.thermocoupleDict[3]['gain'], data_rate = 860, address=self.IOConfig.ADSDict[3]['address'])
        #self.adc3chan = [AnalogIn(self.adc0,ADS.P0), AnalogIn(self.adc3,ADS.P1), AnalogIn(self.adc3,ADS.P2),AnalogIn(self.adc3,ADS.P3)]
        #self.adc0.mode = 0x0000
        #self.loadCell = HX711(dout_pin=self.IOConfig.loadCellDict[0]['DOUT'], pd_sck_pin=self.IOConfig.loadCellDict[0]['CLK'])
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
        self.d0 = 0
        self.d1 = 2.508355*(10**1)
        self.d2 = 7.860106*(10**-2)
        self.d3 = -2.503131*(10**-1)
        self.d4 = 8.315270*(10**-2)
        self.d5 = -1.228034*(10**-2)
        self.d6 = 9.804036*(10**-4)
        self.d7 = -4.413030*(10**-5)
        self.d8 = 1.057734*(10**-6)
        self.d9 = -1.052755*(10**-8)

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
        #self.loadCell.set_scale_ratio(sensors.IOConfig.loadCellDict['scale'])

    def readThermocouples(self): #Thermocouple reading function, checks if the object is a thermocouple and calculates the voltage output, then converts it to a temperature using the thermocouple equation
        for i in range(4):#len(self.IOConfig.thermocoupleDict)):
            if (i < 4 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                self.thermoVolt[i] = self.adc0chan[i].voltage*1000#/self.ADCScaleThermo[i]
            elif (i >= 4 and i < 8 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                0#self.thermoVolt[i] = self.adc1chan[i].voltage*1000#/self.ADCScaleThermo[i]
            elif (i >=8 and i < 12 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                0#self.thermoVolt[i] = self.adc2chan[i].voltage*1000#*self.ADCScaleThermo[i]
            elif (i >= 12 and i < 16 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Thermo"):
                0#self.thermoVolt[i] = self.adc3chan[i].voltage*1000#*self.ADCScaleThermo[i]
            else:
                0
            self.thermocoupleData[i] = self.d0 + self.d1*self.thermoVolt[i] + self.d2*(self.thermoVolt[i]**2) + self.d3*(self.thermoVolt[i]**3) + self.d4*(self.thermoVolt[i]**4) + self.d5*(self.thermoVolt[i]**5) + self.d6*(self.thermoVolt[i]**6) + self.d7*(self.thermoVolt[i]**7) + self.d8*(self.thermoVolt[i]**8) + self.d9*(self.thermoVolt[i]**9)
            self.thermocoupleData[i] = (9/5)*self.thermocoupleData[0] + 32 + 68
            #print("temperature: ", self.thermocoupleData[i])
        return self.thermocoupleData

    def readDucers(self): #Pressure transducer reading function, checks if the object is a transducer and calculates the voltage output, then converts it into a pressure reading using the scale defined in the JSON file
        for i in range(len(self.IOConfig.ducerDict)):
            if (i < 4 and self.IOConfig.ducerDict[i]['type'] == "ADS1115Ducer"):
                0#self.ducerVolt[i] = self.adc2.read(i,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            elif (i >= 4 and i < 8 and self.IOConfig.ducerDict[i]['type'] == "ADS1115Ducer"):
                0#self.ducerVolt[i] = self.adc2.read(i-4,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            elif (i >=8 and i < 12 and self.IOConfig.ducerDict[i]['type'] == "ADS1115Ducer"):
                0#self.ducerVolt[i] = self.adc3.read(i-8,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            elif (i >= 12 and i < 16 and self.IOConfig.thermocoupleDict[i]['type'] == "ADS1115Ducer"):
                0#self.ducerVolt[i] = self.adc3.read(i-12,self.ADCGainDucer[i])*self.ADCScaleDucer[i]
            else:
                return
            #self.ducerData[i] = self.ducerVolt[i]*self.ducerPressureScale[i]
        return self.ducerData

    def readLoadCell(self): #Load cell reading function, uses the "get_weight()" function from the HX711 library to get thrust data
        #self.loadCellData = self.loadCell.get_weight()
        return self.loadCellData
    def calibrate(self):
        self.scales()
    def run(self): #Main running function, collects data from all devices after setting the scale
        self.thermocoupleData = self.readThermocouples()
        self.ducerData = self.readDucers()
        self.loadCellData = self.readLoadCell()
    
if __name__ == "__main__":
    sensors = SensorRead()
    sensors.calibrate()

    startTime = time.time()
    
    for i in range(1000):
        sensors.readThermocouples()
        #print("temp: ",sensors.thermocoupleData[0])
    print (time.time() - startTime)

    #for i in range(len(sensors.thermocoupleData)):
        #print(sensors.thermocoupleData[i])

    #for i in range(len(sensors.ducerData)):
        #print(sensors.ducerData[i])

    #for i in range(len(sensors.loadCellData)):
        #print(sensors.loadCellData)

else:
    sensors = SensorRead()
    sensors.run()

