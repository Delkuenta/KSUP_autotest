from .base_page import BasePage
from .locators import PresalePageLocators
from .locators import PresaleElementLocators


class PresaleElementPage(BasePage):

    # Кнопка внутри пресейла для создания ЗП типа тендер (проверяем доступность и нажимаем)
    def go_to_create_zp_tender_based_on_presale(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.TENDER_APPLICATION_ELEMENT), \
            'Кнопка "Внести информацию о конкурсе" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.TENDER_APPLICATION_ELEMENT).click()

    # Кнопка внутри пресейла для создания ЗП типа "Внести информацию о запросе цен" (проверяем доступность и нажимаем)
    def go_to_create_zp_presale_аct_based_on_presale(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.PRESALE_ACT_ELEMENT), \
            'Кнопка Внести информацию о запросе цен" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.PRESALE_ACT_ELEMENT).click()

    # Кнопка внутри пресейла для создания ЗП типа "Внести информацию о коммерческом предложении" (проверяем
    # доступность и нажимаем)
    def go_to_create_zp_commercial_offer_based_on_presale(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.COMMERCIAL_OFFER_ELEMENT), \
            'Кнопка Внести информацию о запросе цен" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.COMMERCIAL_OFFER_ELEMENT).click()

    def go_to_create_contract_based_on_presale(self):
        self.browser.find_element(*PresaleElementLocators.CREATE_CONTRACT_ELEMENT).click()
