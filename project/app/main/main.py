import os, sys
from unicodedata import name
from dotenv import load_dotenv
from os import getenv

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from app.domain.models.models import User as ModelUser
from app.domain.models.user import User as SchemaUser

load_dotenv()

from app.services.helpers.envs import get_database_name, get_database_password, get_database_port, get_database_username

db_url = 'postgresql://{username}:{password}@db:{port}/{database}'.format(
    username=get_database_username(),
    password=get_database_password(),
    port=get_database_port(),
    database=get_database_name()
)

app = FastAPI(
    title="LIBRAS",
    version="1.0.0"
)

app.add_middleware(DBSessionMiddleware, db_url=db_url)
@app.post("/user", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        name="teste",
        email="teste",
        password="teste"
    )
    db.session.add(db_user)
    db.session.commit()

    return db_user



from app.main.routes import *