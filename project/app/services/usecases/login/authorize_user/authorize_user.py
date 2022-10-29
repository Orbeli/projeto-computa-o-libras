from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.usecases import Login as AuthorizeUserContract
from app.domain.usecases import LoginResponse
from app.services.contracts import UserRepositoryContract
from app.services.helpers.http import HttpResponse, HttpStatus
from app.main.config.authorization import verify_password, create_access_token, create_refresh_token


class AuthorizeUser(AuthorizeUserContract):
    def __init__(
        self,
        user_repository: UserRepositoryContract
    ) -> None:
        self.user_repository = user_repository

    def execute(self, params: OAuth2PasswordRequestForm = Depends()) -> HttpResponse:

        user = self.user_repository.get_user_by_email(params.username)
        if user is None:
            return HttpStatus.bad_request_400(
                "Incorrect email or password"
            )

        hashed_pass = user.password
        if not verify_password(params.password, hashed_pass):
            return HttpStatus.bad_request_400(
                "Incorrect email or password"
            )

        return HttpStatus.ok_200(
            LoginResponse(
                access_token=create_access_token(user.email),
                refresh_token=create_refresh_token(user.email)
            )
        )
