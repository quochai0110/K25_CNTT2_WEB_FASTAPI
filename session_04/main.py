"""
1. path parameter :
    đường dẫn có tham số
    
2. query parameter :
    truy vấn có tham số 
3. request body
4. type hints
"""

from fastapi import FastAPI
from pydantic import BaseModel

# lấy dữ liệu trong db
students = [
    {"id": 1, "name": "Phan Đức Anh", "age": 20},
    {"id": 2, "name": "Lê Minh Đức", "age": 21},
    {"id": 3, "name": "Vũ Hồng Vân", "age": 20},
]
app = FastAPI()

class Student(BaseModel):
    name:str
    age: int
    id : int
    
@app.get("/students")
def get_students():
    return {"message": "lấy danh sách sinh viên thành công!",
            "data": students}
# lấy chi tiết thông tin của 1 bạn sinh viên

@app.get("/students/{student_id}")
def get_student_detail(student_id):
    #  trả về thông tin chi tiết của sinh viên
    print("giá trị id nhận về", student_id)
    for student in students:
        if str(student["id"]) == student_id:
            return {
                "message": "lấy chi tiết sinh viên thành công?",
                "data": student
            }
    return{
            "message":"không tìm thấy sinh viên",
            "data":[]
        }

# query parameter : tìm kiếm, lọc, phân trang
# lọc các sinh viên có tuổi 21

@app.get("/search")
# def search_student_by_age(age):
#     print("giá trị tuổi nhận vào", age)
#     result = []
#     for student in students:
#         if str(student["age"]) == age:
#             result.append(student) 
#     return{
#         "số lượng sinh viên tìm lấy":len(result),
#         "data": result
#     }
def search_student_by_name(keyword,age):
    # print("keyword: ", keyword)
    # print("age:",age)
    result = []
    for student in students:
        if keyword.lower() in student["name"].lower() and int(age) == student["age"]:
            result.append(student)
    return {
        "data":result
    }
#  query nhiều điền kiện thì làm thế nào? &

# request body
# thêm sinh viên vào lớp 
@app.post("/students")
def create_student(student:Student):
    new_student = {
        "id":student.id,
        "name":student.name,
        "age":student.age
    }
    print("thông tin sinh viên cần thêm", new_student)
    # print("đã gọi phương thức để thêm sinh viên",student)
    return{
        "message":"thêm sinh viên thành công!"
    }


    