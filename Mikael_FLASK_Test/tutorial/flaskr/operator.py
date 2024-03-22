from flask import Blueprint, request, render_template, redirect, url_for
import sqlite3

bp = Blueprint("operator", __name__)

@bp.route('/')
def home():
    return render_template("auth/operator.html")

@bp.route('/logout', methods=['POST'])
def logout():
    print("Log Out button clicked")
    return redirect(url_for('auth.logout'))

@bp.route('/acknowledge', methods=['POST'])
def acknowledge():
    print("Acknowledge button clicked")
    return ('', 204)

@bp.route('/operator')
def operator():
    return render_template('operator.html')

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
    labels = ['January', 'February', 'March', 'April', 'May', 'June']
    data = [10, 20, 30, 20, 10, 50]

    # Pass the data to the template
    return render_template('chart.html', labels=labels, data=data)