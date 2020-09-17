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

# UnitSale\Seller -DKS
"""
1_[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json
2_[Atest_Seller] PA+ZP+DK,Tender, categoryB, softwareDev, UnitSale.json
3_[Atest_Seller] PA+ZP+DK,Tender, categoryC, softwareDev, UnitSale.json
4_[Atest_Seller] PA+ZP+DK,Tender, categoryA, OtherType, UnitSale.json
5_[Atest_Seller] PA+ZP+DK,Tender, categoryB, OtherType, UnitSale.json
6_[Atest_Seller] PA+ZP+DK,Tender, categoryC, OtherType, UnitSale.json
7_[Аtest_Seller2] PA+ZP+DK, CommercialOffer, categoryA, softwareDev, UnitSale.json
8_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryB, softwareDev, UnitSale.json
9_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryC, softwareDev, UnitSale.json
10_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryA, OtherType, UnitSale.json
11_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryB, OtherType, UnitSale.json
12_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryC, OtherType, UnitSale.json
13_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryA, softwareDev, UnitSale.json
14_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryB, softwareDev, UnitSale.json
15_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryC, softwareDev, UnitSale.json
16_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryA, OtherType, UnitSale.json
17_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryB, OtherType, UnitSale.json
18_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryC, OtherType, UnitSale.json
"""

# UnitSale\Dir - DKS
"""
1_[Atest_Dir] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json
2_[Atest_Dir] PA+ZP+DK,Tender, categoryB, softwareDev, UnitSale.json
3_[Atest_Dir] PA+ZP+DK,Tender, categoryC, softwareDev, UnitSale.json
4_[Atest_Dir] PA+ZP+DK,Tender, categoryA, OtherType, UnitSale.json
5_[Atest_Dir] PA+ZP+DK,Tender, categoryB, OtherType, UnitSale.json
6_[Atest_Dir] PA+ZP+DK,Tender, categoryC, OtherType, UnitSale.json
7_[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryA, softwareDev, UnitSale.json
8_[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryB, softwareDev, UnitSale.json
9_[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryС, softwareDev, UnitSale.json
10_[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryA, OtherType, UnitSale.json
11_[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryB, OtherType, UnitSale.json
12_[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryC, OtherType, UnitSale.json
13_[Atest_Dir] PA+ZP+DK, RequestPrice, categoryA, softwareDev, UnitSale.json
14_[Atest_Dir] PA+ZP+DK, RequestPrice, categoryB, softwareDev, UnitSale.json
15_[Atest_Dir] PA+ZP+DK, RequestPrice, categoryC, softwareDev, UnitSale.json
16_[Atest_Dir] PA+ZP+DK, RequestPrice, categoryA, OtherType, UnitSale.json
17_[Atest_Dir] PA+ZP+DK, RequestPrice, categoryB, OtherType, UnitSale.json.json
18_[Atest_Dir] PA+ZP+DK, RequestPrice, categoryC, OtherType, UnitSale.json.json
"""

# UnitSale\Seller2 - DirGS
"""
1_[Atest_Seller2] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json
2_[Atest_Seller2] PA+ZP+DK,Tender, categoryB, softwareDev, UnitSale.json
3_[Atest_Seller2] PA+ZP+DK,Tender, categoryС, softwareDev, UnitSale.json
"""

# До первой ошибки --maxfail=1
# Браузер для запуска --browser_name=firefox
@pytest.mark.parametrize('path_data_file', [
    r"UnitSale\Dir - DKS\1_[Atest_Dir] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json"
    #r"UnitSale\Dir - DKS\7_[Atest_Dir] PA+ZP+DK, CommercialOffer, categoryA, softwareDev, UnitSale.json",
    #r"UnitSale\Dir - DKS\13_[Atest_Dir] PA+ZP+DK, RequestPrice, categoryA, softwareDev, UnitSale.json"
    ])
class TestUnitSaleFullBusinessCyclePaZpDk:
    def test_create_presale(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(user_data_dict["create_account"])
        login_page.verify_username(user_data_dict["create_account"])
        presale_list_page = PresalePage(browser, link)
        presale_list_page.go_to_presale_list()
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        create_presale_page = PresaleFormCreate(browser, link)
        create_presale_page.form_create_presale_all_type(user_data_dict)
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser, browser.current_url)
        presale_element_page.verify_general_information_in_presale(user_data_dict)

    def test_create_zakup_based_on_presale(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(user_data_dict["create_account"])
        login_page.verify_username(user_data_dict["create_account"])
        presale_list_page = PresalePage(browser, browser.current_url)
        presale_list_page.go_to_presale_list()
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page = PresaleElementPage(browser, browser.current_url)
        presale_element_page.go_to_create_zp_based_on_presale(user_data_dict)
        zakup_form_create_page = ZakupFormCreate(browser, browser.current_url)
        zakup_form_create_page.form_create_zakup_all_type(user_data_dict)
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_draft_status_zakup()

    def test_send_zakup_for_approval(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(user_data_dict["create_account"])
        login_page.verify_username(user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_draft_status_zakup()
        zakup_element_page.send_zakup_for_approval()
        if user_data_dict["contractorType"] == "Тендерная заявка":
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
        elif user_data_dict["contractorType"] != "Тендерная заявка" \
                and user_data_dict["price_category"] != "C" \
                and user_data_dict["groupTypeWork"] == "Software":
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            zakup_element_page.verify_zakup_not_require_status_approval()

    def test_approval_zakup_for_legal(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup_legal()
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_approval_zakup_for_count(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup_count()
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_approval_zakup_for_fin(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_Fin")
            login_page.verify_username("Mr_KSUP_Fin")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup_fin()
            zakup_element_page.verify_zakup_successfully_status_approval_fin(user_data_dict)
            if user_data_dict["groupTypeWork"] == "Software" \
                    and user_data_dict["price_category"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif user_data_dict["groupTypeWork"] == "Other" \
                    and user_data_dict["price_category"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_approval_zakup_for_udprpo(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["price_category"] != "C":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.approval_zakup_udprpo()
            zakup_element_page.verify_zakup_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка" \
                    and user_data_dict["price_category"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_approval_zakup_for_kkp(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка" and user_data_dict["price_category"] == "A":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_zakup_list()
            zakup_list_page = ZakupListPage(browser, browser.current_url)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser, browser.current_url)
            zakup_element_page.approval_zakup_kkp()
            zakup_element_page.verify_zakup_successfully_status_approval_kkp(user_data_dict)
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой ККП не требуется")

    def test_create_contract_based_on_zakup(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(user_data_dict["create_account"])
        login_page.verify_username(user_data_dict["create_account"])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupListPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.go_to_create_contract_based_on_zp()
        contract_form_create = ContractFormCreate(browser, browser.current_url)
        contract_form_create.form_create_contract_based_on_zakup(user_data_dict)
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)

    def test_send_contract_for_approval(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(user_data_dict["create_account"])
        login_page.verify_username(user_data_dict["create_account"])
        login_page.go_to_contract_list()
        contract_list = ContractPage(browser, browser.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.send_contract_for_approval()
        contract_element_page.verify_contract_waiting_status_approval_legal()

    def test_approval_contract_for_legal(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()

    def test_approval_contract_for_count(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_count()
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()

    def test_approval_contract_for_fin(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_fin()
        contract_element_page.verify_contract_successfully_status_approval_fin()
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["price_category"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif user_data_dict["groupTypeWork"] == "Other" \
                and user_data_dict["price_category"] == "A" \
                and user_data_dict["contractorType"] != "Тендерная заявка":
            contract_element_page.verify_contract_waiting_status_approval_kkp()

    def test_approval_contract_for_udprpo(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["price_category"] != "C":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_contract_list()
            contract_list_page = ContractPage(browser, browser.current_url)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser, browser.current_url)
            contract_element_page.approval_contract_udprpo()
            contract_element_page.verify_contract_successfully_status_approval_udprpo()
            if user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["price_category"] == "A":
                contract_element_page.verify_contract_waiting_status_approval_kkp()
        else:
            print("\nВнутреннее согласование контракта со службой УДПР ПО не требуется")

    def test_approval_contract_for_kkp(self, browser, path_data_file):
        user_data_dict = BasePage.read_json(browser, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser, user_data_dict)
        if user_data_dict["contractorType"] != "Тендерная заявка" \
                and user_data_dict["price_category"] == "A":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_contract_list()
            contract_list_page = ContractPage(browser, browser.current_url)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser, browser.current_url)
            contract_element_page.approval_contract_kkp()
            contract_element_page.verify_contract_successfully_status_approval_kkp()
        else:
            print("\nВнутреннее согласование контракта со службой ККП не требуется")
