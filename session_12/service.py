# VIẾT CÁC HÀM ĐI LẤY DỮ LIỆU TRONG DATABASE
from models import Product
from fastapi import HTTPException
#  HÀM LẤY TẤT CẢ SẢN PHẨM
def get_products(db):
    products = db.query(Product).all()
    return products

# HÀM LẤY CHI TIẾT SẢN PHẨM
def get_product_detail(product_id :int, db):
    product = db.query(Product).filter(Product.id == product_id).first()
    return product

# HÀM THÊM MỚI SẢN PHẨM
def add_product (product, db):
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

# HÀM XÓA SẢN PHẨM
def delete_product(product_id:int,db):
    product = db.query(Product).filter(Product.id==product_id).first()
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

# HÀM CẬP NHẬT SẢN PHẨM
def update_product(product_id, product, db):
     product = db.query(Product).filter(Product.id == product_id) .first()
     return product