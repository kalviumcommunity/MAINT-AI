from flask import Blueprint, request

from controllers.auth_controller import register_user, login_user


auth_router = Blueprint(
    "auth_router",
    __name__,
    url_prefix="/api/auth"
)


@auth_router.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    return register_user(data)


@auth_router.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    return login_user(data)