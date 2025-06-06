#aqui declaramos las importaciones 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, asc, desc
from fastapi import HTTPException
from app.models.M_Classroom import Paralelo
from app.schemas.S_Classroom import ClassroomCreate, ClassroomUpdate

#nos ayud a obtener una lista de paralelos con opciones de filtro, ordenamiento y paginacion
async def get_classrooms(
    db: AsyncSession,
    nombre: str = None,
    order_by: str = None,
    limit: int = None,
    offset: int = None
):
    query = select(Paralelo)

    # Filtro por nombre si se proporciona
    if nombre:
        query = query.where(Paralelo.nombre.ilike(f"%{nombre}%"))

    # Ordenamiento
    if order_by:
        if order_by.startswith("-"):
            campo = order_by[1:]
            orden = desc
        else:
            campo = order_by
            orden = asc

        if hasattr(Paralelo, campo):
            query = query.order_by(orden(getattr(Paralelo, campo)))
        else:
            raise HTTPException(status_code=400, detail=f"Campo '{campo}' no válido para ordenamiento")

    # Paginación
    if offset is not None:
        query = query.offset(offset)
    if limit is None:
        limit = 50  # ← Límite por defecto
    query = query.limit(limit)

    result = await db.execute(query)
    return result.scalars().all()

#crea un nuevo paralelo, por aqui se reciben los datos validados por ClassroomCreate lo que crea 
#un nuevo objeto llamado paralelo que lo guarda en la base de datos para al final devolverlo 
#como el objetivo creado
async def create_classroom(db: AsyncSession, classroom: ClassroomCreate):
    nuevo = Paralelo(nombre=classroom.nombre)
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

#actualiza un paralelo ya existente 
#Busca el paralelo por ID y actualiza su nombre.
#Usa sqlalchemy_update para aplicar cambios en la base de datos.
async def update_classroom(db: AsyncSession, classroom_id: int, classroom: ClassroomUpdate):
    query = (
        sqlalchemy_update(Paralelo)
        .where(Paralelo.id == classroom_id)
        .values(nombre=classroom.nombre)
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(query)
    await db.commit()

#elimina un paralelo 
#Busca el paralelo por ID.
#Si no existe, lanza un error 404.
#Si existe, lo elimina de la base de datos.
async def delete_classroom(db: AsyncSession, classroom_id: int):
    result = await db.execute(select(Paralelo).where(Paralelo.id == classroom_id))
    classroom = result.scalar_one_or_none()
    if classroom is None:
        raise HTTPException(status_code=404, detail="Paralelo no encontrado")
    await db.delete(classroom)
    await db.commit()
