import sqlite3 as sql
import os
import sys
import serial
import signal

# Define signal handler to stop loop on signal
def signal_handler(signal, frame):
    global logging
    logging = False

# Call signal handler on SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Get database name as input argument
dbname = sys.argv[1]

# Connect to database
conn = sql.connect(dbname)
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS daq (
    t INTEGER,
    P1 REAL,
    P2 REAL,
    P3 REAL,
    T1 REAL,
    T2 REAL,
    T3 REAL,
    F REAL)
    """)

conn.commit()

# Connect to serial
ser = serial.Serial(port='COM7', baudrate=115200, timeout=10)
# ser = serial.Serial(port='/dev/tty0', baudrate=115200, timeout=10)

# Initialize loop boolean
logging = True

# Loop
while logging:
    # Read line from serial
    line = ser.readline().decode('utf=8')

    # Parse line   
    comps = line.split(",")

    # Check that line is data
    if (comps[0] == 'Sample'):

        # Print data to terminal
        # print(line)

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

        # Query data to DB
        c.execute('INSERT INTO daq(t,P1,P2,P3,T1,T2,T3,F) VALUES (:t,:P1,:P2,:P3,:T1,:T2,:T3,:F)',
            {'t':t,'P1':P1,'P2':P2,'P3':P3,'T1':T1,'T2':T2,'T3':T3,'F':F})

        conn.commit()

        print('Sampled')



# Close database connection
c.close()
conn.close()

print('Clean Exit')