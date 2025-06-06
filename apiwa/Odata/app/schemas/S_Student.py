from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    classroom_id: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

    class Config:
        from_attributes = True
