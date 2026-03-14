from logging import exception
from allure import epic, title


@epic('smoke_customer')
@title('Проверка авторизации')
def test_assert_auth(home_page_customer):
    home_page_customer
    

def test_assert_requests(create_quote_req):
    create_quote_req


