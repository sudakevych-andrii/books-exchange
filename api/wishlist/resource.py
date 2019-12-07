from flask_restful import Resource, marshal_with

from db import UsersModel
from .structure import book_structure


class Wishlist(Resource):

    @marshal_with(book_structure)
    def get(self, value):
        return UsersModel.query.get(value).wishlist
