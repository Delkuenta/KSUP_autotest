from .base_page import BasePage
from pages.locators import PresaleListLocators
from userdata.user_data import UserData

class PresalePage(BasePage):

    #Кнопка создания пресейла на странице пресейла
    def go_to_create_presale(self):
        button_create_presale = self.browser.find_element(*PresaleListLocators.PRESALE_CREATE_BUTTON)
        button_create_presale.click()

    # Проверка доступности кнопки создания пресейла
    def should_be_clickable_create_button(self):
        assert self.is_element_clickable(*PresaleListLocators.PRESALE_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'

    # Проверка есть ли элемент в списке по названию. название берется из user_data или txt
    def should_be_element_on_presale_list(self):
        assert self.is_element_present(*PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST), \
            f'Пресейловая активность с именем "{UserData.user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_presale_element(self):
        self.browser.find_element(*PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST).click()