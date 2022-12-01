from app.domain.usecases import CreateLesson as CreateLessonContract
from app.domain.usecases import CreateLessonParams
from app.services.contracts import LessonRepositoryContract, SaveLessonParams
from app.services.helpers.http import HttpResponse, HttpStatus


class CreateLesson(CreateLessonContract):
    def __init__(
        self,
        lesson_repository: LessonRepositoryContract
    ) -> None:
        self.lesson_repository = lesson_repository

    def execute(self, params: CreateLessonParams) -> HttpResponse:
        lesson_id = self.lesson_repository.create_lesson(
            SaveLessonParams(
                name=params.name,
                duration=params.duration,
                module=params.module,
            )
        )

        return HttpStatus.created_201({
            'lesson': lesson_id
        })
