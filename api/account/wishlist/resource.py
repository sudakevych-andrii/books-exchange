import json

from flask import request
from flask_restful import Resource, marshal_with

from db import UsersModel, BookModel, db
from utils import get_authorized_user
from .structure import book_structure


class Wishlist(Resource):

    @marshal_with(book_structure)
    def get(self):
        user = get_authorized_user(UsersModel)
        return user.wishlist

    # Need to move to books resource
    def post(self, value):
        data = json.loads(request.data)
        user = UsersModel.query.get(value)
        book = BookModel.query.get(data.get("id"))
        user.wishlist.append(book)
        db.session.commit()
        return "Successfully added a book to wishlist"

    def delete(self):
        data = json.loads(request.data)
        user = get_authorized_user(UsersModel)
        book = BookModel.query.get(data.get("id"))
        user.wishlist.remove(book)
        db.session.commit()
        return "Successfully deleted a book from wishlist"
