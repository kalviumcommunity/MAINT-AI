from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

from backend.utils.database import Base


class Equipment(Base):
    __tablename__ = "equipment"

    equipment_id = Column(Integer, primary_key=True, index=True)
    equipment_code = Column(String(50), unique=True, nullable=False)
    equipment_name = Column(String(150), nullable=False)
    equipment_type = Column(String(100))
    model = Column(String(100))
    manufacturer = Column(String(100))
    status = Column(String(50), default="Operational")
    last_maintenance_date = Column(Date)
    created_at = Column(DateTime, server_default=func.current_timestamp())