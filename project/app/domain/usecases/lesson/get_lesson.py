from abc import abstractmethod

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class GetLessonParams(BaseModel):
    id: int


class GetLessonResponse(GetLessonParams):
    pass


class GetLesson(Usecase):
    @abstractmethod
    def execute(self, params: GetLessonParams) -> HttpResponse:
        raise NotImplementedError()
