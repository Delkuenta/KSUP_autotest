import pytest
from pages.presale_element_page import PresaleElementPage
from pages.presale_list_page import PresalePage
from pages.zakup_create_form_page import ZakupFormCreate
from pages.zakup_element_page import ZakupElementPage
from userdata.user_data import UserData
from pages.login_data import LoginData
from pages.presale_create_form_page import PresaleFormCreate
from pages.zakup_list_page import ZakupListPage


class TestRejectEscalationZakup:

    def test_create_presale(self, browser):
        print(UserData.user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        presale_list_page = PresalePage(browser, link)
        presale_list_page.go_to_presale_list()
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page = PresaleFormCreate(browser, link)
        create_presale_page.form_create_presale_all_type()
        presale_list_page.should_be_element_on_presale_list()

    def test_create_zakup_based_on_presale(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        presale_list_page = PresalePage(browser, browser.current_url)
        presale_list_page.go_to_presale_list()
        presale_list_page.should_be_element_on_presale_list()
        presale_list_page.go_to_presale_element()
        presale_element_page = PresaleElementPage(browser, browser.current_url)
        presale_element_page.go_to_create_zp_based_on_presale()
        zakup_form_create_page = ZakupFormCreate(browser, browser.current_url)
        zakup_form_create_page.form_create_zakup_all_type()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.should_be_element_on_zakup_list()
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.verify_draft_status_zakup()

    def test_send_zakup_for_approval_cycle1(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.send_zakup_for_approval()
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
        elif UserData.user_data_dict["contractorType"] != "Тендерная заявка" \
                and UserData.user_data_dict["price_category"] != "C" \
                and UserData.user_data_dict["groupTypeWork"] == "Software":
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            zakup_element_page.verify_zakup_not_require_status_approval()

    def test_reject_zakup_for_legal_cycle1(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.reject_zakup_legal()
        zakup_element_page.verify_zakup_reject_status_approval_legal()

    def test_send_zakup_for_approval_cycle2(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.send_zakup_for_approval()
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
        elif UserData.user_data_dict["contractorType"] != "Тендерная заявка" \
                and UserData.user_data_dict["price_category"] != "C" \
                and UserData.user_data_dict["groupTypeWork"] == "Software":
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            zakup_element_page.verify_zakup_not_require_status_approval()

    def test_approval_zakup_for_legal_cycle2(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_legal()
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_reject_zakup_for_count_cycle2(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.reject_zakup_count()
        zakup_element_page.verify_zakup_reject_status_approval_count()

    def test_send_zakup_for_approval_cycle3(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.send_zakup_for_approval()
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
        elif UserData.user_data_dict["contractorType"] != "Тендерная заявка" \
                and UserData.user_data_dict["price_category"] != "C" \
                and UserData.user_data_dict["groupTypeWork"] == "Software":
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            zakup_element_page.verify_zakup_not_require_status_approval()

    def test_approval_zakup_for_legal_cycle3(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_legal()
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_approval_zakup_for_count_cycle3(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_count()
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_reject_zakup_for_fin_cycle3(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.reject_zakup_fin()
        zakup_element_page.verify_zakup_reject_status_approval_fin()

    def test_send_zakup_for_approval_cycle4(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.send_zakup_for_approval()
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
        elif UserData.user_data_dict["contractorType"] != "Тендерная заявка" \
                and UserData.user_data_dict["price_category"] != "C" \
                and UserData.user_data_dict["groupTypeWork"] == "Software":
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            zakup_element_page.verify_zakup_not_require_status_approval()

    def test_approval_zakup_for_legal_cycle4(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_legal()
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_approval_zakup_for_count_cycle4(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_count()
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_approval_zakup_for_fin_cycle4(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Fin")
            login_page.verify_username("Mr_KSUP_Fin")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_fin()
            zakup_element_page.verify_zakup_successfully_status_approval_fin()
            if UserData.user_data_dict["groupTypeWork"] == "Software" \
                    and UserData.user_data_dict["price_category"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif UserData.user_data_dict["groupTypeWork"] == "Other" \
                    and UserData.user_data_dict["price_category"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_reject_zakup_for_udprpo_cycle4(self, browser):
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.reject_zakup_udprpo()
            zakup_element_page.verify_zakup_reject_status_approval_udprpo()

    def test_send_zakup_for_escalate_on_kkp_cycle5(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.escalate_on_kkp()
        zakup_element_page.verify_zakup_waiting_status_approval_kkp()

    def test_send_zakup_for_revision_from_kkp_cycle5(self, browser):
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.revision_zakup_from_kkp()
            zakup_element_page.verify_zakup_revision_status_approval()

    def test_send_zakup_for_approval_cycle6(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.send_zakup_for_approval()
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
        elif UserData.user_data_dict["contractorType"] != "Тендерная заявка" \
                and UserData.user_data_dict["price_category"] != "C" \
                and UserData.user_data_dict["groupTypeWork"] == "Software":
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            zakup_element_page.verify_zakup_not_require_status_approval()

    def test_approval_zakup_for_legal_cycle6(self, browser):
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_legal()
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()

    def test_approval_zakup_for_count_cycle6(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_count()
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_approval_zakup_for_fin_cycle6(self, browser):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Fin")
            login_page.verify_username("Mr_KSUP_Fin")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup()
            zakup_element_page.approval_zakup_fin()
            zakup_element_page.verify_zakup_successfully_status_approval_fin()
            if UserData.user_data_dict["groupTypeWork"] == "Software" \
                    and UserData.user_data_dict["price_category"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif UserData.user_data_dict["groupTypeWork"] == "Other" \
                    and UserData.user_data_dict["price_category"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_approval_zakup_for_udprpo_cycle6(self, browser):
        if UserData.user_data_dict["groupTypeWork"] == "Software" \
                and UserData.user_data_dict["price_category"] != "C":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.approval_zakup_udprpo()
            zakup_element_page.verify_zakup_successfully_status_approval_udprpo()
            if UserData.user_data_dict["contractorType"] == "Тендерная заявка" \
                    and UserData.user_data_dict["price_category"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_reject_zakup_for_kkp_cycle6(self, browser):
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element()
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.reject_zakup_kkp()
            zakup_element_page.verify_zakup_reject_status_approval_kkp()

    def test_unvisibility_approval_button(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup()
        zakup_element_page.verify_unvisibility_approval_button()
