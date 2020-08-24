from flask import render_template

from .. import mongo
from . import todos as todos_blueprint


@todos_blueprint.route("/todos")
def todos_list():
    todos = mongo.db.todos.find()
    return render_template("todos/list.html", todos=todos)


@todos_blueprint.route("/todos/new", methods=["GET", "POST"])
def todos_new():
    todos = mongo.db.todos.find()
    return render_template("todos/list.html", todos=todos)


@todos_blueprint.route("/todos/<ObjectId:id>")
def todos_detail(id):
    todo = mongo.db.todos.find_one_or_404(id)
    return render_template("todos/detail.html", todo=todo)


@todos_blueprint.route("/todos/<ObjectId:id>")
def todos_change(id):
    todo = mongo.db.todos.find_one_or_404(id)
    return render_template("todos/detail.html", todo=todo)
