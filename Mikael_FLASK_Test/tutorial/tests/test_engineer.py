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
    response = client.get(url_for('engineer.home'))
    assert response.status_code == 200

def test_acknowledge(client):
    response = client.post(url_for('engineer.acknowledge'))
    assert response.status_code == 204

def test_alarm_report(client):
    response = client.post(url_for('engineer.alarm_report'))
    assert response.status_code == 200

def test_operator_actions(client):
    response = client.post(url_for('engineer.operator_actions'))
    assert response.status_code == 200

def test_acknowledge_history(client):
    response = client.post(url_for('engineer.acknowledge_history'))
    assert response.status_code == 200

def test_alarm_history(client):
    response = client.post(url_for('engineer.alarm_history'))
    assert response.status_code == 200

def test_forecasting_actions(client):
    response = client.post(url_for('engineer.forecasting_actions'))
    assert response.status_code == 200

def test_forecasting_data(client):
    response = client.post(url_for('engineer.forecasting_data'))
    assert response.status_code == 200

def test_engineer(client):
    response = client.get(url_for('engineer.engineer'))
    assert response.status_code == 200

def test_index(client):
    response = client.get(url_for('engineer.index'))
    assert response.status_code == 200
