import math

import pytest

from pages.Contract.contract_create_form_page import ContractFormCreate
from pages.Contract.contract_element_page import ContractElementPage
from pages.Contract.contract_list_page import ContractPage
from pages.OperplanDepartment.opp_element_page import OppElementPage
from pages.OperplanDepartment.opp_list_page import OppListPage
from pages.Presale.presale_element_page import PresaleElementPage
from pages.base_page import BasePage
from pages.Presale.presale_list_page import PresalePage

from pages.login_data import LoginData
from pages.Presale.presale_create_form_page import PresaleFormCreate


@pytest.mark.parametrize('path_data_file', [
    r"TPAC\3_UnitSale\Seller2\1_[Atest_Seller2] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json"])
class TestUnitSaleFullBusinessCyclePaZpDk:
    def test_login(self, browser_session, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        login_page = LoginData(browser_session, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        presale_list_page.go_to_presale_list(link)

    @pytest.mark.repeat(27)
    def test_create_presale(self, browser_session, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page.form_create_presale_all_type(user_data_dict)


def test_number():
    number = 55000000.33
    integer_part = int(math.modf(number)[1])
    decimal_part = int(round(math.modf(number)[0], 2) * 100)
    integer_string = ('{:,d}'.format(integer_part)).replace(",", " ")
    sum_value = f'{integer_string}' + ',' + f'{decimal_part}'
    print(sum_value)