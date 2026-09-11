from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models.user import User


SECRET_KEY = "maint-ai-secret-key"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

def register_user(data, db: Session):

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "Technician")

    # Validate required fields
    if not name or not email or not password:
        return {
            "message": "Name, email and password are required"
        }, 400

    # Check existing user
    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return {
            "message": "Email already registered"
        }, 409

    # Hash password
    password_hash = pwd_context.hash(password)

    # Create user
    user = User(
        name=name,
        email=email,
        password_hash=password_hash,
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }, 201


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

def login_user(data, db: Session):

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {
            "message": "Email and password are required"
        }, 400

    # Find user
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return {
            "message": "Invalid email or password"
        }, 401

    # Verify password
    password_valid = pwd_context.verify(
        password,
        user.password_hash
    )

    if not password_valid:
        return {
            "message": "Invalid email or password"
        }, 401

    # JWT payload
    payload = {
        "user_id": user.user_id,
        "email": user.email,
        "role": user.role,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "Bearer",
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }, 200