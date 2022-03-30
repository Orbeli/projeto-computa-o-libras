from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: Optional[str] = None


    class Config:
        orm_mode = True
