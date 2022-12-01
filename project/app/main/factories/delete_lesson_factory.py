from app.domain.usecases import Usecase
from app.services.usecases.lesson import DeleteLesson
from app.infra.database.repositories import LessonRepository
from fastapi_sqlalchemy import db


def delete_lesson_factory() -> Usecase:

    return DeleteLesson(
        lesson_repository=LessonRepository(db)
    )
