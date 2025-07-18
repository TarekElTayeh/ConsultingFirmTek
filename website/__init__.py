from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
import os

# Initialize extensions
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load config from environment
    app.config['SECRET_KEY'] =os.environ.get('SECRET_KEY', 'dev_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Init extensions
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)

    #Register blueprints
    from .auth import auth as auth_blueprint
    from .client_dashboard import client as client_blueprint
    from .consultant_dashboard import consultant as consultant_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(client_blueprint)
    app.register_blueprint(consultant_blueprint)

    return app