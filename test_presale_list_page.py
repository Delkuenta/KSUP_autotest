import pytest
from pages.base_page import BasePage
from pages.presale_list_page import PresalePage
from pages.zakup_list_page import ZakupPage
from userdata.login_data import LoginData
from userdata.user_data import UserData
from pages.presale_create_form_page import PresaleFormCreate
from pages.presale_element_page import PresaleElementPage
from pages.zakup_list_page import ZakupPage
from pages.zakup_create_form_page import ZakupFormCreate
from pages.locators import ZakupPageLocators


class TestNameUnknown:
    def test_verify_user_name(self, browser):
        link = LoginData.Mr_KSUP_Seller
        page = PresalePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.verify_username("Mr_KSUP_Seller")
        page.should_be_clickable_create_button()

    def test_create_presale(self, browser):
        link = LoginData.Mr_KSUP_Seller
        page = PresalePage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.verify_username("Mr_KSUP_Seller")
        page.should_be_clickable_create_button()
        page.go_to_create_presale()
        presale_create_form = PresaleFormCreate(browser, browser.current_url)
        presale_create_form.form_create_presale_tender()
        page.should_be_element_on_presale_list()

    def test_create_zp_based_on_presale(self, browser):
        link = LoginData.Mr_KSUP_Seller
        page = PresalePage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.verify_username("Mr_KSUP_Seller")
        page.go_to_presale_element()
        page_presale_element = PresaleElementPage(browser, browser.current_url)
        page_presale_element.go_to_create_zp_tender_based_on_presale()
        zakup_create_form = ZakupFormCreate(browser, browser.current_url)
        zakup_create_form.form_create_zp_based_on_presale_tender()
        page_zakup_list = ZakupPage(browser, browser.current_url)
        page_zakup_list.should_be_element_on_zakup_list()
