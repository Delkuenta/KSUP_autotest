import pytest
from pages.base_page import BasePage
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_element_page import ContractElementPage
from pages.contract_list_page import ContractPage
from pages.knowledge_search_page import KnowledgeSearchPage
from pages.login_data import LoginData


@pytest.mark.parametrize('path_data_file', [
    r"UnitSale\Seller2 - DirGS\19_[Atest_Seller2] DK, categoryA, softwareDev.json"])
class TestCreateElementBeforeTests:

    def test_create_contract(self, browser_session, path_data_file):
        user_data_dict = BasePage.read_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_session, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_contract_list()
        contract_page = ContractPage(browser_session, browser_session.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser_session, link)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_session, browser_session.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)


class TestKnowledgeBaseSearch:

    def test_default_filter(self, browser_function):
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        login_page.verify_username("Mr_KSUP_Seller")
        login_page.go_to_knowledge_search()
        knowledge_page = KnowledgeSearchPage(browser_function, link)
        knowledge_page.test_default_fast_filter()
        knowledge_page.test_filter_project()
        knowledge_page.test_filter_contract()
        knowledge_page.test_filter_division()
        knowledge_page.test_filter_technology()
        knowledge_page.test_filter_legal()
