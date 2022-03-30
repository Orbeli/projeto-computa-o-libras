import os

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from app.domain.models.models import User as ModelUser
from app.domain.models.user import User as SchemaUser
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI(
    title="LIBRAS",
    version="1.0.0"
)

app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:postgres@db/test_db")

@app.post("/user", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        name=user.name, email=user.email, age=user.age
    )
    db.session.add(db_user)
    db.session.commit()

    return db_user



from app.main.routes import *