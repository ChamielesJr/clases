#aqui declaramos las importaciones 
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.models.M_Classroom import Paralelo
from app.schemas.S_Classroom import ClassroomCreate, ClassroomRead, ClassroomUpdate
from app.crud.C_Classroom import get_classrooms, create_classroom, update_classroom, delete_classroom

#creamos el enrutador con un prefijo comun para todas las rutas de paralelos
router = APIRouter(
    prefix="/classrooms",
    tags=["classrooms"]
)

#ruta get para obtener una lista de paralelos
#permite filtros por nombre, ordenamiento, limite y desplazamiento
@router.get("/", response_model=list[ClassroomRead])
async def read_classrooms(
    nombre: str = Query(None, description="filtrar por nombre del paralelo"),
    order_by: str = Query("id", description="campo por el que se ordena (ej. id, nombre, -nombre)"),
    limit: int = Query(10, ge=1, le=100, description="cantidad máxima de resultados"),
    offset: int = Query(0, ge=0, description="cuántos resultados omitir"),
    db: AsyncSession = Depends(get_db)
):
    return await get_classrooms(
        db=db,
        nombre=nombre,
        order_by=order_by,
        limit=limit,
        offset=offset
    )

#ruta post para crear un nuevo paralelo
#recibe los datos del esquema classroomcreate
@router.post("/", response_model=ClassroomRead)
async def add_classroom(classroom: ClassroomCreate, db: AsyncSession = Depends(get_db)):
    return await create_classroom(db, classroom)

#ruta put para actualizar un paralelo existente
#recibe el id y los nuevos datos a actualizar
@router.put("/{classroom_id}")
async def edit_classroom(classroom_id: int, classroom: ClassroomUpdate, db: AsyncSession = Depends(get_db)):
    await update_classroom(db, classroom_id, classroom)
    return {"message": "paralelo actualizado"}

#ruta delete para eliminar un paralelo por su id
@router.delete("/{classroom_id}")
async def remove_classroom(classroom_id: int, db: AsyncSession = Depends(get_db)):
    await delete_classroom(db, classroom_id)
    return {"message": "paralelo eliminado"}
