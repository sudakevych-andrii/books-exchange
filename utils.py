from flask import request


def get_authorized_user(model):
    if request.headers.get("Authorization"):
        access_token = request.headers.get("Authorization").split(" ")[1]
        user_id = model.decode_token(access_token)
        return model.query.get(user_id)
    else:
        return None
