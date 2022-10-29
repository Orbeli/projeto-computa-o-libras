from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

from app.domain.models import User

@dataclass
class SaveUserParams:
    name: str
    email: str
    password: str


class UserRepositoryContract(ABC):
    @abstractmethod
    def get_user_by_email(
        self,
        email: str
    ) -> User:
        raise NotImplementedError()

    def create_user(
        self,
        params: SaveUserParams
    ) -> str:
        raise NotImplementedError()
