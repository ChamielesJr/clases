from pydantic import BaseModel, EmailStr # type: ignore
from typing import Optional

# Modelo base que define los campos comunes para estudiante
class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    cedula: str 
    correo: EmailStr
    paralelo_id: Optional[int]

# Modelo para crear un estudiante (POST)
class EstudiantePOST(EstudianteBase):
    pass

# Modelo para actualizar un estudiante (PUT), incluye el id
class EstudiantePUT(EstudianteBase):
    id: int

# Modelo para obtener un estudiante (GET), incluye el id
class EstudianteGET(BaseModel):
    id: int
    nombre: str
    apellido: str
    cedula: str  # <--- AÑADIDO
    correo: EmailStr
    paralelo_id: int

    model_config = {
        "from_attributes": True
    }

# Modelo para eliminar un estudiante (DELETE), devuelve id y nombre
class EstudianteDELETE(BaseModel):
    id: int
    nombre: str

    model_config = {
        "from_attributes": True
    }
