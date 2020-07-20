import pytest
from pages.base_page import BasePage
from pages.presale_list_page import PresalePage

class TestPresaleList:
    def test_verify_user_name(self, browser):
        user_name = "Mr_KSUP_Seller"
        link = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_windows/default.aspx?ReturnUrl=%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F%255Fwindows%252Fdefault%252Easpx&Source=%2f_windows%2fdefault.aspx"
        page = PresalePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.verify_username(user_name)
        page.should_be_clickable_create_button()

