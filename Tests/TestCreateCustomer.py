import delayed_assert
import pytest

from pages.base_page import BasePage
from pages.customer_create_form import CustomerFormCreate
from pages.customer_list_page import CustomerPage
from pages.login_data import LoginData


@pytest.mark.parametrize('path_data_file', [r"TPAC\KnowledgeElementSearch\4[Atest] Customer, Roga&Kopita.json"])
class TestCustomer:

    def test_create_customer(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_customer_list(link)
        customer_page = CustomerPage(browser_function, link)
        customer_page.go_to_create_customer()
        customer_create_form = CustomerFormCreate(browser_function, link)
        customer_create_form.create_customer_form(user_data_dict)
        delayed_assert.assert_expectations()
