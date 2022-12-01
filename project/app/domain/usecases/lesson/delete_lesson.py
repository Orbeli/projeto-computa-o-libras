from abc import abstractmethod

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class DeleteLessonParams(BaseModel):
    id: int


class DeleteLessonResponse(DeleteLessonParams):
    pass


class DeleteLesson(Usecase):
    @abstractmethod
    def execute(self, params: DeleteLessonParams) -> HttpResponse:
        raise NotImplementedError()
