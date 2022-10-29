from http import HTTPStatus
from fastapi import Response, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_sqlalchemy import db

from app.main.main import app
from app.main.adapters import fast_api_adapter
from app.main.factories import create_account_factory, login_factory
from app.main.routes.helpers import (HandledError, InternalServerError,
                                     Unauthorized)
from app.main.routes.middlewares.auth import basic_authorization, jwt_authorization
from app.main.config.authorization import verify_password, create_access_token, create_refresh_token

from app.domain.models.models import User
from app.domain.usecases import CreateAccountParams, CreateAccountResponse, LoginResponse


@app.get("/teste_no_auth")
async def pong():
    return {"authorization": "Nenhuma :/"}


@app.get("/teste_basic")
async def get_me(authorization: bool = Depends(basic_authorization)):
    return {"authorization": authorization}


@app.get("/teste_jwt")
async def get_me(authorization: User = Depends(jwt_authorization)):
    return {"authorization": authorization}


@app.post(
    '/account/create',
    responses={
        HTTPStatus.CREATED.value: {'model': CreateAccountResponse},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.BAD_REQUEST.value: {
            'model': HandledError, 'description': 'User with this email already exist'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        }
    },
    status_code=HTTPStatus.CREATED,
    tags=['Account']
)
def create_account(body: CreateAccountParams, response: Response, authorization: bool = Depends(basic_authorization)):
    request = {'body': body, 'headers': None, 'query': None}
    result = fast_api_adapter(request, create_account_factory())
    response.status_code = result.status_code
    return result.body


@app.post(
    '/login',
    responses={
        HTTPStatus.OK.value: {'model': LoginResponse},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.BAD_REQUEST.value: {
            'model': HandledError, 'description': 'Incorrect email or password'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        },
    },
    summary="Create access and refresh tokens for user"
)
def login(response: Response, body: OAuth2PasswordRequestForm = Depends(), authorization: bool = Depends(basic_authorization)):
    request = {'body': body, 'headers': None, 'query': None}
    result = fast_api_adapter(request, login_factory())
    response.status_code = result.status_code
    return result.body
