import pytest

from flaskr import create_app

@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
