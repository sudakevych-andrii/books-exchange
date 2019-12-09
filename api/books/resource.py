import json

from flask import request
from flask_restful import Resource, marshal_with

from db import BookModel, db, UsersModel
from utils import get_authorized_user
from .utils import *
from .parser import books_parser
from .structure import book_structure


class Books(Resource):

    @marshal_with(book_structure)
    def get(self, value=None):
        try:
            user = get_authorized_user(UsersModel)
            args = books_parser.parse_args()
            if value:
                return BookModel.query.get(value)
            else:
                return show_books(args, BookModel, user)
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when got list of books with following error - {error}"

    @marshal_with(book_structure)
    def post(self):
        try:
            data = json.loads(request.data)
            user = get_authorized_user(UsersModel)
            book = BookModel.query.get(data.get("id"))
            destination_dict = {
                "library": add_book_to_library,
                "wishlist": add_book_to_wishlist
            }
            if "destination" in data:
                destination_dict[data["destination"]](user, book)
            else:
                new_book = BookModel(**data)
                db.session.add(new_book)
                db.session.commit()
                return new_book
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when added room with following error - {error}"

    @marshal_with(book_structure)
    def put(self):
        try:
            data = json.loads(request.data)
            book = BookModel.query.get(data.get("id"))
            for key, value in data.items():
                setattr(book, key, value)
            db.session.commit()
            return book
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when updated book with following error - {error}"

    def delete(self):
        try:
            data = json.loads(request.data)
            book = BookModel.query.get(data.get("id"))
            db.session.delete(book)
            db.session.commit()
            return f"Successfully deleted a book {book.title}"
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when updated book with following error - {error}"
