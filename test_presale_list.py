from pages.login_data import LoginData
from userdata.user_data import UserData
from pages.presale_list_page import PresalePage
from pages.presale_create_form_page import PresaleFormCreate
from pages.presale_element_page import PresaleElementPage


class Test_single_presale_self_sale:

    def test_create_presale_tender_zaprosCen_self_sale(self, browser):
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
        presale_create_form.form_create_presale_all_type()
        presale_list_page.should_be_element_on_presale_list()
        presale_list_page.go_to_presale_element()
        presale_element = PresaleElementPage(browser, browser.current_url)
        presale_element.verify_self_sale_status_approval()


    def test_create_presale_kommPred_nonType_self_sale(self,browser):
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
        presale_create_form.form_create_presale_all_type()
        presale_list_page.should_be_element_on_presale_list()
        presale_list_page.go_to_presale_element()
        presale_element = PresaleElementPage(browser, browser.current_url)
        presale_element.verify_self_sale_status_approval()

# отправка на согласование из формы создания пресейла
class Test1_single_presale_separate_sale:

    def test_create_presale_tender_and_send_to_approval_in_create_form(self, browser):
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
        presale_create_form.form_create_presale_all_type()
        presale_create_form.send_presale_to_approval_in_form_create()
        presale_list_page.should_be_element_on_presale_list()
        presale_list_page.go_to_presale_element()
        presale_element = PresaleElementPage(browser, browser.current_url)
        presale_element.verify_separate_sale_status_was_send_approval()

    def test_approval_presale(self, browser):
        link = LoginData.link
        login_page = LoginData(browser, link)
        login_page.open()  # открываем страницу
        login_page.login(*UserData.login_for_approval_presale)
        login_page.verify_username(UserData.login_for_approval_presale[0])
        presale_list_page = PresalePage(browser, link)
        presale_list_page.go_to_presale_list()
        presale_list_page.should_be_element_on_presale_list()
        presale_list_page.go_to_presale_element()
        presale_element = PresaleElementPage(browser, browser.current_url)
        presale_element.verify_separate_sale_status_was_send_approval()
        presale_element.approval_presale()
        presale_element.browser.refresh()
        presale_element.verify_separate_sale_successfully_status_approval()


# отправка на согласование из страницы пресейла
class Test2_single_presale_separate_sale:
    def test_create_presale_tender_and_send_to_approval_on_element_page(self, browser):
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
        presale_create_form.form_create_presale_all_type()
        presale_create_form.abort_send_presale_to_approval_in_form_create()
        presale_list_page.should_be_element_on_presale_list()
        presale_list_page.go_to_presale_element()
        presale_element = PresaleElementPage(browser, browser.current_url)
        presale_element.verify_separate_sale_status_was_aborted_approval()
        presale_element.go_to_approval_presale()
        presale_element.verify_separate_sale_status_was_send_approval()




