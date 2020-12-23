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


@pytest.mark.parametrize('path_data_file', [r"TPAC\UnitSale\Seller\1_[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json"])
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

    @pytest.mark.repeat(200)
    @pytest.mark.xfail(reason="Баг https://jira.lanit.ru/browse/KSUP-1041")
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


old_user_data_dict1 = r"TPAC\12_Op_department\1_[Atest_Dir2] PA, red, Tender, categoryA, softwareDev, UnitSale.json"
new_user_data_dict1 = r"TPAC\12_Op_department\1_[Atest_Dir2] PAedited, red, Tender, categoryA, softwareDev, UnitSale.json"
old_user_data_dict2 = r"TPAC\12_Op_department\2_[Atest_Dir2] DK, red, categoryA, softwareDev.json"
new_user_data_dict2 = r"TPAC\12_Op_department\2_[Atest_Dir2] DKedited, red,  categoryA, softwareDev.json"
old_user_data_dict3 = r"TPAC\12_Op_department\3_[Atest_Dir2] PA, orange, Tender, categoryA, softwareDev, UnitSale.json"
new_user_data_dict3 = r"TPAC\12_Op_department\3_[Atest_Dir2] PAedited, orange, Tender, categoryA, softwareDev, UnitSale.json"
new_user_data_dict4 = r"TPAC\12_Op_department\4_[Atest_Dir2] DK, green, categoryC, OtherType.json"
new_user_data_dict5 = r"TPAC\12_Op_department\4_[Аtest_Dir2] PA, green, CommercialOffer, categoryA, softwareDev, UnitSale.json"
user_data_dict6 = r"TPAC\12_Op_department\5_[Atest_Dir2] PA+DK,Tender, categoryA, softwareDev, UnitSale.json"

@pytest.fixture(scope="session")
def test_login(browser_session):
    link = LoginData.link
    login_page = LoginData(browser_session, link)
    login_page.open()
    login_page.login("Mr_KSUP_Dir2") # Mr_KSUP_Seller
    login_page.verify_username("Mr_KSUP_Dir2")


class TestCreateOp:

    @pytest.mark.parametrize('path_data_file', [old_user_data_dict1, old_user_data_dict3, user_data_dict6])
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

    @pytest.mark.parametrize('path_data_file', [old_user_data_dict2])
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

    def test_create_op(self, browser_session, test_login):
        user_data_dict1 = BasePage.read_file_json(browser_session, old_user_data_dict1)
        user_data_dict1 = BasePage.dict_preparation(browser_session, user_data_dict1)

        user_data_dict2 = BasePage.read_file_json(browser_session, old_user_data_dict3)
        user_data_dict2 = BasePage.dict_preparation(browser_session, user_data_dict2)

        user_data_dict3 = BasePage.read_file_json(browser_session, user_data_dict6)
        user_data_dict3 = BasePage.dict_preparation(browser_session, user_data_dict3)

        user_data_dict4 = BasePage.read_file_json(browser_session, old_user_data_dict2)
        user_data_dict4 = BasePage.dict_preparation(browser_session, user_data_dict4)

        link = LoginData.link
        operplan_list_page = OppListPage(browser_session, link)
        operplan_list_page.go_to_operplan_direction(link)
        # operplan_list_page.create_opp("2020")
        operplan_list_page.should_be_element_on_operplan_list("Дирекция по работе с государственным сектором", "2020")
        operplan_list_page.go_to_operplan_element("Дирекция по работе с государственным сектором", "2020")
        operplan_element_page = OppElementPage(browser_session, link)
        operplan_element_page.verify_element_in_operplan(2020, "presale", user_data_dict1)
        operplan_element_page.verify_element_in_operplan(2020, "presale", user_data_dict2)
        operplan_element_page.verify_element_in_operplan(2020, "presale", user_data_dict3)
        operplan_element_page.verify_element_in_operplan(2020, "contract", user_data_dict4)



