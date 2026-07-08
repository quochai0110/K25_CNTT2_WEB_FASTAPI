from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker,declarative_base, Session
app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/fastapi"
# địa chỉ của MYSQL
engine = create_engine(DATABASE_URL)
#  engine là cầu nối để kết nối với mysql
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)
# SessionLocal : là phiên làm việc với database 
Base = declarative_base()
# base : khai báo cơ sở 
class Product(Base):
    __tablename__ = "product" 
    # tên bảng 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
#  class Product : bản thiết kế giống bảng trong MYSQL
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    # tạo phiên làm việc với mysql
    
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all() #ORM
    # câu lệnh lấy tất cả các sản phẩm trong bảng product
    return {
        "message": "Lấy danh sách sản phẩm thành công",
            "data": products
        }
    # lấy chi tiết, thêm , sửa, xóa  