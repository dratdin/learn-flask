from bson.objectid import ObjectId
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from .. import bcrypt, login_manager, mongo
from . import users as blueprint
from .forms import LoginForm, RegistrationForm
from .models import User


@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one(ObjectId(user_id))
    if user_data:
        return User(user_data)

    return user_data


@blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        if form.validate():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            mongo.db.users.insert_one(
                {
                    "username": form.username.data,
                    "email": form.email.data,
                    "password": hashed_password,
                }
            )
            flash("You have been successfully registered!", "success")
            return redirect(url_for("users.register"))
        else:
            flash("Data invalid, check messages below", "danger")
    return render_template("users/register.html", form=form)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.is_submitted():
        if form.validate():
            user_data = mongo.db.users.find_one({"email": form.email.data})
            if user_data and bcrypt.check_password_hash(
                user_data["password"], form.password.data
            ):
                login_user(User(user_data))
                flash("Welcome!", "success")
                return redirect(url_for("todos.list"))
        flash("Unsuccessfull login, please check data", "danger")

    return render_template("users/login.html", form=form)


@blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.login"))
