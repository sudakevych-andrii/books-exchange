import json

from flask import request
from flask_restful import Resource, marshal_with

from db import UsersModel, BookModel, db
from utils import get_authorized_user
from .structure import book_structure


class Library(Resource):

    @marshal_with(book_structure)
    def get(self):
        user = get_authorized_user(UsersModel)
        return user.library

    # Need to move to books resource
    def post(self, value):
        data = json.loads(request.data)
        user = UsersModel.query.get(value)
        book = BookModel.query.get(data.get("id"))
        user.library.append(book)
        db.session.commit()
        return "Successfully added a book to library"

    def put(self):
        data = json.loads(request.data)
        book = BookModel.query.get(data.get("id"))
        for key, value in data.items():
            setattr(book, key, value)
            if not data.get("visibility"):
                book.exchange = 0
        db.session.commit()
        return "Successfully updated a book in library"

    def delete(self, value):
        data = json.loads(request.data)
        user = UsersModel.query.get(value)
        book = BookModel.query.get(data.get("id"))
        user.library.remove(book)
        db.session.commit()
        return "Successfully deleted a book from library"
