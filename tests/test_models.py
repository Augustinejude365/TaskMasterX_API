import pytest
from app import db, create_app
from models import Task, User


@pytest.fixture(scope='module')
def test_client():
    app = create_app('TestingConfig')
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()

    yield testing_client

    with app.app_context():
        db.drop_all()


def test_task_creation(test_client):
    response = test_client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'Test Description'
    })
    assert response.status_code == 201
    assert 'id' in response.json


def test_task_retrieval(test_client):
    response = test_client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'Test Description'
    })
    task_id = response.json['id']

    response = test_client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert response.json['title'] == 'Test Task'
    assert response.json['description'] == 'Test Description'


def test_task_update(test_client):
    response = test_client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'Test Description'
    })
    task_id = response.json['id']

    response = test_client.put(f'/tasks/{task_id}', json={
        'title': 'Updated Task Title',
        'description': 'Updated Description'
    })
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Task Title'
    assert response.json['description'] == 'Updated Description'


def test_task_deletion(test_client):
    response = test_client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'Test Description'
    })
    task_id = response.json['id']

    response = test_client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Task deleted'

    response = test_client.get(f'/tasks/{task_id}')
    assert response.status_code == 404
