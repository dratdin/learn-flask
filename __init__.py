from flask import Flask
from flask_pymongo import PyMongo

from .config import configs

mongo = PyMongo()


def create_app(config_name):
    from .todos import todos as todos_blueprint

    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)
    mongo.init_app(app)

    app.register_blueprint(todos_blueprint)
    return app
