from abc import abstractmethod

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class LoginParams(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class Login(Usecase):
    @abstractmethod
    def execute(self, params: LoginParams) -> HttpResponse:
        raise NotImplementedError()
