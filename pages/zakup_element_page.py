from pages.base_page import BasePage
from pages.locators import ZakupElementLocators
from userdata.user_data import UserData


class ZakupElementPage(BasePage):

    def verify_price_category_zakup(self):
        if UserData.user_data_dict["currency"] == "Доллар":
            sum_in_rub = UserData.user_data_dict["sum"] * 70
        elif UserData.user_data_dict["currency"] == "Евро":
            sum_in_rub = UserData.user_data_dict["sum"] * 80
        else:
            sum_in_rub = UserData.user_data_dict["sum"]

        price_category = ""
        if sum_in_rub >= 50000000:
            price_category = "A"
            assert self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_ELEMENT_IN_ZP) == price_category, \
                "Ценовая категория проекта не корректна"
        elif 30000000 <= sum_in_rub < 50000000:
            price_category = "B"
            assert self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_ELEMENT_IN_ZP) == price_category, \
                "Ценовая категория проекта не корректна"
        elif sum_in_rub < 30000000:
            price_category = "C"

        assert self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_ELEMENT_IN_ZP) == price_category, \
            f"Ценовая категория проекта не корректна, сумма контракта: {sum_in_rub}, " \
            f"\nтекущая категория сущности: {self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_ELEMENT_IN_ZP)}"




