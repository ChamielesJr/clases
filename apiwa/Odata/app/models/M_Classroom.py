from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Classroom(Base):
    __tablename__ = "Paralelos"  # usa la tabla existente

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
