import pytest
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_element_page import ContractElementPage
from pages.contract_list_page import ContractPage
from userdata.user_data import UserData
from pages.login_data import LoginData


class TestDkFullBusinessCycle:

    def test_create_contract(self, browser):
        print(UserData.user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_contract_list()
        contract_page = ContractPage(browser, browser.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser, link)
        create_contract_page.form_create_contract()
        contract_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.verify_general_information_contract()

    def test_send_contract_for_approval(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login(UserData.user_data_dict["create_account"])
        login_page.verify_username(UserData.user_data_dict["create_account"])
        login_page.go_to_contract_list()
        contract_list = ContractPage(browser, browser.current_url)
        contract_list.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.send_contract_for_approval()
        contract_element_page.verify_contract_waiting_status_approval_legal()

    def test_approval_contract_for_legal(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()

    def test_approval_contract_for_count(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_count()
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()

    def test_approval_contract_for_fin(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_fin()
        contract_element_page.verify_contract_successfully_status_approval_fin()
        if UserData.user_data_dict["groupTypeWork"] == "Software" and UserData.user_data_dict["price_category"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif UserData.user_data_dict["groupTypeWork"] == "Other" \
                and UserData.user_data_dict["price_category"] == "A" \
                and UserData.user_data_dict["contractorType"] != "Тендерная заявка":
            contract_element_page.verify_contract_waiting_status_approval_kkp()

    def test_approval_contract_for_udprpo(self, browser):
        if UserData.user_data_dict["groupTypeWork"] == "Software" \
                and UserData.user_data_dict["price_category"] != "C":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_contract_list()
            contract_list_page = ContractPage(browser, browser.current_url)
            contract_list_page.go_to_contract_element()
            contract_element_page = ContractElementPage(browser, browser.current_url)
            contract_element_page.approval_contract_udprpo()
            contract_element_page.verify_contract_successfully_status_approval_udprpo()
            if UserData.user_data_dict["contractorType"] != "Тендерная заявка" \
                    and UserData.user_data_dict["price_category"] == "A":
                contract_element_page.verify_contract_waiting_status_approval_kkp()
        else:
            print("\nВнутреннее согласование контракта со службой УДПР ПО не требуется")

    def test_approval_contract_for_kkp(self, browser):
        if UserData.user_data_dict["contractorType"] != "Тендерная заявка" \
                and UserData.user_data_dict["price_category"] == "A":
            link = LoginData.link
            login_page = LoginData(browser, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_contract_list()
            contract_list_page = ContractPage(browser, browser.current_url)
            contract_list_page.go_to_contract_element()
            contract_element_page = ContractElementPage(browser, browser.current_url)
            contract_element_page.approval_contract_kkp()
            contract_element_page.verify_contract_successfully_status_approval_kkp()
        else:
            print("\nВнутреннее согласование контракта со службой ККП не требуется")