from email import header
from wsgiref import headers
import requests as req
from pytest import fixture


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

