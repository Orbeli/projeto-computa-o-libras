from typing import List

from app.services.contracts import UserRepositoryContract, SaveUserParams
from app.domain.models import User


class UserRepository(UserRepositoryContract):
    def __init__(
        self,
        db_session
    ):
        self._db = db_session

    def get_user_by_email(self, email: str) -> User:
        with self._db():
            try:
                return self._db.session.query(User).filter(User.email == email).first()
            except Exception as error:
                print("Erro ao recuperar user")

    def create_user(self, params: SaveUserParams) -> str:
        with self._db():
            db_user = User(
                name=params.name,
                email=params.email,
                password=params.password
            )
            self._db.session.add(db_user)
            self._db.session.commit()
            self._db.session.refresh(db_user)
        return db_user.id
