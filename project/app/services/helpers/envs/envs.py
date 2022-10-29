from os import getenv


def get_database_username() -> str:
    return getenv('DATABASE_USERNAME', '')


def get_database_password() -> str:
    return getenv('DATABASE_PASSWORD', '')


def get_database_port() -> str:
    return getenv('DATABASE_PORT', '5432')


def get_database_name() -> str:
    return getenv('DATABASE_NAME', '')


def get_service_username() -> str:
    return getenv('USERNAME', '')


def get_service_password() -> str:
    return getenv('PASSWORD', '')
