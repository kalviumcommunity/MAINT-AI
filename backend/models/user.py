from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from utils.database import db

class User(db.Model):
    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # User information
    name = Column(
        String(100),
        nullable=False,
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True,
    )

    # Store hashed password only
    password_hash = Column(
        String(255),
        nullable=False,
    )

    # User role
    role = Column(
        String(50),
        nullable=False,
        default="Technician",
    )

    # Account creation time
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    queries = relationship(
        "Query",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    documents = relationship(
        "Document",
        back_populates="uploader",
    )

    feedback = relationship(
        "Feedback",
        back_populates="user",
        cascade="all, delete-orphan",
    )