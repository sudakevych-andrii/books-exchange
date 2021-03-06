import json

from flask import make_response, request, jsonify
from flask.views import MethodView

from db import UsersModel


class Registration(MethodView):

    def post(self):
        try:
            data = json.loads(request.data)
            user = UsersModel.query.filter_by(email=data["email"]).first()
            if not user:
                user = UsersModel(**data)
                user.save()
                return "You registered successfully. Please log in."
            else:
                return 'User already exists. Please login.'
        except Exception as error:
            return str(error)


class Login(MethodView):

    def post(self):
        try:
            data = json.loads(request.data)
            user = UsersModel.query.filter_by(email=data["email"]).first()
            if user and user.password_is_valid(data["password"]):
                access_token = user.generate_token(user.id)
                if access_token:
                    response = {
                        "message": "You logged in successfully.",
                        "access_token": access_token.decode()
                    }
                    return make_response(jsonify(response))
                else:
                    return "Invalid email or password, Please try again"
        except Exception as error:
            return str(error)
