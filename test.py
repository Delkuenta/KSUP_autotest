import pytest
import delayed_assert

from pages.base_page import BasePage
from pages.presale_element_page import PresaleElementPage
from pages.presale_list_page import PresalePage

from pages.login_data import LoginData
from pages.presale_create_form_page import PresaleFormCreate



class Test_123124:
    def test_1234(self, browser_function):
        link = "https://google.com"
        login_page = LoginData(browser_function, link)
        login_page.open()
        browser_function.find_element_by_css_selector("[class='gLFyf gsfi']").send_keys("hello")
        breakpoint()
