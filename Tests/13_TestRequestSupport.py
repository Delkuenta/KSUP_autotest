import delayed_assert
import pytest

from pages.Support.support_form_page import SupportFormCreate
from pages.base_page import BasePage
from pages.login_data import LoginData

# До первой ошибки --maxfail=1
# Браузер для запуска --browser_name=firefox


@pytest.mark.parametrize('path_data_file', [r"PPAC\13_Request_support\1_[Atest_Seller] ReqSupport.json"])
class TestUnitSaleFullBusinessCyclePaZpDk:
    def test_create_reqsupport(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_request_support()
        support_form_page = SupportFormCreate(browser_function, link)
        support_form_page.form_create_request_support(user_data_dict)
        login_page.logout()
        delayed_assert.assert_expectations()