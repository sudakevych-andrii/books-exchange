import json

from flask import request
from flask_restful import Resource, marshal_with

from db import UsersModel, BookModel, db
from .structure import wishlist_structure


class Wishlist(Resource):

    @marshal_with(wishlist_structure)
    def get(self, value):
        return UsersModel.query.get(value)

    def post(self, value):
        data = json.loads(request.data)
        user = UsersModel.query.get(value)
        book = BookModel.query.get(data.get("id"))
        user.wishlist.append(book)
        db.session.commit()
        return "Successfully added a book to wishlist"

    def delete(self, value):
        data = json.loads(request.data)
        user = UsersModel.query.get(value)
        book = BookModel.query.get(data.get("id"))
        user.wishlist.remove(book)
        db.session.commit()
        return "Successfully deleted a book from wishlist"
