import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'c1ea1a224d78e8555f3d46116db503db')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///instance/taskmaster.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
