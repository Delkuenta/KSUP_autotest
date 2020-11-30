import pytest
from pages.base_page import BasePage
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_element_page import ContractElementPage
from pages.contract_list_page import ContractPage
from pages.presale_element_page import PresaleElementPage
from pages.presale_list_page import PresalePage
from pages.zakup_create_form_page import ZakupFormCreate
from pages.zakup_element_page import ZakupElementPage
from pages.login_data import LoginData
from pages.presale_create_form_page import PresaleFormCreate
from pages.zakup_list_page import ZakupListPage


r"""
SeparateSale\Seller - Seller2
1[Atest_Seller] PA+ZP+DK, Tender, categoryA,  SoftwareDev, SeparateSale.json
2[Atest_Seller] PA+ZP+DK, CommercialOffer, categoryA, SoftwareDev, SeparateSale.json
3[Atest_Seller] PA+ZP+DK, RequestPrice, categoryA, softwareDev, SeparateSale.json
4[Atest_Seller2] PA+ZP+DK, Tender, categoryA,  SoftwareDev, SeparateSale.json
5[Atest_Seller2] PA+ZP+DK, CommercialOffer, categoryA, SoftwareDev, SeparateSale.json
6[Atest_Seller2] PA+ZP+DK, RequestPrice, categoryA, softwareDev, SeparateSale.json

SeparateSale\Dir - Dir2
1[Atest_Dir] PA+ZP+DK, Tender, categoryA,  SoftwareDev, SeparateSale.json
2[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryA, SoftwareDev, SeparateSale.json
3[Atest_Dir] PA+ZP+DK, RequestPrice, categoryA, softwareDev, SeparateSale.json
4[Atest_Dir2] PA+ZP+DK, Tender, categoryA,  SoftwareDev, SeparateSale.json
5[Atest_Dir2] PA+ZP+DK, CommercialOffer, categoryA, SoftwareDev, SeparateSale.json
6[Atest_Dir2] PA+ZP+DK, RequestPrice, categoryA, softwareDev, SeparateSale.json
"""

# До первой ошибки --maxfail=1
@pytest.mark.parametrize('path_data_file', [
    r"TPAC\SeparateSale\Seller - Seller2\1[Atest_Seller] PA+ZP+DK, Tender, categoryA,  SoftwareDev, SeparateSale.json"])
class TestSeparateSaleFullBusinessCyclePaZpDk:

    def test_create_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        print(user_data_dict)
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
        create_presale_page.form_create_presale_all_type(user_data_dict)
        presale_list_page.go_to_sent_elements_tabs()
        presale_list_page.verify_approval_status_in_presale_list()
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_presale_approval_waiting_status()
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        login_page.logout()

    def test_approval_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
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
        presale_list_page.go_to_approval_elements_tabs()
        presale_list_page.verify_approval_status_in_presale_list()
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.approval_presale(user_data_dict)
        presale_element_page.verify_presale_approval_successfully_status()
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        login_page.logout()

    def test_verify_visibility_zakup_button_salesManager(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller2")
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_visibility_button_create_contract_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_commercial_offer_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_presale_act_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_tender_based_on_presale()

    def test_verify_visibility_zakup_button_salesUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir2")
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_visibility_button_create_contract_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_commercial_offer_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_presale_act_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_tender_based_on_presale()
        login_page.logout()

    def test_verify_visibility_zakup_button_executiveUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir")
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_visibility_button_create_contract_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_commercial_offer_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_presale_act_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_tender_based_on_presale()
        login_page.logout()

    def test_verify_visibility_zakup_button_executiveManager(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        presale_list_page = PresalePage(browser_function, link)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, link)
        presale_element_page.verify_visibility_button_create_contract_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_commercial_offer_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_presale_act_based_on_presale()
        presale_element_page.verify_visibility_button_create_zp_tender_based_on_presale()
        login_page.logout()

    def test_create_zakup_based_on_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        presale_list_page = PresalePage(browser_function, browser_function.current_url)
        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser_function, browser_function.current_url)
        presale_element_page.go_to_create_zp_based_on_presale(user_data_dict)
        zakup_form_create_page = ZakupFormCreate(browser_function, browser_function.current_url)
        zakup_form_create_page.form_create_zakup_all_type_based_on_presale(user_data_dict)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_draft_status_zakup()
        login_page.logout()

    def test_verify_visibility_zp_approval_button_salesManager(self, browser_function, path_data_file):
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
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_approval_button_zp()
        login_page.logout()

    def test_verify_visibility_zp_approval_button_salesUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir2")
        zakup_list_page = ZakupListPage(browser_function, link)
        zakup_list_page.go_to_zakup_list(link)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, link)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_approval_button_zp()
        login_page.logout()

    def test_verify_visibility_zp_approval_button_executiveUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir")
        zakup_list_page = ZakupListPage(browser_function, link)
        zakup_list_page.go_to_zakup_list(link)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, link)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_approval_button_zp()
        login_page.logout()

    def test_verify_visibility_zp_approval_button_executiveManager(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        zakup_list_page = ZakupListPage(browser_function, link)
        zakup_list_page.go_to_zakup_list(link)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, link)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_approval_button_zp()
        login_page.logout()

    def test_send_zakup_for_approval(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.send_zakup_for_approval()
        if user_data_dict["contractorType"] == "Тендерная заявка":
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
        elif user_data_dict["contractorType"] != "Тендерная заявка" \
                and user_data_dict["priceCategory"] != "C" \
                and user_data_dict["groupTypeWork"] == "Software":
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            zakup_element_page.verify_zakup_not_require_status_approval()
        login_page.logout()

    def test_approval_zakup_for_legal(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup_legal()
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_approval_zakup_for_count(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup_count()
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_approval_zakup_for_fin(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Fin")
            login_page.verify_username("Mr_KSUP_Fin")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup_fin()
            zakup_element_page.verify_zakup_successfully_status_approval_fin(user_data_dict)
            if user_data_dict["groupTypeWork"] == "Software" \
                    and user_data_dict["priceCategory"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif user_data_dict["groupTypeWork"] == "Other" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_approval_zakup_for_udprpo(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" \
                and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup_udprpo()
            zakup_element_page.verify_zakup_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_approval_zakup_for_kkp(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка" \
                and user_data_dict["priceCategory"] == "A":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup_kkp()
            zakup_element_page.verify_zakup_successfully_status_approval_kkp(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой ККП не требуется")

    def test_verify_visibility_create_contract_button_salesManager(self, browser_function, path_data_file):
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
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_button_create_contract()
        login_page.logout()

    def test_verify_visibility_create_contract_button_salesUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir2")
        zakup_list_page = ZakupListPage(browser_function, link)
        zakup_list_page.go_to_zakup_list(link)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, link)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_button_create_contract()
        login_page.logout()

    def test_verify_visibility_create_contract_button_executiveUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir")
        zakup_list_page = ZakupListPage(browser_function, link)
        zakup_list_page.go_to_zakup_list(link)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, link)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_button_create_contract()
        login_page.logout()

    def test_verify_visibility_create_contract_button_executiveManager(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        zakup_list_page = ZakupListPage(browser_function, link)
        zakup_list_page.go_to_zakup_list(link)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, link)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_visibility_button_create_contract()
        login_page.logout()

    def test_create_contract_based_on_zakup(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.go_to_create_contract_based_on_zp()
        contract_form_create = ContractFormCreate(browser_function, browser_function.current_url)
        contract_form_create.form_create_contract_based_on_zakup(user_data_dict)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)
        login_page.logout()

    def test_verify_visibility_contract_approval_button_salesManager(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller2")
        contract_list_page = ContractPage(browser_function, link)
        contract_list_page.go_to_contract_list(link)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, link)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_visibility_button_send_to_approval_contract()
        login_page.logout()

    def test_verify_visibility_contract_approval_button_salesUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir2")
        contract_list_page = ContractPage(browser_function, link)
        contract_list_page.go_to_contract_list(link)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, link)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_visibility_button_send_to_approval_contract()
        login_page.logout()

    def test_verify_visibility_contract_approval_button_executiveUnit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Dir")
        contract_list_page = ContractPage(browser_function, link)
        contract_list_page.go_to_contract_list(link)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, link)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_visibility_button_send_to_approval_contract()
        login_page.logout()

    def test_verify_visibility_contract_approval_button_executiveManager(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Seller")
        contract_list_page = ContractPage(browser_function, link)
        contract_list_page.go_to_contract_list(link)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, link)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_visibility_button_send_to_approval_contract()
        login_page.logout()

    def test_send_contract_for_approval(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.send_contract_for_approval()
        contract_element_page.verify_contract_waiting_status_approval_legal()
        login_page.logout()

    def test_approval_contract_for_legal(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()
        login_page.logout()

    def test_approval_contract_for_count(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract_count()
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()
        login_page.logout()

    def test_approval_contract_for_fin(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract_fin()
        contract_element_page.verify_contract_successfully_status_approval_fin()
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif user_data_dict["groupTypeWork"] == "Other" \
                and user_data_dict["priceCategory"] == "A" \
                and user_data_dict["contractorType"] != "Тендерная заявка":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.logout()

    def test_approval_contract_for_udprpo(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" \
                and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract_udprpo()
            contract_element_page.verify_contract_successfully_status_approval_udprpo()
            if user_data_dict["contractorType"] != "Тендерная заявка" \
                    and user_data_dict["priceCategory"] == "A":
                contract_element_page.verify_contract_waiting_status_approval_kkp()
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой УДПР ПО не требуется")

    def test_approval_contract_for_kkp(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] != "Тендерная заявка" \
                and user_data_dict["priceCategory"] == "A":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract_kkp()
            contract_element_page.verify_contract_successfully_status_approval_kkp()
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой ККП не требуется")