from flask_restful import Resource, marshal_with

from .structure import library_structure
from db import UsersModel


class Library(Resource):

    @marshal_with(library_structure)
    def get(self, value):
        return UsersModel.query.get(value)
