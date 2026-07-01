from fastapi import FastAPI
from pydantic import BaseModel

"""
CRUD:
C: CREATE
R: READ
U: UPDATE
D: DELETE

"""

""" QUẢN LÝ SẢN PHẨM  """
# TẠO DỮ LIỆU DANH SÁCH SẢN PHẨM BAN ĐẦU.
products = [
    {"id": 1, "product_name": "iphone 14", "price": 15000000, "stock": 15},
    {"id": 2, "product_name": "iphone 15", "price": 19000000, "stock": 3},
    {"id": 3, "product_name": "iphone 16", "price": 25000000, "stock": 8},
]
app = FastAPI()


#  Viết API hiển thị danh sách tất cả sản phẩm
@app.get("/products")
def get_products():
    return {"message": "lấy danh sách tất cả sản phẩm", "data": products}


# Viết API lấy chi tiết 1 sản phẩm
@app.get("/products/{id}")
def get_product_display(id: int):
    for product in products:
        if product["id"] == id:
            return {"message": "hiển tị thông tin chi tiết sản phẩm", "data": product}
    return {"message": "sản phẩm không tồn tại", "data": ""}


class Product(BaseModel):
    id: int
    product_name: str
    price: int
    stock: int
# Viết API thêm sản phẩm
@app.post("/products")
def add_product(product: Product):
    new_product = {
        "id": products[-1]["id"] + 1,
        "product_name": product.product_name,
        "price": product.price,
        "stock": product.stock,
    }
    print("sản phẩm vừa mới thêm", new_product)
    products.append(new_product)
    return {"message": "thêm sản phẩm thành công!", "data": products}


#  Viết API xóa sản phẩm


@app.delete("/products/{product_id}")
def delete_product(product_id):
    print("id sản phẩm cần xóa", product_id)
    for index, product in enumerate(products):
        if int(product_id) == product["id"]:
            result = products.pop(index)
            return {"message": "xóa sản phẩm thành công", "data": result}
    return {"message": "xóa sản phẩm thất bại", "data": ""}
# Viết API cập nhật sản phẩm
# 2 method PUT||PATCH
@app.put("/products/{product_id}")
def update_product(product_id, product:Product):
    print("id sản phẩm cần cập nhật",product_id)
    print("thông tin giá trị cần cập nhật", product)
    for i in products:
        if i["id"] == product_id:
            i["product_name"] = product.product_name
            i["price"] = product.price
            i["stock"] = product.stock
            return {
                "message":"cập nhật thành công ",
                "data":product
            }
    return  {
        "message":"cập nhật thất bại"
    }