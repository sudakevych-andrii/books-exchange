import json

from flask import request
from flask_restful import Resource, marshal_with

from db import UsersModel, BookModel, db
from .structure import library_structure


class Library(Resource):

    @marshal_with(library_structure)
    def get(self, value):
        return UsersModel.query.get(value)

    def post(self, value):
        data = json.loads(request.data)
        user = UsersModel.query.get(value)
        book = BookModel.query.get(data.get("id"))
        user.library.append(book)
        db.session.commit()
        return "Successfully added a book to library"

    def delete(self, value):
        data = json.loads(request.data)
        user = UsersModel.query.get(value)
        book = BookModel.query.get(data.get("id"))
        user.library.remove(book)
        db.session.commit()
        return "Successfully deleted a book from library"
