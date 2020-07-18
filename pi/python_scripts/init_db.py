import sqlite3 as sql
import os
import sys

# Get database name as input argument
dbname = sys.argv[1]

# Connect to database
conn = sql.connect(dbname)
c = conn.cursor()

# Load SQL file
query = open('../db_files/make_databse.sql').read()

# Execute script
c.executescript(query)

conn.commit()

c.close()
conn.close()