from abc import abstractmethod

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class CreateModuleParams(BaseModel):
    name: str
    subject: str
    duration: str


class CreateModuleResponse(CreateModuleParams):
    pass


class CreateModule(Usecase):
    @abstractmethod
    def execute(self, params: CreateModuleParams) -> HttpResponse:
        raise NotImplementedError()
