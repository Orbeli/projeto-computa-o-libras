from app.domain.usecases import Usecase
from app.services.usecases.lesson import CreateLesson
from app.infra.database.repositories import LessonRepository
from fastapi_sqlalchemy import db


def create_lesson_factory() -> Usecase:

    return CreateLesson(
        lesson_repository=LessonRepository(db)
    )
