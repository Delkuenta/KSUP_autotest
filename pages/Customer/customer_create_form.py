import time

import delayed_assert
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import FormCreateCustomerLocators


class CustomerFormCreate(BasePage):

    def create_customer_form(self, user_data_dict):
        # Вводим ОГРН в окне "Введите ОГРН/ОГРНИП"
        self.browser.find_element(*FormCreateCustomerLocators.OGRN_ELEMENT).click()
        self.browser.find_element(*FormCreateCustomerLocators.SEARCH_OGRN_ELEMENT).send_keys(user_data_dict["ogrn"])

        # Выбираем найденное значение
        how, what = FormCreateCustomerLocators.OGRN_DROPDOWN_ELEMENT
        what = what.replace("customer_ogrn", str(user_data_dict["ogrn"]))
        self.browser.find_element(how, what).click()

        # Жмем кнопку "ок"
        self.browser.find_element(*FormCreateCustomerLocators.CONFIRM_BUTTON).click()

        # Проверяем название формы в зависимости от ОГРН
        if len(str(user_data_dict["ogrn"])) == 13:
            assert self.is_text_to_be_present_in_element(*FormCreateCustomerLocators.TITLE_IN_CUSTOMER_FORM,
                                                         "Юридическое лицо")
        else:
            assert self.is_text_to_be_present_in_element(*FormCreateCustomerLocators.TITLE_IN_CUSTOMER_FORM,
                                                         "Индивидуальный предприниматель")

        # Нажимаем кнопку "Поиск допустимого варианта" у поля "Отрасль"
        self.browser.find_element(*FormCreateCustomerLocators.SEARCH_INDUSTRY_BUTTON).click()
        time.sleep(2)

        # Выбираем нужное значение
        self.select_elements_in_frame(user_data_dict["industry"], 2)
        self.is_text_to_be_present_in_element(*FormCreateCustomerLocators.INDUSTRY_FIELD, user_data_dict["industry"])

        # Выбираем значение в выпадающем списке "Значимость *"
        Select(self.browser.find_element(*FormCreateCustomerLocators.SIGNIFICANCE_ELEMENT)).select_by_value(
            user_data_dict["significance"])

        # Ищем поле "Описание" и вводим значение
        self.browser.find_element(*FormCreateCustomerLocators.DESCRIPTION_FIELD).send_keys(
            user_data_dict["description"])

        # Ищем поле "Контактные лица" и вводим значение
        self.browser.find_element(*FormCreateCustomerLocators.CONTACT_PERSONS_FIELD).send_keys(
            user_data_dict["сontactPersons"])

        # Ищем поле "Конкуренты ЛАНИТ" и вводим значение
        self.browser.find_element(*FormCreateCustomerLocators.COMPETITORS_FIELD).send_keys(
            user_data_dict["сompetitors"])

        # Ищем поле "Сайт" и вводим значение
        self.browser.find_element(*FormCreateCustomerLocators.SITE_FIELD).send_keys(user_data_dict["site"])

        # Ищем поле "Статус взаимодействия" и выбираем значение
        Select(self.browser.find_element(*FormCreateCustomerLocators.INTERACTION_STATUS_FIELD)).select_by_value(
            user_data_dict["interactionStatus"])

        if user_data_dict["createAccount"] != "Mr_KSUP_Admin":
            # Проверяем отображение поля "Дирекция, ответственная за взаимодействие"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.DIRECTION_ELEMENT).is_displayed() is False,
                'Отображено поле "Дирекция, ответственная за взаимодействие". '
                'Данное поле отображается только под ролью Admin')

            # Проверяем отображение поля "Департаменты, ответственные за взаимодействие"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.DIVISION_ELEMENT).is_displayed() is False,
                'Отображено поле "Департаменты, ответственные за взаимодействие". '
                'Данное поле отображается только под ролью Admin')

            # Проверяем отображение чек-бокса "ГК ЛАНИТ"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.IS_LANIT_CHECKBOX).is_displayed() is False,
                'Отображен чек-бокс "ГК ЛАНИТ". '
                'Данный чек-бокс отображается только под ролью Admin')

            # Проверяем не отображение поля "Руководители"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.CUSTOMER_HEAD_FIELD).is_displayed() is False,
                'Отображено поле "Руководители". '
                'Данный чек-бокс отображается только под ролью Admin')

            # Проверяем  не отображение чек-бокса "Уведомлять руководителя"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.SHOULD_NOTIFY_CHECKBOX).is_displayed() is False,
                'Отображен чек-бокс "Уведомлять руководителя". '
                'Данный чек-бокс отображается только под ролью Admin')

            # Проверяем не отображение чек-боксов поля "Уведомлять о"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.NOTIFY_ABOUT_FIELD).is_displayed() is False,
                'Отображено поле с чек-боксами "Уведомлять о". '
                'Данный чек-бокс отображается только под ролью Admin')
        else:
            # Ищем поле "Дирекция, ответственная за взаимодействие" и выбираем значение
            self.browser.find_element(*FormCreateCustomerLocators.DIRECTION_ELEMENT).click()
            self.browser.find_element(*FormCreateCustomerLocators.DIRECTION_SEARCH_FIELD).send_keys(user_data_dict["direction"])
            how, what = FormCreateCustomerLocators.DIRECTION_DROPDOWN_ELEMENT
            what = what.replace("direction_name", user_data_dict["direction"])
            self.browser.find_element(how, what).click()

            # Ищем поле "Департаменты, ответственные за взаимодействие
            for element in user_data_dict["department"]:
                self.browser.find_element(*FormCreateCustomerLocators.DIVISION_ELEMENT).click()
                self.browser.find_element(*FormCreateCustomerLocators.DIVISION_SEARCH_FIELD).send_keys(element)
                how, what = FormCreateCustomerLocators.DIVISION_DROPDOWN_ELEMENT
                what = what.replace("division_name", element)
                self.browser.find_element(how, what).click()

            # Проверяем деактивацию чек-бокса "ГК ЛАНИТ"
            assert self.browser.find_element(*FormCreateCustomerLocators.IS_LANIT_CHECKBOX).get_attribute(
                "checked") is None, \
                'Чек-бокс "ГК ЛАНИТ" по умолчанию активирован'

            # Проверяем не отображение поля "Руководители"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.CUSTOMER_HEAD_FIELD).is_displayed() is False,
                'Отображено поле "Руководители". '
                'Данный чек-бокс отображается только под ролью Admin')

            # Проверяем не отображение чек-бокса "Уведомлять руководителя"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.SHOULD_NOTIFY_CHECKBOX).is_displayed() is False,
                'Отображен чек-бокс "Уведомлять руководителя". '
                'Данный чек-бокс отображается только под ролью Admin')

            # Проверяем не отображение чек-боксов поля "Уведомлять о"
            delayed_assert.expect(
                self.browser.find_element(*FormCreateCustomerLocators.NOTIFY_ABOUT_FIELD).is_displayed() is False,
                'Отображено поле с чек-боксами "Уведомлять о". '
                'Данный чек-бокс отображается только под ролью Admin')

            if user_data_dict["gklanit"] == 1:
                # Активируем чек-бокс "ГК ЛАНИТ"
                self.browser.find_element(*FormCreateCustomerLocators.IS_LANIT_CHECKBOX).click()

                # Проверяем отображение поля "Руководители"
                delayed_assert.expect(
                    self.browser.find_element(*FormCreateCustomerLocators.CUSTOMER_HEAD_FIELD).is_displayed(),
                    'Не отображено поле "Руководители" после активации чек-бокс "ГК ЛАНИТ".')

                # Проверяем отображение чек-бокса "Уведомлять руководителя"
                delayed_assert.expect(
                    self.browser.find_element(*FormCreateCustomerLocators.SHOULD_NOTIFY_CHECKBOX).is_displayed(),
                    'Не отображен чек-бокс "Уведомлять руководителя" после активации чек-бокса "ГК ЛАНИТ".')

                # Проверяем деактивацию чек-бокса "Уведомлять руководителя"
                assert self.browser.find_element(*FormCreateCustomerLocators.SHOULD_NOTIFY_CHECKBOX).get_attribute(
                    "checked") is None, \
                    'Чек-бокс "Уведомлять руководителя" по умолчанию активирован'

                # Проверяем не отображение чек-боксов поля "Уведомлять о"
                delayed_assert.expect(
                    self.browser.find_element(*FormCreateCustomerLocators.NOTIFY_ABOUT_FIELD).is_displayed() is False,
                    'Отображено поле с чек-боксами "Уведомлять о". '
                    'Данный чек-бокс отображается только под ролью Admin')
                # Заполняем поле "Руководители"

                if len(user_data_dict["egrulHead"]) > 0:
                    for element in user_data_dict["egrulHead"]:
                        self.browser.find_element(*FormCreateCustomerLocators.CUSTOMER_HEAD_FIELD).send_keys(element)
                        how, what = FormCreateCustomerLocators.CUSTOMER_HEAD_DROPDOWN_ELEMENT
                        what = what.replace("name", element)
                        self.browser.find_element(how, what).click()

                if user_data_dict["notifyHead"] == 1:
                    # Активируем чек-бокс "Уведомлять руководителя"
                    self.browser.find_element(*FormCreateCustomerLocators.SHOULD_NOTIFY_CHECKBOX).click()

                    # Проверяем отображение поля "Уведомлять о"
                    assert self.browser.find_element(*FormCreateCustomerLocators.NOTIFY_ABOUT_FIELD).is_displayed(), \
                        'Не отображено поле "Уведомлять о" после активации чек-бокс "Уведомлять руководителя".'

                    # Активируем чек-боксы в поле "Уведомлять о"
                    for element in user_data_dict["notifyAbout"]:
                        how, what = FormCreateCustomerLocators.NOTIFY_ABOUT_CHECKBOX
                        what = what.replace("name", element)
                        self.browser.find_element(how, what).click()

                # Заполняем поле "Сотрудники юридической службы"
                if len(user_data_dict["ServiceEmployeeLegal"]) > 0:
                    for element in user_data_dict["ServiceEmployeeLegal"]:
                        self.browser.find_element(*FormCreateCustomerLocators.EMPLOYEE_LEGAL_FIELD).send_keys(element)
                        how, what = FormCreateCustomerLocators.EMPLOYEE_LEGAL_DROPDOWN_ELEMENT
                        what = what.replace("name", element)
                        self.browser.find_element(how, what).click()

                # Заполняем поле "Сотрудники бухгалтерии"
                if len(user_data_dict["ServiceEmployeeCount"]) > 0:
                    for element in user_data_dict["ServiceEmployeeCount"]:
                        self.browser.find_element(*FormCreateCustomerLocators.EMPLOYEE_COUNT_FIELD).send_keys(element)
                        how, what = FormCreateCustomerLocators.EMPLOYEE_COUNT_DROPDOWN_ELEMENT
                        what = what.replace("name", element)
                        self.browser.find_element(how, what).click()

                # Заполняем поле "Сотрудники финансовой службы"
                if len(user_data_dict["ServiceEmployeeFin"]) > 0:
                    for element in user_data_dict["ServiceEmployeeFin"]:
                        self.browser.find_element(*FormCreateCustomerLocators.EMPLOYEE_FIN_FIELD).send_keys(element)
                        how, what = FormCreateCustomerLocators.EMPLOYEE_FIN_DROPDOWN_ELEMENT
                        what = what.replace("name", element)
                        self.browser.find_element(how, what).click()

        # Жмем кнопку "Создать"
        self.browser.find_element(*FormCreateCustomerLocators.CONFIRM_CREATE_BUTTON).click()
