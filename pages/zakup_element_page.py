from pages.base_page import BasePage
from pages.locators import ZakupPageLocators

class ZakupElementPage(BasePage):

    def go_to_create_zp_tender_based_on_presale(self):
        self.browser.find_element(*ZakupPageLocators.FIND_ELEMENT_IN_ZAKUP_LIST).click()

