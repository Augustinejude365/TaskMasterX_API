from flask import Flask
from config import Config
from models import db
from routes import task_routes
from auth import auth_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(task_routes)
    app.register_blueprint(auth_bp)

    return app


app = create_app()
