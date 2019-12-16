from flask import Flask
from flask_cors import CORS

from config import run_config
from db import db, migrate
from api.auth import auth
from api.users import users
from api.account.library import account_library
from api.account.wishlist import account_wishlist
from api.books import books
from api.library import library
from api.wishlist import wishlist


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(run_config())

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(account_library)
    app.register_blueprint(account_wishlist)
    app.register_blueprint(books)
    app.register_blueprint(library)
    app.register_blueprint(wishlist)

    db.create_all(app=app)

    return app
