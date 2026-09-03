from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from utils.database import db


class Query(db.Model):
    __tablename__ = "queries"

    query_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="SET NULL")
    )
    equipment_id = Column(
        Integer,
        ForeignKey("equipment.equipment_id", ondelete="SET NULL")
    )
    issue_id = Column(
        Integer,
        ForeignKey("issues.issue_id", ondelete="SET NULL")
    )
    query_text = Column(Text, nullable=False)
    ai_response = Column(Text)
    created_at = Column(DateTime, server_default=func.current_timestamp())
