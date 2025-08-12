from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

app = FastAPI(title="Student Management API")

# Dữ liệu lưu tạm thời bằng Dictionary
students_db: Dict[str, "Student"] = {}

# Định nghĩa model dữ liệu sinh viên
class Student(BaseModel):
    id: str
    name: str
    birthdate: Optional[str] = None
    class_name: Optional[str] = None
    email: Optional[EmailStr] = None

# Thêm sinh viên mới
@app.post("/students", summary="Thêm sinh viên mới")
def add_student(student: Student):
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Mã sinh viên đã tồn tại.")
    students_db[student.id] = student
    return {"message": "Thêm sinh viên thành công.", "student": student}

#  Tra cứu sinh viên theo mã
@app.get("/students/{student_id}", summary="Tra cứu sinh viên theo mã")
def get_student(student_id: str):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên.")
    return student

# Lấy danh sách tất cả sinh viên
@app.get("/students", summary="Lấy danh sách tất cả sinh viên")
def list_students():
    return {"students": list(students_db.values())}

# Cập nhật thông tin sinh viên
@app.put("/students/{student_id}", summary="Cập nhật thông tin sinh viên")
def update_student(student_id: str, updated_student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên để cập nhật.")
    if student_id != updated_student.id:
        raise HTTPException(status_code=400, detail="ID không khớp với dữ liệu cập nhật.")
    students_db[student_id] = updated_student
    return {"message": "Cập nhật thông tin thành công.", "student": updated_student}

# Xóa sinh viên
@app.delete("/students/{student_id}", summary="Xóa sinh viên")
def delete_student(student_id: str):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên để xóa.")
    deleted_student = students_db.pop(student_id)
    return {"message": "Xóa sinh viên thành công.", "student": deleted_student}
