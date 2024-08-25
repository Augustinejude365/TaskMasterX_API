import pytest
from your_project_name import create_app, db


@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()

    yield testing_client

    with app.app_context():
        db.drop_all()


@pytest.fixture(scope='module')
def init_database():
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        # Add initial data if needed
        yield db
        db.drop_all()
