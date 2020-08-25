import datetime
from flask import render_template, flash, redirect, url_for
from .. import mongo
from . import todos as todos_blueprint
from .forms import TodoCreateForm


@todos_blueprint.route("/todos")
def list():
    todos = mongo.db.todos.find()
    return render_template("todos/list.html", todos=todos)


@todos_blueprint.route("/todos/new", methods=["GET", "POST"])
def create():
    form = TodoCreateForm()
    if form.validate_on_submit():
        mongo.db.todos.insert_one({
            "title": form.title.data,
            "text": form.text.data,
            "url": form.url.data,
            "date": datetime.datetime.combine(form.date.data, datetime.time.min),
        })

        flash(f"Todo {form.title.data} successfully created", "success")
        return redirect(url_for("todos.list"))
    else:
        flash("Something went wrong ;(", "danger")

    return render_template("todos/create.html", form=form)


@todos_blueprint.route("/todos/<ObjectId:id>")
def detail(id):
    todo = mongo.db.todos.find_one_or_404(id)
    return render_template("todos/detail.html", todo=todo)


@todos_blueprint.route("/todos/<ObjectId:id>")
def change(id):
    todo = mongo.db.todos.find_one_or_404(id)
    return render_template("todos/detail.html", todo=todo)
