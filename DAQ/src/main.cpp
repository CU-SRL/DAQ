#include <Arduino.h>
#include <HX711.h>
#include <Servo.h>
#include <SparkFunMAX31855k.h> // Using the max31855k driver
#include <SPI.h>  // Included here too due Arduino IDE; Used in above header

// HX711 library: https://github.com/bogde/HX711
// this is also in the lib manager - authors Bogdan Necula, Andreas Motl

// #define calibration_factor 386050.00 // kg
#define calibration_factor 1280 //Nnbvx
//I calibrated this using random stuff i had lying around (207g battery pack, 120g solenoid, 3kg metal stock)
//it's not great. I'm also wondering if we should calibrate it using known loads that are close to what we expect to be measuring?

#define LOADCELL_DOUT_PIN  3
#define LOADCELL_SCK_PIN  2


HX711 loadCell;
SparkFunMAX31855k probe1(10);
SparkFunMAX31855k probe2(9);
SparkFunMAX31855k probe3(8);

void setup() {
  Serial.begin(9600);
  loadCell.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  loadCell.set_scale(calibration_factor);
  loadCell.tare(); // zero at startup
}

void loop() {
  float temperature1 = probe1.readTempK();
  float temperature2 = probe2.readTempK();
  float temperature3 = probe3.readTempK();
  double Pressure = 14400;
  Pressure = Pressure * analogRead(A0);
  Pressure = Pressure - 1507000;
  logLoad(Pressure, temperature1, temperature2, temperature3);
}


void logLoad(double Pressure, float temp1, float temp2, float temp3){
  Serial.print(millis());
  Serial.print(", ");
  Serial.print(Pressure);
  Serial.print(", ");
  Serial.print(temp1);
  Serial.print(", ");
  Serial.print(temp2);
  Serial.print(", ");
  Serial.print(temp3);
  Serial.print(", ");
  Serial.println(loadCell.get_units(), 5); //returns a float. 2nd param is # of decimal places to display/record. In grams the 1st dec is definitely unreliable. 
}