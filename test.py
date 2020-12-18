import pytest
import delayed_assert

from pages.base_page import BasePage
from pages.presale_element_page import PresaleElementPage
from pages.presale_list_page import PresalePage

from pages.login_data import LoginData
from pages.presale_create_form_page import PresaleFormCreate
from pages.zakup_element_page import ZakupElementPage
from pages.zakup_list_page import ZakupListPage


@pytest.mark.parametrize('path_data_file', [r"TPAC\UnitSale\Seller\1_[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json"])
class TestUnitSaleFullBusinessCyclePaZpDk:
    def test_login(self, browser_session, path_data_file):
        user_data_dict = BasePage.read_json(browser_session, path_data_file)
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
        user_data_dict = BasePage.read_json(browser_session, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page.form_create_presale_all_type(user_data_dict)


def test_function_split():
    dick = ["хуй"]
    print(dick[-1])