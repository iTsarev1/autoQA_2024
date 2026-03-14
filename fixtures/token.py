import pytest
from pytest import fixture
import requests as req
    

@fixture
def auth(env, Base_url, kk_url, keykloak_url, url_get_organization, user_session):
    """Авторизация через Bearer token"""
    payload = {
        "user_id": env("USER_ID"),
        "login": env("LOGIN"),
        "password": env("PASSWORD")
    }

    try:
        # Получение Bearer токена
        bearer_token = _get_token(payload, kk_url, keykloak_url)
        
        # Обновление заголовков с Bearer токеном
        _update_session_headers(user_session, {"Authorization": f"Bearer {bearer_token}"})

        # Получение ID организации
        organization_id = get_organization_id(user_session, Base_url, url_get_organization)
        
        # Обновление заголовков с ID организации
        _update_session_headers(user_session, {"X-Auth-Org": f"{organization_id}"})

        return user_session
    except Exception as e:
        raise ValueError(f"Ошибка при авторизации: {e}")



def _get_token(payload, kk_url, keykloak_url):
    """Получение авторизационного токена"""
    return req.post(f'{kk_url}{keykloak_url}', data=payload).json()["access_token"]


def _update_session_headers(user_session, **kwargs):
    """Добавление заголовков в headers"""
    user_session.headers.update(kwargs)


def get_organization_id(user_session, Base_url, url_get_organization) -> str:
    """Получение id организации"""
    return user_session.get(f"{Base_url}{url_get_organization}").json()[0]["organization"]["id"]



  