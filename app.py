from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import logging.config
import os

# Importing models to ensure they are recognized by Alembic
from models import Task, User
from routes import api_blueprint

# Initializing Flask app
app = Flask(__name__)

# Loading configurations
app.config.from_object('config.Config')

# Initializing extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Loading logging configuration
logging.config.fileConfig('logging.conf')

# Registering routes after initializing app
app.register_blueprint(api_blueprint)

# Initializing logging
logger = logging.getLogger(__name__)

# Running the app
if __name__ == "__main__":
    app.run(debug=True)
