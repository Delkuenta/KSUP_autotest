import json
import os
import time
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from userdata.user_data import UserData
from pages.locators import BasePageLocators


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

    # Проверка, доступен ли элемент к нажатию
    def is_element_clickable(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=50):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Проверка что элемент отображен и имеет размер
    def is_visibility_of_element_located(self, how, what, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((how, what)))
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
    def go_to_presale_list(self, link):
        presale_link = link + BasePageLocators.PRESALE_LIST_LINK
        self.browser.get(presale_link)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.PRESALE_LIST_TITLE, "Пресейловые активности"), \
            "Титул страницы не соответствует переходу"

    # Переход на страницу "Закупочная процедура"
    def go_to_zakup_list(self, link):
        zakup_link = link + BasePageLocators.ZAKUP_LIST_LINK
        self.browser.get(zakup_link)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.ZAKUP_LIST_TITLE, "Закупочные процедуры"), \
            "Титул страницы не соответствует переходу"

    # Переход на страницу "Договор/контракт"
    def go_to_contract_list(self, link):
        contract_link = link + BasePageLocators.CONTRACT_LIST_LINK
        self.browser.get(contract_link)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.CONTRACT_LIST_TITLE, "Договоры (контракты)"), \
            "Титул страницы не соответствует переходу"

    def go_to_customer_list(self, link):
        customer_link = link + BasePageLocators.CUSTOMER_LIST_LINK
        self.browser.get(customer_link)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.CUSTOMER_TITLE, "Заказчики и исполнители"), \
            "Титул страницы не соответствует переходу"

    # Переход на страницу База знаний
    def go_to_knowledge_search(self, link):
        knowledge_link = link + BasePageLocators.KNOWLEDGE_SEARCH_LINK
        self.browser.get(knowledge_link)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.KNOWLEDGE_SEARCH_TITLE, "Поиск по базе знаний"), \
            "Титул страницы не соответствует переходу"

    def go_to_project_list(self, link):
        project_link = link + BasePageLocators.PROJECT_LIST_LINK
        self.browser.get(project_link)
        assert self.is_text_to_be_present_in_element(*BasePageLocators.PROJECT_TITLE, "Проекты"), \
            "Титул страницы не соответствует переходу"

    def go_to_operplan_department(self, link):
        operplan_link = link + BasePageLocators.OPERPLAN_DEPARTMENT_LINK
        self.browser.get(operplan_link)
        assert self.is_element_text(*BasePageLocators.OPERPLAN_DEPARTMENT_TITLE) == "Оперпланы департаментов", \
            "Не корректный титул на странице оперпланы департамента.\n" \
            "Ожидаемый результат: Оперпланы департаментов"

    def go_to_operplan_direction(self, link):
        operplan_link = link + BasePageLocators.OPERPLAN_DIRECTION_LINK
        self.browser.get(operplan_link)
        assert self.is_element_text(*BasePageLocators.OPERPLAN_DEPARTMENT_TITLE) == "Оперпланы дирекции", \
            "Не корректный титул на странице оперпланы дирекции.\n" \
            "Ожидаемый результат: Оперпланы дирекции"

    def read_file_json(self, path_file):
        full_path_file = os.path.join(UserData.current_dir, path_file)
        with open(full_path_file, "r", encoding='utf-8') as file:
            data = json.load(file)
        user_data_dict = dict(data['main_data'])
        return user_data_dict

    def dict_preparation(self, user_data_dict):

        # Определяем валюту и переводим в рубли
        raw_sum = user_data_dict["sum"]
        if user_data_dict["currency"] == "Доллар":
            sum_in_rub = raw_sum * 65
        elif user_data_dict["currency"] == "Евро":
            sum_in_rub = raw_sum * 75
        else:
            sum_in_rub = raw_sum

        sum_in_rub_dict = {"sumInRub": sum_in_rub}
        user_data_dict.update(sum_in_rub_dict)

        # Присваиваем категорию на основе суммы в рублях
        priceCategory = ""
        if sum_in_rub >= 50000000:
            priceCategory = "A"
        elif 30000000 <= sum_in_rub < 50000000:
            priceCategory = "B"
        elif sum_in_rub < 30000000:
            priceCategory = "C"

        # Добавляем в словарь ценовую категорию
        price_category_dict = {"priceCategory": priceCategory}
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
        if "territory" in user_data_dict:
            user_data_dict["territory"].sort()
        return user_data_dict

    def select_in_frame_type_work_and_services(self, list_type_work):
        self.browser.implicitly_wait(2)
        # Работаем во фрейме и выбираем категории
        self.is_frame_to_be_available_and_switch_to_it()

        # Открываем все доступные категории
        if len(self.browser.find_elements(*BasePageLocators.GROUP_CATEGORY_ELEMENT1)) == 1:
            self.browser.find_element(*BasePageLocators.GROUP_CATEGORY_ELEMENT1).click()
        if len(self.browser.find_elements(*BasePageLocators.GROUP_CATEGORY_ELEMENT2)) == 1:
            self.browser.find_element(*BasePageLocators.GROUP_CATEGORY_ELEMENT2).click()
        if len(self.browser.find_elements(*BasePageLocators.GROUP_CATEGORY_ELEMENT3)) == 1:
            self.browser.find_element(*BasePageLocators.GROUP_CATEGORY_ELEMENT3).click()
        if len(self.browser.find_elements(*BasePageLocators.GROUP_CATEGORY_ELEMENT4)) == 1:
            self.browser.find_element(*BasePageLocators.GROUP_CATEGORY_ELEMENT4).click()
        if len(self.browser.find_elements(*BasePageLocators.GROUP_CATEGORY_ELEMENT5)) == 1:
            self.browser.find_element(*BasePageLocators.GROUP_CATEGORY_ELEMENT5).click()

        # Выбираем нужный элемент
        for element in list_type_work:
            how, what = BasePageLocators.WORK_SERVICE_ELEMENT
            what = what.replace("name_type_works", element)
            if self.is_visibility_of_element_located(how, what, 3):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*BasePageLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                self.browser.find_element(*BasePageLocators.SCROLL_DOWN_SOFTWARE_BUTTON).click()
                assert self.is_visibility_of_element_located(how, what, 3) is True, \
                    f"Не найден тип работ и услуг с именем {element}"
                self.browser.find_element(how, what).click()
                self.browser.find_element(*BasePageLocators.CHOICE_IFRAME_BUTTON).click()

        self.browser.find_element(*BasePageLocators.CONFIRM_IFRAME_BUTTON).click()
        # Возврат к форм создания.
        self.is_frame_to_parent()
        time.sleep(1)

    def select_elements_in_frame_territory(self, list_territories):
        self.browser.implicitly_wait(2)
        self.is_frame_to_be_available_and_switch_to_it()
        # Развернуть узел "Все субъекты если кнопка отображена"
        if len(self.browser.find_elements(*BasePageLocators.GROUP_TERRITORY_ELEMENT)) == 1:
            self.browser.find_element(*BasePageLocators.GROUP_TERRITORY_ELEMENT).click()
        # Выбираем территории из списка
        for territory in list_territories:
            how, what = BasePageLocators.TERRITORY_ELEMENT
            what = what.replace("territory_name", territory)
            if self.is_visibility_of_element_located(how, what, 1):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*BasePageLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 7
                while self.is_visibility_of_element_located(how, what, 1) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*BasePageLocators.SCROLL_DOWN_BUTTON_TERRITORY).click()
                    scrolls += 1
                self.browser.find_element(how, what).click()
                self.browser.find_element(*BasePageLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_visibility_of_element_located(how, what, 1) is False and scrolls == max_scrolls:
                    print(f"Не найдена территория  с именем {territory}")

        self.browser.find_element(*BasePageLocators.CONFIRM_IFRAME_BUTTON).click()

        # возврат к основной форме
        self.is_frame_to_parent()
        time.sleep(2)

    def select_elements_in_frame(self, list_elements, max_scrolls):
        self.browser.implicitly_wait(2)
        if isinstance(list_elements, str):
            list_elements = [list_elements]
        # Выбираем значение в поле "Ключевые технологии"
        self.is_frame_to_be_available_and_switch_to_it()
        for element in list_elements:
            how, what = BasePageLocators.ELEMENT_IN_FRAME
            what = what.replace("name", element)
            if self.is_visibility_of_element_located(how, what, 1):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*BasePageLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                while self.is_visibility_of_element_located(how, what, 1) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*BasePageLocators.SCROLL_DOWN_BUTTON).click()
                    scrolls += 1

                self.browser.find_element(how, what).click()
                self.browser.find_element(*BasePageLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_visibility_of_element_located(how, what, 1) is False and scrolls == max_scrolls:
                    print(f"Не найдена технология с именем {element}")

        self.browser.find_element(*BasePageLocators.CONFIRM_IFRAME_BUTTON).click()
        self.is_frame_to_parent()
        time.sleep(2)

    # Вспомогательный метод: собирает текст у всех найденных элементов в список.
    def item_text_collector(self, how, what):
        web_elements = self.browser.find_elements(how, what)
        list_text_element = []
        for item in web_elements:
            list_text_element.append(item.text)
        return list_text_element
