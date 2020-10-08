from pages.base_page import BasePage
from pages.locators import ProjectPageLocators


class ProjectPage(BasePage):

    # Кнопка создания пресейла на странице пресейла
    def go_to_create_project(self):
        button_create_presale = self.browser.find_element(*ProjectPageLocators.PROJECT_CREATE_BUTTON)
        button_create_presale.click()

    # Проверка доступности кнопки создания пресейла
    def should_be_clickable_create_button(self):
        assert self.is_element_clickable(*ProjectPageLocators.PROJECT_CREATE_BUTTON), \
            'Кнопка "Создать" не доступна для нажатия'

    # Проверка есть ли элемент в списке по названию. название берется из user_data или txt
    def should_be_element_on_project_list(self, user_data_dict):
        how, what = ProjectPageLocators.FIND_ELEMENT_IN_PROJECT_LIST
        what = what.replace("Test_name", user_data_dict["fullName"])
        assert self.is_visibility_of_element_located(how, what), \
            f'Пресейловая активность с именем "{user_data_dict["fullName"]}" не найдена в списке'

