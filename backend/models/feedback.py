from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.sql import func

from utils.database import db


class Feedback(db.Model):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(
        Integer,
        ForeignKey("queries.query_id", ondelete="CASCADE"),
        nullable=False
    )
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="SET NULL")
    )
    rating = Column(Integer)
    comments = Column(Text)
    created_at = Column(DateTime, server_default=func.current_timestamp())

    __table_args__ = (
        CheckConstraint(
            "rating >= 1 AND rating <= 5",
            name="rating_range"
        ),
    )
