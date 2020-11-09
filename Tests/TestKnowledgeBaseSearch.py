import delayed_assert
import pytest

from Tests import TestDkFullBusinessCycle
from pages.base_page import BasePage
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_element_page import ContractElementPage
from pages.contract_list_page import ContractPage
from pages.knowledge_search_page import KnowledgeSearchPage
from pages.login_data import LoginData
from pages.project_create_form_page import ProjectFormCreate
from pages.project_element_page import ProjectElementPage
from pages.project_list_page import ProjectPage

project_path_file = r"TPAC\KnowledgeElementSearch\2[Atest_Seller] Project, categoryA, softwareDev.json"
contract_path_file = r"TPAC\KnowledgeElementSearch\1[Atest_Seller] DK, categoryA, softwareDev_new.json"


class TestCreateElementBeforeTests:
    @pytest.mark.parametrize('path_data_file', [contract_path_file])
    def test_create_contract_for_knowledge(self, browser_session, path_data_file):
        user_data_dict = BasePage.read_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_session, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_contract_list(link)
        contract_page = ContractPage(browser_session, browser_session.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser_session, link)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_session, browser_session.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)

    @pytest.mark.parametrize('path_data_file', [project_path_file])
    def test_create_project(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_project_list(link)
        project_list_page = ProjectPage(browser_function, link)
        project_list_page.go_to_create_project()
        project_create_page = ProjectFormCreate(browser_function, link)
        project_create_page.form_create_project(user_data_dict)
        project_element_page = ProjectElementPage(browser_function, link)
        project_element_page.verify_general_information_in_project(user_data_dict)


class TestKnowledgeBaseSearch:

    def test_login_for_knowledge_test(self, browser_session):
        link = LoginData.link
        login_page = LoginData(browser_session, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        login_page.verify_username("Mr_KSUP_Seller")
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.go_to_knowledge_search(link)

    def test_default_block_filter(self, browser_session):
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.verify_default_fast_filter()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.verify_fast_filter_project()
        knowledge_page.deactivate_checkbox_need_to_find("Проект")
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.verify_fast_filter_contract()
        knowledge_page.deactivate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.activate_checkbox_need_to_find("Подразделение")
        knowledge_page.verify_fast_filter_division()
        knowledge_page.deactivate_checkbox_need_to_find("Подразделение")
        knowledge_page.activate_checkbox_need_to_find("Технологию")
        knowledge_page.verify_fast_filter_technology()
        knowledge_page.deactivate_checkbox_need_to_find("Технологию")
        knowledge_page.activate_checkbox_need_to_find("Юр.лицо/ИП")
        knowledge_page.verify_fast_filter_legal()
        knowledge_page.deactivate_checkbox_need_to_find("Юр.лицо/ИП")
        knowledge_page.reset_button_knowledge()
        delayed_assert.assert_expectations()

    def test_search_line_by_name_project(self, browser_session):
        project_data_dict = BasePage.read_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        # knowledge_page.go_to_knowledge_search()
        knowledge_page.search_lien_by_name(project_data_dict)

    def test_search_line_by_name_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_lien_by_name(contract_data_dict)

    def test_search_line_by_customer(self, browser_session):
        pass

    def test_search_with_customer_block_filter_in_project(self, browser_session):
        project_data_dict = BasePage.read_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_customer_block_filter(project_data_dict)

    def test_search_with_legal_block_filter_in_project(self, browser_session):
        project_data_dict = BasePage.read_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_legal_block_filter(project_data_dict)

    def test_search_with_performer_block_filter_in_project(self, browser_session):
        project_data_dict = BasePage.read_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_performer_block_filter(project_data_dict)

    def test_search_with_type_works_block_filter_in_project(self, browser_session):
        project_data_dict = BasePage.read_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_type_works_block_filter(project_data_dict)

    def test_search_with_technologies_block_filter_in_project(self, browser_session):
        project_data_dict = BasePage.read_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_technologies_block_filter(project_data_dict)

    def test_search_with_all_fast_filter_in_project(self, browser_session):
        project_data_dict = BasePage.read_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_all_fast_filter_on_project(project_data_dict)

    @pytest.mark.xfail(reason='Не осуществляется поиск если в поля "Сумма проекта" От и До  ввести одинаковое значение /KSUP-1090')
    def test_search_with_sum_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_sum_block_filter(contract_data_dict)

    @pytest.mark.xfail(reason='Значение в поле Дата заключения и Дата завершения отличается на -1 день от реальных значений /KSUP-1092')
    def test_search_with_start_date_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_start_date_block_filter(contract_data_dict)

    @pytest.mark.xfail(reason='Значение в поле Дата заключения и Дата завершения отличается на -1 день от реальных значений /KSUP-1092')
    def test_search_with_end_date_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_end_date_block_filter(contract_data_dict)

    @pytest.mark.xfail(reason='В БЗ по сущности ДК не работает фильтрация по блоку "Статус контракта" /KSUP-1074')
    def test_search_with_status_contract_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_status_block_filter(contract_data_dict)

    @pytest.mark.xfail(reason="В карточке ДК отсутствует поле Заказчик /KSUP-1092")
    def test_search_with_customer_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_customer_block_filter(contract_data_dict)

    def test_search_with_legal_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_legal_block_filter(contract_data_dict)

    def test_search_with_performer_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_performer_block_filter(contract_data_dict)

    def test_search_with_type_works_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_type_works_block_filter(contract_data_dict)

    @pytest.mark.xfail(reason="В карточке ДК отсутствует поле Технологии /KSUP-1092")
    def test_search_with_technologies_block_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_technologies_block_filter(contract_data_dict)

    @pytest.mark.xfail(reason='В БЗ по сущности ДК не работает фильтрация по блоку "Статус контракта" /KSUP-1074')
    def test_search_with_all_fast_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_all_fast_filter_on_contract(contract_data_dict)



