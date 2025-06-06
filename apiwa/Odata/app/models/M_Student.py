from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Student(Base):
    __tablename__ = "Estudiantes"  # usa la tabla existente

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    paralelo_id = Column(Integer, ForeignKey("Paralelos.id"), nullable=False)
