# aqui declaramos las importaciones necesarias
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_db
from app.schemas import S_Student
from app.crud import C_Student

# definimos el enrutador con el prefijo /estudiantes
router = APIRouter(prefix="/estudiantes", tags=["estudiantes"])

# ruta get para listar estudiantes
# permite filtros por nombre, apellido, correo y paralelo
# soporta ordenamiento, paginación y búsqueda parcial
@router.get("/", response_model=List[S_Student.EstudianteGET])
async def listar_estudiantes(
    nombre: Optional[str] = Query(None, description="buscar por nombre"),
    apellido: Optional[str] = Query(None, description="buscar por apellido"),
    correo: Optional[str] = Query(None, description="buscar por correo"),
    paralelo_id: Optional[int] = Query(None, description="filtrar por id del paralelo"),
    order_by: Optional[str] = Query("id", description="campo por el que se ordena. ej: 'nombre', '-apellido'"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db)
):
    return await C_Student.get_all_students(
        db=db,
        nombre=nombre,
        apellido=apellido,
        correo=correo,
        paralelo_id=paralelo_id,
        order_by=order_by,
        limit=limit,
        offset=offset
    )

# ruta get para obtener un estudiante por su id
# si no lo encuentra, lanza un error 404
@router.get("/{estudiante_id}", response_model=S_Student.EstudianteGET)
async def obtener_estudiante(estudiante_id: int, db: AsyncSession = Depends(get_db)):
    estudiante = await C_Student.get_student_by_id(db, estudiante_id)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")
    return estudiante

# ruta post para crear un nuevo estudiante
# recibe los datos validados con estudiantepost
@router.post("/", response_model=S_Student.EstudianteGET)
async def crear_estudiante(estudiante: S_Student.EstudiantePOST, db: AsyncSession = Depends(get_db)):
    return await C_Student.create_student(db, estudiante)

# ruta put para actualizar un estudiante por su id
# si no se encuentra, lanza un error 404
@router.put("/{estudiante_id}", response_model=S_Student.EstudianteGET)
async def actualizar_estudiante(estudiante_id: int, estudiante: S_Student.EstudiantePUT, db: AsyncSession = Depends(get_db)):
    db_estudiante = await C_Student.update_student(db, estudiante_id, estudiante)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")
    return db_estudiante

# ruta delete para eliminar un estudiante por su id
# si no se encuentra, lanza un error 404
@router.delete("/{estudiante_id}", response_model=S_Student.EstudianteDELETE)
async def eliminar_estudiante(estudiante_id: int, db: AsyncSession = Depends(get_db)):
    db_estudiante = await C_Student.delete_student(db, estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")
    return db_estudiante
