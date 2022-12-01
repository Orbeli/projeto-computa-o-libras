from http import HTTPStatus
from fastapi import Response, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.main.main import app
from app.main.adapters import fast_api_adapter
from app.main.factories import (
    create_account_factory,
    login_factory,
    create_module_factory,
    get_module_factory,
    create_lesson_factory,
    delete_lesson_factory,
    get_lesson_factory,
    delete_module_factory
)

from app.main.routes.helpers import (HandledError, InternalServerError,
                                     Unauthorized)
from app.main.routes.middlewares.auth import basic_authorization, jwt_authorization

from app.domain.models.models import User
from app.domain.usecases import (
    CreateAccountParams,
    CreateAccountResponse,
    LoginResponse,
    CreateModuleParams,
    CreateModuleResponse,
    GetModuleParams,
    GetModuleResponse,
    CreateLessonParams,
    DeleteLessonParams,
    GetLessonParams,
    GetLessonResponse,
    DeleteModuleParams,
    DeleteModuleResponse
)


@app.get(
    "/teste_no_auth",
    tags=['Authorization']
)
async def pong():
    return {"authorization": "Nenhuma :/"}


@app.get(
    "/teste_basic",
    tags=['Authorization']
)
async def get_me(authorization: bool = Depends(basic_authorization)):
    return {"authorization": authorization}


@app.get(
    "/teste_jwt",
    tags=['Authorization']
)
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
    summary="Create access and refresh tokens for user",
    tags=['Authorization']
)
def login(response: Response, body: OAuth2PasswordRequestForm = Depends(), authorization: bool = Depends(basic_authorization)):
    request = {'body': body, 'headers': None, 'query': None}
    result = fast_api_adapter(request, login_factory())
    response.status_code = result.status_code
    return result.body


@app.post(
    '/module/create',
    responses={
        HTTPStatus.CREATED.value: {'model': CreateModuleResponse},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        }
    },
    status_code=HTTPStatus.CREATED,
    tags=['Module']
)
def create_module(body: CreateModuleParams, response: Response, authorization: User = Depends(jwt_authorization)):
    request = {'body': body, 'headers': None, 'query': None}
    result = fast_api_adapter(request, create_module_factory())
    response.status_code = result.status_code
    return result.body


@app.get(
    '/module/get/{module_id}',
    responses={
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Module not found'
        },
        HTTPStatus.OK.value: {
            'description': 'Module found',
            'model': GetModuleResponse
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        }
    },
    status_code=HTTPStatus.OK,
    tags=['Module']
)
def get_module(module_id: int, response: Response, authorization: User = Depends(jwt_authorization)):
    request = {'body': GetModuleParams(id=module_id), 'headers': None, 'query': None}
    result = fast_api_adapter(request, get_module_factory())
    response.status_code = result.status_code
    return result.body


@app.post(
    '/lesson/create',
    responses={
        HTTPStatus.CREATED.value: {'model': CreateModuleResponse},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        }
    },
    status_code=HTTPStatus.CREATED,
    tags=['Lesson']
)
def create_lesson(body: CreateLessonParams, response: Response, authorization: User = Depends(jwt_authorization)):
    request = {'body': body, 'headers': None, 'query': None}
    result = fast_api_adapter(request, create_lesson_factory())
    response.status_code = result.status_code
    return result.body


@app.delete(
    '/lesson/delete/{lesson_id}',
    responses={
        HTTPStatus.NO_CONTENT.value: {'description': 'Lesson deleted'},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        }
    },
    status_code=HTTPStatus.NO_CONTENT,
    tags=['Lesson']
)
def delete_lesson(lesson_id: int, response: Response, authorization: User = Depends(jwt_authorization)):
    request = {'body': DeleteLessonParams(id=lesson_id), 'headers': None, 'query': None}
    result = fast_api_adapter(request, delete_lesson_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@app.get(
    '/lesson/get/{lesson_id}',
    responses={
        HTTPStatus.NO_CONTENT.value: {'description': 'Lesson deleted'},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        }
    },
    status_code=HTTPStatus.NO_CONTENT,
    tags=['Lesson']
)
def get_lesson(lesson_id: int, response: Response, authorization: User = Depends(jwt_authorization)):
    request = {'body': GetLessonParams(id=lesson_id), 'headers': None, 'query': None}
    result = fast_api_adapter(request, get_lesson_factory())
    response.status_code = result.status_code
    return result.body


@app.delete(
    '/module/delete/{module_id}',
    responses={
        HTTPStatus.NO_CONTENT.value: {'description': 'Module deleted'},
        HTTPStatus.UNAUTHORIZED.value: {
            'model': Unauthorized, 'description': 'Invalid credentials'
        },
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        }
    },
    status_code=HTTPStatus.NO_CONTENT,
    tags=['Module']
)
def delete_module(module_id: int, response: Response, authorization: User = Depends(jwt_authorization)):
    request = {'body': DeleteModuleParams(id=module_id), 'headers': None, 'query': None}
    result = fast_api_adapter(request, delete_module_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response
