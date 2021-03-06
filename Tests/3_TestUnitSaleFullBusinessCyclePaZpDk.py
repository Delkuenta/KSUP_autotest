import pytest
import delayed_assert

from pages.base_page import BasePage
from pages.Contract.contract_create_form_page import ContractFormCreate
from pages.Contract.contract_element_page import ContractElementPage
from pages.Contract.contract_list_page import ContractPage
from pages.Presale.presale_element_page import PresaleElementPage
from pages.Presale.presale_list_page import PresalePage
from pages.Zakup.zakup_create_form_page import ZakupFormCreate
from pages.Zakup.zakup_element_page import ZakupElementPage
from pages.login_data import LoginData
from pages.Presale.presale_create_form_page import PresaleFormCreate
from pages.Zakup.zakup_list_page import ZakupListPage
from userdata.user_data import UserData

r"""
UnitSale\Seller
1_[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json
2_[Atest_Seller] PA+ZP+DK,Tender, categoryB, softwareDev, UnitSale.json
3_[Atest_Seller] PA+ZP+DK,Tender, categoryC, softwareDev, UnitSale.json
4_[Atest_Seller] PA+ZP+DK,Tender, categoryA, OtherType, UnitSale.json
5_[Atest_Seller] PA+ZP+DK,Tender, categoryB, OtherType, UnitSale.json
6_[Atest_Seller] PA+ZP+DK,Tender, categoryC, OtherType, UnitSale.json
7_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryA, softwareDev, UnitSale.json
8_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryB, softwareDev, UnitSale.json
9_[Atest_Seller] PA+ZP+DK, CommercialOffer, categoryC, softwareDev, UnitSale.json
10_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryA, OtherType, UnitSale.json
11_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryB, OtherType, UnitSale.json
12_[Аtest_Seller] PA+ZP+DK, CommercialOffer, categoryC, OtherType, UnitSale.json
13_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryA, softwareDev, UnitSale.json
14_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryB, softwareDev, UnitSale.json
15_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryC, softwareDev, UnitSale.json
16_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryA, OtherType, UnitSale.json
17_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryB, OtherType, UnitSale.json
18_[Atest_Seller] PA+ZP+DK, RequestPrice, categoryC, OtherType, UnitSale.json

UnitSale\Dir
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
20_[Atest_Dir] PA+ZP+DK,Tender, JointBidding, categoryA, softwareDev, UnitSale.json

UnitSale\Seller2
1_[Atest_Seller2] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json
2_[Atest_Seller2] PA+ZP+DK,Tender, categoryB, softwareDev, UnitSale.json
3_[Atest_Seller2] PA+ZP+DK,Tender, categoryС, softwareDev, UnitSale.json
4_[Atest_Seller2] PA+ZP+DK,Tender, categoryA, OtherType, UnitSale.json
5_[Atest_Seller2] PA+ZP+DK,Tender, categoryB, OtherType, UnitSale.json
6_[Atest_Seller2] PA+ZP+DK,Tender, categoryC, OtherType, UnitSale.json
7_[Аtest_Seller2] PA+ZP+DK, CommercialOffer, categoryA, softwareDev, UnitSale.json
8_[Аtest_Seller2] PA+ZP+DK, CommercialOffer, categoryB, softwareDev, UnitSale.json
9_[Аtest_Seller2] PA+ZP+DK, CommercialOffer, categoryC, softwareDev, UnitSale.json
10_[Аtest_Seller2] PA+ZP+DK, CommercialOffer, categoryA, OtherType, UnitSale.json
11_[Аtest_Seller2] PA+ZP+DK, CommercialOffer, categoryB, OtherType, UnitSale.json
12_[Аtest_Seller2] PA+ZP+DK, CommercialOffer, categoryC, OtherType, UnitSale.json
13_[Atest_Seller2] PA+ZP+DK, RequestPrice, categoryA, softwareDev, UnitSale.json
14_[Atest_Seller2] PA+ZP+DK, RequestPrice, categoryB, softwareDev, UnitSale.json
15_[Atest_Seller2] PA+ZP+DK, RequestPrice, categoryC, softwareDev, UnitSale.json
16_[Atest_Seller2] PA+ZP+DK, RequestPrice, categoryA, OtherType, UnitSale.json
17_[Atest_Seller2] PA+ZP+DK, RequestPrice, categoryB, OtherType, UnitSale.json
18_[Atest_Seller2] PA+ZP+DK, RequestPrice, categoryC, OtherType, UnitSale.json
"""


# До первой ошибки --maxfail=1
# Браузер для запуска --browser_name=firefox
@pytest.mark.parametrize('path_data_file', [
    r"PPAC\3_UnitSale\Seller\1_[Atest_Seller] PA+ZP+DK,Tender, categoryA, softwareDev, UnitSale.json"
])
class TestUnitSaleFullBusinessCyclePaZpDk:

    def test_create_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        presale_list_page = PresalePage(browser_function, link)
        create_presale_page = PresaleFormCreate(browser_function, link)
        presale_element_page = PresaleElementPage(browser_function, browser_function.current_url)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        presale_list_page.go_to_presale_list(link)
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        # Проверяем предзаполнения менеджеров Баг https://jira.lanit.ru/browse/KSUP-1041
        # create_presale_page.verify_prefill_department_manager(user_data_dict)
        create_presale_page.form_create_presale_all_type(user_data_dict)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            presale_list_page.go_to_mine_elements_tab()
        else:
            presale_list_page.go_to_allmydepartment_tab()
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page.verify_general_information_in_presale(user_data_dict)
        presale_element_page.verify_presale_not_require_status_approval()
        presale_element_page.verify_payments_information_in_presale(user_data_dict)
        login_page.logout()
        delayed_assert.assert_expectations()

    def test_create_zakup_based_on_presale(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        presale_list_page = PresalePage(browser_function, browser_function.current_url)
        presale_element_page = PresaleElementPage(browser_function, browser_function.current_url)
        zakup_form_create_page = ZakupFormCreate(browser_function, browser_function.current_url)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)

        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])

        presale_list_page.go_to_presale_list(link)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            presale_list_page.go_to_mine_elements_tab()
        else:
            presale_list_page.go_to_allmydepartment_tab()
        presale_list_page.should_be_element_on_presale_list(user_data_dict)
        presale_list_page.go_to_presale_element(user_data_dict)
        presale_element_page.go_to_create_zp_based_on_presale(user_data_dict)
        zakup_form_create_page.form_create_zakup_all_type_based_on_presale(user_data_dict)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            zakup_list_page.go_to_mine_elements_tab()
        else:
            zakup_list_page.go_to_allmydepartment_tab()
        zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        # Проверка вкладки "Общие сведения"
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_draft_status_zakup()
        # Проверка вкладки "Прикрепленные файлы"
        zakup_element_page.verify_attached_files_information(user_data_dict)
        login_page.logout()
        delayed_assert.assert_expectations()

    def test_send_zakup_for_approval(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        # Логин
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_zakup_list(link)

        # Переход на страницу карточка сущности "Закупочная процедура"
        zakup_list_page.go_to_zakup_element(user_data_dict)
        # Проверка корректности заполненных полей и статуса созданной сущности
        zakup_element_page.verify_general_information_in_zakup(user_data_dict)
        zakup_element_page.verify_attached_files_information(user_data_dict)
        # zakup_element_page.verify_draft_status_zakup()
        user_data_dict = zakup_element_page.attribute_approval_with_dept_head(user_data_dict)
        BasePage.load_file_json(browser_function, path_data_file, user_data_dict)
        # Отправка сущности на внутреннее согласование
        zakup_element_page.send_zakup_for_approval(user_data_dict)
        # На основе: Типа закупочной процедуры, Ценовой категории, Типа работ и услуг
        # проверка обновления статуса согласования
        if user_data_dict["contractorType"] == "Тендерная заявка":
            # Отправка на согласование с правами Руководителя подразделения + руководитель юр.лица
            if user_data_dict["createAccount"] == "Mr_KSUP_Dir" or user_data_dict["createAccount"] == "Mr_KSUP_Dir2":
                if user_data_dict["divisionHeadApproves"] == "Да":
                    zakup_element_page.verify_zakup_successfully_status_approval_department_head()
                zakup_element_page.verify_zakup_waiting_status_approval_legal()
                zakup_element_page.verify_zakup_waiting_status_approval_audit()
            else:
                if user_data_dict["divisionHeadApproves"] == "Да":
                    zakup_element_page.verify_zakup_waiting_status_approval_department_head()
            zakup_element_page.verify_visibility_budget_button()
            # Добавление файла бюджета возможные названия файла test_jpg.jpg, test_doc.docx, test_excel.xlsx, test_video.mp4, test_pdf.pdf
            zakup_element_page.add_file_of_budget("test_doc.docx")
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.verify_attached_files_information(user_data_dict)
            zakup_element_page.verify_attached_budget_files("test_doc.docx")

        elif user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] != "C" and \
                user_data_dict["groupTypeWork"] == "Software":
            # Отправка на согласование с правами Руководителя подразделения
            if user_data_dict["createAccount"] == "Mr_KSUP_Dir" or user_data_dict["createAccount"] == "Mr_KSUP_Dir2":
                if user_data_dict["divisionHeadApproves"] == "Да":
                    zakup_element_page.verify_zakup_successfully_status_approval_department_head()
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            else:
                if user_data_dict["divisionHeadApproves"] == "Да":
                    zakup_element_page.verify_zakup_waiting_status_approval_department_head()
        else:
            # Отправка на согласование с правами Руководителя подразделения
            if user_data_dict["createAccount"] == "Mr_KSUP_Dir" or user_data_dict["createAccount"] == "Mr_KSUP_Dir2":
                zakup_element_page.verify_zakup_not_require_status_approval()
            else:
                if user_data_dict["divisionHeadApproves"] == "Да":
                    zakup_element_page.verify_zakup_waiting_status_approval_department_head()

        login_page.logout()
        delayed_assert.assert_expectations()

    def test_approval_zakup_for_department_head(self, browser_function, path_data_file):
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
                login_page.go_to_zakup_list(link)
                zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
                zakup_list_page.go_to_approval_head_dept_tab()
                # zakup_list_page.go_to_allmydepartment_tab()
                zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
                zakup_list_page.go_to_zakup_element(user_data_dict)
                zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
                zakup_element_page.verify_general_information_in_zakup(user_data_dict)
                zakup_element_page.approval_zakup(UserData.comment_approval_depatment_head, UserData.file_path_for_link_pdf)
                if user_data_dict["contractorType"] == "Тендерная заявка":
                    zakup_element_page.verify_zakup_successfully_status_approval_department_head()
                    zakup_element_page.verify_zakup_waiting_status_approval_legal()
                    zakup_element_page.verify_zakup_waiting_status_approval_audit()
                elif user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] != "C" and \
                        user_data_dict["groupTypeWork"] == "Software":
                    zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
                else:
                    zakup_element_page.verify_zakup_successfully_status_approval_department_head()
            else:
                print("\nВнутреннее согласование закупочной процедуры за Руководителя подразделения не требуется")
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя подразделения не требуется "
                  "из-за отключения этапа согласования с руководителем подразделения")

    """
    Этап убран перенесется в конец цикла согласования
    def test_approval_zakup_for_egrulhead(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)

        if ((user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Dir")
            and UserData.egrulHead["Mr_KSUP_Dir"] != user_data_dict["executiveUnitLegal"]) or \
            ((user_data_dict["createAccount"] == "Mr_KSUP_Seller2" or user_data_dict["createAccount"] == "Mr_KSUP_Dir2")
             and UserData.egrulHead["Mr_KSUP_Dir2"] != user_data_dict["executiveUnitLegal"]):

            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            # Определяем руководителя по значению юр.лица-исполнителя в словаре
            account_name = {value: key for key, value in UserData.egrulHead.items()}[user_data_dict["executiveUnitLegal"]]
            login_page.login(account_name)
            login_page.verify_username(account_name)

            login_page.go_to_zakup_egrul_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_head_egrul_tab()
            # zakup_list_page.go_to_allmydepartment_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.approval_zakup(UserData.comment_approval_depatment_head, UserData.file_path_for_link_pdf)
            zakup_element_page.verify_zakup_successfully_status_approval_egrulhead(user_data_dict)
            if user_data_dict["contractorType"] == "Тендерная заявка":
                zakup_element_page.verify_zakup_waiting_status_approval_legal()
            elif user_data_dict["contractorType"] != "Тендерная заявка" and user_data_dict["priceCategory"] != "C" and \
                    user_data_dict["groupTypeWork"] == "Software":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Руководителя юр.лица/ИП не требуется")
    """

    def test_approval_zakup_for_legal(self, browser_function, path_data_file):
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

    def test_approval_zakup_for_count(self, browser_function, path_data_file):
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
            # zakup_list_page.go_to_approved_elements_tabs()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры за Бухгалтерию не требуется")

    def test_approval_zakup_for_fin(self, browser_function, path_data_file):
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
            zakup_element_page.verify_visibility_budget_button()
            # Добавление файла бюджета возможные названия файла test_jpg.jpg, test_doc.docx, test_excel.xlsx, test_video.mp4, test_pdf.pdf
            zakup_element_page.add_file_of_budget("test_excel.xlsx")
            zakup_element_page.verify_general_information_in_zakup(user_data_dict)
            zakup_element_page.verify_attached_files_information(user_data_dict)
            zakup_element_page.verify_attached_budget_files("test_excel.xlsx")
            zakup_element_page.approval_zakup(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
            zakup_element_page.verify_zakup_successfully_status_approval_fin(user_data_dict)
            if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
                zakup_element_page.verify_zakup_waiting_status_approval_udprpo()
            elif user_data_dict["groupTypeWork"] == "Other" and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_kkp()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры c финансовой службой не требуется")

    def test_approval_zakup_for_udprpo(self, browser_function, path_data_file):
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
            if user_data_dict["contractorType"] == "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
                zakup_element_page.verify_zakup_waiting_status_approval_audit()
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой УДПР ПО не требуется")

    def test_approval_zakup_for_audit(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("sa_dks_ksup_audit")
            # login_page.verify_username("Mr_KSUP_Audit")
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

    def test_approval_zakup_for_kkp(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        if user_data_dict["contractorType"] == "Тендерная заявка" and user_data_dict["priceCategory"] == "A":
            link = LoginData.link
            login_page = LoginData(browser_function, link)
            login_page.open()
            login_page.login("Mr_KSUP_KKP")
            login_page.verify_username("Mr_KSUP_KKP")
            login_page.go_to_zakup_list(link)
            zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
            zakup_list_page.go_to_approval_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            zakup_list_page.go_to_zakup_element(user_data_dict)
            zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
            zakup_element_page.approval_zakup(UserData.comment_approval_kkp, UserData.file_path_for_link_doc)
            zakup_element_page.verify_zakup_successfully_status_approval_kkp(user_data_dict)
            login_page.go_to_zakup_list(link)
            zakup_list_page.go_to_approved_elements_tab()
            zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование закупочной процедуры со службой ККП не требуется")

    def test_create_contract_based_on_zakup(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        user_data_dict = BasePage.dict_preparation(browser_function, user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_zakup_list(link)
        zakup_list_page = ZakupListPage(browser_function, browser_function.current_url)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            zakup_list_page.go_to_mine_elements_tab()
        else:
            zakup_list_page.go_to_allmydepartment_tab()
        zakup_list_page.should_be_element_on_zakup_list(user_data_dict)
        zakup_list_page.go_to_zakup_element(user_data_dict)
        zakup_element_page = ZakupElementPage(browser_function, browser_function.current_url)
        zakup_element_page.go_to_create_contract_based_on_zp()
        contract_form_create = ContractFormCreate(browser_function, browser_function.current_url)
        contract_form_create.form_create_contract_based_on_zakup(user_data_dict)
        contract_list_page = ContractPage(browser_function, browser_function.current_url)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            contract_list_page.go_to_mine_elements_tab()
        else:
            contract_list_page.go_to_allmydepartment_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_related_presale(user_data_dict)
        contract_element_page.verify_related_zakup(user_data_dict)
        if user_data_dict["jointBidding"] == "Да":
            contract_element_page.verify_joint_bidding_inform_contract(user_data_dict)
        login_page.logout()

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
                contract_element_page.approval_contract(UserData.comment_approval_legal, UserData.file_path_for_link_jpg)
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
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        contract_element_page.approval_contract(UserData.comment_approval_count, UserData.file_path_for_link_doc)
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
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
        contract_list_page.go_to_approval_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        contract_list_page.go_to_contract_element(user_data_dict)
        contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
        # Добавление файла бюджета возможные названия файла test_jpg.jpg, test_doc.docx, test_excel.xlsx, test_video.mp4, test_pdf.pdf
        contract_element_page.verify_visibility_budget_button()
        contract_element_page.add_file_of_budget("test_pdf.pdf")
        contract_element_page.verify_general_information_contract(user_data_dict)
        contract_element_page.verify_attached_files_information()
        contract_element_page.verify_attached_budget_files("test_pdf.pdf")
        contract_element_page.approval_contract(UserData.comment_approval_fin, UserData.file_path_for_link_excel)
        contract_element_page.verify_contract_successfully_status_approval_fin(user_data_dict)
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] != "C":
            contract_element_page.verify_contract_waiting_status_approval_udprpo()
        elif user_data_dict["groupTypeWork"] == "Other" \
                and user_data_dict["priceCategory"] == "A" \
                and user_data_dict["contractorType"] != "Тендерная заявка":
            contract_element_page.verify_contract_waiting_status_approval_audit()
        login_page.go_to_contract_list(link)
        contract_list_page.go_to_approved_elements_tab()
        contract_list_page.should_be_element_on_contract_list(user_data_dict)
        login_page.logout()

    def test_approval_contract_for_udprpo(self, browser_function, path_data_file):
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
                contract_element_page.verify_contract_waiting_status_approval_kkp()
            login_page.go_to_contract_list(link)
            contract_list_page.go_to_approved_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
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
        # login_page.verify_username("Mr_KSUP_Audit")
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
            contract_list_page.go_to_approval_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            contract_list_page.go_to_contract_element(user_data_dict)
            contract_element_page = ContractElementPage(browser_function, browser_function.current_url)
            contract_element_page.approval_contract(UserData.comment_approval_kkp, UserData.file_path_for_link_mp4)
            contract_element_page.verify_contract_successfully_status_approval_kkp(user_data_dict)
            login_page.go_to_contract_list(link)
            contract_list_page.go_to_approved_elements_tab()
            contract_list_page.should_be_element_on_contract_list(user_data_dict)
            login_page.logout()
        else:
            print("\nВнутреннее согласование контракта со службой ККП не требуется")
