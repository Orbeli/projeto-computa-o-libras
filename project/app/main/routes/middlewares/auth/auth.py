import secrets

from jose import jwt
from datetime import datetime
from pydantic import BaseModel, ValidationError

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from fastapi_sqlalchemy import db

from app.domain.models.models import User
from app.services.helpers.envs import get_service_password, get_service_username
from app.main.config.authorization import (
    ALGORITHM,
    JWT_SECRET_KEY
)


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


security = HTTPBasic()

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


def basic_authorization(credentials: HTTPBasicCredentials = Depends(security)) -> bool:

    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = get_service_username().encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = get_service_password().encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    return True


async def jwt_authorization(token: str = Depends(reuseable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    user = db.session.query(User).filter(User.email == token_data.sub).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user
