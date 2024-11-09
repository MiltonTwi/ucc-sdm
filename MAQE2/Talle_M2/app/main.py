from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

app = FastAPI()

DATABASE_URL = "postgresql://Milton:12345678@db:5432/E11EVENN"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    return {"message": "Universidad Cooperativa de Colombia 11/08/2024"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
