import os
from pytest import fixture
from dotenv import load_dotenv
from playwright.sync_api import Playwright





@fixture
def get():
    #Возвращаемое значение фикстуры
    return '200 OK'


# -------------------- Подключаем env --------------------




@fixture()
def env():
    """Переменная окружения"""
    return os.getenv



#driver


@fixture
def driver(playwright: Playwright, env):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=['--start-maximized']) # or "firefox" or "webkit".
    context = browser.new_context(no_viewport = True)
    page = context.new_page()
    page.goto(env('Base_url'))


    yield page


    context.close()
    browser.close()



