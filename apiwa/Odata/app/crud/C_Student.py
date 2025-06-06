from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.models.M_Student import Student
from app.schemas.S_Student import StudentCreate, StudentUpdate

async def get_students(db: AsyncSession):
    result = await db.execute(select(Student))
    return result.scalars().all()

async def create_student(db: AsyncSession, student: StudentCreate):
    new_student = Student(**student.dict())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student

async def update_student(db: AsyncSession, student_id: int, student: StudentUpdate):
    await db.execute(update(Student).where(Student.id == student_id).values(**student.dict()))
    await db.commit()

async def delete_student(db: AsyncSession, student_id: int):
    await db.execute(delete(Student).where(Student.id == student_id))
    await db.commit()
