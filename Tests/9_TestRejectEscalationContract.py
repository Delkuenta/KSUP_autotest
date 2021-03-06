import pytest
from pages.base_page import BasePage
from pages.Contract.contract_create_form_page import ContractFormCreate
from pages.Contract.contract_element_page import ContractElementPage
from pages.Contract.contract_list_page import ContractPage
from pages.login_data import LoginData
import delayed_assert

# До первой ошибки --maxfail=1
from userdata.user_data import UserData


# 3_[Atest_Seller] Reject DK, categoryA, softwareDev.json
# 4_[Atest_Dir] Reject DK, categoryA, softwareDev.json

@pytest.mark.parametrize('path_data_file',
                         [r"PPAC\7_RejectApproval\3_[Atest_Seller2] Reject DK, categoryA, softwareDev.json"])
class TestRejectStepBackContract:

    def test_create_contract(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        delayed_assert.assert_expectations()

    # Цикл 0
    def test_send_contract_for_approval_cycle0(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_department_head()
        contract_element_page.withdraw_zakup(UserData.comment_withdraw)
        contract_element_page.verify_contract_withdraw_status_approval()
        login_page.logout()

    # Цикл 1
    def test_send_contract_for_approval_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_department_head()
        login_page.logout()

    def test_reject_contract_for_department_head_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            if user_data_dict["createAccount"] == "Mr_KSUP_Seller":
                login_page.login("Mr_KSUP_Dir")
                login_page.verify_username("Mr_KSUP_Dir")
            else:
                login_page.login("Mr_KSUP_Dir2")
                login_page.verify_username("Mr_KSUP_Dir2")
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_approval_head_dept_tab()
            # contract_list_page.go_to_allmydepartment_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.verify_general_information_contract(user_data_dict)
            contract_element_page.reject_contract(UserData.comment_reject_depatment_head,
                                                  UserData.file_path_for_link_pdf,
                                                  "Согласование с руководителем подразделения")
            contract_element_page.verify_contract_reject_status_approval_department_head()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя подразделения не требуется")

    # Цикл 2
    def test_send_contract_for_approval_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_department_head()
        login_page.logout()

    def test_approval_contract_for_department_head_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            if user_data_dict["createAccount"] == "Mr_KSUP_Seller":
                login_page.login("Mr_KSUP_Dir")
                login_page.verify_username("Mr_KSUP_Dir")
                department_head = "Mr_KSUP_Dir"
            else:
                login_page.login("Mr_KSUP_Dir2")
                login_page.verify_username("Mr_KSUP_Dir2")
                department_head = "Mr_KSUP_Dir2"
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_approval_head_dept_tab()
            # contract_list_page.go_to_allmydepartment_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract(UserData.comment_approval_legal, UserData.file_path_for_link_jpg)
            contract_element_page.verify_general_information_contract(user_data_dict)
            contract_element_page.verify_contract_successfully_status_approval_department_head()
            contract_element_page.verify_contract_waiting_status_approval_legal()
        else:
            print("\nВнутреннее согласование договор/контракта за Руководителя подразделения не требуется")

    def test_reject_contract_for_legal_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_legal, UserData.file_path_for_link_excel,
                                              "Согласование с руководителем подразделения")
        contract_element_page.verify_contract_reject_status_approval_legal()
        login_page.logout()

    # Цикл 3
    def test_send_contract_for_approval_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_department_head()
        login_page.logout()

    def test_approval_contract_for_department_head_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            if user_data_dict["createAccount"] == "Mr_KSUP_Seller":
                login_page.login("Mr_KSUP_Dir")
                login_page.verify_username("Mr_KSUP_Dir")
                department_head = "Mr_KSUP_Dir"
            else:
                login_page.login("Mr_KSUP_Dir2")
                login_page.verify_username("Mr_KSUP_Dir2")
                department_head = "Mr_KSUP_Dir2"
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_approval_head_dept_tab()
            # contract_list_page.go_to_allmydepartment_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract(UserData.comment_approval_legal, UserData.file_path_for_link_jpg)
            contract_element_page.verify_general_information_contract(user_data_dict)
            contract_element_page.verify_contract_successfully_status_approval_department_head()
            contract_element_page.verify_contract_waiting_status_approval_legal()
        else:
            print("\nВнутреннее согласование договор/контракта за Руководителя подразделения не требуется")

    def test_approval_contract_for_legal_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_legal, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_count_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_count, UserData.file_path_for_link_jpg,
                                              "Согласование юридической службой")
        contract_element_page.verify_contract_reject_status_approval_count()
        login_page.logout()

    # Цикл 4
    def test_send_contract_for_approval_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_legal, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_count_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        # contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_count, UserData.file_path_for_link_doc)
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()
        contract_element_page.verify_contract_waiting_status_approval_audit()
        # login_page.go_to_contract_list(link)
        # contract_list_page.go_to_approved_elements_tab()
        # contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_fin_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_fin, UserData.file_path_for_link_excel,
                                              "Согласование бухгалтерией")
        contract_element_page.verify_contract_reject_status_approval_fin()
        login_page.logout()

    # Цикл 5
    def test_send_contract_for_approval_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_count()
        login_page.logout()

    def test_approval_contract_for_count_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        # contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_count, UserData.file_path_for_link_doc)
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()
        # login_page.go_to_contract_list(link)
        # contract_list_page.go_to_approved_elements_tab()
        # contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_fin_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
        contract_element_page.verify_contract_successfully_status_approval_fin(user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif user_data_dict["groupTypeWork"] == "Other" \
                and user_data_dict["priceCategory"] == "A" \
                and user_data_dict["contractorType"] != "Тендерная заявка":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_udprpo_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_udprpo, UserData.file_path_for_link_excel,
                                              "Согласование финансовой службой")
        contract_element_page.verify_contract_reject_status_approval_udprpo()
        login_page.logout()

    # Цикл 7
    def test_send_contract_for_approval_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_fin()
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_contract_for_fin_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
        contract_element_page.verify_contract_successfully_status_approval_fin(user_data_dict)
        contract_element_page.verify_contract_waiting_status_approval_audit()
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif user_data_dict["groupTypeWork"] == "Other" \
                and user_data_dict["priceCategory"] == "A" \
                and user_data_dict["contractorType"] != "Тендерная заявка":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_udprpo_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_approval_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract(UserData.comment_approval_udprpo, UserData.file_path_for_link_jpg)
            contract_element_page.verify_contract_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
                contract_element_page.verify_contract_waiting_status_approval_audit()
            login_page.go_to_contract_list(link)
            contract_list_page.go_to_approved_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой УДПР ПО не требуется")

    def test_reject_contract_for_audit_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.reject_contract(UserData.comment_reject_audit, UserData.file_path_for_link_jpg, "Согласование Директором по разработке ПО")
        contract_element_page.verify_contract_reject_status_approval_audit()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    # Цикл 7
    def test_send_contract_for_approval_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_udprpo()
        login_page.logout()

    def test_approval_contract_for_udprpo_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_approval_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract(UserData.comment_approval_udprpo, UserData.file_path_for_link_jpg)
            contract_element_page.verify_contract_successfully_status_approval_udprpo(user_data_dict)
            contract_element_page.verify_contract_waiting_status_approval_audit()
            login_page.go_to_contract_list(link)
            contract_list_page.go_to_approved_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой УДПР ПО не требуется")

    def test_approval_contract_for_audit_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        if user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_revision_contract_for_kkp_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.revision_contract_from_kkp(UserData.comment_revision_kkp, "Согласование ККП")
        contract_element_page.verify_contract_revision_status_approval_kkp()
        login_page.logout()

    # Цикл 8
    def test_send_contract_for_approval_cycle8(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_audit()

    def test_approval_contract_for_audit_cycle8(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        if user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_kkp_cycle8(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract_kkp(UserData.comment_reject_kkp, UserData.file_path_for_link_mp4)
        contract_element_page.verify_contract_reject_status_approval_kkp()
        login_page.logout()

    def test_unvisibility_send_approval_button(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_unvisibility_send_approval_button()
        login_page.logout()



@pytest.mark.parametrize('path_data_file',
                         [r"TPAC\7_RejectApproval\4_[Atest_Dir] Reject DK, categoryA, softwareDev.json"])
class TestRejectCurrentStepAndEscalationContract:

    def test_create_contract(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        delayed_assert.assert_expectations()

    # Цикл 0
    def test_send_contract_for_approval_cycle0(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_audit()
        contract_element_page.withdraw_zakup(UserData.comment_withdraw)
        contract_element_page.verify_contract_withdraw_status_approval()
        login_page.logout()

    # Цикл 1
    def test_send_contract_for_approval_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_contract_for_audit_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        #contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        contract_element_page.verify_contract_waiting_status_approval_legal()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_legal_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_legal, UserData.file_path_for_link_excel,
                                              "Согласование юридической службой")
        contract_element_page.verify_contract_reject_status_approval_legal()
        login_page.logout()

    # Цикл 2
    def test_send_contract_for_approval_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_contract_for_audit_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        contract_element_page.verify_contract_waiting_status_approval_legal()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_legal_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_legal, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_count_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_count, UserData.file_path_for_link_jpg,
                                              "Согласование бухгалтерией")
        contract_element_page.verify_contract_reject_status_approval_count()
        login_page.logout()

    # Цикл 3
    def test_send_contract_for_approval_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_contract_for_audit_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        contract_element_page.verify_contract_waiting_status_approval_count()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_count_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        # contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_count, UserData.file_path_for_link_doc)
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()
        # login_page.go_to_contract_list(link)
        # contract_list_page.go_to_approved_elements_tab()
        # contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_fin_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_fin, UserData.file_path_for_link_excel,
                                              "Согласование финансовой службой")
        contract_element_page.verify_contract_reject_status_approval_fin()
        login_page.logout()

    # Цикл 4
    def test_send_contract_for_approval_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_fin()
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_contract_for_audit_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        contract_element_page.verify_contract_waiting_status_approval_fin()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_fin_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
        contract_element_page.verify_contract_successfully_status_approval_fin(user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif user_data_dict["groupTypeWork"] == "Other" \
                and user_data_dict["priceCategory"] == "A" \
                and user_data_dict["contractorType"] != "Тендерная заявка":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_udprpo_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract(UserData.comment_reject_udprpo, UserData.file_path_for_link_excel,
                                              "Согласование Директором по разработке ПО")
        contract_element_page.verify_contract_reject_status_approval_udprpo()
        login_page.logout()

    # Цикл 5
    def test_escalate_contract_on_kkp_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_contract_for_audit_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_revision_contract_for_kkp_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.revision_contract_from_kkp(UserData.comment_revision_kkp,
                                                         "Согласование Директором по разработке ПО")
        contract_element_page.verify_contract_revision_status_approval_kkp()
        login_page.logout()

    # Цикл 6
    def test_send_contract_for_approval_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_contract_waiting_status_approval_udprpo()
        contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_contract_for_udprpo_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_contract_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_approval_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract(UserData.comment_approval_udprpo, UserData.file_path_for_link_jpg)
            contract_element_page.verify_contract_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
                contract_element_page.verify_contract_waiting_status_approval_audit()
            login_page.go_to_contract_list(link)
            contract_list_page.go_to_approved_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой УДПР ПО не требуется")

    def test_approval_contract_for_audit_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_contract_list(link)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_audit()
        contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_reject_contract_for_kkp_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.reject_contract_kkp(UserData.comment_reject_kkp, UserData.file_path_for_link_mp4)
        contract_element_page.verify_contract_reject_status_approval_kkp()
        login_page.logout()

    def test_unvisibility_send_approval_button(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.verify_unvisibility_send_approval_button()
        login_page.logout()
