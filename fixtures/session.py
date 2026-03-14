import requests
from pytest import fixture


@fixture
def user_session():
    """Фикстура для создания сессии"""
    session = requests.Session()

    yield session

    session.close()