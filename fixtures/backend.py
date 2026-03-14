from email import header
from wsgiref import headers
import requests as req
from pytest import fixture


#--------------------Сессия--------------------


@fixture
def user_session():
    """Фикстура для создания сессии"""
    session = req.Session()

    yield session

    session.close()


#--------------------Base URL--------------------


@fixture
def Base_url(env):
    '''URL тестового стенда'''
    return env('BASE_URL')



#--------------------URL Авторизации--------------------


@fixture
def url_auth(env):
    '''URL авторизации'''
    return env('URL_AUTH')


#--------------------Создание ЦЗ--------------------


def create_quoterequest():
    '''URL авторизации'''
    return f'{Base_url}api/v1/quote-requests'


@fixture
def kk_url(env):
    """урл keycloak для авторизации"""
    return env('KK_URL')


@fixture
def keykloak_url(env):
    """путь до получения токена"""
    return env('KEYKLOAL_URL')


@fixture
def url_get_quote_requests(env):
    """урл keycloak для авторизации"""
    return env('URL_GET_QUOTE_REQUESTS')


@fixture
def url_get_organization(env):
    """путь до метода получения данных об организации пользователя"""
    return env('URL_GET-ORGANIZATION')
    


@fixture
def mail():
    return ['/api/v1/account/ordered-tariffs', '/api/v1/account/purchasable-tariffs']



#--------------------Фикстура авторизации--------------------


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



@fixture
def headers(env, organization_id):
    return {
        f'Authorization: Bearer {env("token")}', 
        f'X-Auth-Org: {organization_id}'
    }


@fixture
def post(headers):
    def auth(*args):
        headers[*args] = headers
        return req.post
    return auth


#--------------------Схема получения Ценового запроса--------------------


@fixture
def resp_schema_get_qr():
    return {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "number": {"type": "integer"},
            "customer": {"type": "object"},
            "name": {"type": "string"},
            "delivery": {"type": "object"},
            "requirements": {"type": "object"},
            "status": {"type": "string"},
            "responseDate": {"type": "string"},
            "comment": {"type": ["string", "null"]},
            "quoteItemsCount": {"type": "integer"},
            "cost": {"type": ["number", "null"]},
            "purchaseStatusCount": {"type": "object"},
            "discountLastDateResponse": {"type": ["string", "null"]},
            "updatedAt": {"type": "string"},
            "purchaseType": {"type": "string"},
            "isExpress": {"type": "boolean"},
            "maxPriceOfContract": {"type": ["number", "null"]},
            "listMethodSignContract": {
                "type": "array",
                "items": {"type": "string"}
            }
        }
    }