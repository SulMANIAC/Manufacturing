from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/logout', methods=['POST'])
def logout():
    print("Log Out button clicked")
    return redirect(url_for('index'))

@app.route('/acknowledge', methods=['POST'])
def acknowledge():
    print("Acknowledge button clicked")
    return ('', 204)

@app.route('/alarm_report', methods=['POST'])
def alarm_report():
    print("Alarm Report button clicked")
    conn = sqlite3.connect('alarmreports.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AlarmReports")  # Assuming AlarmReports is your table name
    data = cursor.fetchall()
    return render_template('table.html', header="Alarm Reports", data=data)

@app.route('/operator_actions', methods=['POST'])
def operator_actions():
    print("Operator Actions button clicked")
    conn = sqlite3.connect('operatoractions.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OperatorActions")  # Assuming OperatorActions is your table name
    data = cursor.fetchall()
    return render_template('table.html', header="Operator Actions", data=data)

@app.route('/acknowledge_history', methods=['POST'])
def acknowledge_history():
    print("Acknowledge History button clicked")
    conn = sqlite3.connect('ackhistory.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AcknowledgeHistory")  # Assuming AcknowledgeHistory is your table name
    data = cursor.fetchall()
    return render_template('table.html', header="Acknowledge History", data=data)

@app.route('/alarm_history', methods=['POST'])
def alarm_history():
    print("Alarm History button clicked")
    conn = sqlite3.connect('alarmhistory.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AlarmHistory")  # Assuming AlarmHistory is your table name
    data = cursor.fetchall()
    return render_template('table.html', header="Alarm History", data=data)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
