from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str = None


    class Config:
        orm_mode = True
