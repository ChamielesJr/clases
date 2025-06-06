from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.M_Classroom import Paralelo

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    cedula = Column(String, unique=True)
    correo = Column(String, nullable=False, unique=True)
    paralelo_id = Column(Integer, ForeignKey("paralelos.id"), nullable=True)

    paralelo = relationship("Paralelo", back_populates="estudiantes")
