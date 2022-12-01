from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.models import Lesson

@dataclass
class SaveLessonParams:
    name: str
    duration: str
    module: int


class LessonRepositoryContract(ABC):
    @abstractmethod
    def get_lesson_by_id(
        self,
        id: int
    ) -> Lesson:
        raise NotImplementedError()

    @abstractmethod
    def delete_lesson_by_id(
        self,
        id: int
    ) -> None:
        raise NotImplementedError()

    def create_lesson(
        self,
        params: SaveLessonParams
    ) -> str:
        raise NotImplementedError()
