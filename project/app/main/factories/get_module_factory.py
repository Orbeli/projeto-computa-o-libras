from app.domain.usecases import Usecase
from app.services.usecases.module import GetModule
from app.infra.database.repositories import ModuleRepository
from fastapi_sqlalchemy import db


def get_module_factory() -> Usecase:

    return GetModule(
        module_repository=ModuleRepository(db)
    )
