from app.domain.usecases import Usecase
from app.services.usecases.module import CreateModule
from app.infra.database.repositories import ModuleRepository
from fastapi_sqlalchemy import db


def create_module_factory() -> Usecase:

    return CreateModule(
        module_repository=ModuleRepository(db)
    )
