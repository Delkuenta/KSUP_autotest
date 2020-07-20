
from .base_page import BasePage
from .locators import PresalePageLocators


class PresalePage(BasePage):
    def should_be_clickable_create_button(self):
        assert self.is_element_clickable(*PresalePageLocators.PRESALE_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'
