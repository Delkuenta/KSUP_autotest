import time

from pages.base_page import BasePage
from pages.locators import CustomerListLocators


class CustomerPage(BasePage):

    # Поиск сущности в списке
    def should_be_element_on_customer_list(self, user_data_dict):
        how, what = CustomerListLocators.FIND_ELEMENT_IN_CUSTOMER_LIST
        what = what.replace("Test_name", user_data_dict["shortName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Сущность "Заказчики и исполнители" с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_customer_element(self, user_data_dict):
        how, what = CustomerListLocators.FIND_ELEMENT_IN_CUSTOMER_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Cущность с названием {user_data_dict["fullName"]} не найдена'
        self.browser.find_element(how, what).click()

    # Кнопка создания пресейла на странице пресейла
    def go_to_create_customer(self):
        assert self.is_element_clickable(*CustomerListLocators.CUSTOMER_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'
        self.browser.find_element(*CustomerListLocators.CUSTOMER_CREATE_BUTTON).click()

    def go_to_all_tab(self):
        self.is_visibility_of_element_located(*CustomerListLocators.ALL_ELEMENTS_TAB, 5)
        self.browser.find_element(*CustomerListLocators.ALL_ELEMENTS_TAB).click()

    def go_to_gklanit_tab(self):
        self.is_visibility_of_element_located(*CustomerListLocators.GK_LANIT_ELEMENTS_TAB, 5)
        self.browser.find_element(*CustomerListLocators.GK_LANIT_ELEMENTS_TAB).click()

    def go_to_ip_tab(self):
        self.is_visibility_of_element_located(*CustomerListLocators.IP_ELEMENTS_TAB, 5)
        self.browser.find_element(*CustomerListLocators.IP_ELEMENTS_TAB).click()

    def go_to_ul_tab(self):
        self.is_visibility_of_element_located(*CustomerListLocators.UL_ELEMENTS_TAB, 5)
        self.browser.find_element(*CustomerListLocators.UL_ELEMENTS_TAB).click()
