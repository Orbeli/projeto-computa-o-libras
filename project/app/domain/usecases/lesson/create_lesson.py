from abc import abstractmethod

from pydantic import BaseModel

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class CreateLessonParams(BaseModel):
    name: str
    duration: str
    module: int


class CreateLessonResponse(CreateLessonParams):
    pass


class CreateLesson(Usecase):
    @abstractmethod
    def execute(self, params: CreateLessonParams) -> HttpResponse:
        raise NotImplementedError()
