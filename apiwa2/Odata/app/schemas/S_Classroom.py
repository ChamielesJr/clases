from pydantic import BaseModel
from datetime import datetime

# Modelo base que define los campos comunes del paralelo
class ClassroomBase(BaseModel):
    nombre: str

# Modelo para crear un paralelo (POST)
class ClassroomCreate(ClassroomBase):
    pass

# Modelo para actualizar un paralelo (PUT)
class ClassroomUpdate(ClassroomBase):
    pass

# Modelo para obtener un paralelo (GET), incluye campos adicionales
class ClassroomRead(ClassroomBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True  # Permite crear el modelo desde objetos ORM
    }
