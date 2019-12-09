import json

from flask import request
from flask_restful import Resource, marshal_with

from db import UsersModel, BookModel, db
from utils import get_authorized_user
from .structure import book_structure


class Wishlist(Resource):

    @marshal_with(book_structure)
    def get(self):
        try:
            user = get_authorized_user(UsersModel)
            return user.wishlist
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when got account wishlist with following error - {error}"

    def delete(self):
        try:
            data = json.loads(request.data)
            user = get_authorized_user(UsersModel)
            book = BookModel.query.get(data.get("id"))
            user.wishlist.remove(book)
            db.session.commit()
            return f"Successfully deleted a book {book.name} from wishlist"
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when deleted book from account wishlist with following error - {error}"
