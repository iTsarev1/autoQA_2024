from pytest import fixture
import time
from playwright.sync_api import Playwright, expect
from datetime import datetime, timedelta


#--------------------Авторизация--------------------/1
@fixture
def auth_customer(come_in, login, password, random, button_customer_ok, env):
    come_in.click()
    login.fill(env('LOGIN_CUSTOMER'))
    password.fill(env('PASSWORD_CUSTOMER'))
    random.click()
    button_customer_ok.click()
    

#--------------------Выбор роли
@fixture
def home_page_customer(auth_customer, button_role_customer, button_role_ok):
    auth_customer
    button_role_customer.click()
    button_role_ok.click()
    #button_back.click()
    time.sleep(1)
    


#--------------------Создание Ценового запроса--------------------/2
@fixture
def create_quote_req(home_page_customer, vitrina, my_requests, button_create_qr, name_qr, adress_delivery, adress_delivery_click, date_From, input_terms, analogues_Accept, response_Date, response_Date_input, button_save, button_items, button_add_item, button_my_price_list, search_items, button_search, checkbox_1, checkbox_2, button_next, input_elements, button_add, button_mass_actual, actual_all, input_quantity_1, button_save_1, input_quantity_2, button_save_2, button_publish,):
    home_page_customer
    vitrina.click()
    my_requests.click()
    button_create_qr.click()
    name_qr.click()
    name_qr.fill("Ценовой запрос 0,1")
    adress_delivery.click()
    adress_delivery.fill("Саратов, Весенний проезд 8")
    adress_delivery_click.click()
    date_From.click()
    date_From.fill("31122024")
    input_terms.click()
    input_terms.fill("Оплата на расчетный счет")
    analogues_Accept.click()
    response_Date.click()
    response_Date_input
    response_Date.fill(response_Date_input)
    button_save.click()
#--------------------Добавление позиций
    button_items.click()
    button_add_item.click()
    button_my_price_list.click()
    search_items.click()
    search_items.fill("Автотест")
    button_search.click()
    checkbox_1.click()
    checkbox_2.click()
    button_next.click()
    input_elements
    button_add.click()
    button_mass_actual.click()
    actual_all.click()
    input_quantity_1.click()
    input_quantity_1.fill("5.236")
    button_save_1.click()
    input_quantity_2.click()
    input_quantity_2.fill("14")
    button_save_2.click()
    button_publish.click()




   

