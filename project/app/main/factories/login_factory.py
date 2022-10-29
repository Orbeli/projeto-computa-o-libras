from app.domain.usecases import Usecase
from app.services.usecases.login import AuthorizeUser
from app.infra.database.repositories import UserRepository
from fastapi_sqlalchemy import db


def login_factory() -> Usecase:

    return AuthorizeUser(
        user_repository=UserRepository(db)
    )
