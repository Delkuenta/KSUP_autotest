import time

from pages.base_page import BasePage
from pages.locators import ContractListLocators


class ContractPage(BasePage):

    # Поиск сущности в списке
    def should_be_element_on_contract_list(self,user_data_dict):
        how, what = ContractListLocators.FIND_ELEMENT_IN_CONTRACT_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_contract_element(self, user_data_dict):
        time.sleep(2)
        how, what = ContractListLocators.FIND_ELEMENT_IN_CONTRACT_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Cущность с названием {user_data_dict["fullName"]} не найдена'
        self.browser.find_element(how, what).click()

    # Кнопка создания контракта
    def go_to_create_contract(self):
        assert self.is_element_clickable(
            *ContractListLocators.CONTRACT_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'
        self.browser.find_element(*ContractListLocators.CONTRACT_CREATE_BUTTON).click()

    # Перейти на вкладку "Мои"
    def go_to_mine_elements_tab(self):
        assert self.is_visibility_of_element_located(*ContractListLocators.MINE_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Мои"'
        self.browser.find_element(*ContractListLocators.MINE_ELEMENTS_TAB).click()

    # Перейти на вкладку "На согласовании"
    def go_to_approval_elements_tab(self):
        assert self.is_visibility_of_element_located(*ContractListLocators.APPROVAL_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "На согласовании"'
        self.browser.find_element(*ContractListLocators.APPROVAL_ELEMENTS_TAB).click()

    # Перейти на вкладку "Отклонено"
    def go_to_rejected_elements_tab(self):
        assert self.is_visibility_of_element_located(*ContractListLocators.REJECTED_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Отклонено"'
        self.browser.find_element(*ContractListLocators.REJECTED_ELEMENTS_TAB).click()

    # Перейти на вкладку "Согласовано"
    def go_to_approved_elements_tab(self):
        assert self.is_visibility_of_element_located(*ContractListLocators.APPROVED_ELEMENTS_TAB, 5), \
            'Не отображена вкладка "Согласовано"'
        self.browser.find_element(*ContractListLocators.APPROVED_ELEMENTS_TAB).click()

    # Перейти на вкладку "Все моего подразделения"
    def go_to_allmydepartment_tab(self):
        assert self.is_visibility_of_element_located(*ContractListLocators.ALL_IN_MY_DEPARTMENT_TAB, 5), \
            'Не отображена вкладка "Все моего подразделения"'
        self.browser.find_element(*ContractListLocators.ALL_IN_MY_DEPARTMENT_TAB).click()
