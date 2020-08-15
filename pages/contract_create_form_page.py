import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import FormCreateContractLocators
from userdata.user_data import UserData


class ContractFormCreate(BasePage):
    def form_create_contract_based_on_zakup(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT,
                                              UserData.user_data_dict["customer"])

        # Проверяем заголовок страницы
        assert self.is_element_text(*FormCreateContractLocators.CONTRACT_TITLE) == "Договор (контракт)"

        # Проверяем автоматическое предзаполнение от пресейла
        assert UserData.user_data_dict["customer"] in self.is_element_text(
            *FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Заказчик"

        assert UserData.user_data_dict["salesUnit"] in self.is_element_text(
            *FormCreateContractLocators.SALES_UNIT_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"

        assert UserData.user_data_dict["salesManager"] in \
            self.is_element_text(*FormCreateContractLocators.SALES_MANAGER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"

        assert UserData.user_data_dict["executiveUnit"] in self.is_element_text(
            *FormCreateContractLocators.EXECUTIVE_UNIT_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-исполнитель"

        assert UserData.user_data_dict["executiveManager"] in self.is_element_text(
            *FormCreateContractLocators.EXECUTIVE_MANAGER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"

        assert UserData.user_data_dict["executiveUnitLegal"] in self.is_element_text(
            *FormCreateContractLocators.EXECUTIVE_UNIT_LEGAL_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Исполнитель (юридическое лицо)"

        assert UserData.user_data_dict["fullName"] in self.is_element_text(
            *FormCreateContractLocators.PRESALE_SELECT), \
            "Некорректная информация в поле Пресейловые активности"

        assert UserData.user_data_dict["fullName"] in self.is_element_text(*FormCreateContractLocators.ZAKUP_SELECT), \
            "Некорректная информация в поле Связанная закупочная процедура"

        # Заполняем поле Номер
        self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).send_keys(
            UserData.user_data_dict["number_contract"])

        # Заполняем поле Ссылка на договор/контракт на Официальном сайте ЕИС
        self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).send_keys(
            UserData.user_data_dict["eis_contract_link"])

        # Выбираем значение в поле "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        self.browser.find_element(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT).click()
        for territory in UserData.user_data_dict["territory"]:
            TERRITORY_ELEMENT = (By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{territory}']")
            if self.is_element_present(*TERRITORY_ELEMENT):
                self.browser.find_element(*TERRITORY_ELEMENT).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 7
                while self.is_element_present(*TERRITORY_ELEMENT) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON_TERRITORY).click()
                    scrolls += 1
                self.browser.find_element(*TERRITORY_ELEMENT).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_element_present(*TERRITORY_ELEMENT) is False and scrolls == max_scrolls:
                    print(f"Не найдена территория  с именем {territory}")

        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        # возврат к основной форме
        self.is_frame_to_parent()
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TERRITORY_ELEMENT,
                                              f'{UserData.user_data_dict["territory"]};')

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        for technologies in UserData.user_data_dict["technologies"]:
            TECHNOLOGIES_ELEMENT = (By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{technologies}']")
            if self.is_element_present(*TECHNOLOGIES_ELEMENT):
                self.browser.find_element(*TECHNOLOGIES_ELEMENT).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 3
                while self.is_element_present(*TECHNOLOGIES_ELEMENT) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON_TECHNOLOGIES).click()
                    scrolls += 1

                self.browser.find_element(*TECHNOLOGIES_ELEMENT).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_element_present(*TECHNOLOGIES_ELEMENT) is False and scrolls == max_scrolls:
                    print(f"Не найдена технология с именем {technologies}")

        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        self.is_frame_to_parent()
        # Проверяем, строку
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TECHNOLOGIES_ELEMENT,
                                              f"{UserData.user_data_dict['technologies']};")

        # заполняем поле Количественные показатели реализации проекта
        self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).send_keys(
            UserData.user_data_dict["quantitative_indicators_project"])

        # Уникальный код проекта
        self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).send_keys(
            UserData.user_data_dict["project_unique_code"])

        # Выбираем связанный проект
        self.browser.find_element(*FormCreateContractLocators.PROJECT_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.PROJECT_FIND_ELEMENT).send_keys(
            UserData.user_data_dict["project"])
        self.browser.find_element(*FormCreateContractLocators.PROJECT_DROPDOWN_ELEMENT).click()

        # прикрепляем файл Контракт
        self.browser.find_element(*FormCreateContractLocators.FILE_CONTRACT).send_keys(UserData.file_path_for_link_doc)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_CONTRACT_NAME, UserData.name_doc_to_link)

        # прикрепляем файл Бюджет проекта
        self.browser.find_element(*FormCreateContractLocators.FILE_BUDGET_OF_PROJECT).send_keys(
            UserData.file_path_for_link_jpg)
        self.is_text_to_be_present_in_element(
            *FormCreateContractLocators.FILE_BUDGET_OF_PROJECT_NAME, UserData.name_jpg_to_link)

        # прикрепляем файл Пояснительная служебная записка
        self.browser.find_element(*FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(
            UserData.file_path_for_link_excel)
        self.is_text_to_be_present_in_element(
            *FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM_NAME, UserData.name_excel_to_link)

        # прикрепляем файл Реестр рисков, Карта рисков
        self.browser.find_element(*FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY).send_keys(
            UserData.file_path_for_link_jpg)
        self.is_text_to_be_present_in_element(
            *FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY_NAME, UserData.name_jpg_to_link)

        # прикрепляем файл Иное
        self.browser.find_element(*FormCreateContractLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_mp4)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_OTHER_NAME, UserData.name_mp4_to_link)

        # Жмем кнопку создать
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON).click()
        # Подтверждаем внесение изменений  в связанный проект
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CHANGE_PROJECT_BUTTON).click()
