from flask import Blueprint, request, render_template, redirect, url_for
import sqlite3

bp = Blueprint("maintenance", __name__)

@bp.route('/')
def home():
    return render_template("auth/maintenance.html")

@bp.route('/logout', methods=['POST'])
def logout():
    print("Log Out button clicked")
    return redirect(url_for('auth.logout'))

@bp.route('/acknowledge', methods=['POST'])
def acknowledge():
    print("Acknowledge button clicked")
    return ('', 204)

@bp.route('/alarm_report', methods=['POST'])
def alarm_report():
    print("Alarm Report button clicked")
    conn = sqlite3.connect("alarminfo.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alarmreports")
    rows = cursor.fetchall()
    data = [dict(row) for row in rows]
    return render_template('table.html', header="Alarm Reports", data=data)

@bp.route('/operator_actions', methods=['POST'])
def operator_actions():
    print("Operator Actions button clicked")
    conn = sqlite3.connect("alarminfo.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OperatorActions")
    rows = cursor.fetchall()
    data = [dict(row) for row in rows]
    return render_template('table.html', header="Operator Actions", data=data)

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

def maintenance_current_alarm():
    conn = sqlite3.connect("current_alarms.db")  # Connect to the database
    cursor = conn.cursor()

    # Execute the SQL script
    with open('current_alarms.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)

    # Query the data
    cursor.execute("SELECT * FROM current_alarms")  
    rows = cursor.fetchall()
    data = [dict(row) for row in rows]
    print(data)  # Debug print
    return render_template('maintenance.html', current_alarms=data)

@bp.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    bp.run(debug=True)
