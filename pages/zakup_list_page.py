from .base_page import BasePage
from .locators import ZakupPageLocators
from userdata.user_data import UserData
from .locators import ZakupElementLocators

class ZakupPage(BasePage):

    def should_be_element_on_zakup_list(self):
        assert self.is_element_present(*ZakupPageLocators.FIND_ELEMENT_IN_ZAKUP_LIST), \
            f'Пресейловая активность с именем "{UserData.name_zp_based_on_presale}" не найдена в списке'

    # Проверка доступности кнопки создания закупочной процедуры
    def should_be_clickable_zakup_create_button(self):
        assert self.is_element_clickable(
            *ZakupPageLocators.ZAKUP_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_zakup_element(self):
        assert self.is_element_present(*ZakupPageLocators.FIND_ELEMENT_IN_ZAKUP_LIST), \
            f'Cущность с названием {UserData.name_zp_based_on_presale} не найдена'
        self.browser.find_element(*ZakupPageLocators.FIND_ELEMENT_IN_ZAKUP_LIST).click()

