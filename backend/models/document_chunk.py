from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector

from utils.database import db


class DocumentChunk(db.Model):
    __tablename__ = "document_chunks"

    chunk_id = Column(Integer, primary_key=True, index=True)
    document_id = Column(
        Integer,
        ForeignKey("documents.document_id", ondelete="CASCADE"),
        nullable=False
    )
    chunk_index = Column(Integer, nullable=False)
    chunk_text = Column(Text, nullable=False)
    page_number = Column(Integer)
    embedding = Column(Vector(1024))
    created_at = Column(DateTime, server_default=func.current_timestamp())
