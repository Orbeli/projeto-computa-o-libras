from abc import abstractmethod

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class DeleteModuleParams(BaseModel):
    id: int


class DeleteModuleResponse(DeleteModuleParams):
    pass


class DeleteModule(Usecase):
    @abstractmethod
    def execute(self, params: DeleteModuleParams) -> HttpResponse:
        raise NotImplementedError()
