import delayed_assert
import pytest


from pages.base_page import BasePage
from pages.Contract.contract_create_form_page import ContractFormCreate
from pages.Contract.contract_element_page import ContractElementPage
from pages.Contract.contract_list_page import ContractPage
from pages.KnowledgeBase.knowledge_search_page import KnowledgeSearchPage
from pages.login_data import LoginData
from pages.Project.project_create_form_page import ProjectFormCreate
from pages.Project.project_element_page import ProjectElementPage
from pages.Project.project_list_page import ProjectPage

project_path_file = r"TPAC\6_KnowledgeElementSearch\1[Atest_Seller] Project, categoryA, softwareDev.json"
contract_path_file = r"TPAC\6_KnowledgeElementSearch\2[Atest_Seller] DK, categoryA, softwareDev.json"
department_path_file = r"TPAC\6_KnowledgeElementSearch\3[Atest] Department, DKS.json"
ulip_path_file = r"TPAC\1_Customer\[Atest]Customer, OOO.json"


@pytest.fixture(scope="session")
def login_for_knowledge(browser_session):
    link = LoginData.link
    login_page = LoginData(browser_session, link)
    login_page.open()
    login_page.login("Mr_KSUP_Seller")
    login_page.verify_username("Mr_KSUP_Seller")
    knowledge_page = KnowledgeSearchPage(browser_session, link)
    knowledge_page.go_to_knowledge_search(link)


class TestCreateElementBeforeTests:
    @pytest.mark.parametrize('path_data_file', [project_path_file])
    def test_create_project(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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

    @pytest.mark.parametrize('path_data_file', [contract_path_file])
    def test_create_contract_for_knowledge(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_contract_list(link)
        contract_page = ContractPage(browser_function, browser_function.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser_function, link)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)


class TestKnowledgeBaseSearch:
    # Проверка отображения фильтров по умолчанию(при входе и активации чек-боксов в блоке Нужно найти)
    def test_default_block_filter(self, browser_session, login_for_knowledge):
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
    # Проверка поиска сущностей при активации чек-бокса в блоке "Заказчик"
    # Проверка поиска сущностей при активации чек-бокса в блоке "Юр.лицо-исполнитель"
    # Проверка поиска сущностей при активации чек-бокса в блоке "Подразделение-исполнитель"
    # Проверка поиска сущностей при активации чек-бокса в блоке "Тип работ и услуг"
    # Проверка поиска сущностей при активации чек-бокса в  блоке "Технологии"

    # Поиск проекта в строке по названию
    def test_search_line_project_by_name(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.search_line_by_name(project_data_dict["fullName"])

    # Поиск проекта в строке поиска по подразделению
    def test_search_line_project_by_department(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_line_by_department(project_data_dict)

    # Поиск проекта в строке поиска по заказчику
    def test_search_line_project_by_customer(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_line_by_customer(project_data_dict)

    # Поиск проекта в строке поиска по исполнителю
    @pytest.mark.xfail(reason='Не отображено поле "Юр.лицо-исполнитель" в карточке сущности Проект /KSUP-1082')
    def test_search_line_project_by_executive_unit_legal(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_line_by_executive_unit_legal(project_data_dict)

    # Поиск проекта в строке поиска по Типу работ и услуг
    @pytest.mark.xfail(reason='Не отображено поле "Тип работ и услуг" в карточке сущности Проект /KSUP-1082')
    def test_search_line_project_by_type_work_and_services(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_line_by_type_works_and_services(project_data_dict)

    # Поиск проекта в строке поиска по Технологии
    def test_search_line_project_by_technologies(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_line_by_technologies(project_data_dict)

    # Поиск проекта в строке поиска по Категории
    def test_search_line_project_by_category(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_line_by_category(project_data_dict)

    # Поиск договора/контракта в строке по названию
    def test_search_line_contract_by_name(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.search_line_by_name(contract_data_dict["fullName"])

    # Поиск договора/контракта в строке поиска по заказчику
    @pytest.mark.xfail(reason='Не отображено поле "Заказчик" в карточке сущности ДК /KSUP-1092')
    def test_search_line_contract_by_customer(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)+")
        knowledge_page.search_line_by_customer(contract_data_dict)

    # Поиск договора/контракта в строке поиска по исполнителю
    def test_search_line_contract_by_executive_unit_legal(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_line_by_executive_unit_legal(contract_data_dict)

    # Поиск договора/контракта в строке поиска по подразделению
    def test_search_line_contract_by_department(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_line_by_department(contract_data_dict)

    # Поиск договора/контракта в строке поиска по номеру контракта
    def test_search_line_contract_by_number(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_line_by_number(contract_data_dict)

    # Поиск договора/контракта в строке поиска по Типу работ и услуг
    def test_search_line_contract_by_type_work_and_services(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_line_by_type_works_and_services(contract_data_dict)

    # Поиск договора/контракта в строке поиска по Технологии
    def test_search_line_contract_by_technologies(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_line_by_technologies(contract_data_dict)

    # Поиск Юр.лицо/ИП в строке поиска поиска по короткому названию
    def test_search_line_ulip_by_short_name(self, browser_session, login_for_knowledge):
        ulip_data_dict = BasePage.read_file_json(browser_session, ulip_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Юр.лицо/ИП")
        knowledge_page.search_line_ulip_by_name(ulip_data_dict)

    # Поиск Юр.лицо/ИП в строке поиска по отрасль
    def test_search_line_ulip_by_industry(self, browser_session, login_for_knowledge):
        ulip_data_dict = BasePage.read_file_json(browser_session, ulip_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Юр.лицо/ИП")
        knowledge_page.search_line_by_industry(ulip_data_dict)

    # Поиск Юр.лицо/ИП в строке поиска по огрн
    @pytest.mark.xfail(reason='Значение в поле ОГРН разделено пробелом по 3 знака /KSUP-1088')
    def test_search_line_ulip_by_ogrn(self, browser_session, login_for_knowledge):
        ulip_data_dict = BasePage.read_file_json(browser_session, ulip_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Юр.лицо/ИП")
        knowledge_page.search_line_by_ogrn(ulip_data_dict)

    # Поиск Юр.лицо/ИП в строке поиска по ИНН
    @pytest.mark.xfail(reason='Значение в поле ИНН разделено пробелом по 3 знака /KSUP-1088')
    def test_search_line_ulip_by_inn(self, browser_session, login_for_knowledge):
        ulip_data_dict = BasePage.read_file_json(browser_session, ulip_path_file)
        if len(str(ulip_data_dict["ogrn"])) == 13:
            link = browser_session.current_url
            knowledge_page = KnowledgeSearchPage(browser_session, link)
            knowledge_page.reset_button_knowledge()
            knowledge_page.activate_checkbox_need_to_find("Юр.лицо/ИП")
            knowledge_page.search_line_by_inn(ulip_data_dict)
        else:
            print("Проверка отображения и поиска по ИНН осущеставляется только для Юр.лиц, где ОГРН = 13 символам")

    # Поиск Юр.лицо/ИП в строке поиска по КПП
    @pytest.mark.xfail(reason='Значение в поле КПП разделено пробелом по 3 знака /KSUP-1088')
    def test_search_line_ulip_by_kpp(self, browser_session, login_for_knowledge):
        ulip_data_dict = BasePage.read_file_json(browser_session, ulip_path_file)
        if len(str(ulip_data_dict["ogrn"])) == 13:
            link = browser_session.current_url
            knowledge_page = KnowledgeSearchPage(browser_session, link)
            knowledge_page.reset_button_knowledge()
            knowledge_page.activate_checkbox_need_to_find("Юр.лицо/ИП")
            knowledge_page.search_line_by_inn(ulip_data_dict)
        else:
            print("Проверка отображения и поиска по КПП осущеставляется только для Юр.лиц, где ОГРН = 13 символам")

    # Поиск Подразделение в строке поиска поиска по названию
    def test_search_line_department_by_name(self, browser_session, login_for_knowledge):
        department_dict = BasePage.read_file_json(browser_session, department_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Подразделение")
        knowledge_page.search_line_by_name(department_dict["fullName"])

    # Поиск проекта с блоком фильтрации "Заказчик"
    def test_search_project_with_customer_block_filter(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_customer_block_filter(project_data_dict)

    # Поиск проекта с блоком фильтрации "Юр.лицо-исполнитель"
    def test_search_project_with_legal_block_filter(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_legal_block_filter(project_data_dict)

    # Поиск проекта с блоком фильтрации "Подразделение-исполнитель"
    def test_search_project_with_performer_block_filter(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_performer_block_filter(project_data_dict)

    # Поиск проекта с блоком фильтрации "Тип работ и услуг"
    def test_search_project_with_type_works_block_filter(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_type_works_block_filter(project_data_dict)

    # Поиск проекта с блоком фильтрации "Технологии"
    def test_search_project_with_technologies_block_filter(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_technologies_block_filter(project_data_dict)

    # Поиск проекта с активацией всех быстрых фильтров по очереди
    def test_search_project_with_all_fast_filter(self, browser_session, login_for_knowledge):
        project_data_dict = BasePage.read_file_json(browser_session, project_path_file)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Проект")
        knowledge_page.search_with_all_fast_filter_on_project(project_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Стоимость проекта (руб.)"
    @pytest.mark.xfail(reason='Не осуществляется поиск если в поля "Сумма проекта" От и До  ввести одинаковое значение /KSUP-1090')
    def test_search_with_sum_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_sum_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Дата заключения"
    @pytest.mark.xfail(reason='Не осуществляется поиск если в поля "Дата заключения" От  ввести равное значение из ДК /KSUP-1138')
    def test_search_with_start_date_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_start_date_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Дата окончания"
    @pytest.mark.xfail(reason='Не осуществляется поиск если в поля "Дата окончания" От  ввести равное значение из ДК /KSUP-1138')
    def test_search_with_end_date_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_end_date_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Статус контракта"
    @pytest.mark.xfail(reason='В БЗ по сущности ДК не работает фильтрация по блоку "Статус контракта" /KSUP-1074')
    def test_search_with_status_contract_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_status_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Заказчик"
    @pytest.mark.xfail(reason="В карточке ДК отсутствует поле Заказчик /KSUP-1092")
    def test_search_with_customer_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_customer_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Юр.лицо-исполнитель"
    def test_search_with_legal_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_legal_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Подразделение-исполнитель"
    def test_search_with_performer_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_performer_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Тип работ и услуг"
    def test_search_with_type_works_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_type_works_block_filter(contract_data_dict)

    # Поиск договор/контракта с блоком фильтрации "Технологии"
    @pytest.mark.xfail(reason="В карточке ДК отсутствует поле Технологии /KSUP-1092")
    def test_search_with_technologies_block_filter_in_contract(self, browser_session, login_for_knowledge):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_technologies_block_filter(contract_data_dict)

    # Поиск договор/контракта с активацией всех быстрых фильтров по очереди
    @pytest.mark.xfail(reason='В БЗ по сущности ДК не работает фильтрация по блоку "Статус контракта" /KSUP-1074')
    def test_search_with_all_fast_filter_in_contract(self, browser_session):
        contract_data_dict = BasePage.read_file_json(browser_session, contract_path_file)
        contract_data_dict = BasePage.dict_preparation(browser_session, contract_data_dict)
        link = browser_session.current_url
        knowledge_page = KnowledgeSearchPage(browser_session, link)
        knowledge_page.reset_button_knowledge()
        knowledge_page.activate_checkbox_need_to_find("Договор (контракт)")
        knowledge_page.search_with_all_fast_filter_on_contract(contract_data_dict)



