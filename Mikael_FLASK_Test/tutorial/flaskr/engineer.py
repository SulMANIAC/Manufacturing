from flask import Blueprint, request, render_template, redirect, url_for
import sqlite3

bp = Blueprint("engineer", __name__)

@bp.route('/')
def home():
    print("Accessed Engineer Alarms Route.")
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

    # Render the engineer.html template with the alarms data
    return render_template('auth/engineer.html', current_alarms=current_alarms, past_alarms=past_alarms)

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

@bp.route('/forecasting_actions', methods=['POST'])
def forecasting_actions():
    return render_template('graphView.html')

@bp.route('/forecasting_data', methods=['POST'])
def forecasting_data():
    print("Forecasting Data button clicked")
    conn = sqlite3.connect("alarminfo.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM forecastingdata")
    rows = cursor.fetchall()
    data = [dict(row) for row in rows]
    return render_template('table.html', header="Forecasting Data", data=data)



@bp.route('/engineer')
def engineer():
    return render_template('engineer.html')

@bp.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    bp.run(debug=True)
