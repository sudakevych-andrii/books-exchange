from flask_restful import Resource, marshal_with

from db import UsersModel
from .structure import book_structure


class Wishlist(Resource):

    @marshal_with(book_structure)
    def get(self, value):
        try:
            return UsersModel.query.get(value).wishlist
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when got library with following error - {error}"
