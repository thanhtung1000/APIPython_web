from pydantic import BaseModel
from typing import Optional
from datetime import date

class StudentCreate(BaseModel):
    full_name: str
    class_: str  
    gender: str
    birth_date: date
    phone_number: Optional[str]
    masinhvien: Optional[str]

class Student(StudentCreate):
    id: int

    class Config:
        orm_mode = True
