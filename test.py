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
    r"TPAC\3_UnitSale\Seller\[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json"])
class TestUnitSaleFullBusinessCyclePaZpDk:
    def test_login(self, browser_session, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        login_page = LoginData(browser_session, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        login_page.verify_username("Mr_KSUP_Seller")
        presale_list_page.go_to_presale_list(link)

    """
    def test_create_presale(self, browser_session, path_data_file):
        count = 1
        max_count = 50
        while count <= max_count:
            print(count)
            user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
            user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
            print(user_data_dict)
            link = LoginData.link
            presale_list_page = PresalePage(browser_session, link)
            create_presale_page = PresaleFormCreate(browser_session, link)
            presale_list_page.should_be_clickable_create_button()
            presale_list_page.go_to_create_presale()
            create_presale_page.form_create_presale_all_type(user_data_dict, count)
            count += 1
    """
    def test_create_contract_based_on_presale(self, browser_session, path_data_file):
        count = 1
        max_count = 50
        while count <= max_count:
            print(count)
            user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
            user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
            link = LoginData.link

            presale_list_page = PresalePage(browser_session, link)
            presale_element_page = PresaleElementPage(browser_session, link)
            contract_form_create = ContractFormCreate(browser_session, browser_session.current_url)

            presale_list_page.go_to_presale_list(link)
            presale_list_page.should_be_element_on_presale_list(user_data_dict, count)
            presale_list_page.go_to_presale_element(user_data_dict, count)

            presale_element_page.go_to_create_contract_based_on_presale()

            contract_form_create.form_create_contract_based_on_zakup(user_data_dict,count)
            contract_list_page = ContractPage(browser_session, browser_session.current_url)
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            count += 1

def test_number():
    pass