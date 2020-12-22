from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_session import Session

from .config import configs

mongo = PyMongo()
bcrypt = Bcrypt()
session = Session()

login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"


def create_app(config_name):
    from .todos import todos as todos_blueprint
    from .users import users as users_blueprint

    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)
    mongo.init_app(app, port=int(app.config.get("MONGO_PORT")), host=app.config.get("MONGO_HOST"))
    bcrypt.init_app(app)
    session.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(todos_blueprint)
    app.register_blueprint(users_blueprint)
    return app
