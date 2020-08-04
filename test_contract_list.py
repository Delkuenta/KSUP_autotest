from pages.login_data import LoginData
from userdata.user_data import UserData
from pages.contract_list_page import ContractPage
from pages.contract_create_form_page import ContractFormCreate
from pages.contract_element_page import ContractElementPage

class Test19_DK_katA_razrabPO:
    def test_create_contract_razrabPO(self, browser):
        link = LoginData.link
        login_page = LoginData(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_create_contract)
        login_page.verify_username(UserData.login_for_create_contract[0])
        login_page.go_to_contract_list()
        contract_list_page = ContractPage(browser, browser.current_url)
        contract_list_page.go_to_create_contract()
        contract_form_create = ContractFormCreate(browser, browser.current_url)
        contract_form_create.form_create_contract_single()
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
        contract_element_page.approval_contract_count()
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
        contract_element_page.approval_contract_fin()
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
        contract_element_page.approval_contract_udprpo()
        contract_element_page.verify_contract_successfully_status_approval_udprpo()
        contract_element_page.verify_contract_waiting_status_approval_kkp()

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
        contract_element_page.approval_contract_udprpo()
        contract_element_page.verify_contract_successfully_status_approval_kkp()



