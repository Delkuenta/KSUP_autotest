import pytest

from pages.base_page import BasePage
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_element_page import ContractElementPage
from pages.contract_list_page import ContractPage

from pages.login_data import LoginData


# До первой ошибки --maxfail=1
@pytest.mark.parametrize('path_data_file', [r"TPAC\RejectApproval\3_[Atest_Seller] Reject DK, categoryA, softwareDev.json"])
class TestRejectEscalationContract:

    def test_create_contract(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_contract_list(link)
        contract_page = ContractPage(browser_function, browser_function.current_url)
        contract_page.go_to_create_contract()
        create_contract_page = ContractFormCreate(browser_function, link)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)
        login_page.logout()

    def test_send_contract_for_approval_cycle1(self, browser_function, path_data_file):
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

    def test_reject_contract_for_legal_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.reject_contract_legal()
        contract_element_page.verify_contract_reject_status_approval_leagal()
        login_page.logout()

    def test_send_contract_for_approval_cycle2(self, browser_function, path_data_file):
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

    def test_approval_contract_for_legal_cycle2(self, browser_function, path_data_file):
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

    def test_reject_contract_for_count_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.reject_contract_count()
        contract_element_page.verify_contract_reject_status_approval_count()
        login_page.logout()

    def test_send_contract_for_approval_cycle3(self, browser_function, path_data_file):
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

    def test_approval_contract_for_legal_cycle3(self, browser_function, path_data_file):
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

    def test_approval_contract_for_count_cycle3(self, browser_function, path_data_file):
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

    def test_reject_contract_for_fin_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.reject_contract_fin()
        contract_element_page.verify_contract_reject_status_approval_fin()
        login_page.logout()

    def test_send_contract_for_approval_cycle4(self, browser_function, path_data_file):
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

    def test_approval_contract_for_legal_cycle4(self, browser_function, path_data_file):
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

    def test_approval_contract_for_count_cycle4(self, browser_function, path_data_file):
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

    def test_approval_contract_for_fin_cycle4(self, browser_function, path_data_file):
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

    def test_reject_contract_for_udprpo_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_UDPRPO")
        login_page.verify_username("Mr_KSUP_UDPRPO")
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.reject_contract_udprpo()
        contract_element_page.verify_contract_reject_status_approval_udprpo()
        login_page.logout()

    def test_send_contract_for_escalate_on_kkp_cycle5(self, browser_function, path_data_file):
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
        contract_element_page.escalate_contract_on_kkp()
        contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.logout()

    def test_send_contract_for_revision_from_kkp_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_KKP")
        login_page.verify_username("Mr_KSUP_KKP")
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.revision_contract_from_kkp()
        contract_element_page.verify_contract_revision_status_approval_kkp()
        login_page.logout()

    def test_send_contract_for_approval_cycle6(self, browser_function, path_data_file):
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

    def test_approval_contract_for_legal_cycle6(self, browser_function, path_data_file):
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

    def test_approval_contract_for_count_cycle6(self, browser_function, path_data_file):
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

    def test_approval_contract_for_fin_cycle6(self, browser_function, path_data_file):
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

    def test_approval_contract_for_udprpo_cycle6(self, browser_function, path_data_file):
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

    def test_reject_contract_for_kkp_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_KKP")
        login_page.verify_username("Mr_KSUP_KKP")
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.reject_contract_kkp()
        contract_element_page.verify_contract_reject_status_approval_kkp()
        login_page.logout()

    def test_unvisibility_approval_button(self, browser_function, path_data_file):
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
        contract_element_page.verify_unvisibility_approval_button()
        login_page.logout()
