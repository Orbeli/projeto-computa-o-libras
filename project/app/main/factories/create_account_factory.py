from app.domain.usecases import Usecase
from app.services.usecases.account import CreateAccount

def create_account_factory() -> Usecase:
    return CreateAccount()