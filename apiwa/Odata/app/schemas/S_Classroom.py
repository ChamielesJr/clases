# app/schemas/S_Classroom.py

from pydantic import BaseModel

class ClassroomCreate(BaseModel):
    nombre: str  # debe coincidir con el modelo

class ClassroomRead(ClassroomCreate):
    id: int

    class Config:
        from_attributes = True

class ClassroomUpdate(BaseModel):
    nombre: str
