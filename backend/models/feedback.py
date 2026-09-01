from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Query for which feedback was given
    query_id = Column(
        Integer,
        ForeignKey("queries.query_id"),
        nullable=False,
    )

    # User who submitted the feedback
    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False,
    )

    # True = Helpful, False = Not Helpful
    is_helpful = Column(
        Boolean,
        nullable=False,
    )

    # Optional feedback comment
    comment = Column(
        Text,
        nullable=True,
    )

    # Feedback timestamp
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    query = relationship(
        "Query",
        back_populates="feedback",
    )

    user = relationship(
        "User",
        back_populates="feedback",
    )