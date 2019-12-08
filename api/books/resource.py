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
        user = get_authorized_user(UsersModel)
        args = books_parser.parse_args()
        if value:
            return BookModel.query.get(value)
        else:
            return show_books(args, BookModel, user)

    def post(self):
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
        return "Successfully added a new book"

    def put(self):
        data = json.loads(request.data)
        book = BookModel.query.get(data.get("id"))
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return "Successfully updated a book"

    def delete(self):
        data = json.loads(request.data)
        book = BookModel.query.get(data.get("id"))
        db.session.delete(book)
        db.session.commit()
        return "Successfully deleted a book"
