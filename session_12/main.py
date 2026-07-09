#  VIẾT API

from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models  import Product
app = FastAPI()
@app.get("/")
def home():
    return{
        "message": "api đang chạy"
    }

# TẠO CLASS THÊM SẢN PHẨM
class ProductCreate(BaseModel):
    name: str
    price: float
    
# Tạo hàm mở phiên làm việc với mysql
def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()
# VIẾT API LẤY DANH SÁCH SẢN PHẨM
@app.get("/products")
def get_products(db:Session = Depends(get_db)):
    products = db.query(Product).all()
    return {
        "message":"lấy danh sách sản phẩm thành công!",
        "data"   : products
    }
#  VIẾT API LẤY CHI TIẾT 1 SẢN PHẨM

@app.get("/products/{product_id}")
def get_product_detail(product_id:int, db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if product is None:
        raise HTTPException(
            status_code= 404,
            detail="không tìm thấy sản phẩm!"
        )
    return {
        "message":"lấy chi tiết sản phẩm thành công!",
        "data"   : product
    }
#  VIẾT API THÊM SẢN PHẨM
@app.post("/products")
def add_product(product: ProductCreate, db:Session = Depends(get_db)):
    new_product = Product(
        name  = product.name,
        price = product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {
        "message":"thêm sản phẩm thành công!",
        "data"   : new_product
    }

# VIẾT API XÓA SẢN PHẨM
@app.delete("/products/{product_id}")
def delete_product(product_id:int, db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id ).first()
    if product is None:
        raise HTTPException(
            status_code= 404,
            detail= "sản phẩm không tồn tại!"
        )
    db.delete(product)
    db.commit()
    return {
        "message":"xóa sản phẩm thành công!",
        "data"   :product
       }
# VIẾT API CẬP NHẬT

@app.put("/products/{product_id}")
def update_product(product_id:int, update_product:ProductCreate, db:Session = Depends(get_db)):
    # tìm kiếm xem có tồn tại sản phẩm hay không mới đi cập nhật
    product = db.query(Product).filter(Product.id == product_id) .first()
    if product is None:
        raise HTTPException(
            status_code= 404 ,
            detail= "không tìm thấy sản phẩm cần cập nhật!"
        )
    product.name = update_product.name 
    product.price = update_product. price 
    db.commit()
    db.refresh(product)
    return {
        "message": "cập nhật sản phẩm thành công!",
        "data"   : product
    }