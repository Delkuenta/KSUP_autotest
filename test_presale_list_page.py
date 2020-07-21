import pytest
from pages.base_page import BasePage
from pages.presale_list_page import PresalePage
from userdata.login_data import LoginData
from userdata.user_data import UserData

class TestPresaleList:
    def test_verify_user_name(self, browser):
        link = LoginData.Mr_KSUP_Seller
        page = PresalePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.verify_username("Mr_KSUP_Seller")
        page.should_be_clickable_create_button()

    def test_create_presale_tender(self, browser):
        link = LoginData.Mr_KSUP_Seller
        presale_list = PresalePage(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        presale_list.open()                          # открываем страницу
        presale_list.verify_username("Mr_KSUP_Seller")      # проверяем корректность логина
        presale_list.should_be_clickable_create_button() # проверяем доступность кнопки создания
        presale_list.go_to_create_presale()              # нажимаем кнопку создания
        form_presale = PresalePage(browser, browser.current_url) # переходим на страницу создния
        form_presale.form_create_presale_tender() # Создаем пресейл
        presale_list.should_be_element_on_list() # Проверяем создание пресейла в списке

    def test_create_zp_based_on_presale(self, browser):
        link = LoginData.Mr_KSUP_Seller
        presale_list = PresalePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        presale_list.open()  # открываем страницу
        presale_list.verify_username("Mr_KSUP_Seller")  # проверяем корректность логина
        presale_list.go_to_presale_element() # переходим внутрь пресейловой активности
        presale_element = PresalePage(browser, browser.current_url) # передаем экземпляр браузера и ссылку
        presale_element.go_to_create_zp_tender_based_on_presale() # жмем кнопку создания конкурса на основе ПА
        form_create_zp = PresalePage(browser, browser.current_url) # передаем экземпляр браузера и ссылку
        form_create_zp.form_create_zp_based_on_presale_tender() # проверяем и заполняем форму
