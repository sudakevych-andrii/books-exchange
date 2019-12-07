from flask import Blueprint
from flask_restful import Api

from .resource import Library

account_library = Blueprint("account_library", __name__)
api_account_library = Api(account_library)

api_account_library.add_resource(Library, "/account/library")
