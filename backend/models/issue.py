from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from utils.database import db


class Issue(db.Model):
    __tablename__ = "issues"

    issue_id = Column(Integer, primary_key=True, index=True)
    equipment_id = Column(
        Integer,
        ForeignKey("equipment.equipment_id", ondelete="CASCADE"),
        nullable=False
    )
    reported_by = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="SET NULL")
    )
    error_code = Column(String(100))
    description = Column(Text, nullable=False)
    category = Column(String(100))
    severity = Column(String(20), default="Medium")
    status = Column(String(30), default="Open")
    reported_at = Column(DateTime, server_default=func.current_timestamp())
    resolved_at = Column(DateTime)
