from flask import Blueprint
from flask_restful import Api

from .resource import Library

library = Blueprint("library", __name__)
api_library = Api(library)

api_library.add_resource(Library, "/users/<value>/library")
