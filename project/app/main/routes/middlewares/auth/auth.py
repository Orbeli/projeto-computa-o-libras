from base64 import b64decode
from http import HTTPStatus
from secrets import compare_digest
from typing import Dict

from fastapi import Request
from starlette.responses import JSONResponse

from app.main.main import app
from app.services.helpers.envs import get_service_password, get_service_username


def _is_authenticate_route(path: str) -> bool:
    not_authenticated_routes = ['/openapi.json', '/docs']
    return path not in not_authenticated_routes


def _is_valid_credentials(headers: Dict) -> bool:
    try:
        authorization_type, authorization_credentials = str(
            headers.get('Authorization')).split(' ')

        if authorization_type.lower() != 'basic':
            return False

        client_id, client_secret = b64decode(
            authorization_credentials).decode().split(':')

        valid_client_id = compare_digest(
            get_service_username(), client_id)
        valid_client_secret = compare_digest(
            get_service_password(), client_secret)

        return valid_client_id and valid_client_secret
    except Exception:
        return False


def _mount_unauthorized_payload() -> JSONResponse:
    return JSONResponse(content={
        'message': 'Unauthorized'
    }, status_code=HTTPStatus.UNAUTHORIZED)


@app.middleware('http')
async def auth(request: Request, call_next):
    headers = request.headers

    if not _is_authenticate_route(request.get('path')):
        response = await call_next(request)
        return response

    if not _is_valid_credentials(headers):
        return _mount_unauthorized_payload()

    response = await call_next(request)
    return response
