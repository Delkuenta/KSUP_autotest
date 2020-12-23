import pytest
import delayed_assert

from pages.base_page import BasePage
from pages.login_data import LoginData
from pages.Presale.presale_create_form_page import PresaleFormCreate
from pages.Presale.presale_element_page import PresaleElementPage
from pages.Presale.presale_list_page import PresalePage

@pytest.mark.parametrize('path_data_file', [
    r"TPAC\7_RejectApproval\5_[Atest_Seller] Reject PA, Tender, categoryA,  SoftwareDev, SeparateSale.json"])
class TestRejectPresale:

    def test_create_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page = PresaleFormCreate(browser_function, link)
        # Проверяем предзаполнения менеджеров Баг https://jira.lanit.ru/browse/KSUP-1041
        # create_presale_page.verify_prefill_department_manager(user_data_dict)
        create_presale_page.form_create_presale_all_type(user_data_dict)
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_presale_approval_waiting_status()
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        login_page.logout()
        delayed_assert.assert_expectations()

    def test_reject_presale_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" \
                or user_data_dict["createAccount"] == "Mr_KSUP_Dir":
            login_page.login("Mr_KSUP_Dir2")
            login_page.verify_username("Mr_KSUP_Dir2")
        else:
            login_page.login("Mr_KSUP_Dir")
            login_page.verify_username("Mr_KSUP_Dir")
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.reject_approval_presale(user_data_dict)
        # Баг (https://jira.lanit.ru/browse/KSUP-1107) после отклонения выкидывает на страницу по умолчанию, а не остается в карточке
        # убрать две строки после фикса
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        # -------------------------------------------------------
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_presale_approval_reject_status()
        login_page.logout()

    def test_send_approval_presale_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.send_to_approval_presale(user_data_dict)
        presale_element_page.verify_presale_approval_waiting_status()
        login_page.logout()

    def test_reject_presale_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" \
                or user_data_dict["createAccount"] == "Mr_KSUP_Dir":
            login_page.login("Mr_KSUP_Dir2")
            login_page.verify_username("Mr_KSUP_Dir2")
        else:
            login_page.login("Mr_KSUP_Dir")
            login_page.verify_username("Mr_KSUP_Dir")
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.reject_approval_presale(user_data_dict)
        # Баг (https://jira.lanit.ru/browse/KSUP-1107) после отклонения выкидывает на страницу по умолчанию, а не остается в карточке
        # убрать две строки после фикса
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        # -------------------------------------------------------
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_presale_approval_reject_status()
        login_page.logout()

    def test_send_approval_presale_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.send_to_approval_presale(user_data_dict)
        presale_element_page.verify_presale_approval_waiting_status()
        login_page.logout()

    def test_approval_presale_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" \
                or user_data_dict["createAccount"] == "Mr_KSUP_Dir":
            login_page.login("Mr_KSUP_Dir2")
            login_page.verify_username("Mr_KSUP_Dir2")
        else:
            login_page.login("Mr_KSUP_Dir")
            login_page.verify_username("Mr_KSUP_Dir")
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.approval_presale(user_data_dict)
        presale_element_page.verify_presale_approval_successfully_status()
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        login_page.logout()
