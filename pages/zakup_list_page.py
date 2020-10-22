from pages.base_page import BasePage
from pages.locators import ZakupListLocators
from userdata.user_data import UserData


class ZakupListPage(BasePage):

    def should_be_element_on_zakup_list(self,user_data_dict):
        how, what = ZakupListLocators.FIND_ELEMENT_IN_ZAKUP_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Проверка доступности кнопки создания закупочной процедуры
    def should_be_clickable_zakup_create_button(self):
        assert self.is_element_clickable(
            *ZakupListLocators.ZAKUP_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла или user_data.
    def go_to_zakup_element(self, user_data_dict):
        how, what = ZakupListLocators.FIND_ELEMENT_IN_ZAKUP_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Cущность с названием {user_data_dict["fullName"]} не найдена'
        self.browser.find_element(how, what).click()
