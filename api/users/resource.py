from flask_restful import Resource, marshal_with

from .structure import users_structure
from db import UsersModel


class Users(Resource):

    @marshal_with(users_structure)
    def get(self, value=None):
        try:
            if value:
                return UsersModel.query.get(value)
            return UsersModel.query.all()
        except (ValueError, KeyError, TypeError) as error:
            return f"Something went wrong when got users list with following error - {error}"
