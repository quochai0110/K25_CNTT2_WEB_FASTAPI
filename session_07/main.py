# viết API lấy toàn bộ danh sách sinh viên lớp CNTT2
from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
app = FastAPI()
students = [
    {"id": 1, "name": "Vinh", "password": 123456},
    {"id": 2, "name": "Nhung", "password": 454545},
    {"id": 3, "name": "Đức", "password": 232323},
]
result = [
    {"id": 1, "name": "Vinh"},
    {"id": 2, "name": "Nhung"},
    {"id": 3, "name": "Đức"},
]
#  CẤU HÌNH BASEMODEL TRẢ VỀ 1 SINH VIÊN
class StudentResponse(BaseModel):
    id: int
    name:str
# CẤU HÌNH BASEMODE TRẢ VỀ DANH SÁCH SINH VIÊN
class StudentListResponse(BaseModel):
    data: list[StudentResponse]
@app.get("/students",response_model=StudentListResponse)
def get_students():
    return {
        "message":"lấy danh sách thành công!",
        "data":students
    }
""" 
C1: DÙNG RESPONSE MODEL
C2: XỬ LÝ DANH SÁCH SINH VIÊN BỎ TRƯỜNG PASSWORD

"""
# VIẾT API LẤY CHI TIẾT THÔNG TIN CỦA 1 SINH VIÊN
@app.get("/students/{student_id}",response_model=StudentResponse)
def get_student_detail(student_id:int):
    print("id của sinh viên", student_id)
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(
        status_code = 404,
        detail="Không tìm thấy sinh viên"
    )
    
#  API thêm sinh viên
class Student(BaseModel):
    id: int
    name: str
    password: str
    
@app.post("/students",status_code = status.HTTP_201_CREATED)
def create_student(student: Student):
    print("thông tin sinh viên vừa thêm",student)
    students.append(student)
""" 

    HTTP status code:
    200- 299: thành công hoặc thất bại 
    400- 499: Lỗi client
    >= 500  : Lỗi server
    thêm sinh viên thành công: 201
    thêm sinh viên thất bại:  400 bad request 
"""
""" 

CẤU TRÚC API RESPONSE

5 THUỘC TÍNH CHÍNH:
1: SUCCESS : THÔNG BÁO THÀNH CÔNG HOẶC THẤT BẠI
2: MESSAGE : THÔNG BÁO MÔ TẢ KẾT QUẢ TRẢ VỀ
3: DATA    : DỮ LIỆU CHÍNH TRẢ VỀ
4: ERRORS  : CHI TIẾT BUG
5: META    : DỮ LIỆU ĐÍNH KÈM THÊM (PHÂN TRANG) 
"""