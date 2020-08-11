from pages.base_page import BasePage
from pages.locators import ContractPageLocators
from userdata.user_data import UserData


class ContractPage(BasePage):

    # Поиск сущности в списке
    def should_be_element_on_contract_list(self):
        assert self.is_element_present(*ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST), \
            f'Пресейловая активность с именем "{UserData.user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_contract_element(self):
        assert self.is_element_present(*ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST), \
            f'Cущность с названием {UserData.user_data_dict["fullName"]} не найдена'
        self.browser.find_element(*ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST).click()

    # Кнопка создания пресейла на странице пресейла
    def go_to_create_contract(self):
        assert self.is_element_clickable(
            *ContractPageLocators.CONTRACT_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'
        self.browser.find_element(*ContractPageLocators.CONTRACT_CREATE_BUTTON).click()
