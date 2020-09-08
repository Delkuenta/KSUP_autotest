import json
import os

from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from userdata.user_data import UserData
from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
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
            WebDriverWait(self.browser, 5).until(ec.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            return False
        return True

    # Проверка что элемент присутствует в DOM(не явное ожидание)
    def is_element_present(self, how, what):
        try:
            self.browser.implicitly_wait(3)
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Проверка, доступен ли элемент к нажатию
    def is_element_clickable(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Переключение на активный фрейм
    def is_frame_to_be_available_and_switch_to_it(self, timeout=3):
        try:
            iframe = self.browser.switch_to.active_element
            WebDriverWait(self.browser, timeout).until(ec.frame_to_be_available_and_switch_to_it(iframe))
        except TimeoutException:
            return False
        return True

    # Переключение на родительский фрейм
    def is_frame_to_parent(self):
        self.browser.switch_to.default_content()

    # Переход на страницу "Пресейловая активность"
    def go_to_presale_list(self):
        self.browser.get(BasePageLocators.PRESALE_LIST_LINK)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.PRESALE_LIST_TITLE, "Пресейловые активности"), \
            "Титул страницы не соответствует переходу"

    # Переход на страницу "Закупочная процедура"
    def go_to_zakup_list(self):
        self.browser.get(BasePageLocators.ZAKUP_LIST_LINK)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.ZAKUP_LIST_TITLE, "Закупочные процедуры"), \
            "Титул страницы не соответствует переходу"

    # Переход на страницу "Договор/контракт"
    def go_to_contract_list(self):
        self.browser.get(BasePageLocators.CONTRACT_LIST_LINK)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.CONTRACT_LIST_TITLE, "Договоры (контракты)"), \
            "Титул страницы не соответствует переходу"

    # Проверка что элемент отображен и имеет размер
    def is_visibility_of_element_located(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def read_json(self, name_file):
        path_file = r"D:\WORK\Git\KSUP_autotest\userdata"
        full_path_file = os.path.join(path_file, name_file)
        print(full_path_file)
        with open(full_path_file, "r", encoding='utf-8') as file:
            data = json.load(file)
        user_data_dict = dict(data['main_data'])
        return user_data_dict

    def dict_preparation(self, user_data_dict):

        # Определяем валюту и переводим в рубли
        raw_sum = user_data_dict["sum"]
        if user_data_dict["currency"] == "Доллар":
            sum_in_rub = raw_sum * 70
        elif user_data_dict["currency"] == "Евро":
            sum_in_rub = raw_sum * 80
        else:
            sum_in_rub = raw_sum

        # Присваиваем категорию на основе суммы в рублях
        price_category = ""
        if sum_in_rub >= 50000000:
            price_category = "A"
        elif 30000000 <= sum_in_rub < 50000000:
            price_category = "B"
        elif sum_in_rub < 30000000:
            price_category = "C"

        # Добавляем в словарь ценовую категорию
        price_category_dict = {"price_category": price_category}
        user_data_dict.update(price_category_dict)

        # Определяем входит ли элемент в категорию "Разработка ПО"
        i = 0
        for category in user_data_dict["typeOfWorkServices"]:
            if category in UserData.group_software:
                i += 1
        if i >= 1:
            group_type_dict = {"groupTypeWork": "Software"}

        else:
            group_type_dict = {"groupTypeWork": "Other"}
        user_data_dict.update(group_type_dict)

        # Сортировка списка территорий по алфавиту
        user_data_dict["territory"].sort()
        return user_data_dict
