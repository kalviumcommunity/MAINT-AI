from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from utils.database import db

class User(db.Model):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, default="Technician")
    created_at = Column(DateTime, server_default=func.current_timestamp())