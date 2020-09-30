from pages.base_page import BasePage
from pages.locators import ContractPageLocators
from userdata.user_data import UserData


class ContractPage(BasePage):

    # Поиск сущности в списке
    def should_be_element_on_contract_list(self,user_data_dict):
        how, what = ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_contract_element(self, user_data_dict):
        how, what = ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what), \
            f'Cущность с названием {user_data_dict["fullName"]} не найдена'
        self.browser.find_element(how, what).click()

    # Кнопка создания пресейла на странице пресейла
    def go_to_create_contract(self):
        assert self.is_element_clickable(
            *ContractPageLocators.CONTRACT_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'
        self.browser.find_element(*ContractPageLocators.CONTRACT_CREATE_BUTTON).click()
