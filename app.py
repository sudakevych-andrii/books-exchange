from flask import Flask

from config import run_config
from db import db
from api.auth import auth
from api.users import users
from api.books import books
from api.library import library


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(books)
    app.register_blueprint(library)

    db.create_all(app=app)

    return app
