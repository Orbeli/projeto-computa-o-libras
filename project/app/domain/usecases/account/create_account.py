from abc import abstractmethod
from typing import Optional

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class CreateAccountParams(BaseModel):
    name: str
    email: str
    password: str


class CreateAccountResponse(CreateAccountParams):
    pass


class CreateAccount(Usecase):
    @abstractmethod
    def execute(self, params: CreateAccountParams) -> HttpResponse:
        raise NotImplementedError()
