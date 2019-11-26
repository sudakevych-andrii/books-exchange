from flask_restful import fields

book_structure = {
    "id": fields.Integer,
    "author": fields.String,
    "title": fields.String,
    "edition": fields.String,
    "year_edition": fields.String,
    "translator": fields.String,
    "user_id": fields.Integer
}
