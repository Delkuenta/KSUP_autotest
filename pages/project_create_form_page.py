import time

from pages.base_page import BasePage
from pages.locators import FormCreateProjectLocators


class ProjectFormCreate(BasePage):

    # Форма создания пресейла
    def form_create_project(self, user_data_dict):
        # Ищем поле "Название проекта" и заполняем
        self.browser.find_element(*FormCreateProjectLocators.NAME_PROJECT_ELEMENT).send_keys(user_data_dict["fullName"])

        # Ищем поле "Ссылка на закупку на Официальном сайте ЕИС" и заполняем его
        self.browser.find_element(*FormCreateProjectLocators.EIS_PURCHSE_LINK_CONTRACT).send_keys(user_data_dict["eisPriceLink"])

        # Заполняем поле "Заказчик"
        self.browser.find_element(*FormCreateProjectLocators.CUSTOMER_ELEMENT).click()
        how, what = FormCreateProjectLocators.CUSTOMER_DROPDOWN_ELEMENT
        what = what.replace("customer_name", user_data_dict["customer"])
        self.browser.find_element(how, what).click()

        # Выбираем значение в поле "Отрасль"
        self.browser.find_element(*FormCreateProjectLocators.SEARCH_INDUSTRY_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()

        for industry in user_data_dict["industry"]:
            how, what = FormCreateProjectLocators.INDUSTRY_ELEMENT
            what = what.replace("industry_name", industry)
            if self.is_visibility_of_element_located(how, what):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateProjectLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 3
                while self.is_visibility_of_element_located(how, what) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*FormCreateProjectLocators.SCROLL_DOWN_BUTTON_INDUSTRY).click()
                    scrolls += 1
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateProjectLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_visibility_of_element_located(how, what) is False and scrolls == max_scrolls:
                    print(f"Не найдена территория  с именем {industry}")

        self.browser.find_element(*FormCreateProjectLocators.CONFIRM_IFRAME_BUTTON).click()
        # возврат к основной форме
        self.is_frame_to_parent()
        time.sleep(2)

        # Ищем кнопку "Тип работ и услуг"
        self.browser.find_element(*FormCreateProjectLocators.SEARCH_TYPE_AND_SERVICES_ELEMENT).click()
        time.sleep(2)

        # Работаем во фрейме и выбираем категории
        self.is_frame_to_be_available_and_switch_to_it()

        # Открываем все доступные категории
        if len(self.browser.find_elements(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT1)) == 1:
            self.browser.find_element(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT1).click()
        if len(self.browser.find_elements(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT2)) == 1:
            self.browser.find_element(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT2).click()
        if len(self.browser.find_elements(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT3)) == 1:
            self.browser.find_element(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT3).click()
        if len(self.browser.find_elements(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT4)) == 1:
            self.browser.find_element(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT4).click()
        if len(self.browser.find_elements(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT5)) == 1:
            self.browser.find_element(*FormCreateProjectLocators.GROUP_CATEGORY_ELEMENT5).click()

        # Выбираем нужный элемент
        for work_and_services in user_data_dict["typeOfWorkServices"]:
            how, what = FormCreateProjectLocators.WORK_AND_SERVICIES_ELEMENT
            what = what.replace("work_and_services_name", work_and_services)
            if self.is_visibility_of_element_located(how, what):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateProjectLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                self.browser.find_element(*FormCreateProjectLocators.SCROLL_DOWN_BUTTON).click()
                assert self.is_visibility_of_element_located(how, what) is True, \
                    f"Не найден тип работ и услуг с именем {work_and_services}"
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateProjectLocators.CHOICE_IFRAME_BUTTON).click()

        self.browser.find_element(*FormCreateProjectLocators.CONFIRM_IFRAME_BUTTON).click()

        # Возврат к форм создания.
        self.is_frame_to_parent()
        time.sleep(2)
        breakpoint()
