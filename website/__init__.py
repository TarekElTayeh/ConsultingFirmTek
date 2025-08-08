"""Application factory and extensions."""

import logging
import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


# Initialize extensions
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
migrate = Migrate()
logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """Create and configure the Flask application."""

    app = Flask(__name__)

    # Load config from environment with fallbacks
    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        logger.warning("SECRET_KEY not set; using a development key")
        secret_key = "dev_key"
    app.config["SECRET_KEY"] = secret_key

    database_uri = os.environ.get("DATABASE_URI")
    if not database_uri:
        logger.warning("DATABASE_URI not set; using SQLite")
        database_uri = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Init extensions
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .auth import auth as auth_blueprint
    from .client_dashboard import client as client_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(client_blueprint)

    return app

