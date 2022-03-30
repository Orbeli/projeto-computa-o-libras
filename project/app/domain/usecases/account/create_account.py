from abc import abstractmethod
from typing import Optional

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class CreateAccountParams(BaseModel):
    person_name: str
    person_mail: str
    person_age: Optional[str]


class CreateAccountResponse(CreateAccountParams):
    pass


class CreateAccount(Usecase):
    @abstractmethod
    def execute(self, create_account: CreateAccountParams) -> HttpResponse:
        raise NotImplementedError()
