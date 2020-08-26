import os

from flask import render_template

from . import create_app, mongo

app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.shell_context_processor
def make_shell_context():
    return dict(mongo=mongo)


@app.route("/")
def index():
    todos = mongo.db.todos.find()
    return render_template("index.html", **{"todos": todos})
