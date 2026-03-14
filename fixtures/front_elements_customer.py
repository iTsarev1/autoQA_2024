from lib2to3.pgen2 import driver
from pytest import fixture
from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta


#--------------------Страница авторизации--------------------
@fixture
def come_in(driver):
    return driver.locator('.header__button:has-text("Войти")')


@fixture
def login(driver):
    return driver.locator('#username')


@fixture
def password(driver):
    return driver.locator('#password')


@fixture
def random(driver):
    return driver.locator('#toggle_password_container')


@fixture
def button_customer_ok(driver):
    return driver.locator('#kc-login')


#--------------------Страница выбора роли--------------------
#@fixture
#def button_organization(driver):
#    return driver.locator('//input[@class="text-body--3" and @placeholder="Организация"]')


#@fixture
#def organization_choice(driver):
#    return driver.locator('//div[@class= "text-secondary--2 c-grey-4" and text()="ИНН 5001048893; КПП 500101001"]')


@fixture
def button_role_customer(driver):
    return driver.locator('//span[text()="Заказчик"]')


@fixture
def button_role_ok(driver):
    return driver.locator('//span[text()=" Выбрать "]')


#@fixture
#def button_back(driver):
#    return driver.locator('span[data-v-28e0e559].text-body--2:has-text("Назад")')


#--------------------Витрина -> Мои запросы--------------------
@fixture
def vitrina(driver):
    return driver.locator('//span[@data-v-884830b3 and text()="Витрина"]')


@fixture
def my_requests(driver):
    return driver.locator('//span[@data-v-884830b3 and text()="Мои запросы"]')


#--------------------Страница создания ЦЗ--------------------
@fixture
def button_create_qr(driver):
    return driver.locator('//button[@class="ui-button"]')


@fixture
def name_qr(driver):
    return driver.locator('//input[@class="text-body--3"][@placeholder="Введите название запроса"]')


@fixture
def adress_delivery(driver):
    return driver.locator('//input[@class="text-body--3"][@id="address"]')


@fixture
def adress_delivery_click(driver):
    return driver.locator('//span[@data-v-6b58c4fd and text()= "410017, Саратовская обл, г Саратов, Октябрьский р-н, Весенний проезд, д 8"]')


@fixture
def date_From(driver):
    return driver.locator('//input[@class="text-body--3"][@id="dateFrom"]')


@fixture
def input_terms(driver):
    return driver.locator('//textarea[@class="fancy_scrollbar text-body--1" and @placeholder="Введите условие оплаты"]')


@fixture
def analogues_Accept(driver):
    return driver.locator('//span[@class="text-body--3 ml-[12px]" and text()="Принимать аналоги"]')


@fixture
def response_Date(driver):
    return driver.locator('//input[@class="text-body--3" and @id="responseDate"]')


# Рассчитать время через 4 минуты от текущего
@fixture
def response_Date_input():
    future_time = datetime.now() + timedelta(minutes=4)
    formatted_time = future_time.strftime('%d.%m.%Y %H:%M')
    return formatted_time


@fixture
def button_save(driver):
    return driver.locator('//span[@class="text-body--2" and text()=" Сохранить "]')


#--------------------Страница добавления позиций--------------------
@fixture
def button_items(driver):
    return driver.locator('//div[@class="relative" and text()="Позиции"]')


@fixture
def button_add_item(driver):
    return driver.locator('//span[@class="text-body--2 mr-[10px]" and text()=" Добавить позицию "]')


@fixture
def button_my_price_list(driver):
    return driver.locator('//div[@class="relative flex items-center w-full" and normalize-space()="Из своего прайс-листа"]')


@fixture
def search_items(driver):
    return driver.locator('//input[@class="text-body--3" and @placeholder="Наименование позиции"]')


@fixture
def button_search(driver):
    return driver.locator('//span[@class="text-body--2" and text()= "Найти"]')


@fixture
def checkbox_1(driver):
    return driver.locator('//div[contains(text(),"Автотест 1")]/ancestor::tr//button[@class="checkbox"]')


@fixture
def checkbox_2(driver):
    return driver.locator('//div[contains(text(),"Автотест 2")]/ancestor::tr//button[@class="checkbox"]')


@fixture
def button_next(driver):
    return driver.locator('//span[@class="text-body--2" and text()=" Далее "]')


@fixture
def input_elements(driver):
    #Находим все элементы по заданному XPath
    input_quantity = driver.locator('//input[@class="text-body--3" and @placeholder="Введите число"]').all()
    #Перебираем каждый найденный элемент
    for element in input_quantity:
        element.click()
        element.fill("5.123")


@fixture
def button_add(driver):
    return driver.locator('//span[@class="text-body--2" and text()=" Добавить "]')


@fixture
def button_mass_actual(driver):
    return driver.locator('//span[@class="text-body--2 mr-[10px]" and text()=" Массовое редактирование "]')


@fixture
def actual_all(driver):
    return driver.locator('//div[@class="relative flex items-center w-full" and normalize-space()="Редактировать все"]')


@fixture
def input_quantity_1(driver):
    return driver.locator('//input[@class="text-body--3" and @placeholder="Введите число"]')


@fixture
def button_save_1(driver):
    return driver.locator('//span[@class="text-body--2" and text()=" Сохранить "]')


@fixture
def input_quantity_2(driver):
    return driver.locator('//input[@class="text-body--3" and @placeholder="Введите число"]')


@fixture
def button_save_2(driver):
    return driver.locator('//span[@class="text-body--2" and text()=" Сохранить "]')


@fixture
def button_publish(driver):
    return driver.locator('//span[@class="text-body--2" and text()=" Опубликовать "]')
