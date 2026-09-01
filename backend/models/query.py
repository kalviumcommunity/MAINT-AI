from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Query(Base):
    __tablename__ = "queries"

    query_id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # User who submitted the query
    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False,
    )

    # Equipment related to the problem
    equipment_id = Column(
        Integer,
        ForeignKey("equipment.equipment_id"),
        nullable=True,
    )

    # Equipment ID entered by technician
    equipment_code = Column(
        String(100),
        nullable=True,
    )

    # Error code reported by the machine
    error_code = Column(
        String(100),
        nullable=True,
    )

    # Problem / symptoms described by technician
    problem_description = Column(
        Text,
        nullable=False,
    )

    # Additional information provided by technician
    additional_information = Column(
        Text,
        nullable=True,
    )

    # AI-generated troubleshooting response
    response = Column(
        Text,
        nullable=True,
    )

    # Query processing status
    status = Column(
        String(50),
        nullable=False,
        default="pending",
    )

    # Timestamps
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    user = relationship(
        "User",
        back_populates="queries",
    )

    equipment = relationship(
        "Equipment",
        back_populates="queries",
    )

    feedback = relationship(
        "Feedback",
        back_populates="query",
        cascade="all, delete-orphan",
    )