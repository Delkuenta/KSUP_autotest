from .base_page import BasePage
from pages.locators import PresaleListLocators
from userdata.user_data import UserData


class PresalePage(BasePage):

    # Кнопка создания пресейла на странице пресейла
    def go_to_create_presale(self):
        button_create_presale = self.browser.find_element(*PresaleListLocators.PRESALE_CREATE_BUTTON)
        button_create_presale.click()

    # Проверка доступности кнопки создания пресейла
    def should_be_clickable_create_button(self):
        assert self.is_element_clickable(*PresaleListLocators.PRESALE_CREATE_BUTTON), \
            'Кнопка "Создать" не доступна для нажатия'

    # Проверка есть ли элемент в списке по названию. название берется из user_data или txt
    def should_be_element_on_presale_list(self, user_data_dict):
        how, what = PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла.
    def go_to_presale_element(self, user_data_dict):
        how, what = PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        self.browser.find_element(how, what).click()
