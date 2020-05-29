#include <Arduino.h>
#include <HX711.h>
#include <SparkFunMAX31855k.h> // Using the max31855k driver
#include <SdFat.h>
#include <Thread.h>
#include <StaticThreadController.h>

// Deprecated includes

// ================================= HARDWARE DEFINITION =================================

// #define CALIBRATION_FACTOR 386050.00 // kg
// #define CALIBRATION_FACTOR 1280 //Nnbvx
#define CALIBRATION_FACTOR 1
//I calibrated this using random stuff i had lying around (207g battery pack, 120g solenoid, 3kg metal stock)
//it's not great. I'm also wondering if we should calibrate it using known loads that are close to what we expect to be measuring?

// Define loadcell pins
#define LOADCELL_DATA_PIN  29
#define LOADCELL_SCK_PIN  30

// Define SPI power pins
#define SPI_VCC 16
#define SPI_GND 17

// Define Analog pins for pressure transducer
const int pressurePin[] = {A12,A13,A14};

// Define temperature probe chip select pins
const uint8_t probeCS[] = {35,36,37};

// ================================= CLASS/VARIABLE DECLARATIONS =================================

// Initialize sensors
HX711 LoadCell;
SparkFunMAX31855k probe0(probeCS[0],SPI_VCC,SPI_GND);
SparkFunMAX31855k probe1(probeCS[1],SPI_VCC,SPI_GND);
SparkFunMAX31855k probe2(probeCS[2],SPI_VCC,SPI_GND);

// Declare temperature vars
float temp0,temp1,temp2;

// Float to store pressure
double pressure1,pressure2,pressure3;

// Float to store load cell data
float force;

// ================================== THREAD DEFINITIONS ==================================

Thread loadCellThread = Thread();
Thread thermoThread = Thread();
Thread ducerThread = Thread();

StaticThreadController<3> controller(&loadCellThread,&thermoThread,&ducerThread);

// ============================= THREAD FUNCTION DEFINITIONS ==============================

void loadCellLoop() {
  force = LoadCell.get_value();
  Serial.print("F,");
  Serial.println(force,5);
}

// TODO define other threads

void serialPrinter(double pressure1, double pressure2, double pressure3, float temp0, float temp1, float temp2, float force){
  Serial.print("Sample, ");
  Serial.print(millis());
  Serial.print(", ");
  Serial.print(pressure1, 5);
  Serial.print(", ");
  Serial.print(pressure2, 5);
  Serial.print(", ");
  Serial.print(pressure3, 5);
  Serial.print(", ");
  Serial.print(temp0);
  Serial.print(", ");
  Serial.print(temp1);
  Serial.print(", ");
  Serial.print(temp2);
  Serial.print(", ");
  Serial.println(force, 5); //returns a float. 2nd param is # of decimal places to display/record. In grams the 1st dec is definitely unreliable. 
};

void setup() {

  // Start Serial comms
  Serial.begin(115200);

  // Initialize load cell
  LoadCell.begin(LOADCELL_DATA_PIN, LOADCELL_SCK_PIN);
  LoadCell.set_scale(CALIBRATION_FACTOR); // TODO remove calibration (can be performed in Python)
  LoadCell.tare(); // zero at startup

  // Init threads
  loadCellThread.onRun(loadCellLoop);
  loadCellThread.setInterval(20);

  // TODO add more threads here

}

void loop() {

  controller.run();

  // TODO remove everything else!

  // Sample thermocouples
  temp0 = probe0.readTempK();
  temp1 = probe1.readTempK();
  temp2 = probe2.readTempK();

  // Sample pressure transducer
  // pressure = 14400;
  // pressure = pressure * analogRead(pressurePin);
  // pressure = pressure - 1507000;
  pressure1 = analogRead(pressurePin[0]);
  pressure2 = analogRead(pressurePin[1]);
  pressure3 = analogRead(pressurePin[2]);

  // Sample load cell
  force = LoadCell.get_units();

  // Serial print and SD write
  serialPrinter(pressure1, pressure2, pressure3, temp0, temp1, temp2, force);

  // delay(10);
}
