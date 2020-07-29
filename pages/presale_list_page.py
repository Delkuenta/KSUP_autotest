from .base_page import BasePage
from .locators import PresalePageLocators
from .locators import FormCreatePresaleLocators
from .locators import FormCreateZakupLocators

from userdata.user_data import UserData
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class PresalePage(BasePage):
    #Кнопка создания пресейла на странице пресейла
    def go_to_create_presale(self):
        button_create_presale = self.browser.find_element(*PresalePageLocators.PRESALE_CREATE_BUTTON)
        button_create_presale.click()

    # Проверка доступности кнопки создания пресейла
    def should_be_clickable_create_button(self):
        assert self.is_element_clickable(*PresalePageLocators.PRESALE_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'

    # Проверка есть ли элемент в списке по названию. название берется из user_data или txt
    def should_be_element_on_presale_list(self):
        assert self.is_element_present(*PresalePageLocators.FIND_ELEMENT_IN_PRESALE_LIST), \
            f'Пресейловая активность с именем "{UserData.name_presale}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_presale_element(self):
        self.browser.find_element(*PresalePageLocators.FIND_ELEMENT_IN_PRESALE_LIST).click()