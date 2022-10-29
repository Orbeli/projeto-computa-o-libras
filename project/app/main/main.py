from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

load_dotenv()

from app.services.helpers.envs import get_database_name, get_database_password, get_database_port, get_database_username


app = FastAPI(
    title="LIBRAS",
    version="1.0.0"
)

db_url = 'postgresql://{username}:{password}@db:{port}/{database}'.format(
    username=get_database_username(),
    password=get_database_password(),
    port=get_database_port(),
    database=get_database_name()
)

app.add_middleware(DBSessionMiddleware, db_url=db_url)

from app.main.routes import *