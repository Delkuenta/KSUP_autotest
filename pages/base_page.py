from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # неявное ожидание

    def open(self):
        self.browser.get(self.url)

    # Проверка, что логин выполнится под правильной УЗ
    def verify_username(self, user_name, ):

        assert self.is_element_text(*BasePageLocators.USER_NAME) == user_name, "User Name is not presented"

    # Вывод текста из элемента
    def is_element_text(self, how, what):
        try:
            text_in_element = self.browser.find_element(how, what).text
        except NoSuchElementException:
            return False
        return text_in_element

    # Проверка что элемент отображен на странице
    def is_element_present(self, how, what):
        try:
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
