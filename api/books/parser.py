from flask_restful import reqparse

books_parser = reqparse.RequestParser()
books_parser.add_argument("author", type=str)
books_parser.add_argument("title", type=str)
books_parser.add_argument("year_edition", type=str)
books_parser.add_argument("exchange", type=int)

