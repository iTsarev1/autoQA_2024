from pytest import mark
import requests as req



@mark.dev
def test_run(get):
    url = 'https://ru.wikipedia.org/wiki/'
    print (get(url=url))
    response = get(url=url)
    print (response.headers['date'])
    # print(response. text)
    print('-'* 20)


@mark.dev1
def test_get_request():
    response = req.get('https://ru.wikipedia.org/wiki/')
    print(response.status_code) #Статус-код ответа
    print(response.text) #Текст ответа
    print('-'* 20)


@mark.dev2
def test_post_request():
    data = {'key': 'value'}
    response = req.post('https://ru.wikipedia.org/wiki/', data = data)
    print(response.status_code) #Статус-код ответа
    print(response.json()) #Оввет в формате Json
    print('-'* 20)


@mark.dev3
def test_auf(env):
    url = 'https://demo-passport.etpgpb.ru/api/v2/hub/'
    headers = {"Authorization": f"Bearer {env('token_pk')}"}
    response = req.post(url, headers=headers)
    print (response. status_code)
    print('-' * 10)
    print (response.headers)
    print('-'* 10)
    assert type(response.json()['requestId']) == str
    print(response. json()['errors'])
    print('-'* 20)



@mark.dev4
def test_auf_1(env):
    '''test'''
    url = 'https://demo-passport.etpgpb.ru/api/v2/hub/'
    headers = {"Authorization": f"Bearer{env('token_pk')}"}
    response = req.post(url, headers=headers)
    try:
        assert response.ok
        assert response.headers['Content-Type'] == 'application/json'
        assert type(response.json()['requestId']) == str
    except:
        print(response.status_code)
        print(response.headers)
        print('-'* 20)



@mark.devs
def test_sunday():
        response = req.get(url = 'https://demo-passport.etpgpb.ru/api/v2/hub/')
        print(response.status_code)
        print(response.json)
        print('-'* 20)






@mark.devs
def test_auth(env):
     url = 'https://demo-passport.etpgpb.ru/api/v2/hub/'
     headers = {'Authorization': f'Bearer {env('token_pk')}'}
     response = req.post(url, headers=headers)

     try:
          assert response.ok
          assert response.headers['Content-Type'] == 'application/json'
          assert type(response.json()['request_id']) == str
     except:
          print(response.status_code)
          print(response.headers)
          print('-'* 20)



@mark.dev1
def test_auth(env):
     '''test'''
     url = 'https://demo-passport.etpgpb.ru/api/v2/hub/'
     headers = {'Authorization': f'Bearer {env('token_pl')}'}
     response = req.post(url, headers = headers)
     try:
          assert response.status_code == 201
          assert response.headers['Content-Type'] == 'application/json'
          assert type(response.json()['requestId']) == str
     except:
          print(response.status_code)
          print(response.headers)
          print('-'*20)

Hello





