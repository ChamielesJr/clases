from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.models.M_Classroom import Classroom
from app.schemas.S_Classroom import ClassroomCreate, ClassroomUpdate

# Obtener todos los registros
async def get_classrooms(db: AsyncSession):
    result = await db.execute(select(Classroom))
    return result.scalars().all()

# Crear un nuevo registro
async def create_classroom(db: AsyncSession, classroom: ClassroomCreate):
    new_classroom = Classroom(nombre=classroom.nombre)  # ← Campo explícito
    db.add(new_classroom)
    await db.commit()
    await db.refresh(new_classroom)
    return new_classroom

# Actualizar un registro existente
async def update_classroom(db: AsyncSession, classroom_id: int, classroom: ClassroomUpdate):
    await db.execute(
        update(Classroom)
        .where(Classroom.id == classroom_id)
        .values(nombre=classroom.nombre)  # ← Campo explícito
    )
    await db.commit()

# Eliminar un registro
async def delete_classroom(db: AsyncSession, classroom_id: int):
    await db.execute(
        delete(Classroom).where(Classroom.id == classroom_id)
    )
    await db.commit()
