import sqlite3
import csv
import random


# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('alarmPanel.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Define the SQL commands to create the tables
create_current_alarms_table = """
CREATE TABLE IF NOT EXISTS currentAlarms (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Alarms TEXT NOT NULL,
    Date TEXT NOT NULL,
    Priority TEXT NOT NULL,
    Location TEXT NOT NULL
);
"""

create_past_alarms_table = """
CREATE TABLE IF NOT EXISTS pastAlarms (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Alarms TEXT NOT NULL,
    Date TEXT NOT NULL,
    Priority TEXT NOT NULL,
    Location TEXT NOT NULL
);
"""

# Execute the SQL commands to create the tables
cursor.execute(create_current_alarms_table)
cursor.execute(create_past_alarms_table)

# Function to insert data into the specified table
def insert_data(table_name, data):
    cursor.execute(f"INSERT INTO {table_name} (Alarms, Date, Priority, Location) VALUES (?, ?, ?, ?)", data)

# Read the CSV file and select 50 random rows
with open('./Alarm Data/alarms_log_data/alarms_log_data/raw/alarms.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    all_rows = list(csv_reader)
    selected_rows = random.sample(all_rows, 50)

# Assign random priorities
priorities = ['High', 'Low', 'Medium']

# Split the data between the two tables ensuring current alarms are more recent
half_index = len(all_rows) // 2
for i, row in enumerate(all_rows):
    # Map the CSV columns to the SQL columns
    timestamp, alarm, serial = row
    priority = random.choice(priorities)
    data = (alarm, timestamp, priority, serial)
    
    # Insert into currentAlarms if more recent, else insert into pastAlarms
    if i >= half_index:
        insert_data('currentAlarms', data)
    else:
        insert_data('pastAlarms', data)

# Commit the changes
conn.commit()

# Close the database connection
conn.close()

print("Data has been successfully inserted into currentAlarms and pastAlarms tables.")
