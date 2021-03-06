from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), server_default="user")
    library = db.relationship("BookModel", backref="library", foreign_keys="BookModel.user_id")
    wishlist = db.relationship("BookModel", secondary="wishlist", backref=db.backref("wishlist"))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def generate_token(self, user_id):
        try:
            payload = {
                "exp": datetime.utcnow() + timedelta(minutes=5),
                "iat": datetime.utcnow(),
                "sub": user_id
            }
            jwt_string = jwt.encode(
                payload,
                current_app.config.get("SECRET_KEY"),
                algorithm='HS256'
            )
            return jwt_string
        except Exception as e:
            return str(e)

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"), algorithms=['HS256'])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(255))
    year_edition = db.Column(db.Integer)
    translator = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    visibility = db.Column(db.SMALLINT, server_default="1")
    exchange = db.Column(db.SMALLINT, server_default="1")


wishlist = db.Table(
    'wishlist',
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("book_id", db.Integer, db.ForeignKey("books.id"))
)
