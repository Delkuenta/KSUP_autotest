import time

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import BasePageLocators, OpListLocators


class OppListPage(BasePage):
    # Поиск сущности в списке
    def should_be_element_on_operplan_list(self, department, year):
        # Снимаем фильтрацию по году:
        self.browser.find_element(*OpListLocators.YEAR_DROPDOWN_FILTER).click()
        time.sleep(2)
        self.browser.find_element(*OpListLocators.YEAR_CLEAR_FILTER).click()
        self.browser.find_element(*OpListLocators.YEAR_CLOSE_FILTER).click()
        time.sleep(1)
        name = "Оперплан " + department + " " + year
        how, what = OpListLocators.FIND_ELEMENT_IN_OPERPLAN_LIST
        what = what.replace("Test_name", name)
        assert self.is_visibility_of_element_located(how, what, 5), \
            f'Сущность "Заказчики и исполнители" с именем "{name}" не найдена в списке'

    # Кнопка создания пресейла на странице пресейла
    def create_opp(self, year):
        self.browser.implicitly_wait(2)
        assert self.is_element_clickable(*OpListLocators.OPERPLAN_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'
        self.browser.find_element(*OpListLocators.OPERPLAN_CREATE_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*OpListLocators.CREATE_IFRAME))
        Select(self.browser.find_element(*OpListLocators.YEAR_ELEMENT)).select_by_value(year)
        self.browser.find_element(*OpListLocators.CONFIRM_CREATE_OPERPLAN).click()
        self.is_disappeared(*OpListLocators.CREATE_WAITING_TITLE)
        self.is_frame_to_parent()

    # Переход к строкам оперплана
    def go_to_operplan_element(self, department, year):
        name = "Оперплан " + department + " " + year
        how, what = OpListLocators.FIND_ELEMENT_IN_OPERPLAN_LIST
        what = what.replace("Test_name", name)
        self.browser.find_element(how, what).click()

