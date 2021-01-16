from flask import Blueprint

from .views import users_app

users = Blueprint("users", __name__, url_prefix="/users")


users_app(users)
