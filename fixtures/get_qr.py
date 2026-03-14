from pytest import fixture


@fixture
def get_quote_request(auth, Base_url, url_get_quote_requests):
    """
    :param auth: авторизация пользователя
    :param Base_url: урл стенда
    :param url_get_quote_requests: путь до метода получения списка ЦЗ
    :return: объект с ответом после выполнения запроса
    """
    def _get_quote_request(env):
        bearer_token = env('bearer_token')
        return auth.get(f"{Base_url}{url_get_quote_requests}", headers = {"Authorization": f"Bearer {env ("bearer_token")}"})
    return _get_quote_request