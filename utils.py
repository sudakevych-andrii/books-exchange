from flask import request


def get_authorized_user(model):
    auth_header = request.headers.get("Authorization")
    access_token = auth_header.split(" ")[1]
    if access_token:
        user_id = model.decode_token(access_token)
        return model.query.get(user_id)
