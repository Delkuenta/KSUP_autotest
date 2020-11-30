from pages.base_page import BasePage
from pages.locators import ProjectListLocators


class ProjectPage(BasePage):

    # Кнопка создания пресейла на странице пресейла
    def go_to_create_project(self):
        button_create_presale = self.browser.find_element(*ProjectListLocators.PROJECT_CREATE_BUTTON)
        button_create_presale.click()

    # Проверка доступности кнопки создания пресейла
    def should_be_clickable_create_button(self):
        assert self.is_element_clickable(*ProjectListLocators.PROJECT_CREATE_BUTTON), \
            'Кнопка "Создать" не доступна для нажатия'

    # Проверка есть ли элемент в списке по названию. название берется из user_data или txt
    def should_be_element_on_project_list(self, user_data_dict):
        how, what = ProjectListLocators.FIND_ELEMENT_IN_PROJECT_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

    # Зайти внутрь сущности пресейла по названию.имя берется из файла.
    def go_to_project_element(self, user_data_dict):
        how, what = ProjectListLocators.FIND_ELEMENT_IN_PROJECT_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        self.browser.find_element(how, what).click()

    # Переход на вкладку "Интересно"
    def go_to_interested_elements_tab(self):
        self.is_visibility_of_element_located(*ProjectListLocators.INTERESTED_ELEMENTS_TAB, 5)
        self.browser.find_element(*ProjectListLocators.INTERESTED_ELEMENTS_TAB).click()

    def go_to_waiting_info_elements_tab(self):
        self.is_visibility_of_element_located(*ProjectListLocators.WAITING_INFORM_ELEMENTS_TAB, 5)
        self.browser.find_element(*ProjectListLocators.WAITING_INFORM_ELEMENTS_TAB).click()

    def go_to_info_enough_elements_tab(self):
        self.is_visibility_of_element_located(*ProjectListLocators.INFORMATION_ENOUGH_ELEMENTS_TAB, 5)
        self.browser.find_element(*ProjectListLocators.INFORMATION_ENOUGH_ELEMENTS_TAB).click()

    def go_to_not_info_enough_elements_tab(self):
        self.is_visibility_of_element_located(*ProjectListLocators.INFORMATION_NOT_ENOUGH_ELEMENTS_TAB, 5)
        self.browser.find_element(*ProjectListLocators.INFORMATION_NOT_ENOUGH_ELEMENTS_TAB).click()

    def go_to_not_interested_elements_tab(self):
        self.is_visibility_of_element_located(*ProjectListLocators.NOT_INTERESTED_ELEMENTS_TAB, 5)
        self.browser.find_element(*ProjectListLocators.NOT_INTERESTED_ELEMENTS_TAB).click()

    def go_to_waiting_interest_elements_tab(self):
        self.is_visibility_of_element_located(*ProjectListLocators.WAITING_INTEREST_ELEMENTS_TAB, 5)
        self.browser.find_element(*ProjectListLocators.WAITING_INTEREST_ELEMENTS_TAB).click()





