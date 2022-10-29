from typing import Optional

from app.domain.models import User
from app.domain.usecases import CreateAccount as CreateAccountContract
from app.domain.usecases import CreateAccountParams
from app.services.contracts import UserRepositoryContract, SaveUserParams
from app.services.helpers.http import HttpResponse, HttpStatus
from app.main.config.authorization import get_hashed_password


class CreateAccount(CreateAccountContract):
    def __init__(
        self,
        user_repository: UserRepositoryContract
    ) -> None:
        self.user_repository = user_repository

    def execute(self, params: CreateAccountParams) -> HttpResponse:
        user = self.user_repository.get_user_by_email(params.email)
        if user is not None:
                return HttpStatus.bad_request_400(
                    "User with this email already exist"
                )

        user_id = self.user_repository.create_user(
            SaveUserParams(
                name=params.name,
                email=params.email,
                password=get_hashed_password(params.password)
            )
        )

        return HttpStatus.created_201({
            'account': user_id
        })
