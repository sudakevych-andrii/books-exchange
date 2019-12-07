from flask import Blueprint
from flask_restful import Api

from .resource import Wishlist

account_wishlist = Blueprint("account_wishlist", __name__)
api_account_wishlist = Api(account_wishlist)

api_account_wishlist.add_resource(Wishlist, "/account/wishlist")
