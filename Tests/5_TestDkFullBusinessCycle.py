import delayed_assert
import pytest

from pages.base_page import BasePage
from pages.Contract.contract_create_form_page import ContractFormCreate
from pages.Contract.contract_element_page import ContractElementPage
from pages.Contract.contract_list_page import ContractPage
from pages.login_data import LoginData
from userdata.user_data import UserData

r"""
19_[Atest_Seller] DK, categoryA, softwareDev.json
20_[Atest_Seller] DK, categoryB, softwareDev.json
21_[Atest_Seller] DK, categoryC, softwareDev.json
22_[Atest_Seller] DK, categoryA, OtherType.json
23_[Atest_Seller] DK, categoryB, OtherType.json
24_[Atest_Seller] DK, categoryC, OtherType.json

UnitSale\Dir
19_[Atest_Dir] DK, categoryA, softwareDev.json


UnitSale\Seller2
19_[Atest_Seller2] DK, categoryA, softwareDev.json
20_[Atest_Seller2] DK, categoryB, softwareDev.json
"""


# До первой ошибки --maxfail=1
@pytest.mark.parametrize('path_data_file', [
    r"TPAC\3_UnitSale\Dir\19_[Atest_Dir] DK, categoryA, softwareDev.json"

])
class TestDkFullBusinessCycle:

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
        # Проверяем предзаполнения менеджеров Баг https://jira.lanit.ru/browse/KSUP-1041
        # create_contract_page.verify_prefill_department_manager(user_data_dict)
        create_contract_page.form_create_contract(user_data_dict)
        contract_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_payments_information_in_presale(user_data_dict)
        login_page.logout()
        delayed_assert.assert_expectations()

    def test_send_contract_for_approval(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_contract_list(link)
        contract_list = ContractPage(browser_function, browser_function.current_url)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            contract_list.go_to_mine_elements_tab()
        else:
            contract_list.go_to_allmydepartment_tab()
        contract_list.should_be_element_on_contract_list(user_data_dict)
        contract_list.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        user_data_dict = contract_element_page.attribute_approval_with_dept_head(user_data_dict)
        BasePage.load_file_json(browser_function, path_data_file, user_data_dict)
        contract_element_page.send_contract_for_approval()
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_attached_files_information()
        if user_data_dict["createAccount"] == "Mr_KSUP_Dir" or user_data_dict["createAccount"] == "Mr_KSUP_Dir2":
            if user_data_dict["divisionHeadApproves"] == "Да":
                contract_element_page.verify_contract_successfully_status_approval_department_head()
            contract_element_page.verify_contract_waiting_status_approval_legal()
            contract_element_page.verify_contract_waiting_status_approval_audit()
        else:
            if user_data_dict["divisionHeadApproves"] == "Да":
                contract_element_page.verify_contract_waiting_status_approval_department_head()

        # Добавление файла бюджета возможные названия файла test_jpg.jpg, test_doc.docx, test_excel.xlsx, test_video.mp4, test_pdf.pdf
        contract_element_page.verify_visibility_budget_button()
        contract_element_page.add_file_of_budget("test_jpg.jpg")
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_attached_files_information()
        contract_element_page.verify_attached_budget_files("test_jpg.jpg")
        login_page.logout()
        delayed_assert.assert_expectations()

    def test_approval_contract_for_department_head(self, browser_function, path_data_file):

        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["divisionHeadApproves"] == "Да":
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
                contract_element_page.approval_contract(UserData.comment_approval_depatment_head, UserData.file_path_for_link_jpg)
                contract_element_page.verify_general_information_contract(user_data_dict)
                contract_element_page.verify_contract_successfully_status_approval_department_head()
                contract_element_page.verify_contract_waiting_status_approval_legal()
                contract_element_page.verify_contract_waiting_status_approval_audit()
            else:
                print("\nВнутреннее согласование договор/контракта за Руководителя подразделения не требуется")
        else:
            print("\nВнутреннее согласование договор/контракта за Руководителя подразделения не требуется "
                  "из-за отключения этапа согласования с руководителем подразделения")

    """
    def test_approval_contract_for_egrulhead(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)

        if ((user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Dir")
            and UserData.egrulHead["Mr_KSUP_Dir"] != user_data_dict["executiveUnitLegal"]) or \
                ((user_data_dict["createAccount"] == "Mr_KSUP_Seller2" or user_data_dict[
                    "createAccount"] == "Mr_KSUP_Dir2")
                 and UserData.egrulHead["Mr_KSUP_Dir2"] != user_data_dict["executiveUnitLegal"]):

            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            # Определяем руководителя по значению юр.лица-исполнителя в словаре
            account_name = {value: key for key, value in UserData.egrulHead.items()}[
                user_data_dict["executiveUnitLegal"]]
            login_page.login(account_name)
            login_page.verify_username(account_name)
            login_page.go_to_contract_egrul_list(link)
            contract_list_page = ContractPage(browser_function, browser_function.current_url)
            contract_list_page.go_to_approval_head_egrul_tab()
            # contract_list_page.go_to_allmyegrul_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract(UserData.comment_approval_depatment_head,
                                                    UserData.file_path_for_link_pdf)
            contract_element_page.verify_general_information_contract(user_data_dict)
            contract_element_page.verify_contract_successfully_status_approval_egrulhead()
            contract_element_page.verify_contract_waiting_status_approval_legal()
        else:
            print("\nВнутреннее согласование договор/контракта за Руководителя юр.лица/ИП не требуется")
    """

    def test_approval_contract_for_legal(self, browser_function, path_data_file):
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

    def test_approval_contract_for_count(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.approval_contract(UserData.comment_approval_count, UserData.file_path_for_link_jpg)
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()
        login_page.logout()

    def test_approval_contract_for_fin(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        contract_element_page.approval_contract(UserData.comment_approval_fin, UserData.file_path_for_link_doc)
        contract_element_page.verify_contract_successfully_status_approval_fin(user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif user_data_dict["groupTypeWork"] == "Other" \
                and user_data_dict["priceCategory"] == "A":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.logout()

    def test_approval_contract_for_udprpo(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
            contract_element_page.approval_contract(UserData.comment_approval_udprpo, UserData.file_path_for_link_mp4)
            contract_element_page.verify_contract_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["priceCategory"] == "A":
                contract_element_page.verify_contract_waiting_status_approval_kkp()
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой УДПР ПО не требуется")

    def test_approval_contract_for_audit(self, browser_function, path_data_file):
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
        if user_data_dict["priceCategory"] == "A":
            contract_element_page.verify_contract_waiting_status_approval_kkp()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_kkp(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
            contract_element_page.approval_contract(UserData.comment_approval_kkp, UserData.file_path_for_link_excel)
            contract_element_page.verify_contract_successfully_status_approval_kkp(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой ККП не требуется")
