import time

from pages.base_page import BasePage
from pages.locators import ZakupListLocators


class ZakupListPage(BasePage):

    def should_be_element_on_zakup_list(self,user_data_dict):
        how, what = ZakupListLocators.FIND_ELEMENT_IN_ZAKUP_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Проверка доступности кнопки создания закупочной процедуры
    def should_be_clickable_zakup_create_button(self):
        assert self.is_element_clickable(
            *ZakupListLocators.ZAKUP_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'

    def go_to_create_zakup(self):
        button_create_zakup = self.browser.find_element(*ZakupListLocators.ZAKUP_CREATE_BUTTON)
        self.is_element_clickable(*ZakupListLocators.ZAKUP_CREATE_BUTTON)
        button_create_zakup.click()

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_zakup_element(self, user_data_dict):
        how, what = ZakupListLocators.FIND_ELEMENT_IN_ZAKUP_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Cущность с названием {user_data_dict["fullName"]} не найдена'
        self.browser.find_element(how, what).click()

    # Перейти на вкладку "Мои"
    def go_to_mine_elements_tab(self):
        assert self.is_visibility_of_element_located(*ZakupListLocators.MINE_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Мои"'
        self.browser.find_element(*ZakupListLocators.MINE_ELEMENTS_TAB).click()

    # Перейти на вкладку "На согласовании"
    def go_to_approval_elements_tab(self):
        assert self.is_visibility_of_element_located(*ZakupListLocators.APPROVAL_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "На согласовании"'
        self.browser.find_element(*ZakupListLocators.APPROVAL_ELEMENTS_TAB).click()

    # Перейти на вкладку "Отклонено"
    def go_to_rejected_elements_tab(self):
        assert self.is_visibility_of_element_located(*ZakupListLocators.REJECTED_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Отклонено"'
        self.browser.find_element(*ZakupListLocators.REJECTED_ELEMENTS_TAB).click()

    # Перейти на вкладку "Согласовано"
    def go_to_approved_elements_tab(self):
        assert self.is_visibility_of_element_located(*ZakupListLocators.APPROVED_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Согласовано"'
        self.browser.find_element(*ZakupListLocators.APPROVED_ELEMENTS_TAB).click()

    # Перейти на вкладку "Все моего подразделения"
    def go_to_allmydepartment_tab(self):
        assert self.is_visibility_of_element_located(*ZakupListLocators.ALL_IN_MY_DEPARTMENT_TAB, 5), \
            'Не отображена вкладка "Все моего подразделения"'
        self.browser.find_element(*ZakupListLocators.ALL_IN_MY_DEPARTMENT_TAB).click()

    def verify_element_status_in_approval_tab(self, approval_status="На согласовании с юридической службой"):
        self.browser.implicitly_wait(1)
        exception_set = {approval_status}
        actual_status_list = self.item_text_collector(*ZakupListLocators.APPROVAL_STATUS_VALUES)
        while self.is_visibility_of_element_located(*ZakupListLocators.PAGINATOR_NEXT_BUTTON, 0):
            self.browser.find_element(*ZakupListLocators.PAGINATOR_NEXT_BUTTON).click()
            actual_status_list += self.item_text_collector(*ZakupListLocators.APPROVAL_STATUS_VALUES)
        result = list(set(actual_status_list) - exception_set)
        assert len(result) == 0, 'Не корректные элементы на вкладке. ' \
                                 f'\nОжидаемый результат: Отображены только сущности со статусом "{approval_status}"' \
                                 f'\nФактический результат: Отображены сущности со статусом/ми: {result}'

    def verify_element_status_in_rejected_tab(self, rejected_status="Отклонено юридической службой"):
        self.browser.implicitly_wait(1)
        exception_set = {rejected_status}
        actual_status_list = self.item_text_collector(*ZakupListLocators.APPROVAL_STATUS_VALUES)
        while self.is_visibility_of_element_located(*ZakupListLocators.PAGINATOR_NEXT_BUTTON, 0):
            self.browser.find_element(*ZakupListLocators.PAGINATOR_NEXT_BUTTON).click()
            actual_status_list += self.item_text_collector(*ZakupListLocators.APPROVAL_STATUS_VALUES)
        result = list(set(actual_status_list) - exception_set)
        assert len(result) == 0, 'Не корректные элементы на вкладке. ' \
                                 f'\nОжидаемый результат: Отображены только сущности со статусом "{rejected_status}"' \
                                 f'\nФактический результат: Отображены сущности со статусом/ми: {result}'

    def verify_element_status_in_approved_tab(self, login_name):
        self.browser.implicitly_wait(1)
        exception_set = {}
        if login_name == "Mr_KSUP_Legal":
            exception_set = {"На согласовании с бухгалтерией",
                             "На согласовании с финансовой службой",
                             "На согласовании УДПР ПО",
                             "На согласовании в ККП",
                             "Согласовано с финансовой службой",
                             "Согласовано УДПР ПО",
                             "Участие в проекте согласовано в ККП"}
        elif login_name == "Mr_KSUP_Count":
            exception_set = {"На согласовании с финансовой службой",
                             "На согласовании УДПР ПО",
                             "На согласовании в ККП",
                             "Согласовано с финансовой службой",
                             "Согласовано УДПР ПО",
                             "Участие в проекте согласовано в ККП"}
        elif login_name == "Mr_KSUP_Fin":
            exception_set = {"На согласовании УДПР ПО",
                             "На согласовании в ККП",
                             "Согласовано с финансовой службой",
                             "Согласовано УДПР ПО",
                             "Участие в проекте согласовано в ККП"}
        elif login_name == "Mr_KSUP_UDPRPO":
            exception_set = {"На согласовании в ККП",
                             "Согласовано УДПР ПО",
                             "Участие в проекте согласовано в ККП"}
        elif login_name == "Mr_KSUP_KKP":
            exception_set = {"Участие в проекте согласовано в ККП"}

        actual_status_list = self.item_text_collector(*ZakupListLocators.APPROVAL_STATUS_VALUES)
        while self.is_visibility_of_element_located(*ZakupListLocators.PAGINATOR_NEXT_BUTTON, 0):
            self.browser.find_element(*ZakupListLocators.PAGINATOR_NEXT_BUTTON).click()
            actual_status_list += self.item_text_collector(*ZakupListLocators.APPROVAL_STATUS_VALUES)
        result = list(set(actual_status_list) - exception_set)
        assert len(result) == 0, 'Не корректные элементы на вкладке. ' \
                                 f'\nОжидаемый результат: Отображены только сущности со статусом "{exception_set}"' \
                                 f'\nФактический результат: Отображены сущности со статусом/ми: {result}'