from flask import Blueprint

todos = Blueprint("todos", __name__, template_folder="templates")

from . import views  # noqa
