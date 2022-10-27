from os import getenv
from typing import List


def get_database_url() -> str:
    return getenv('DATABASE_URL', '')


def get_service_username() -> str:
    return getenv('USERNAME', '')


def get_service_password() -> str:
    return getenv('PASSWORD', '')
