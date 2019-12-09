from flask_restful import Resource, marshal_with

from db import UsersModel
from utils import get_authorized_user
from .structure import book_structure


class Library(Resource):

    @marshal_with(book_structure)
    def get(self, value):
        try:
            user = get_authorized_user(UsersModel)
            books = UsersModel.query.get(value).library
            if user and (user.id == value or user.role == "admin"):
                return books
            else:
                return [book for book in books if book.visibility]
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when got library with following error - {error}"
