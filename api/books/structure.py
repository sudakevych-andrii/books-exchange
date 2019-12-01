from flask_restful import fields

book_structure = {
    "id": fields.Integer,
    "author": fields.String,
    "title": fields.String,
    "publisher": fields.String,
    "year_edition": fields.String,
    "translator": fields.String,
    "user_id": fields.Integer,
    "visibility": fields.Integer,
    "exchange": fields.Integer
}
