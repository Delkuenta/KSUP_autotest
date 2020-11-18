import pytest
import delayed_assert

from pages.base_page import BasePage
from pages.presale_element_page import PresaleElementPage
from pages.presale_list_page import PresalePage

from pages.login_data import LoginData
from pages.presale_create_form_page import PresaleFormCreate
from pages.zakup_element_page import ZakupElementPage
from pages.zakup_list_page import ZakupListPage


@pytest.mark.parametrize('path_data_file', [
    r"TPAC\SeparateSale\Seller - Seller2\2[Atest_Seller] PA+ZP+DK, CommercialOffer, categoryA, SoftwareDev, SeparateSale.json"])
class TestUnitSaleFullBusinessCyclePaZpDk:
    def test_verify_visibility_zakup_button_salesManager(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller2")
        zakup_list_page = ZakupListPage(browser_function, link)
        zakup_list_page.go_to_zakup_list(link)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, link)
        refresh_count = 0
        while refresh_count <= 50:
            zakup_element_page.verify_visibility_button_create_contract()
            browser_function.refresh()
            refresh_count += 1

