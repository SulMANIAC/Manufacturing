import os
import tempfile
import sys
sys.path.append('tutorial')

from flask import Flask
from flask import Blueprint
import flaskr.maintenance
bp = Blueprint("engineer", __name__)

import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp)
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_logout(client):
    response = client.post('/logout')
    assert response.status_code == 302

def test_acknowledge(client):
    response = client.post('/acknowledge')
    assert response.status_code == 204

def test_alarm_report(client):
    response = client.post('/alarm_report')
    assert response.status_code == 200

def test_operator_actions(client):
    response = client.post('/operator_actions')
    assert response.status_code == 200

def test_acknowledge_history(client):
    response = client.post('/acknowledge_history')
    assert response.status_code == 200

def test_alarm_history(client):
    response = client.post('/alarm_history')
    assert response.status_code == 200

def test_forecasting_actions(client):
    response = client.post('/forecasting_actions')
    assert response.status_code == 200

def test_forecasting_data(client):
    response = client.post('/forecasting_data')
    assert response.status_code == 200

def test_engineer(client):
    response = client.get('/engineer')
    assert response.status_code == 200

def test_index(client):
    response = client.get('/index')
    assert response.status_code == 200
