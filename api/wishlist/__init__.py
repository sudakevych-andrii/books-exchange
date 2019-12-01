from flask import Blueprint
from flask_restful import Api

from .resource import Wishlist

wishlist = Blueprint("wishlist", __name__)
api_users = Api(wishlist)

api_users.add_resource(Wishlist, "/users/<value>/wishlist", "/users/<value>/wishlist")
