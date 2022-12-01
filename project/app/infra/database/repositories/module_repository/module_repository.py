
from app.services.contracts import ModuleRepositoryContract, SaveModuleParams
from app.domain.models import Module


class ModuleRepository(ModuleRepositoryContract):
    def __init__(
        self,
        db_session
    ):
        self._db = db_session

    def get_module_by_id(self, id: int) -> Module:
        with self._db():
            try:
                return self._db.session.query(Module).filter(Module.id == id).first()
            except Exception as error:
                print("Erro ao recuperar modulo")

    def delete_module_by_id(self, id: int) -> None:
        with self._db():
            try:
                self._db.session.query(Module).filter(Module.id == id).delete()
                self._db.session.commit()
            except Exception as error:
                print("Erro ao recuperar modulo")

    def create_module(self, params: SaveModuleParams) -> str:
        with self._db():
            db_module = Module(
                name=params.name,
                subject=params.subject,
                duration=params.duration
            )
            self._db.session.add(db_module)
            self._db.session.commit()
            self._db.session.refresh(db_module)
        return db_module.id
