from sqlalchemy import select, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.M_Student import Estudiante
from app.schemas.S_Student import EstudiantePOST, EstudiantePUT
from fastapi import HTTPException

#aqui tenemos el metodo principal de la lectura de los filtros, orden y paginacion para los estudiantes 
#existentes en la base de datos
async def get_all_students(
    db: AsyncSession,
    nombre: str = None,
    apellido: str = None,
    correo: str = None,
    paralelo_id: int = None,
    order_by: str = None,
    limit: int = None,
    offset: int = None
):
    query = select(Estudiante)

    # Filtros
    if nombre:
        query = query.where(Estudiante.nombre.ilike(f"%{nombre}%"))
    if apellido:
        query = query.where(Estudiante.apellido.ilike(f"%{apellido}%"))
    if correo:
        query = query.where(Estudiante.correo.ilike(f"%{correo}%"))
    if paralelo_id is not None:
        query = query.where(Estudiante.paralelo_id == paralelo_id)

    # Ordenamiento
    #por este if ordena los resultados por el campo especificado ascendente por defecto 
    #o descendente si comienza con un -
    if order_by:
        if order_by.startswith("-"):
            campo = order_by[1:]
            orden = desc
        else:
            campo = order_by
            orden = asc
    #verifica qye ek campo exista enelo modelo estudiante
        if hasattr(Estudiante, campo):
            query = query.order_by(orden(getattr(Estudiante, campo)))

    # Paginación
    #Aplica desplazamiento offset y límite de resultados limit
    if offset is not None:
        query = query.offset(offset)
    if limit is not None:
        query = query.limit(limit)

    #por aqui se ejecuta kla consulta y nos devuelve la lista de estudiantes encontrados 
    result = await db.execute(query)
    return result.scalars().all()

#obtiene los estudiantes por Id
async def get_student_by_id(db: AsyncSession, student_id: int):
    result = await db.execute(
        select(Estudiante).where(Estudiante.id == student_id)
    )
    return result.scalar_one_or_none()

#crea a los estudiantes
async def create_student(db: AsyncSession, student: EstudiantePOST):
    db_student = Estudiante(**student.model_dump())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

#actualizar estudiamtes 
#busca al estudiante por el id
#solo guarda los datos que fueron ingresados y asi mismo ignora lo que no se ingresaron o pasaron 
#guarda los cambios del estudiante y retrna al nmismo estudiante actualizado
async def update_student(db: AsyncSession, student_id: int, student: EstudiantePUT):
    result = await db.execute(
        select(Estudiante).where(Estudiante.id == student_id)
    )
    db_student = result.scalar_one_or_none()
    if db_student:
        for key, value in student.model_dump(exclude_unset=True).items():
            setattr(db_student, key, value)
        await db.commit()
        await db.refresh(db_student)
    return db_student

# busca el estudiante por ID.
#si lo encuentra, lo elimina y confirma la operación.
#retorna el estudiante eliminado (o None si no se encontró).
async def delete_student(db: AsyncSession, student_id: int):
    result = await db.execute(
        select(Estudiante).where(Estudiante.id == student_id)
    )
    db_student = result.scalar_one_or_none()
    if db_student:
        await db.delete(db_student)
        await db.commit()
    return db_student