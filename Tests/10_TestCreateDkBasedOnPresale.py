import delayed_assert
import pytest

from pages.base_page import BasePage
from pages.Contract.contract_create_form_page import ContractFormCreate
from pages.Contract.contract_element_page import ContractElementPage
from pages.Contract.contract_list_page import ContractPage
from pages.login_data import LoginData
from pages.Presale.presale_create_form_page import PresaleFormCreate
from pages.Presale.presale_element_page import PresaleElementPage
from pages.Presale.presale_list_page import PresalePage


class TestDkBasedOnPresale:
    def test_login(self, browser_session):
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        login_page = LoginData(browser_session, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        login_page.verify_username("Mr_KSUP_Seller")
        presale_list_page.go_to_presale_list(link)

    @pytest.mark.xfail(reason="Баг https://jira.lanit.ru/browse/KSUP-1041")
    def test_create_presale(self, browser_session):
        user_data_dict = BasePage.read_file_json(browser_session, r"TPAC\10_DKbasedOnPresale\[Atest_Seller] PA+DK,Tender, categoryA, softwareDev, UnitSale .json")
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        print(user_data_dict)
        link = LoginData.link

        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, link)

        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        # Проверяем предзаполнения менеджеров Баг https://jira.lanit.ru/browse/KSUP-1041
        # create_presale_page.verify_prefill_department_manager(user_data_dict)
        create_presale_page.form_create_presale_all_type(user_data_dict)
        presale_list_page.go_to_mine_elements_tabs()
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        presale_element_page.verify_presale_not_require_status_approval()

        delayed_assert.assert_expectations()

    def test_create_contract_based_on_presale(self, browser_session):
        user_data_dict = BasePage.read_file_json(browser_session, r"TPAC\10_DKbasedOnPresale\[Atest_Seller] PA+DK,Tender, categoryA, softwareDev, UnitSale .json")
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link

        presale_list_page = PresalePage(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, link)
        contract_form_create = ContractFormCreate(browser_session, browser_session.current_url)

        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_mine_elements_tabs()
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)

        presale_element_page.go_to_create_contract_based_on_presale()

        contract_form_create.form_create_contract_based_on_zakup(user_data_dict)
        contract_list_page = ContractPage(browser_session, browser_session.current_url)
        contract_list_page.go_to_mine_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_session, browser_session.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_related_presale(user_data_dict)
