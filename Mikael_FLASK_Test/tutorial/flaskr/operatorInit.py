from flask import Blueprint, request, render_template, redirect, url_for
import sqlite3
import os
import subprocess

bp = Blueprint("operator", __name__)

@bp.route('/')
def home():
    print("Accessed Operator Alarms Route.")
    # Connect to the SQLite database
    conn = sqlite3.connect("alarmPanel.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Query the current alarms, limit to 25
    cursor.execute("SELECT * FROM currentAlarms ORDER BY Date DESC LIMIT 25")
    current_alarms = cursor.fetchall()
    print("Current Alarms:", current_alarms)  # Debugging line

    # Query the past alarms, limit to 25
    cursor.execute("SELECT * FROM pastAlarms ORDER BY Date DESC LIMIT 25")
    past_alarms = cursor.fetchall()
    print("Past Alarms:", past_alarms)  # Debugging line

    # Close the database connection
    conn.close()

    # Render the operator.html template with the alarms data
    return render_template('auth/operator.html', current_alarms=current_alarms, past_alarms=past_alarms)

@bp.route('/logout', methods=['POST'])
def logout():
    print("Log Out button clicked")
    return redirect(url_for('auth.logout'))

@bp.route('/acknowledge', methods=['POST'])
def acknowledge():
    print("Acknowledge button clicked")
    return ('', 204)


@bp.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    bp.run(debug=True)

#opperator aknowledge history 
@bp.route('/acknowledge_history', methods=['POST'])
def acknowledge_history():
    print("Acknowledge History button clicked")
    conn = sqlite3.connect("alarminfo.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AcknowledgeHistory")
    rows = cursor.fetchall()
    data = [dict(row) for row in rows]
    return render_template('table.html', header="Acknowledge History", data=data)

#opperator alarm history 
@bp.route('/alarm_history', methods=['POST'])
def alarm_history():
    print("Alarm History button clicked")
    conn = sqlite3.connect("alarminfo.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AlarmHistory")
    rows = cursor.fetchall()
    data = [dict(row) for row in rows]
    return render_template('table.html', header="Alarm History", data=data)

#alarm history graph
@bp.route('/chart')
def chart():
    # Preset data
    labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6']
    data = [10, 20, 30, 20, 10, 50]

    # Pass the data to the template
    return render_template('chart.html', labels=labels, data=data)