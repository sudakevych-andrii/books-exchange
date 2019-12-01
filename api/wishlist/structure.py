from flask_restful import fields

book_structure = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String
}

wishlist_structure = {
    "id": fields.Integer,
    "wishlist": fields.Nested(book_structure)
}