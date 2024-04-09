import pytest
from flask import url_for

from flaskr import create_app

@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('auth/engineer.html', current_alarms=current_alarms, past_alarms=past_alarms)
    assert response.status_code == 200

def test_logout(client):
    response = client.post('/logout', methods=['POST'])
    assert response.status_code == 302

def test_acknowledge(client):
    response = client.post('/acknowledge', methods=['POST'])
    assert response.status_code == 204

def test_alarm_report(client):
    response = client.post('/alarm_report', methods=['POST'])
    assert response.status_code == 200

def test_operator_actions(client):
    response = client.post('/operator_actions', methods=['POST'])
    assert response.status_code == 200

def test_acknowledge_history(client):
    response = client.post('/acknowledge_history', methods=['POST'])
    assert response.status_code == 200

def test_alarm_history(client):
    response = client.post('/alarm_history', methods=['POST'])
    assert response.status_code == 200

def test_forecasting_actions(client):
    response = client.post('/forecasting_actions', methods=['POST'])
    assert response.status_code == 200

def test_forecasting_data(client):
    response = client.post('/forecasting_data', methods=['POST'])
    assert response.status_code == 200

def test_engineer(client):
    response = client.get('/engineer')
    assert response.status_code == 200

def test_index(client):
    response = client.get('/index')
    assert response.status_code == 200
