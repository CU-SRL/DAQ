#include <Arduino.h>
#include <HX711.h>
#include <SparkFunMAX31855k.h>
#include <SdFat.h>
#include <Thread.h>
#include <StaticThreadController.h>

// ================================= HARDWARE DEFINITION =================================

// Define loadcell pins
#define LOADCELL_DATA_PIN 29
#define LOADCELL_SCK_PIN 30

// Define SPI power pins
#define SPI_VCC 16
#define SPI_GND 17

// Define Analog pins for pressure transducer
#define PRESSURE_PIN_1 A12
#define PRESSURE_PIN_2 A13
#define PRESSURE_PIN_3 A14
// const int pressurePin[] = {A12, A13, A14};

// Define temperature probe chip select pins
#define THERMO_CS_1 35
#define THERMO_CS_2 36
#define THERMO_CS_3 37
// const uint8_t probeCS[] = {35, 36, 37};

// ================================= CLASS/VARIABLE DECLARATIONS =================================

// Initialize sensors
HX711 LoadCell;
SparkFunMAX31855k probe0(THERMO_CS_1, SPI_VCC, SPI_GND);
SparkFunMAX31855k probe1(THERMO_CS_2, SPI_VCC, SPI_GND);
SparkFunMAX31855k probe2(THERMO_CS_3, SPI_VCC, SPI_GND);

// Declare temperature vars
float temp1, temp2, temp3;

// Float to store pressure
double pressure1, pressure2, pressure3;

// Float to store load cell data
float force;

// ================================== THREAD DEFINITIONS ==================================

Thread loadCellThread = Thread();
Thread thermoThread = Thread();
Thread ducerThread = Thread();

StaticThreadController<3> controller(&loadCellThread, &thermoThread, &ducerThread);

// ============================= THREAD FUNCTION DEFINITIONS ==============================

void loadCellLoop()
{
	// Get raw load cell value
	force = LoadCell.get_value();

	// Print values
	Serial.print(millis());
	Serial.print(",");
	Serial.print("F,");
	Serial.println(force, 5);
}

void thermoLoop()
{
	// Sample thermocouples
	temp1 = probe0.readTempK();
	temp2 = probe1.readTempK();
	temp3 = probe2.readTempK();

	// Print values
	Serial.print(millis());
	Serial.print(",");
	Serial.print("T1,");
	Serial.println(temp1, 5);

	Serial.print(millis());
	Serial.print(",");
	Serial.print("T2,");
	Serial.println(temp2, 5);

	Serial.print(millis());
	Serial.print(",");
	Serial.print("T3,");
	Serial.println(temp3, 5);
}

void ducerLoop()
{
	// Read ducers
	pressure1 = analogRead(PRESSURE_PIN_1);
	pressure2 = analogRead(PRESSURE_PIN_2);
	pressure3 = analogRead(PRESSURE_PIN_3);

	// Print values
	Serial.print(millis());
	Serial.print(",");
	Serial.print("P1,");
	Serial.println(pressure1, 5);

	Serial.print(millis());
	Serial.print(",");
	Serial.print("P2,");
	Serial.println(pressure2, 5);

	Serial.print(millis());
	Serial.print(",");
	Serial.print("P3,");
	Serial.println(pressure3, 5);
}

// ================================== SETUP FUNCTION  ===================================

void setup()
{
	// Start Serial comms
	Serial.begin(115200);

	// Initialize load cell
	LoadCell.begin(LOADCELL_DATA_PIN, LOADCELL_SCK_PIN);
	// LoadCell.set_scale(1); // TODO remove calibration (can be performed in Python)
	LoadCell.tare(); // zero at startup

	// Init threads
	loadCellThread.onRun(loadCellLoop);
	loadCellThread.setInterval(20);

	ducerThread.onRun(ducerLoop);
	ducerThread.setInterval(20);

	thermoThread.onRun(thermoLoop);
	thermoThread.setInterval(100);
}

// ==================================== MAIN FUNCTION  ===================================

void loop()
{
	controller.run();
}
