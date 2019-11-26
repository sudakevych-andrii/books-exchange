import json

from flask import request
from flask_restful import Resource, marshal_with

from db import BookModel, db
from .structure import book_structure


class Books(Resource):

    @marshal_with(book_structure)
    def get(self, value=None):
        if value:
            return BookModel.query.get(value)
        return BookModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_book = BookModel(**data)
        db.session.add(new_book)
        db.session.commit()
        return "Successfully added a new book"

    def put(self, value):
        data = json.loads(request.data)
        book = BookModel.query.get(value)
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return "Successfully updated a book"

    def delete(self, value):
        book = BookModel.query.get(value)
        db.session.delete(book)
        db.session.commit()
        return "Successfully deleted a book"
