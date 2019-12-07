from flask_restful import Resource, marshal_with

from db import UsersModel
from .structure import book_structure


class Library(Resource):

    @marshal_with(book_structure)
    def get(self, value):
        books = UsersModel.query.get(value).library
        return [book for book in books if book.query.filter(book.visibility == 1).all()]
