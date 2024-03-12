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
