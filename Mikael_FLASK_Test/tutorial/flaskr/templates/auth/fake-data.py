import sqlite3
import random
from faker import Faker

# Create a new SQLite database (or connect to it if it already exists)
conn = sqlite3.connect('alarminfo.db')
c = conn.cursor()

# Create the tables
c.execute('''
    CREATE TABLE AlarmHistory (
        ID INTEGER PRIMARY KEY,
        AlarmName TEXT NOT NULL,
        AlarmTime TEXT NOT NULL,
        AlarmLocation TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE OperatorActions (
        ID INTEGER PRIMARY KEY,
        OperatorName TEXT NOT NULL,
        ActionTime TEXT NOT NULL,
        ActionDetails TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE AcknowledgeHistory (
        ID INTEGER PRIMARY KEY,
        OperatorName TEXT NOT NULL,
        AcknowledgeTime TEXT NOT NULL,
        AlarmID INTEGER,
        FOREIGN KEY(AlarmID) REFERENCES AlarmHistory(ID)
    )
''')

c.execute('''
    CREATE TABLE AlarmReports (
        ID INTEGER PRIMARY KEY,
        ReportTime TEXT NOT NULL,
        ReportDetails TEXT NOT NULL,
        AlarmID INTEGER,
        FOREIGN KEY(AlarmID) REFERENCES AlarmHistory(ID)
    )
''')

# Generate fake data and insert it into the tables
fake = Faker()
for _ in range(100):
    alarm_name = fake.word()
    alarm_time = fake.date_time().isoformat()
    alarm_location = fake.city()
    c.execute('INSERT INTO AlarmHistory (AlarmName, AlarmTime, AlarmLocation) VALUES (?, ?, ?)', (alarm_name, alarm_time, alarm_location))

    operator_name = fake.name()
    action_time = fake.date_time().isoformat()
    action_details = fake.sentence()
    c.execute('INSERT INTO OperatorActions (OperatorName, ActionTime, ActionDetails) VALUES (?, ?, ?)', (operator_name, action_time, action_details))

    acknowledge_time = fake.date_time().isoformat()
    alarm_id = random.randint(1, 100)
    c.execute('INSERT INTO AcknowledgeHistory (OperatorName, AcknowledgeTime, AlarmID) VALUES (?, ?, ?)', (operator_name, acknowledge_time, alarm_id))

    report_time = fake.date_time().isoformat()
    report_details = fake.paragraph()
    c.execute('INSERT INTO AlarmReports (ReportTime, ReportDetails, AlarmID) VALUES (?, ?, ?)', (report_time, report_details, alarm_id))

# Commit the changes and close the connection
conn.commit()
conn.close()
