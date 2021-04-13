import pytest
from pages.base_page import BasePage
from pages.Presale.presale_element_page import PresaleElementPage
from pages.Presale.presale_list_page import PresalePage
from pages.Zakup.zakup_create_form_page import ZakupFormCreate
from pages.Zakup.zakup_element_page import ZakupElementPage
from pages.login_data import LoginData
from pages.Presale.presale_create_form_page import PresaleFormCreate
from pages.Zakup.zakup_list_page import ZakupListPage
from userdata.user_data import UserData

"""
1_[Atest_Dir] Reject ZP,Tender, categoryA, softwareDev, UnitSale.json
1_[Atest_Seller] Reject ZP,Tender, categoryA, softwareDev, UnitSale.json
"""
# До первой ошибки --maxfail=1
@pytest.mark.parametrize('path_data_file', [
    r"TPAC\7_RejectApproval\1_[Atest_Seller] Reject ZP,Tender, categoryA, softwareDev, UnitSale.json"])
class TestRejectStepBackZakup:

    def test_create_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        login_page.logout()

    def test_create_zakup_based_on_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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

    # Цикл 0
    def test_send_and_withdraw_zakup_for_approval_cycle0(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_department_head()
        zakup_element_page.withdraw_zakup(UserData.comment_withdraw)
        zakup_element_page.verify_zakup_withdraw_status_approval()
        login_page.logout()

    # Цикл 1
    def test_send_zakup_for_approval_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_department_head()
        login_page.logout()

    def test_reject_zakup_for_department_head_cycle1(self, browser_function, path_data_file):
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
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            # zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.go_to_allmydepartment_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.reject_zakup(UserData.comment_reject_depatment_head, UserData.file_path_for_link_pdf,
                                            "Согласование с руководителем подразделения")
            zakup_element_page.verify_zakup_reject_status_approval_department_head()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя подразделения не требуется")

    # Цикл 2
    def test_send_zakup_for_approval_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_department_head()
        login_page.logout()

    def test_approval_zakup_for_department_head_cycle2(self, browser_function, path_data_file):
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
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.go_to_allmydepartment_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_depatment_head, UserData.file_path_for_link_pdf)
            zakup_element_page.verify_zakup_successfully_status_approval_department_head()
            if UserData.egrulHead[department_head] == user_data_dict["executiveUnitLegal"]:
                zakup_element_page.verify_zakup_successfully_status_approval_egrulhead(user_data_dict)
                if user_data_dict["contractorType"] == "Тендерная заявка":
                    zakup_element_page.verify_zakup_waiting_status_approval_legal()
                elif user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict[
                    "priceCategory"] != "C" and \
                        user_data_dict["groupTypeWork"] == "Software":
                    zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            else:
                zakup_element_page.verify_zakup_waiting_status_approval_egrulhead()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя подразделения не требуется")

    def test_reject_zakup_for_egrulhead_cycle2(self, browser_function, path_data_file):
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

            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.go_to_allmydepartment_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.reject_zakup(UserData.comment_reject_egrul_head, UserData.file_path_for_link_pdf,
                                            "Согласование с руководителем подразделения")
            zakup_element_page.verify_zakup_reject_status_approval_egrulhead()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя юр.лица/ИП не требуется")

    # Цикл 3
    def test_send_zakup_for_approval_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_department_head()
        login_page.logout()

    def test_approval_zakup_for_department_head_cycle3(self, browser_function, path_data_file):
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
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.go_to_allmydepartment_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_depatment_head, UserData.file_path_for_link_pdf)
            zakup_element_page.verify_zakup_successfully_status_approval_department_head()
            if UserData.egrulHead[department_head] == user_data_dict["executiveUnitLegal"]:
                zakup_element_page.verify_zakup_successfully_status_approval_egrulhead(user_data_dict)
                if user_data_dict["contractorType"] == "Тендерная заявка":
                    zakup_element_page.verify_zakup_waiting_status_approval_legal()
                elif user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict[
                    "priceCategory"] != "C" and \
                        user_data_dict["groupTypeWork"] == "Software":
                    zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            else:
                zakup_element_page.verify_zakup_waiting_status_approval_egrulhead()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя подразделения не требуется")

    def test_approval_zakup_for_egrulhead_cycle3(self, browser_function, path_data_file):
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

            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_allmyegrul_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_depatment_head, UserData.file_path_for_link_pdf)
            zakup_element_page.verify_zakup_successfully_status_approval_egrulhead(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка":
                zakup_element_page.verify_zakup_waiting_status_approval_legal()
                zakup_element_page.verify_zakup_waiting_status_approval_audit()
            elif user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] != "C" and \
                    user_data_dict["groupTypeWork"] == "Software":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя юр.лица/ИП не требуется")

    def test_reject_zakup_for_legal_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_legal, UserData.file_path_for_link_jpg, "Согласование с руководителем юр. лица/ИП")
        zakup_element_page.verify_zakup_reject_status_approval_legal()
        login_page.logout()

    # Цикл 4
    def test_send_zakup_for_approval_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_egrulhead()
        login_page.logout()

    def test_approval_zakup_for_egrulhead_cycle4(self, browser_function, path_data_file):
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

            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_allmyegrul_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_depatment_head, UserData.file_path_for_link_pdf)
            zakup_element_page.verify_zakup_successfully_status_approval_egrulhead(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка":
                zakup_element_page.verify_zakup_waiting_status_approval_legal()
                zakup_element_page.verify_zakup_waiting_status_approval_audit()
            elif user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] != "C" and \
                    user_data_dict["groupTypeWork"] == "Software":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя юр.лица/ИП не требуется")

    def test_approval_zakup_for_legal_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_legal, UserData.file_path_for_link_doc)
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_audit()
            login_page.go_to_zakup_list(link)
            #zakup_list_page.go_to_approved_elements_tab()
            #zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_reject_zakup_for_count_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_count, UserData.file_path_for_link_jpg, "Согласование юридической службой")
        zakup_element_page.verify_zakup_reject_status_approval_count()
        login_page.logout()

    # Цикл 5
    def test_send_zakup_for_approval_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_legal()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_legal_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_legal, UserData.file_path_for_link_doc)
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_audit()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_approval_zakup_for_count_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_count, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
            zakup_element_page.verify_zakup_waiting_status_approval_audit()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_reject_zakup_for_fin_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_fin, UserData.file_path_for_link_jpg, "Согласование бухгалтерией")
        zakup_element_page.verify_zakup_reject_status_approval_fin()
        login_page.logout()

    # Цикл 6
    def test_send_zakup_for_approval_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_count()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_count_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_count, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
            zakup_element_page.verify_zakup_waiting_status_approval_audit()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_approval_zakup_for_fin_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Fin")
            login_page.verify_username("Mr_KSUP_Fin")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
            zakup_element_page.verify_zakup_successfully_status_approval_fin(user_data_dict)
            zakup_element_page.verify_zakup_waiting_status_approval_audit()
            if user_data_dict["groupTypeWork"] == "Software" \
                    and user_data_dict["priceCategory"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif user_data_dict["groupTypeWork"] == "Other" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_reject_zakup_for_udprpo_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_UDPRPO")
        login_page.verify_username("Mr_KSUP_UDPRPO")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_udprpo, UserData.file_path_for_link_jpg, "Согласование финансовой службой")
        zakup_element_page.verify_zakup_reject_status_approval_udprpo()
        login_page.logout()

    # Цикл 7
    def test_send_zakup_for_approval_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_fin()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_fin_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Fin")
            login_page.verify_username("Mr_KSUP_Fin")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
            zakup_element_page.verify_zakup_successfully_status_approval_fin(user_data_dict)
            zakup_element_page.verify_zakup_waiting_status_approval_audit()
            if user_data_dict["groupTypeWork"] == "Software" \
                    and user_data_dict["priceCategory"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif user_data_dict["groupTypeWork"] == "Other" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_approval_zakup_for_udprpo_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_udprpo, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_audit()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_reject_zakup_for_audit_cycle7(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("sa_dks_ksup_audit")
        login_page.verify_username("Mr_KSUP_Audit")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_approval_elements_tab()
        zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_audit, UserData.file_path_for_link_jpg, "Согласование Директором по разработке ПО")
        zakup_element_page.verify_zakup_reject_status_approval_audit()
        login_page.go_to_zakup_list(link)
        zakup_list_page.go_to_approved_elements_tab()
        zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
        login_page.logout()

    # Цикл 8
    def test_send_zakup_for_approval_cycle8(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_udprpo_cycle8(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_udprpo, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_audit()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_approval_zakup_for_audit_cycle8(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            if user_data_dict["contractorType"] == "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_revision_zakup_for_kkp_cycle8(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_KKP")
        login_page.verify_username("Mr_KSUP_KKP")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.revision_zakup_from_kkp(UserData.comment_revision_kkp, "Согласование ККП")
        zakup_element_page.verify_zakup_revision_status_approval()
        login_page.logout()

    # Цикл 9
    def test_send_zakup_for_approval_cycle9(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_audit_cycle9(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            if user_data_dict["contractorType"] == "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_reject_zakup_for_kkp_cycle9(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_KKP")
        login_page.verify_username("Mr_KSUP_KKP")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup_from_kkp(UserData.comment_reject_kkp)
        zakup_element_page.verify_zakup_reject_status_approval_kkp()
        login_page.logout()

    def test_unvisibility_send_approval_button(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.verify_unvisibility_approval_send_button()
        login_page.logout()



@pytest.mark.parametrize('path_data_file', [
    r"TPAC\7_RejectApproval\2_[Atest_Dir] Reject ZP,Tender, categoryA, softwareDev, UnitSale.json"])
class TestRejectCurrentStepAndEscalationZakup:

    def test_create_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        login_page.logout()

    def test_create_zakup_based_on_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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

    # Цикл 0
    def test_send_and_withdraw_zakup_for_approval_cycle0(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_legal()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        zakup_element_page.withdraw_zakup(UserData.comment_withdraw)
        zakup_element_page.verify_zakup_withdraw_status_approval()
        login_page.logout()

    # Цикл 1
    def test_send_zakup_for_approval_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_legal()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_audit_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            #zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой аудита не требуется")

    def test_reject_zakup_for_legal_cycle1(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Legal")
        login_page.verify_username("Mr_KSUP_Legal")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_legal, UserData.file_path_for_link_jpg, "Согласование юридической службой")
        zakup_element_page.verify_zakup_reject_status_approval_legal()
        login_page.logout()

    # Цикл 2
    def test_send_zakup_for_approval_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_legal()
        login_page.logout()

    def test_approval_zakup_for_audit_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            zakup_element_page.verify_zakup_waiting_status_approval_legal()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой аудита не требуется")

    def test_approval_zakup_for_legal_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Legal")
            login_page.verify_username("Mr_KSUP_Legal")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_legal, UserData.file_path_for_link_doc)
            zakup_element_page.verify_zakup_successfully_status_approval_legal()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Юридическую службу не требуется")

    def test_reject_zakup_for_count_cycle2(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Count")
        login_page.verify_username("Mr_KSUP_Count")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_count, UserData.file_path_for_link_jpg, "Согласование бухгалтерией")
        zakup_element_page.verify_zakup_reject_status_approval_count()
        login_page.logout()

    # Цикл 3
    def test_send_zakup_for_approval_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_count()
        login_page.logout()

    def test_approval_zakup_for_audit_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            zakup_element_page.verify_zakup_waiting_status_approval_count()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой аудита не требуется")

    def test_approval_zakup_for_count_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Count")
            login_page.verify_username("Mr_KSUP_Count")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_count, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_count()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_reject_zakup_for_fin_cycle3(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_Fin")
        login_page.verify_username("Mr_KSUP_Fin")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_fin, UserData.file_path_for_link_jpg, "Согласование финансовой службой")
        zakup_element_page.verify_zakup_reject_status_approval_fin()
        login_page.logout()

    # Цикл 4
    def test_send_zakup_for_approval_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_fin()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_audit_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            zakup_element_page.verify_zakup_waiting_status_approval_fin()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой аудита не требуется")

    def test_approval_zakup_for_fin_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_Fin")
            login_page.verify_username("Mr_KSUP_Fin")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
            zakup_element_page.verify_zakup_successfully_status_approval_fin(user_data_dict)
            if user_data_dict["groupTypeWork"] == "Software" \
                    and user_data_dict["priceCategory"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif user_data_dict["groupTypeWork"] == "Other" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_reject_zakup_for_udprpo_cycle4(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_UDPRPO")
        login_page.verify_username("Mr_KSUP_UDPRPO")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup(UserData.comment_reject_udprpo, UserData.file_path_for_link_jpg, "Согласование Директором по разработке ПО")
        zakup_element_page.verify_zakup_reject_status_approval_udprpo()
        login_page.logout()

    # Цикл 5
    def test_escalate_zakup_on_kkp_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.escalate_on_kkp()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_audit_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой аудита не требуется")

    def test_revision_zakup_for_kkp_cycle5(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_KKP")
        login_page.verify_username("Mr_KSUP_KKP")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.revision_zakup_from_kkp(UserData.comment_revision_kkp, "Согласование Директором по разработке ПО")
        zakup_element_page.verify_zakup_revision_status_approval()
        login_page.logout()

    # Цикл 6
    def test_send_zakup_for_approval_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        zakup_element_page.verify_zakup_waiting_status_approval_audit()
        login_page.logout()

    def test_approval_zakup_for_audit_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            login_page.verify_username("Mr_KSUP_Audit")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_audit, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_audit()
            zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой аудита не требуется")

    def test_approval_zakup_for_udprpo_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_UDPRPO")
            login_page.verify_username("Mr_KSUP_UDPRPO")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_udprpo, UserData.file_path_for_link_jpg)
            zakup_element_page.verify_zakup_successfully_status_approval_udprpo(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка" \
                    and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_reject_zakup_for_kkp_cycle6(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login("Mr_KSUP_KKP")
        login_page.verify_username("Mr_KSUP_KKP")
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.reject_zakup_from_kkp(UserData.comment_reject_kkp)
        zakup_element_page.verify_zakup_reject_status_approval_kkp()
        login_page.logout()

    def test_unvisibility_send_approval_button(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
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
        zakup_element_page.verify_unvisibility_approval_send_button()
        login_page.logout()
