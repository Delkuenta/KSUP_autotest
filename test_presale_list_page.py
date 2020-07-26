import pytest

from pages.presale_list_page import PresalePage
from userdata.login_data import LoginData
from userdata.user_data import UserData
from pages.presale_create_form_page import PresaleFormCreate
from pages.presale_element_page import PresaleElementPage
from pages.zakup_list_page import ZakupPage
from pages.zakup_create_form_page import ZakupFormCreate
from pages.zakup_element_page import ZakupElementPage
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_list_page import ContractPage
from pages.contract_element_page import ContractElementPage


class Test1_PaZpDkTenderKatArazrabPO_fullAprovalCycle:

    #@pytest.mark.repeat(1)
    def test_create_presale_tender(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_presale)
        login_page.verify_username(UserData.login_for_create_presale[0])
        presale_list_page = PresalePage(browser, link)
        presale_list_page.go_to_presale_list()
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        presale_create_form = PresaleFormCreate(browser, browser.current_url)
        presale_create_form.form_create_presale_tender_or_zapros_cen_uslug()
        presale_list_page.should_be_element_on_presale_list()

    def test_create_zakup_konkurs_based_on_presale(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_zakup)
        login_page.verify_username(UserData.login_for_create_zakup[0])
        login_page.go_to_presale_list()
        presale_list_page = PresalePage(browser, browser.current_url)
        presale_list_page.go_to_presale_element()
        page_presale_element = PresaleElementPage(browser, browser.current_url)
        page_presale_element.go_to_create_zp_tender_based_on_presale()
        zakup_create_form = ZakupFormCreate(browser, browser.current_url)
        zakup_create_form.form_create_zp_based_on_presale_tender()
        page_zakup_list = ZakupPage(browser, browser.current_url)
        page_zakup_list.should_be_element_on_zakup_list()

    def test_send_zakup_tender_for_approval(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_zakup)
        login_page.verify_username(UserData.login_for_create_zakup[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.send_zakup_for_approval()
        zakup_element_page.verify_zakup_waiting_status_approval_legal()

    def test_approval_zakup_for_legal(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_legal)
        login_page.verify_username(UserData.login_legal[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.approval_zakup_legal()
        zakup_element_page.verify_zakup_successfully_status_approval_legal()
        zakup_element_page.verify_zakup_waiting_status_approval_count()

    def test_approval_zakup_for_count(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_count)
        login_page.verify_username(UserData.login_count[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.approval_zakup_count()
        zakup_element_page.verify_zakup_successfully_status_approval_count()
        zakup_element_page.verify_zakup_waiting_status_approval_fin()

    def test_approval_zakup_for_fin(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_fin)
        login_page.verify_username(UserData.login_fin[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.approval_zakup_fin()
        zakup_element_page.verify_zakup_successfully_status_approval_fin()
        zakup_element_page.verify_zakup_waiting_status_approval_udprpo()

    def test_approval_zakup_for_udprpo(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_udprpo)
        login_page.verify_username(UserData.login_udprpo[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.approval_zakup_udprpo()
        zakup_element_page.verify_zakup_successfully_status_approval_udprpo()
        zakup_element_page.verify_zakup_waiting_status_approval_kkp()

    def test_approval_zakup_for_kkp(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_kkp)
        login_page.verify_username(UserData.login_kkp[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.approval_zakup_kkp()
        zakup_element_page.verify_zakup_successfully_status_approval_kkp()

    def test_create_contract_based_on_zakup_konkurs(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_contract)
        login_page.verify_username(UserData.login_for_create_contract[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.go_to_create_contract_based_on_zp()
        contract_form_create = ContractFormCreate(browser, browser.current_url)
        contract_form_create.form_create_contract_based_on_zp_konkurs()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.should_be_element_on_contract_list()

    def test_send_contract_for_approval(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_contract)
        login_page.verify_username(UserData.login_for_create_contract[0])
        login_page.go_to_contract_list()
        contract_list = ContractPage(browser, browser.current_url)
        contract_list.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.send_contract_for_approval()
        contract_element_page.verify_contract_waiting_status_approval_legal()

    def test_approval_contract_for_legal(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_legal)
        login_page.verify_username(UserData.login_legal[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()

    def test_approval_contract_for_count(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_count)
        login_page.verify_username(UserData.login_count[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()

    def test_approval_contract_for_fin(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_fin)
        login_page.verify_username(UserData.login_fin[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_fin()
        contract_element_page.verify_contract_waiting_status_approval_udprpo()

    def test_approval_contract_for_udprpo(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_udprpo)
        login_page.verify_username(UserData.login_udprpo[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_udprpo()

class Test2_Pa_ZP_DK_ZaprosCen_KatArazrabPO:

    def test_create_presale_zapros_cen(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_presale)
        login_page.verify_username(UserData.login_for_create_presale[0])
        presale_list_page = PresalePage(browser, link)
        presale_list_page.go_to_presale_list()
        presale_list_page.should_be_clickable_create_button()
        presale_list_page.go_to_create_presale()
        presale_create_form = PresaleFormCreate(browser, browser.current_url)
        presale_create_form.form_create_presale_tender_or_zapros_cen_uslug()
        presale_list_page.should_be_element_on_presale_list()

    def test_create_zakup_based_on_presale(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_zakup)
        login_page.verify_username(UserData.login_for_create_zakup[0])
        login_page.go_to_presale_list()
        presale_list_page = PresalePage(browser, browser.current_url)
        presale_list_page.go_to_presale_element()
        page_presale_element = PresaleElementPage(browser, browser.current_url)
        page_presale_element.go_to_create_zp_presale_аct_based_on_presale()
        zakup_create_form = ZakupFormCreate(browser, browser.current_url)
        zakup_create_form.form_create_zp_based_on_presale_zaproc_cen()
        page_zakup_list = ZakupPage(browser, browser.current_url)
        page_zakup_list.should_be_element_on_zakup_list()

    def test_send_zakup_zaprosCen_for_approval(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_zakup)
        login_page.verify_username(UserData.login_for_create_zakup[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.send_zakup_for_approval()
        zakup_element_page.verify_zakup_waiting_status_approval_udprpo()

    def test_approval_zakup_zaprosCen_for_udprpo(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_udprpo)
        login_page.verify_username(UserData.login_udprpo[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.approval_zakup_udprpo()
        zakup_element_page.verify_zakup_successfully_status_approval_udprpo()
        breakpoint()

    def test_create_contract_based_on_zakup_zaprosCen(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_contract)
        login_page.verify_username(UserData.login_for_create_contract[0])
        login_page.go_to_zakup_list()
        zakup_list_page = ZakupPage(browser, browser.current_url)
        zakup_list_page.go_to_zakup_element()
        zakup_element_page = ZakupElementPage(browser, browser.current_url)
        zakup_element_page.go_to_create_contract_based_on_zp()
        contract_form_create = ContractFormCreate(browser, browser.current_url)
        contract_form_create.form_create_contract_based_on_zp_zapros_cen()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.should_be_element_on_contract_list()

    def test_send_contract_for_approval(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_contract)
        login_page.verify_username(UserData.login_for_create_contract[0])
        login_page.go_to_contract_list()
        contract_list = ContractPage(browser, browser.current_url)
        contract_list.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.send_contract_for_approval()
        contract_element_page.verify_contract_waiting_status_approval_legal()

    def test_approval_contract_for_legal(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_legal)
        login_page.verify_username(UserData.login_legal[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_legal()
        contract_element_page.verify_contract_waiting_status_approval_count()

    def test_approval_contract_for_count(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_count)
        login_page.verify_username(UserData.login_count[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_count()
        contract_element_page.verify_contract_waiting_status_approval_fin()

    def test_approval_contract_for_fin(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_fin)
        login_page.verify_username(UserData.login_fin[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_fin()
        contract_element_page.verify_contract_waiting_status_approval_udprpo()

    def test_approval_contract_for_udprpo(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_udprpo)
        login_page.verify_username(UserData.login_udprpo[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_legal()
        contract_element_page.verify_contract_successfully_status_approval_udprpo()

    def test_approval_contract_for_kkp(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_kkp)
        login_page.verify_username(UserData.login_kkp[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_contract_element()
        contract_element_page = ContractElementPage(browser, browser.current_url)
        contract_element_page.approval_contract_kkp()
        contract_element_page.verify_contract_successfully_status_approval_kkp()





