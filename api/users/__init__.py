from flask import Blueprint
from flask_restful import Api

from .resource import Users

users = Blueprint("users", __name__)
api_users = Api(users)

api_users.add_resource(Users, "/users", "/users/<value>")
