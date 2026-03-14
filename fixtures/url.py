import pytest
from pytest import fixture







#--------------------Base URL--------------------
@fixture
def Base_url(env):
    '''URL тестового стенда'''
    return env('BASE_URL')



#--------------------Authorization URL--------------------
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

