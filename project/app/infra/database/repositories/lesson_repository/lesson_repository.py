
from app.services.contracts import LessonRepositoryContract, SaveLessonParams
from app.domain.models import Lesson


class LessonRepository(LessonRepositoryContract):
    def __init__(
        self,
        db_session
    ):
        self._db = db_session

    def get_lesson_by_id(self, id: int) -> Lesson:
        with self._db():
            try:
                return self._db.session.query(Lesson).filter(Lesson.id == id).first()
            except Exception as error:
                print("Erro ao recuperar a atividade/lição")

    def delete_lesson_by_id(self, id: int) -> None:
        with self._db():
            try:
                self._db.session.query(Lesson).filter(Lesson.id == id).delete()
                self._db.session.commit()
            except Exception as error:
                print("Erro ao remover a atividade/lição")

    def create_lesson(self, params: SaveLessonParams) -> str:
        with self._db():
            db_lesson = Lesson(
                name=params.name,
                duration=params.duration,
                module_id=params.module,
            )
            self._db.session.add(db_lesson)
            self._db.session.commit()
            self._db.session.refresh(db_lesson)
        return db_lesson.id
