from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base


#representa la tabla paralelos en la base de datos.
#hereda de Base para que SQLAlchemy pueda mapearlo como una tabla real.
class Paralelo(Base):
    __tablename__ = "paralelos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    estudiantes = relationship("Estudiante", back_populates="paralelo")
