from flask_restful import fields

book_structure = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String
}
