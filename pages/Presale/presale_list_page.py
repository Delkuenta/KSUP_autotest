import time

from pages.base_page import BasePage
from pages.locators import PresaleListLocators
from userdata.user_data import UserData


class PresalePage(BasePage):

    # Кнопка создания пресейла на странице пресейла
    def go_to_create_presale(self):
        self.browser.implicitly_wait(5)
        self.is_visibility_of_element_located(*PresaleListLocators.PRESALE_CREATE_BUTTON, 10)
        self.browser.find_element(*PresaleListLocators.PRESALE_CREATE_BUTTON).click()

    # Проверка доступности кнопки создания пресейла
    def should_be_clickable_create_button(self):
        time.sleep(2)
        assert self.is_element_clickable(*PresaleListLocators.PRESALE_CREATE_BUTTON), \
           'Кнопка "Создать" не доступна для нажатия'

    # Проверка есть ли элемент в списке по названию. название берется из user_data или txt
    def should_be_element_on_presale_list(self, user_data_dict):
        how, what = PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 2), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла.
    def go_to_presale_element(self, user_data_dict):
        how, what = PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        self.browser.find_element(how, what).click()

    # Перейти на вкладку "В оперплане"
    def go_to_in_op_elements_tab(self):
        assert self.is_visibility_of_element_located(*PresaleListLocators.IN_OP_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "В оперплане"'
        self.browser.find_element(*PresaleListLocators.IN_OP_ELEMENTS_TAB).click()

    # Перейти на вкладку "Вне оперплана"
    def go_to_out_op_elements_tab(self):
        assert self.is_visibility_of_element_located(*PresaleListLocators.OUT_OP_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Вне оперплана"'
        self.browser.find_element(*PresaleListLocators.OUT_OP_ELEMENTS_TAB).click()

    # Перейти на вкладку "На согласовании"
    def go_to_approval_elements_tab(self):
        assert self.is_visibility_of_element_located(*PresaleListLocators.APPROVAL_ELEMENTS_TAB, 10), \
            'Не отображена вкладка "На согласовании"'
        self.is_element_clickable(*PresaleListLocators.APPROVAL_ELEMENTS_TAB)
        self.browser.find_element(*PresaleListLocators.APPROVAL_ELEMENTS_TAB).click()

    # Перейти на вкладку "Отправлено"
    def go_to_sent_elements_tab(self):
        assert self.is_visibility_of_element_located(*PresaleListLocators.SENT_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Отправлено"'
        self.browser.find_element(*PresaleListLocators.SENT_ELEMENTS_TAB).click()

    # Перейти на вкладку "Мои"
    def go_to_mine_elements_tab(self):
        assert self.is_visibility_of_element_located(*PresaleListLocators.MINE_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Мои"'
        self.browser.find_element(*PresaleListLocators.MINE_ELEMENTS_TAB).click()

    # Перейти на вкладку "Все моего подразделения"
    def go_to_allmydepartment_tab(self):
        assert self.is_visibility_of_element_located(*PresaleListLocators.ALL_IN_MY_DEPARTMENT_TAB, 5), \
            'Не отображена вкладка "Все моего подразделения"'
        self.browser.find_element(*PresaleListLocators.ALL_IN_MY_DEPARTMENT_TAB).click()

    def verify_approval_status_in_presale_list(self):
        self.browser.implicitly_wait(1)
        exception_set = {"На согласовании"}
        actual_status_list = self.item_text_collector(*PresaleListLocators.APPROVAL_STATUS_VALUES)
        while self.is_visibility_of_element_located(*PresaleListLocators.PAGINATOR_NEXT_BUTTON, 0):
            self.browser.find_element(*PresaleListLocators.PAGINATOR_NEXT_BUTTON).click()
            actual_status_list += self.item_text_collector(*PresaleListLocators.APPROVAL_STATUS_VALUES)
        result = list(set(actual_status_list) - exception_set)
        assert len(result) == 0, 'Не корректные элементы на вкладке. ' \
                                 '\nОжидаемый результат: Отображены только сущности со статусом "На согласовании"' \
                                 f'\nФактический результат: Отображены сущности со статусом/ми: {result}'



