from fastapi import FastAPI
from routers.product_router import router as product_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI đang chạy"}


app.include_router(product_router)