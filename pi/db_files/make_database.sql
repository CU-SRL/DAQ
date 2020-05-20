-- Table of DAQ parameters with fields for a unique PK, name (e.g., "P1"), a calibration factor to apply to the loaded data, and a description.
CREATE TABLE IF NOT EXISTS parameters (
    name TEXT NOT NULL PRIMARY KEY,
    cal_factor REAL,
    description TEXT DEFAULT '');

CREATE TABLE IF NOT EXISTS daq (
    parameter TEXT,
    recording_id TEXT,
    t INTEGER,
    val REAL,
    PRIMARY KEY(parameter,t));

DELETE FROM daq;
DELETE FROM parameters;

INSERT INTO parameters(name) VALUES 
    (P1),
    (P2),
    (P3),
    (T1),
    (T2),
    (T3),
    (F);
