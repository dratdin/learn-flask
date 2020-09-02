import datetime

from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from .. import mongo
from . import todos as blueprint
from .forms import TodoCreateForm, TodoUpdateForm


@blueprint.route("/todos")
@login_required
def list():
    todos = mongo.db.todos.find()
    return render_template("todos/list.html", todos=todos)


@blueprint.route("/todos/new", methods=["GET", "POST"])
@login_required
def create():
    form = TodoCreateForm()
    if form.is_submitted():
        if form.validate():
            mongo.db.todos.insert_one(
                {
                    "title": form.title.data,
                    "text": form.text.data,
                    "url": form.url.data,
                    "date": datetime.datetime.combine(
                        form.date.data, datetime.time.min
                    ),
                }
            )

            flash(f"Todo {form.title.data} successfully created", "success")
            return redirect(url_for("todos.list"))
        else:
            flash("Something went wrong ;(", "danger")

    return render_template("todos/create.html", form=form)


@blueprint.route("/todos/<ObjectId:id>")
@login_required
def detail(id):
    todo = mongo.db.todos.find_one_or_404(id)
    return render_template("todos/detail.html", todo=todo)


@blueprint.route("/todos/<ObjectId:id>/edit", methods=["GET", "POST"])
@login_required
def update(id):
    todo = mongo.db.todos.find_one_or_404(id)
    form = TodoUpdateForm(data=todo)
    if form.is_submitted():
        if form.validate():
            mongo.db.todos.update_one(
                {"_id": id},
                {
                    "$set": {
                        "title": form.title.data,
                        "text": form.text.data,
                        "url": form.url.data,
                        "date": datetime.datetime.combine(
                            form.date.data, datetime.time.min
                        ),
                    }
                },
            )
            flash(f"Todo {form.title.data} successfully updated", "success")
            return redirect(url_for("todos.detail", id=id))
        else:
            flash("Something went wrong ;(", "danger")
    return render_template("todos/update.html", form=form, todo=todo)


@blueprint.route("/todos/<ObjectId:id>", methods=["POST"])
@login_required
def delete(id):
    title = mongo.db.todos.find_one_or_404(id)["title"]
    mongo.db.todos.delete_one({"_id": id})
    flash(f"Todo {title} successfully deleted", "success")
    return redirect(url_for("todos.list"))
