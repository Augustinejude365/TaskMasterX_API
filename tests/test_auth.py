import pytest
from app import create_app, db
from models import User


@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def init_database(app):
    db.create_all()
    yield
    db.drop_all()


def test_register(client, init_database):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'password'
    })
    assert response.status_code == 201
    assert 'token' in response.json


def test_login(client, init_database):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'password'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'password'
    })
    assert response.status_code == 200
    assert 'token' in response.json


def test_login_fail(client):
    response = client.post('/login', json={
        'username': 'invaliduser',
        'password': 'password'
    })
    assert response.status_code == 401
