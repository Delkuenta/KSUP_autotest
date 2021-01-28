import pytest
from pages.Contract.contract_create_form_page import ContractFormCreate
from pages.Contract.contract_element_page import ContractElementPage
from pages.Contract.contract_list_page import ContractPage
from pages.OperplanDepartment.opp_element_page import OppElementPage
from pages.OperplanDepartment.opp_list_page import OppListPage
from pages.Presale.presale_create_form_page import PresaleFormCreate
from pages.Presale.presale_element_page import PresaleElementPage
from pages.Presale.presale_list_page import PresalePage
from pages.base_page import BasePage
from pages.login_data import LoginData

yearOP = "2020"
departmentOP = "Тестовая дирекция"

old_red_pa_dict = r"TPAC\12_Op_department\1_[Atest_Dir2] PA, red, Tender, categoryA, softwareDev, UnitSale.json"
new_red_pa_dict = r"TPAC\12_Op_department\1_[Atest_Dir2] PAedited, red, Tender, categoryA, softwareDev, UnitSale.json"

old_red_dk_dict = r"TPAC\12_Op_department\2_[Atest_Dir2] DK, red, categoryA, softwareDev.json"
new_red_dk_dict = r"TPAC\12_Op_department\2_[Atest_Dir2] DKedited, red,  categoryA, softwareDev.json"

old_orange_pa_dict = r"TPAC\12_Op_department\3_[Atest_Dir2] PA, orange, Tender, categoryA, softwareDev, UnitSale.json"
new_orange_pa_dict = r"TPAC\12_Op_department\3_[Atest_Dir2] PAedited, orange, Tender, categoryA, softwareDev, UnitSale.json"

new_green_dk_dict = r"TPAC\12_Op_department\4_[Atest_Dir2] DK, green, categoryC, OtherType.json"

new_green_pa_dict = r"TPAC\12_Op_department\4_[Аtest_Dir2] PA, green, CommercialOffer, categoryA, softwareDev, UnitSale.json"

gray_pa_dk_dict = r"TPAC\12_Op_department\5_[Atest_Dir2] PA+DK, gray, Tender, categoryA, softwareDev, UnitSale.json"


@pytest.fixture(scope="session")
def test_login(browser_session):
    link = LoginData.link
    login_page = LoginData(browser_session, link)
    login_page.open()
    login_page.login("Mr_KSUP_Dir2")
    login_page.verify_username("Mr_KSUP_Dir2")


class TestCreateAndUpdateOp:

    # Создание пресейлов которые войдут в оперплан 2020
    @pytest.mark.parametrize('path_data_file', [old_red_pa_dict, old_orange_pa_dict, gray_pa_dk_dict])
    def test_createpresale(self, browser_session, test_login, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, browser_session.current_url)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page.form_create_presale_all_type(user_data_dict)
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        presale_element_page.verify_presale_not_require_status_approval()

    # Создание контракта который войдет в оперплан 2020
    @pytest.mark.parametrize('path_data_file', [old_red_dk_dict])
    def test_createcontract(self, browser_session, test_login, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_session, link)
        login_page.go_to_contract_list(link)
        contract_page = ContractPage(browser_session, browser_session.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser_session, link)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_session, browser_session.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)

    # Создание оперплана и проверка сущностей которые в него попали
    def test_create_op(self, browser_session, test_login):
        user_data_dict1 = BasePage.read_file_json(browser_session, old_red_pa_dict)
        user_data_dict1 = BasePage.dict_preparation(browser_session, user_data_dict1)

        user_data_dict2 = BasePage.read_file_json(browser_session, old_orange_pa_dict)
        user_data_dict2 = BasePage.dict_preparation(browser_session, user_data_dict2)

        user_data_dict3 = BasePage.read_file_json(browser_session, gray_pa_dk_dict)
        user_data_dict3 = BasePage.dict_preparation(browser_session, user_data_dict3)

        user_data_dict4 = BasePage.read_file_json(browser_session, old_red_dk_dict)
        user_data_dict4 = BasePage.dict_preparation(browser_session, user_data_dict4)

        link = LoginData.link
        operplan_list_page = OppListPage(browser_session, link)
        operplan_list_page.go_to_operplan_direction(link)
        operplan_list_page.create_opp(departmentOP, yearOP)
        operplan_list_page.should_be_element_on_operplan_list(departmentOP, yearOP)
        operplan_list_page.go_to_operplan_element(departmentOP, yearOP)
        operplan_element_page = OppElementPage(browser_session, link)
        operplan_element_page.verify_element_in_operplan(2020, "presale", user_data_dict1)
        operplan_element_page.verify_element_in_operplan(2020, "presale", user_data_dict2)
        operplan_element_page.verify_element_in_operplan(2020, "presale", user_data_dict3)
        operplan_element_page.verify_element_in_operplan(2020, "contract", user_data_dict4)

    # Редактирование ПА(изменение вероятности на 0%)
    def test_edit_presale_red(self, browser_session, test_login):
        old_user_data_dict = BasePage.read_file_json(browser_session, old_red_pa_dict)
        old_user_data_dict = BasePage.dict_preparation(browser_session, old_user_data_dict)

        new_user_data_dict = BasePage.read_file_json(browser_session, new_red_pa_dict)
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

    # Редактирование ПА(изменение плановых платежей)
    def test_edit_presale_orange(self, browser_session, test_login):
        old_user_data_dict = BasePage.read_file_json(browser_session, old_orange_pa_dict)
        old_user_data_dict = BasePage.dict_preparation(browser_session, old_user_data_dict)

        new_user_data_dict = BasePage.read_file_json(browser_session, new_orange_pa_dict)
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

    # Редактирование ДК(изменение статуса контракта на "Расторгнут")
    def test_edit_contract_red(self, browser_session, test_login):
        old_user_data_dict = BasePage.read_file_json(browser_session, old_red_dk_dict)
        old_user_data_dict = BasePage.dict_preparation(browser_session, old_user_data_dict)

        new_user_data_dict = BasePage.read_file_json(browser_session, new_red_dk_dict)
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

    # Создание ДК из пресейла (серый цвет)
    @pytest.mark.parametrize('path_data_file', [gray_pa_dk_dict])
    def test_create_contract_based_on_presale(self, browser_session, test_login, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link

        presale_list_page = PresalePage(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, link)
        contract_form_create = ContractFormCreate(browser_session, browser_session.current_url)

        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)

        presale_element_page.go_to_create_contract_based_on_presale()

        contract_form_create.form_create_contract_based_on_zakup(user_data_dict)
        contract_list_page = ContractPage(browser_session, browser_session.current_url)
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_session, browser_session.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_related_presale(user_data_dict)

    # Создание нового пресейла(зеленый цвет)
    @pytest.mark.parametrize('path_data_file', [new_green_pa_dict])
    def test_create_presale(self, browser_session, test_login, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, browser_session.current_url)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page.form_create_presale_all_type(user_data_dict)
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        presale_element_page.verify_presale_not_require_status_approval()

    # Создание нового ДК(зеленый цвет)
    @pytest.mark.parametrize('path_data_file', [new_green_dk_dict])
    def test_create_contract(self, browser_session, test_login, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_session, link)
        login_page.go_to_contract_list(link)
        contract_page = ContractPage(browser_session, browser_session.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser_session, link)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_session, browser_session.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)

    # Обновление ОП
    def test_update_op(self, browser_session, test_login):
        link = LoginData.link
        operplan_list_page = OppListPage(browser_session, link)
        operplan_list_page.go_to_operplan_direction(link)
        operplan_list_page.should_be_element_on_operplan_list(departmentOP, yearOP)
        operplan_list_page.go_to_operplan_element(departmentOP, yearOP)
        operplan_element_page = OppElementPage(browser_session, link)
        operplan_element_page.go_to_update_operplan()

    # Проверка выделения сущности цветом в ОП
    def test_color_row(self, browser_session, test_login):
        red_pa_dict = BasePage.read_file_json(browser_session, new_red_pa_dict)
        red_dk_dict = BasePage.read_file_json(browser_session, new_red_dk_dict)
        orange_pa_dict = BasePage.read_file_json(browser_session, new_orange_pa_dict)
        green_pa_dict = BasePage.read_file_json(browser_session, new_green_pa_dict)
        green_dk_dict = BasePage.read_file_json(browser_session, new_green_dk_dict)
        gray_dk_dict = BasePage.read_file_json(browser_session, gray_pa_dk_dict)
        link = LoginData.link
        operplan_list_page = OppListPage(browser_session, link)
        operplan_list_page.go_to_operplan_direction(link)
        operplan_list_page.should_be_element_on_operplan_list("Тестовая дирекция", "2020")
        operplan_list_page.go_to_operplan_element("Тестовая дирекция", "2020")
        operplan_element_page = OppElementPage(browser_session, link)
        operplan_element_page.verify_color_element(red_pa_dict, "red")
        operplan_element_page.verify_color_element(red_dk_dict, "red")
        operplan_element_page.verify_color_element(orange_pa_dict, "orange")
        operplan_element_page.verify_color_element(green_pa_dict, "green")
        operplan_element_page.verify_color_element(green_dk_dict, "green")
        operplan_element_page.verify_color_element(gray_dk_dict, "gray")
