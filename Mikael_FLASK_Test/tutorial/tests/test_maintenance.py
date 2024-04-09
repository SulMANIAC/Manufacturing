import os
import tempfile
import sys
sys.path.append('tutorial')

from flask import Flask
from flask import Blueprint
import flaskr.maintenance
bp = Blueprint("maintenance", __name__)

import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp)
    with app.test_client() as client:
        yield client

#This test checks if the home page is working correctly. It sends a GET request to the home page and checks 
#if the response status code is 200, which indicates a successful HTTP request.
def test_home(client):
    response = client.get('/') #Add URL
    assert response.status_code == 200

#It sends a POST request to the logout route and checks if the response status code is 302, which indicates a redirection. 
#This is expected because after logging out, users are typically redirected to another page.
def test_logout(client):
    response = client.post('/logout', methods=['POST']) #Add URL
    assert response.status_code == 302

def test_acknowledge(client):
    response = client.post('/acknowledge', methods=['POST']) #Add URL
    assert response.status_code == 204

def test_alarm_report(client):
    response = client.post('/alarm_report', methods=['POST']) #Add URL
    assert response.status_code == 200

def test_operator_actions(client):
    response = client.post('/operator_actions', methods=['POST']) #Add URL
    assert response.status_code == 200

def test_acknowledge_history(client):
    response = client.post('/acknowledge_history', methods=['POST']) #Add URL
    assert response.status_code == 200

def test_alarm_history(client):
    response = client.post('/alarm_history', methods=['POST']) #Add URL
    assert response.status_code == 200

def test_maintenance(client):
    response = client.get('auth/maintenance.html', current_alarms=current_alarms, past_alarms=past_alarms) #Add URL
    assert response.status_code == 200

def test_index(client):
    response = client.get('/index') #Add URL
    assert response.status_code == 200
