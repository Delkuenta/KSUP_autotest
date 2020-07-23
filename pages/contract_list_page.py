from pages.locators import ContractPageLocators
from userdata.user_data import UserData
from pages.base_page import BasePage


class ContractPage(BasePage):

    # Поиск сущности в списке
    def should_be_element_on_contract_list(self):
        assert self.is_element_present(*ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST), \
            f'Пресейловая активность с именем "{UserData.name_contract_based_on_zakup}" не найдена в списке'

    # Проверка доступности кнопки создания закупочной процедуры
    def should_be_clickable_contract_create_button(self):
        assert self.is_element_clickable(
            *ContractPageLocators.CONTRACT_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_contract_element(self):
        assert self.is_element_present(*ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST), \
            f'Cущность с названием {UserData.name_contract_based_on_zakup} не найдена'
        self.browser.find_element(*ContractPageLocators.FIND_ELEMENT_IN_CONTRACT_LIST).click()