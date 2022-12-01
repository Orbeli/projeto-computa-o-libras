from app.domain.usecases import Usecase
from app.services.usecases.lesson import GetLesson
from app.infra.database.repositories import LessonRepository
from fastapi_sqlalchemy import db


def get_lesson_factory() -> Usecase:

    return GetLesson(
        lesson_repository=LessonRepository(db)
    )
