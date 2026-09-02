from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from utils.database import db

class Document(db.Model):
    __tablename__ = "documents"

    document_id = Column(Integer, primary_key=True, index=True)
    equipment_id = Column(
        Integer,
        ForeignKey("equipment.equipment_id", ondelete="SET NULL")
    )
    document_name = Column(String(255), nullable=False)
    document_type = Column(String(50), nullable=False)
    file_path = Column(Text, nullable=False)
    uploaded_by = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="SET NULL")
    )
    uploaded_at = Column(DateTime, server_default=func.current_timestamp())