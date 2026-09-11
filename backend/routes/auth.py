from sqlalchemy.orm import Session

from controllers.auth_controller import (
    register_user,
    login_user
)


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

def register(data, db: Session):
    """
    Register a new user.
    """

    return register_user(
        data,
        db
    )


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

def login(data, db: Session):
    """
    Authenticate an existing user.
    """

    return login_user(
        data,
        db
    )