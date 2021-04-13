import time

import delayed_assert
from selenium.webdriver.support.select import Select
import random
from pages.base_page import BasePage
from pages.locators import FormCreateRequestSupportLocators
from userdata.user_data import UserData


class SupportFormCreate(BasePage):

    def form_create_request_support(self, user_data_dict):
        # Получаем рабочую почту из профиля
        work_email_in_profile = self.mail_in_user_profile(self.browser.current_url)

        # Проверяем предзаполнение рабочей почты
        prefill_email = self.browser.find_element(*FormCreateRequestSupportLocators.EMAIL_FIELD).get_attribute("value")
        print()
        delayed_assert.expect(work_email_in_profile.strip() == prefill_email,
                              'Некорректное предзаполнение в поле "Email"'
                              f'\n ОР: *{work_email_in_profile}*'
                              f'\n ФР *{prefill_email}*')
        # Заполняем поле "email" если отсутствует предзаполнение
        if len(prefill_email) == 0:
            self.browser.find_element(*FormCreateRequestSupportLocators.EMAIL_FIELD).send_keys(user_data_dict["email"])

        # Заполняем поле "Личный телефон"
        self.browser.find_element(*FormCreateRequestSupportLocators.PERSONAL_NUBMER_FIELD).send_keys(
            user_data_dict["personalNumber"])

        # Заполняем поле "Рабочий телефон"
        self.browser.find_element(*FormCreateRequestSupportLocators.WORK_NUMBER_FIELD).send_keys(
            user_data_dict["workNumber"])

        # Выбираем значение в поле "Тип запроса"
        Select(self.browser.find_element(*FormCreateRequestSupportLocators.TYPE_REQUEST_SELECT)).select_by_value(
            user_data_dict["typeRequest"])

        # Выбираем значение в поле "Классификация" группа
        Select(self.browser.find_element(*FormCreateRequestSupportLocators.CLASSIFICATION_GROUP_SELECT)).select_by_value(
            user_data_dict["classificationGroup"])
        time.sleep(2)
        # Выбираем значение в поле "Классификация" тип
        Select(self.browser.find_element(*FormCreateRequestSupportLocators.CLASSIFICATION_TYPE_SELECT)).select_by_visible_text(
            user_data_dict["classificationType"])

        # Заполняем поле "Тема"
        self.browser.find_element(*FormCreateRequestSupportLocators.THEME_FIELD).send_keys(user_data_dict["theme"])

        # Заполняем поле "Описание"
        self.browser.find_element(*FormCreateRequestSupportLocators.DESCRIPTION_FIELD).send_keys(user_data_dict["description"])

        # Прикрепляем файл
        self.browser.find_element(*FormCreateRequestSupportLocators.FILES_FIELD).send_keys(UserData.file_path_for_link_pdf)
        self.browser.find_element(*FormCreateRequestSupportLocators.SEND_BUTTON).click()

        self.is_visibility_of_element_located(*FormCreateRequestSupportLocators.TITLE_SEND_SUCCESS, 10)
        # Проверка успешной отправки запроса
        # Проверка тайтла
        delayed_assert.expect(self.is_element_text(*FormCreateRequestSupportLocators.TITLE_SEND_SUCCESS) == "Ваше обращение принято",
                              f"Некорректный заголовок страницы успешной отправки запроса в техподдержку\n"
                              f"ОР: Ваше обращение принято\n"
                              f"ФР: *{self.is_element_text(*FormCreateRequestSupportLocators.TITLE_SEND_SUCCESS)}*")

        # Проверка текста на странице успешной отправки
        delayed_assert.expect(self.is_element_text(*FormCreateRequestSupportLocators.TEXT_SEND_SUCCESS) == "Обращение доступно по ссылке -",
                              f"\nНекорректный текст на странице успешной отправки запроса в техподдержку"
                              f"\nОР: Обращение доступно по ссылке - "
                              f"\nФР: *{self.is_element_text(*FormCreateRequestSupportLocators.TEXT_SEND_SUCCESS)}*")

        link = "https://jira.lanit.ru/projects/KSUPS/issues/KSUPS"
        # Проверка отображения ссылки жиру на странице успешной отправки
        assert link in self.is_element_text(*FormCreateRequestSupportLocators.LINK_SEND_SUCCESS), \
            "\nНекорректная ссылка на странице успешной отправки" \
            f"\nОР: ссылка содержит - *{link}*" \
            f"\nФР: отображенная ссылка: {self.is_element_text(*FormCreateRequestSupportLocators.LINK_SEND_SUCCESS)}"

