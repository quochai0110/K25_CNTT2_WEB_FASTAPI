from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_student():
    return {
        "message":"lấy danh sách sinh viên CNTT2"
    }

""" 
    KIỂM TRA KẾT NỐI VỚI DATABASE 
    ORM: Object relational mapping
    object: đối tượng/ class trong python
    relational : liên kết
    mapping: ánh xạ 
    ORM bản chất biến các bảng trong MYSQL thành các đối tượng (class) trong python
    tạo bảng trong mysql : 
    CREATE TABLE product(
        id INT AUTO_INCREAMENT,
        name VARCHAR(255),
        price decimal (12,2)
    )
    
    class Product(Base):
        INT(Integer)
        name(String)
        price(Float)
    
    ORM còn giúp truy vấn dữ liệu giữa FASTAPI và cơ sở dữ liệu MYSQL
    mysql: SELECT * FROM product
    ORM  : db.query(product).all()
"""