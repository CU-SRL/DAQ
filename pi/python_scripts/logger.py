import sqlite3 as sql
import os
import sys
import serial

# Get database name as input argument
dbname = sys.argv[1]

# Connect to database
conn = sql.connect()
c = conn.cursor()

# Connect to serial
# ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=10)
ser = serial.Serial('COM4', 19200, timeout=10)

# Initialize loop boolean
logging = True

# Loop
while logging:
    # Read line from serial
	line = ser.readline()

    # Parse line   
    comps = line.split(",")

    # Check that line is data
    if (comps[0] == 'Sample'):

        # Print data to terminal
        Print(line)

        # Parse data
        t = int(comps[1])
        P1 = float(comps[2])
        P2 = float(comps[3])
        P3 = float(comps[4])
        T1 = float(comps[5])
        T2 = float(comps[6])
        T3 = float(comps[7])
        F = float(comps[8])

	    # TODO | pass values to SQL

# Close database connection
conn.close()