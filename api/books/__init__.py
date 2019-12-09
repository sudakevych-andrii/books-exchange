from flask import Blueprint
from flask_restful import Api

from .resource import Books

books = Blueprint("books", __name__)
api_books = Api(books)

api_books.add_resource(Books, "/books", "/books/<book_id>")
