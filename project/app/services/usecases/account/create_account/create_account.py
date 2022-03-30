from typing import Optional, Tuple
from uuid import uuid4
from fastapi import Depends
from starlette.responses import HTMLResponse

from app.domain.models import User
from app.domain.usecases import CreateAccount as CreateAccountContract
from app.domain.usecases import CreateAccountParams
# from app.services.contracts import PstiAvailableBankAccountsContract
# from app.services.helpers.dates.format_date import get_current_timestamp
from app.services.helpers.http import HttpResponse, HttpStatus


class CreateAccount(CreateAccountContract):
    def __init__(
        self,
    ):
        pass

    def execute(self, create_account: CreateAccountParams) -> HttpResponse:

        return HttpStatus.created_201({
            'account': "pong"
        })
