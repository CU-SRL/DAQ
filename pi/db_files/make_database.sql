-- Table of DAQ parameters to be logged
    -- name:        name of parameter (e.g., "P1")
    -- cal_factor:  calibration factor from raw data to output value
    -- units: units of the value returned from the calibration factor
    -- description: description of the parameter
CREATE TABLE IF NOT EXISTS parameters (
    name TEXT NOT NULL PRIMARY KEY,
    cal_factor REAL,
    units TEXT,
    description TEXT DEFAULT '');

-- Table of DAQ data
    -- parameter: name of parameter being logged, e.g., "P1" (foreign key from `parameters` table)
    -- recording_id: unique identifier of the current recording, as input by the user (this is probably a terrible idea and I know that I should serialize this key instead)
    -- t: timestamp (seconds)
    -- val: value being recorded, with any calibration factor applied
CREATE TABLE IF NOT EXISTS daq (
    parameter TEXT,
    recording_id TEXT,
    t INTEGER,
    val REAL,
    PRIMARY KEY(parameter,t));

-- Clear out any content from these tables in case there's any data there
DELETE FROM daq;
DELETE FROM parameters;

INSERT INTO parameters(name,units,description) VALUES 
    (P1,'kPa','Pressure Transducer 1'),
    (P2,'kPa','Pressure Transducer 2'),
    (P3,'kPa','Pressure Transducer 3'),
    (T1,'K','Thermocouple 1'),
    (T2,'K','Thermocouple 2'),
    (T3,'K','Thermocouple 3'),
    (F,'N','Load Cell');
