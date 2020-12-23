import delayed_assert
import pytest

from pages.base_page import BasePage
from pages.Customer.customer_create_form import CustomerFormCreate
from pages.Customer.customer_list_page import CustomerPage
from pages.login_data import LoginData

"""
Customer\[Atest]Customer, OOO.json
Customer\[Atest]Customer, IP.json
"""
@pytest.mark.parametrize('path_data_file', [r"TPAC\1_Customer\[Atest]Customer, IP.json",
                                            r"TPAC\1_Customer\[Atest]Customer, OOO.json"])
class TestCustomer:

    def test_create_customer(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        # login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_customer_list(link)
        customer_page = CustomerPage(browser_function, link)
        customer_page.go_to_create_customer()
        customer_create_form = CustomerFormCreate(browser_function, link)
        customer_create_form.create_customer_form(user_data_dict)
        if user_data_dict["gklanit"] == 1:
            customer_page.go_to_gklanit_tab()
            customer_page.should_be_element_on_customer_list(user_data_dict)
        if len(str(user_data_dict["ogrn"])) == 13:
            customer_page.go_to_ul_tab()
            customer_page.should_be_element_on_customer_list(user_data_dict)
        else:
            customer_page.go_to_ip_tab()
            customer_page.should_be_element_on_customer_list(user_data_dict)
        delayed_assert.assert_expectations()
