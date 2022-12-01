from app.domain.usecases import Usecase
from app.services.usecases.module import DeleteModule
from app.infra.database.repositories import ModuleRepository
from fastapi_sqlalchemy import db


def delete_module_factory() -> Usecase:

    return DeleteModule(
        module_repository=ModuleRepository(db)
    )
