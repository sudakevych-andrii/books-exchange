from flask_restful import fields

book_structure = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String
}

library_structure = {
    "id": fields.Integer,
    "name": fields.String,
    "library": fields.Nested(book_structure)
}