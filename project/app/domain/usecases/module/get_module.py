from abc import abstractmethod

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class GetModuleParams(BaseModel):
    id: int


class GetModuleResponse(GetModuleParams):
    pass


class GetModule(Usecase):
    @abstractmethod
    def execute(self, params: GetModuleParams) -> HttpResponse:
        raise NotImplementedError()
