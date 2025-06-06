from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import SessionLocal
from app.schemas.S_Classroom import ClassroomCreate, ClassroomRead, ClassroomUpdate
from app.crud.C_Classroom import get_classrooms, create_classroom, update_classroom, delete_classroom

router = APIRouter(
    prefix="/classrooms",
    tags=["Classrooms"]
)


async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/", response_model=list[ClassroomRead])
async def read_classrooms(db: AsyncSession = Depends(get_db)):
    return await get_classrooms(db)

@router.post("/", response_model=ClassroomRead)
async def add_classroom(classroom: ClassroomCreate, db: AsyncSession = Depends(get_db)):
    return await create_classroom(db, classroom)

@router.put("/{classroom_id}")
async def edit_classroom(classroom_id: int, classroom: ClassroomUpdate, db: AsyncSession = Depends(get_db)):
    await update_classroom(db, classroom_id, classroom)
    return {"message": "Classroom updated"}

@router.delete("/{classroom_id}")
async def remove_classroom(classroom_id: int, db: AsyncSession = Depends(get_db)):
    await delete_classroom(db, classroom_id)
    return {"message": "Classroom deleted"}

