from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to your database
    conn = sqlite3.connect('alarminfo.db')

    # Create a cursor
    cur = conn.cursor()

    # Execute your SQL query
    cur.execute("SELECT * FROM current_alarm")

    # Fetch all results from the query
    alarms = cur.fetchall()

    # Close the connection
    conn.close()

    # Pass the alarms to your template
    return render_template('operator.html', alarms=alarms)
