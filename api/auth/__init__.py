from flask import Blueprint
from .resource import Registration, Login

auth = Blueprint("auth", __name__)

registration_view = Registration.as_view('register_view')
auth.add_url_rule(
    "/auth/register",
    view_func=registration_view,
    methods=['POST']
)

login_view = Login.as_view('login_view')
auth.add_url_rule(
    "/auth/login",
    view_func=login_view,
    methods=['POST']
)
