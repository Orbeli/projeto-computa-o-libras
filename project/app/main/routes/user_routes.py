from http import HTTPStatus
from fastapi import Response
from app.main.main import app
from app.domain.usecases import CreateAccountParams, CreateAccountResponse
from app.main.factories import create_account_factory
from app.main.adapters import fast_api_adapter
from app.main.routes.helpers import (HandledError, InternalServerError,
                                     Unauthorized)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.post(
    '/account/create',
    responses={
        HTTPStatus.CREATED.value: {'model': CreateAccountResponse},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.BAD_REQUEST.value: {
            'model': HandledError, 'description': 'Company or tenant not found'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        },
        HTTPStatus.NOT_ACCEPTABLE.value: {
            'model': HandledError, 'description': 'Account with the information provided already open'
        },
    },
    status_code=HTTPStatus.CREATED,
    tags=['Account']
)
def create_account(body: CreateAccountParams, response: Response):
    request = {'body': body, 'headers': None, 'query': None}
    result = fast_api_adapter(request, create_account_factory())
    response.status_code = result.status_code
    return result.body