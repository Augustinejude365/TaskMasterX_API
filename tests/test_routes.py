import pytest
from taskmaster_api import create_app, db
from taskmaster_api.models import Task


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_task(client):
    response = client.post(
        '/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
    assert response.status_code == 201
    assert response.json['title'] == 'Test Task'


def test_get_tasks(client):
    client.post('/tasks', json={'title': 'Test Task',
                'description': 'Test Description'})
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json) > 0


def test_get_task(client):
    response = client.post(
        '/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
    task_id = response.json['id']
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert response.json['title'] == 'Test Task'


def test_update_task(client):
    response = client.post(
        '/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
    task_id = response.json['id']
    response = client.put(
        f'/tasks/{task_id}', json={'title': 'Updated Task', 'description': 'Updated Description'})
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Task'


def test_delete_task(client):
    response = client.post(
        '/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
    task_id = response.json['id']
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 204
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 404
