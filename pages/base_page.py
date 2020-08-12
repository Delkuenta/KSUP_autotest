from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # неявное ожидание

    def open(self):
        self.browser.get(self.url)

    # Проверка, что логин выполнится под правильной УЗ
    def verify_username(self, user_name):
        assert self.is_element_text(*BasePageLocators.USER_NAME) in user_name, "User Name is not presented"

    # Вывод текста из элемента
    def is_element_text(self, how, what):
        try:
            text_in_element = self.browser.find_element(how, what).text
        except NoSuchElementException:
            return False
        return text_in_element

    # Проверка текста с переменной
    def is_text_to_be_present_in_element(self, how, what, text):
        try:
            WebDriverWait(self.browser, 5).until(EC.text_to_be_present_in_element((how, what), text))
        except:
            return False
        return True

    # Проверка что элемент отображен на странице
    def is_element_present(self, how, what):
        try:
            self.browser.implicitly_wait(5)
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Проверка, доступен ли элемент к нажатию
    def is_element_clickable(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Переключение на активный фрейм
    def is_frame_to_be_available_and_switch_to_it(self, timeout=5):
        try:
            iframe = self.browser.switch_to.active_element
            WebDriverWait(self.browser, timeout).until(
                EC.frame_to_be_available_and_switch_to_it(iframe))
        except TimeoutException:
            return False
        return True

    # Переключение на родительский фрейм
    def is_frame_to_parent (self):
        self.browser.switch_to.default_content()

    def go_to_presale_list(self):
        self.browser.get(BasePageLocators.PRESALE_LIST_LINK)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.PRESALE_LIST_TITLE, "Пресейловые активности"), \
            "Титул страницы не соответствует переходу"

    def go_to_zakup_list(self):
        self.browser.get(BasePageLocators.ZAKUP_LIST_LINK)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.ZAKUP_LIST_TITLE, "Закупочные процедуры"), \
            "Титул страницы не соответствует переходу"

    def go_to_contract_list(self):
        self.browser.get(BasePageLocators.CONTRACT_LIST_LINK)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.CONTRACT_LIST_TITLE, "Договоры (контракты)"), \
            "Титул страницы не соответствует переходу"

    def is_visibility_of_element_located(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

