import json

from flask import request
from flask_restful import Resource, marshal_with

from db import UsersModel, BookModel, db
from utils import get_authorized_user
from .structure import book_structure


class Library(Resource):

    @marshal_with(book_structure)
    def get(self):
        try:
            user = get_authorized_user(UsersModel)
            return user.library
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when got account library with following error - {error}"

    def put(self):
        try:
            data = json.loads(request.data)
            book = BookModel.query.get(data.get("id"))
            for key, value in data.items():
                setattr(book, key, value)
                if not data.get("visibility"):
                    book.exchange = 0
            db.session.commit()
            return book
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when updated book in account library with following error - {error}"

    def delete(self, value):
        try:
            data = json.loads(request.data)
            user = UsersModel.query.get(value)
            book = BookModel.query.get(data.get("id"))
            user.library.remove(book)
            db.session.commit()
            return f"Successfully deleted a book {book.name} from library"
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when deleted book from account library with following error - {error}"
