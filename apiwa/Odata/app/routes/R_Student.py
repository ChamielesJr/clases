# app/routes/R_Student.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import SessionLocal
from app.models.M_Student import Student
from app.schemas.S_Student import StudentCreate, StudentRead, StudentUpdate
from typing import List

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[StudentRead])
async def read_students(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Student))
    return result.scalars().all()

@router.get("/{student_id}", response_model=StudentRead)
async def read_student(student_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/", response_model=StudentRead)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_session)):
    db_student = Student(**student.dict())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

@router.put("/{student_id}", response_model=StudentRead)
async def update_student(student_id: int, student: StudentUpdate, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    db_student = result.scalar_one_or_none()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)
    await db.commit()
    await db.refresh(db_student)
    return db_student

@router.delete("/{student_id}")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    db_student = result.scalar_one_or_none()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    await db.delete(db_student)
    await db.commit()
    return {"message": "Student deleted"}
