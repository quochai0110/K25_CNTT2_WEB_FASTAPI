from sqlalchemy import create_engine, text
""" 
sqlalchemy là cầu nối để kết nối fastapi với mysql

"""
DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/fastapi1"
engine = create_engine(DATABASE_URL)
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Kết nối MySQL thành công")

except Exception as e:
    print("Kết nối MySQL thất bại")
    print("Lỗi:", e)