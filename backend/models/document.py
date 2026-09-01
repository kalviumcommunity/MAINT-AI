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


class Document(Base):
    __tablename__ = "documents"

    document_id = Column(Integer, primary_key=True, index=True)

    # Basic document information
    document_name = Column(String(255), nullable=False)
    document_type = Column(String(50), nullable=False, default="PDF")
    description = Column(Text, nullable=True)

    # File information
    file_path = Column(String(500), nullable=False)
    file_size = Column(Integer, nullable=True)

    # Document categorization
    category = Column(String(100), nullable=True)

    # Equipment association
    equipment_id = Column(
        Integer,
        ForeignKey("equipment.equipment_id"),
        nullable=True,
    )

    # Document processing / RAG indexing status
    processing_status = Column(
        String(50),
        nullable=False,
        default="pending",
    )

    # Number of chunks created from the document
    chunk_count = Column(Integer, nullable=False, default=0)

    # Timestamps
    uploaded_at = Column(
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

    # User who uploaded the document
    uploaded_by = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=True,
    )

    # Relationships
    equipment = relationship(
        "Equipment",
        back_populates="documents",
    )

    uploader = relationship(
        "User",
        back_populates="documents",
    )