from flask import jsonify
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta

from models.user import User
from utils.database import db


bcrypt = Bcrypt()


# Secret key
SECRET_KEY = "maint-ai-secret-key"


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

def register_user(data):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "Technician")

    # Validate required fields
    if not name or not email or not password:
        return jsonify({
            "message": "Name, email and password are required"
        }), 400

    # Check existing user
    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return jsonify({
            "message": "Email already registered"
        }), 409

    # Hash password
    password_hash = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    # Create user
    user = User(
        name=name,
        email=email,
        password_hash=password_hash,
        role=role
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }), 201


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

def login_user(data):

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required"
        }), 400

    # Find user
    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    # Verify password
    password_valid = bcrypt.check_password_hash(
        user.password_hash,
        password
    )

    if not password_valid:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    # JWT payload
    payload = {
        "user_id": user.user_id,
        "email": user.email,
        "role": user.role,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({
        "message": "Login successful",
        "access_token": token,
        "token_type": "Bearer",
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }), 200