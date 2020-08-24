from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()


def create_app(config_name):
    from .todos import todos as todos_blueprint
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/flask-app"
    mongo.init_app(app)

    app.register_blueprint(todos_blueprint)
    return app
