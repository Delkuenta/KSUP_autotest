import delayed_assert
import pytest

from pages.base_page import BasePage
from pages.login_data import LoginData
from pages.presale_create_form_page import PresaleFormCreate
from pages.presale_element_page import PresaleElementPage
from pages.presale_list_page import PresalePage


class TestCreatePresaleAndEdit:
    def test_login(self, browser_session):
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        login_page = LoginData(browser_session, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        login_page.verify_username("Mr_KSUP_Seller")
        presale_list_page.go_to_presale_list(link)

    @pytest.mark.xfail(reason="Баг https://jira.lanit.ru/browse/KSUP-1041")
    def test_create_presale(self, browser_session):
        user_data_dict = BasePage.read_file_json(browser_session, "TPAC\Edit_PA_DK\[Atest_Seller] PA,Tender, categoryA, softwareDev, UnitSale.json")
        user_data_dict = BasePage.dict_preparation(browser_session, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, link)

        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page.form_create_presale_all_type(user_data_dict)
        presale_list_page.go_to_mine_elements_tabs()
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        presale_element_page.verify_presale_not_require_status_approval()

        delayed_assert.assert_expectations()

    def test_edit_presale(self, browser_session):
        old_user_data_dict = BasePage.read_file_json(browser_session,
                                                "TPAC\Edit_PA_DK\[Atest_Seller] PA,Tender, categoryA, softwareDev, UnitSale.json")
        old_user_data_dict = BasePage.dict_preparation(browser_session, old_user_data_dict)
        new_user_data_dict = BasePage.read_file_json(browser_session,
                                                "TPAC\Edit_PA_DK\[Atest_Seller] editorPA,Tender, categoryA, softwareDev, UnitSale.json")
        new_user_data_dict = BasePage.dict_preparation(browser_session, new_user_data_dict)

        link = LoginData.link
        presale_list_page = PresalePage(browser_session, link)
        create_presale_page = PresaleFormCreate(browser_session, link)
        presale_element_page = PresaleElementPage(browser_session, link)

        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(old_user_data_dict)
        presale_element_page.go_to_edit_presale()
        create_presale_page.form_edit_presale(old_user_data_dict, new_user_data_dict)
        presale_list_page.go_to_mine_elements_tabs()
        presale_list_page.should_be_element_on_presale_list(new_user_data_dict)
        presale_list_page.go_to_presale_element(new_user_data_dict)
        presale_element_page.verify_general_information_in_presale(new_user_data_dict)
        presale_element_page.verify_presale_not_require_status_approval()