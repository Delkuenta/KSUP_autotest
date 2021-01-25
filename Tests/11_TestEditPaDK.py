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


@pytest.fixture(scope="session")
def test_login(browser_session):
    link = LoginData.link
    login_page = LoginData(browser_session, link)
    login_page.open()
    login_page.login("Mr_KSUP_Seller") # Mr_KSUP_Seller
    login_page.verify_username("Mr_KSUP_Seller")


class TestCreatePresaleAndEdit:
    def test_create_presale(self, browser_session, test_login):
        user_data_dict = BasePage.read_file_json(browser_session, r"TPAC\11_Edit_PA_DK\[Atest_Seller] PA,Tender, categoryA, softwareDev, UnitSale.json")
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

    def test_edit_presale(self, browser_session, test_login):
        old_user_data_dict = BasePage.read_file_json(browser_session,
                                                r"TPAC\11_Edit_PA_DK\[Atest_Seller] PA,Tender, categoryA, softwareDev, UnitSale.json")
        old_user_data_dict = BasePage.dict_preparation(browser_session, old_user_data_dict)
        new_user_data_dict = BasePage.read_file_json(browser_session,
                                                r"TPAC\11_Edit_PA_DK\[Atest_Seller] editorPA,Tender, categoryA, softwareDev, UnitSale.json")
        new_user_data_dict = BasePage.dict_preparation(browser_session, new_user_data_dict)

        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, link)

        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(old_user_data_dict)
        presale_element_page.go_to_edit_presale()
        create_presale_page.form_edit_presale(old_user_data_dict, new_user_data_dict)
        presale_list_page.should_be_element_on_presale_list(new_user_data_dict)
        presale_list_page.go_to_presale_element(new_user_data_dict)
        presale_element_page.verify_general_information_in_presale(new_user_data_dict)
        presale_element_page.verify_presale_not_require_status_approval()


class TestCreateContractAndEdit:

    def test_create_contract(self, browser_session, test_login):
        user_data_dict = BasePage.read_file_json(browser_session, r"TPAC\12_Op_department\3_[Atest_Dir2] DK, categoryA, softwareDev.json")
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_session, link)

        login_page.go_to_contract_list(link)
        contract_page = ContractPage(browser_session, browser_session.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser_session, link)
        # Проверяем предзаполнения менеджеров Баг https://jira.lanit.ru/browse/KSUP-1041
        # create_contract_page.verify_prefill_department_manager(user_data_dict)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_session, link)
        contract_element_page.verify_general_information_contract(user_data_dict)
        login_page.logout()

    def test_edit_contract(self, browser_session, test_login):
        old_user_data_dict = BasePage.read_file_json(browser_session,
                                                r"TPAC\12_Op_department\3_[Atest_Dir2] DK, categoryA, softwareDev.json")
        old_user_data_dict = BasePage.dict_preparation(browser_session, old_user_data_dict)
        new_user_data_dict = BasePage.read_file_json(browser_session,
                                                r"TPAC\12_Op_department\3_[Atest_Dir2] DKedited, categoryA, softwareDev.json")
        new_user_data_dict = BasePage.dict_preparation(browser_session, new_user_data_dict)

        link = LoginData.link
        contract_list_page = ContractPage(browser_session, link)
        create_contract_page = ContractFormCreate(browser_session, link)
        contract_element_page = ContractElementPage(browser_session, link)

        contract_list_page.go_to_contract_list(link)
        contract_list_page.go_to_contract_element(old_user_data_dict)
        contract_element_page.go_to_edit_contract()
        create_contract_page.form_edit_contract(old_user_data_dict, new_user_data_dict)
        contract_list_page.go_to_contract_element(new_user_data_dict)
        contract_element_page.verify_general_information_contract(new_user_data_dict)
