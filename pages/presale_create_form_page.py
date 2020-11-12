import time
import pytest_check as check
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.locators import FormCreatePresaleLocators
import delayed_assert


class PresaleFormCreate(BasePage):
    # Форма создания пресейла
    def form_create_presale_all_type(self, user_data_dict):
        time.sleep(2)

        # Проверяем предзаполнение полей:
        # "Ответственный менеджер подразделения-продавца" и "Ответственный менеджер подразделения-исполнителя" для УЗ продавца
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller":
            delayed_assert.expect(self.is_element_text(*FormCreatePresaleLocators.SALES_MANAGER_ELEMENT_VALUE) ==
                                  user_data_dict["executiveManager"],
                                  f'Для роли {user_data_dict["createAccount"]} '
                                  f'поле "Ответственный менеджер подразделения-продавца" '
                                  f'должно быть предзаполненно значением: "{user_data_dict["executiveManager"]}"')
            # Баг https://jira.lanit.ru/browse/KSUP-1041
            delayed_assert.expect(self.is_element_text(*FormCreatePresaleLocators.EXECUTIVE_MANAGER_ELEMENT_VALUE) ==
                                  user_data_dict["executiveManager"],
                                  f'Для роли {user_data_dict["createAccount"]} '
                                  f'поле "Ответственный менеджер подразделения-исполнителя" '
                                  f'должно быть предзаполненно значением: "{user_data_dict["executiveManager"]}"')
        elif user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            delayed_assert.expect(self.is_element_text(*FormCreatePresaleLocators.SALES_MANAGER_ELEMENT_VALUE) ==
                                  user_data_dict["salesManager"],
                                  f'Для роли {user_data_dict["createAccount"]} '
                                  f'поле "Ответственный менеджер подразделения-продавца" '
                                  f'должно быть предзаполненно значением: "{user_data_dict["salesManager"]}"')
            # Баг https://jira.lanit.ru/browse/KSUP-1041
            delayed_assert.expect(self.is_element_text(*FormCreatePresaleLocators.EXECUTIVE_MANAGER_ELEMENT_VALUE) ==
                                  user_data_dict["salesManager"],
                                  f'Для роли {user_data_dict["createAccount"]} '
                                  f'поле "Ответственный менеджер подразделения-исполнителя" '
                                  f'должно быть предзаполненно значением: "{user_data_dict["salesManager"]}"')

        # Ищем поле "Предмет контракта" и заполняем
        self.browser.find_element(*FormCreatePresaleLocators.NAME_PRESALE_ELEMENT).send_keys(
            user_data_dict["fullName"])

        # Ищем поле "Способ определения поставщика" и выбираем значение
        Select(self.browser.find_element(*FormCreatePresaleLocators.CONTRACTOR_TYPE_ELEMENT)).select_by_value(
            user_data_dict["contractorType"])

        # Ищем поле "Заказчик" и выбираем значение
        how, what = FormCreatePresaleLocators.CUSTOMER_DROPDOWN_ELEMENT
        what = what.replace("customer_name", user_data_dict["customer"])
        self.browser.find_element(*FormCreatePresaleLocators.CUSTOMER_ELEMENT).click()
        self.browser.find_element(how, what).click()

        # Ищем поле "Подразделение-продавец" и выбираем значение
        how, what = FormCreatePresaleLocators.SALES_UNIT_DROPDOWN_ELEMENT
        what = what.replace("salesUnit_name", user_data_dict["salesUnit"])
        self.browser.find_element(*FormCreatePresaleLocators.SALES_UNIT_ELEMENT).click()
        self.browser.find_element(how, what).click()

        # Ищем поле "Ответственный менеджер подразделения-продавца" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.SALES_MANAGER_ELEMENT).click()
        if user_data_dict["separateSale"] == "Да":
            how, what = FormCreatePresaleLocators.SALES_MANAGER_DROPDOWN_ELEMENT
            what = what.replace("salesManager_name", user_data_dict["salesManager"])
            self.browser.find_element(how, what).click()
        else:
            if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or \
                    user_data_dict["createAccount"] == "Mr_KSUP_Dir":
                how, what = FormCreatePresaleLocators.EXECUTIVE_MANAGER_DROPDOWN_ELEMENT
                what = what.replace("executiveManager_name", user_data_dict["executiveManager"])
                self.browser.find_element(how, what).click()
            else:
                how, what = FormCreatePresaleLocators.SALES_MANAGER_DROPDOWN_ELEMENT
                what = what.replace("salesManager_name", user_data_dict["salesManager"])
                self.browser.find_element(how, what).click()

        # Ищем поле "Подразделение-исполнитель" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_UNIT_ELEMENT).click()
        how, what = FormCreatePresaleLocators.EXECUTIVE_UNIT_DROPDOWN_ELEMENT
        what = what.replace("executiveUnit_name", user_data_dict["executiveUnit"])
        self.browser.find_element(how, what).click()

        # Ищем поле "Ответственный менеджер подразделения-исполнителя" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_MANAGER_ELEMENT).click()
        if user_data_dict["separateSale"] == "Да":
            how, what = FormCreatePresaleLocators.EXECUTIVE_MANAGER_DROPDOWN_ELEMENT
            what = what.replace("executiveManager_name", user_data_dict["executiveManager"])
            self.browser.find_element(how, what).click()
        else:
            if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or \
                    user_data_dict["createAccount"] == "Mr_KSUP_Dir":
                how, what = FormCreatePresaleLocators.EXECUTIVE_MANAGER_DROPDOWN_ELEMENT
                what = what.replace("executiveManager_name", user_data_dict["executiveManager"])
                self.browser.find_element(how, what).click()
            else:
                how, what = FormCreatePresaleLocators.SALES_MANAGER_DROPDOWN_ELEMENT
                what = what.replace("salesManager_name", user_data_dict["salesManager"])
                self.browser.find_element(how, what).click()

        # Ищем поле "Исполнитель (юридическое лицо)" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_UNIT_LEGAL_ELEMENT).click()
        how, what = FormCreatePresaleLocators.EXECUTIVE_UNIT_LEGAL_DROPDOWN_ELEMENT
        what = what.replace("executiveUnitLegal_name", user_data_dict["executiveUnitLegal"])
        self.browser.find_element(how, what).click()

        # Проверка отображения поля Порядок проведения закупочной процедуры
        if user_data_dict["contractorType"] == "Тендерная заявка" \
                or user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            assert self.is_visibility_of_element_located(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT, 3), \
                f'Ошибка: При выбранном способе определения поставщика: {user_data_dict["contractorType"]} ' \
                f'не отображено поле: "Порядок проведения закупочной процедуры"'

            # Ищем поле "Порядок проведения закупочной процедуры" и выбираем значение из выпадающего списка
            sale_law_type_element = Select(
                self.browser.find_element(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT))
            sale_law_type_element.select_by_value(user_data_dict["saleLawType"])

        if user_data_dict["contractorType"] == "Коммерческое предложение" \
                or user_data_dict["contractorType"] == "Информация отсутствует":
            assert self.browser.find_element(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT).is_displayed() is False, \
                f'Ошибка: При выбранном Способе определения поставщика: {user_data_dict["contractorType"]} ' \
                f'поле "Порядок проведения закупочной" процедуры не должно отображаться'

        # Ищем кнопку "Тип работ и услуг"
        self.browser.find_element(*FormCreatePresaleLocators.SEARCH_VALID_OPTION_ELEMENT).click()
        time.sleep(2)

        # Выбираем элементы во фрейме "Тип работ и услуг"
        self.select_in_frame_type_work_and_services(user_data_dict["typeOfWorkServices"])

        # Ищем поле "Сумма" и вводим значение
        self.browser.find_element(*FormCreatePresaleLocators.SUM_ELEMENT).send_keys(user_data_dict["sum"])

        # Ищем поле "Валюта" и выбираем значение
        Select(self.browser.find_element(*FormCreatePresaleLocators.CURRENCY_ELEMENT)).select_by_value(
            user_data_dict["currency"])

        # Ищем поле "Размер обеспечения заявки" и вводим значение
        self.browser.find_element(*FormCreatePresaleLocators.APPLICATION_SIZE_ELEMENT).send_keys(
            user_data_dict["applicationSize"])

        # Ищем поле "Размер обеспечения договора/контракта" и заполняем его
        self.browser.find_element(*FormCreatePresaleLocators.CONTRACT_SIZE_ELEMENT).send_keys(
            user_data_dict["contractSize"])

        # Ищем поле "Самостоятельная продажа" и выбираем значение
        Select(self.browser.find_element(*FormCreatePresaleLocators.SEPARATE_SALE_ELEMENT)).select_by_value(
            user_data_dict["separateSale"])

        # Ищем поле "Плановый срок подачи на конкурс" и вводим значение
        competition_deadline_from_element = self.browser.find_element(
            *FormCreatePresaleLocators.COMPETITION_DEADLINE_FROM_ELEMENT)
        competition_deadline_from_element.send_keys(user_data_dict["competitionDeadlineFrom"])

        # Ищем поле "Плановая дата заключения договора/контракта" и вводим значение
        plan_date_contract_conclusion_element = self.browser.find_element(
            *FormCreatePresaleLocators.PLAN_DATE_CONTRACT_CONCLUSION_ELEMENT)
        plan_date_contract_conclusion_element.send_keys(user_data_dict["startDate"])

        # Ищем поле "Плановая дата окончания договора/контракта" и вводим значение
        plan_date_contract_finish_element = self.browser.find_element(
            *FormCreatePresaleLocators.PLAN_DATE_CONTRACT_FINISH_ELEMENT)
        plan_date_contract_finish_element.send_keys(user_data_dict["endDate"])

        # Ищем поле "Вероятность заключения договора/контракта" и вводим значение
        project_probability_element = self.browser.find_element(*FormCreatePresaleLocators.PROJECT_PROBABILITY_ELEMENT)
        project_probability_element.send_keys(user_data_dict["projectProbability"])

        # Ищем поле "Краткое описание" и вводим значение
        description_plain_text_element = self.browser.find_element(
            *FormCreatePresaleLocators.DESCRIPTION_PLAIN_TEXT_ELEMENT)
        description_plain_text_element.send_keys(user_data_dict["descriptionText"])

        # Ищем поле "Риски" и вводим значение
        risks_element = self.browser.find_element(*FormCreatePresaleLocators.RISKS_ELEMENT)
        risks_element.send_keys(user_data_dict["risksText"])

        # Заполняем таблицу плановых платежей
        payments_sum = 0
        count_payments_line = len(user_data_dict["payments"])
        print(f'\nКоличество строчек плановых платежей: {count_payments_line}')
        current_line = 0
        while current_line < count_payments_line:
            # Заполняем поле "Сумма" в текущей строке
            sum_field = self.browser.find_elements(*FormCreatePresaleLocators.SUMTABLE)[current_line]
            sum_field.send_keys(user_data_dict["payments"][current_line]["sum"])

            # Заполняем поле "Год" в текущей строке
            year_field = self.browser.find_elements(*FormCreatePresaleLocators.YEARTABLE)[current_line]
            year_field.send_keys(user_data_dict["payments"][current_line]["year"])

            # Заполняем поле "Квартал" в текущей строке
            quarter_field = self.browser.find_elements(*FormCreatePresaleLocators.QUARTERTABLE)[current_line]
            Select(quarter_field).select_by_visible_text(
                f'{user_data_dict["payments"][current_line]["quarter"]} квартал')

            payments_sum += user_data_dict["payments"][current_line]["sum"]
            current_line += 1

        # Если сумма платежей не совпадает появляется алерт, при подтверждении сущность создается
        # Баг - отображено два одинаковых алерта, убрать один после фикса
        if payments_sum != user_data_dict["sum"]:
            confirm_presale_button = self.browser.find_element(*FormCreatePresaleLocators.CONFIRM_PRESALE_BUTTON)
            confirm_presale_button.click()
            time.sleep(1)
            alert = self.browser.switch_to.alert
            # Дублирующий алерт некорректных платежей
            alert.accept()
            if user_data_dict["separateSale"] == "Да":
                alert.accept()
            else:
                # Алерт отправки на согласование в дирекции или департамент
                self.browser.switch_to.alert.accept()
                self.browser.switch_to.frame(self.browser.find_element(*FormCreatePresaleLocators.iframe))
                self.browser.find_element(*FormCreatePresaleLocators.APPROVAL_DEPARTMENT_ELEMENT).click()
                self.browser.find_element(*FormCreatePresaleLocators.SALES_UNIT_DROPDOWN_ELEMENT).click()
                self.browser.find_element(*FormCreatePresaleLocators.APPROVAL_CONFIRM_SEND_BUTTON).click()
                # Дублирующий алерт некорректных платежей
                alert.accept()
        else:
            confirm_presale_button = self.browser.find_element(*FormCreatePresaleLocators.CONFIRM_PRESALE_BUTTON)
            confirm_presale_button.click()
            if user_data_dict["separateSale"] == "Нет":
                self.browser.switch_to.alert.accept()
                self.browser.switch_to.frame(self.browser.find_element(*FormCreatePresaleLocators.iframe))
                if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or \
                        user_data_dict["createAccount"] == "Mr_KSUP_Dir":

                    # Проверяем предзаполнение поля "Подразделение"
                    delayed_assert.expect(
                        self.is_element_text(*FormCreatePresaleLocators.APPROVAL_DEPARTMENT_ELEMENT) == user_data_dict[
                            "salesUnit"],
                        f'При отправке на согласование под ролью {user_data_dict["createAccount"]} '
                        f'поле "Подразделение" должно предзаполняться значением из поля "Подразделение-продавец"')
                    self.browser.find_element(*FormCreatePresaleLocators.APPROVAL_DEPARTMENT_ELEMENT).click()
                    how, what = FormCreatePresaleLocators.SALES_UNIT_DROPDOWN_ELEMENT
                    what = what.replace("salesUnit_name", user_data_dict["salesUnit"])
                    self.browser.find_element(how, what).click()
                else:
                    # Проверяем предзаполнение поля "Подразделение"
                    delayed_assert.expect(
                        self.is_element_text(*FormCreatePresaleLocators.APPROVAL_DEPARTMENT_ELEMENT) == user_data_dict[
                            "executiveUnit"],
                        f'При отправке на согласование под ролью {user_data_dict["createAccount"]} '
                        f'поле "Подразделение" должно предзаполняться значением из поля "Подразделение-исполнитель"')
                    self.browser.find_element(*FormCreatePresaleLocators.APPROVAL_DEPARTMENT_ELEMENT).click()
                    how, what = FormCreatePresaleLocators.EXECUTIVE_UNIT_DROPDOWN_ELEMENT
                    what = what.replace("executiveUnit_name", user_data_dict["executiveUnit"])
                    self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreatePresaleLocators.APPROVAL_CONFIRM_SEND_BUTTON).click()
