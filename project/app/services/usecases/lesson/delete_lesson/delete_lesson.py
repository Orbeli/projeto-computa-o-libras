from app.domain.usecases import DeleteLesson as DeleteLessonContract
from app.domain.usecases import DeleteLessonParams
from app.services.contracts import LessonRepositoryContract
from app.services.helpers.http import HttpResponse, HttpStatus


class DeleteLesson(DeleteLessonContract):
    def __init__(
        self,
        lesson_repository: LessonRepositoryContract
    ) -> None:
        self.lesson_repository = lesson_repository

    def execute(self, params: DeleteLessonParams) -> HttpResponse:
        lesson = self.lesson_repository.get_lesson_by_id(params.id)
        if not lesson:
            return HttpStatus.not_found_404(
                f"Lesson [{params.id}] does not exist"
            )

        self.lesson_repository.delete_lesson_by_id(
            id=lesson.id
        )

        return HttpStatus.no_content_204()
