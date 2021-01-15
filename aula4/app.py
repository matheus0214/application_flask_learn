from flask import Flask

from views import init_app
from users import users


def create_app():
    """Factory principal"""
    app = Flask(__name__)

    init_app(app)

    app.register_blueprint(users)

    return app
