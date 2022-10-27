from dotenv import load_dotenv
from os import getenv

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from app.domain.models.models import User as ModelUser
from app.domain.models.user import User as SchemaUser

load_dotenv()

app = FastAPI(
    title="LIBRAS",
    version="1.0.0"
)

app.add_middleware(DBSessionMiddleware, db_url=getenv('DATABASE_URL', ''))
@app.post("/user", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        name=user.name, email=user.email, age=user.age
    )
    db.session.add(db_user)
    db.session.commit()

    return db_user



from app.main.routes import *