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


@pytest.mark.parametrize('path_data_file', [
    r"TPAC\UnitSale\Seller\1_[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale new.json"])
def test_create_presale(browser_function, path_data_file):
    user_data_dict = BasePage.read_json(browser_function, path_data_file)
    user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
    print(user_data_dict)
    link = LoginData.link
    login_page = LoginData(browser_function, link)
    login_page.open()
    login_page.login(user_data_dict["createAccount"])
    login_page.verify_username(user_data_dict["createAccount"])
    presale_list_page = PresalePage(browser_function, link)
    presale_list_page.go_to_presale_list(link)
    presale_list_page.should_be_clickable_create_button()
    presale_list_page.go_to_create_presale()
    time.sleep(3)
    payments_sum = 0
    count_payments_line = len(user_data_dict["payments"])
    print(f'\nКоличество строчек плановых платежей: {count_payments_line}')
    current_line = 0
    while current_line < count_payments_line:
        # Заполняем поле "Сумма"
        sum_field = browser_function.find_elements(*FormCreatePresaleLocators.SUMTABLE)[current_line]
        sum_field.send_keys(user_data_dict["payments"][current_line]["sum"])

        # Заполняем поле "Год"
        year_field = browser_function.find_elements(*FormCreatePresaleLocators.YEARTABLE)[current_line]
        year_field.send_keys(user_data_dict["payments"][current_line]["year"])

        # Заполняем поле "Квартал"
        quarter_field = browser_function.find_elements(*FormCreatePresaleLocators.QUARTERTABLE)[current_line]
        Select(quarter_field).select_by_visible_text(f'{user_data_dict["payments"][current_line]["quarter"]} квартал')

        payments_sum += user_data_dict["payments"][current_line]["sum"]
        current_line += 1
    breakpoint()