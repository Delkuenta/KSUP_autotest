import time

import pytest
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_element_page import ContractElementPage
from pages.contract_list_page import ContractPage
from pages.locators import FormCreatePresaleLocators

from pages.login_data import LoginData
from pages.presale_create_form_page import PresaleFormCreate
from pages.presale_element_page import PresaleElementPage
from pages.presale_list_page import PresalePage
from pages.zakup_create_form_page import ZakupFormCreate
from pages.zakup_list_page import ZakupListPage


@pytest.mark.parametrize('path_data_file', [r"TPAC\UnitSale\Seller\1_[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json"])
def test_create_zakup(browser_function, path_data_file):
    user_data_dict = BasePage.read_json(browser_function, path_data_file)
    user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
    print(user_data_dict)
    link = LoginData.link
    login_page = LoginData(browser_function, link)
    login_page.open()
    login_page.login(user_data_dict["createAccount"])
    login_page.verify_username(user_data_dict["createAccount"])
    zakup_list_page = ZakupListPage(browser_function, link)
    zakup_list_page.go_to_zakup_list(link)
    zakup_list_page.go_to_create_zakup()
    zakup_create_form_page = ZakupFormCreate(browser_function, link)
    zakup_create_form_page.form_create_zakup(user_data_dict)
