from app.domain.usecases import Usecase
from app.services.usecases.account import CreateAccount
from app.infra.database.repositories import UserRepository
from fastapi_sqlalchemy import db


def create_account_factory() -> Usecase:

    return CreateAccount(
        user_repository=UserRepository(db)
    )
