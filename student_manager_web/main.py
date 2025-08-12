from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Sinhvien
from schemas import StudentCreate, Student
from fastapi.middleware.cors import CORSMiddleware

# Khởi tạo bảng nếu chưa có
from database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quản Lý Sinh Viên")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  Thêm sinh viên
@app.post("/students", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    sv = Sinhvien(**student.dict())
    db.add(sv)
    db.commit()
    db.refresh(sv)
    return sv

#  Lấy danh sách sinh viên
@app.get("/students", response_model=list[Student])
def get_students(db: Session = Depends(get_db)):
    return db.query(Sinhvien).all()

#  Tìm sinh viên theo mã
@app.get("/students/search", response_model=list[Student])
def search_student_by_code(masinhvien: str, db: Session = Depends(get_db)):
    return db.query(Sinhvien).filter(Sinhvien.masinhvien == masinhvien).all()

#  Cập nhật sinh viên
@app.put("/students/{id}", response_model=Student)
def update_student(id: int, student: StudentCreate, db: Session = Depends(get_db)):
    sv = db.query(Sinhvien).filter(Sinhvien.id == id).first()
    if not sv:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên.")
    for key, value in student.dict().items():
        setattr(sv, key, value)
    db.commit()
    db.refresh(sv)
    return sv

#  Xóa sinh viên
@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    sv = db.query(Sinhvien).filter(Sinhvien.id == id).first()
    if not sv:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên.")
    db.delete(sv)
    db.commit()
    return {"message": "Xóa sinh viên thành công."}
