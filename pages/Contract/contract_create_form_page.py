import time

import pytest_check as check
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import FormCreateContractLocators
from userdata.user_data import UserData
import delayed_assert


class ContractFormCreate(BasePage):
    def form_create_contract_based_on_zakup(self, user_data_dict):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT,
                                              user_data_dict["customer"])

        # Проверяем заголовок страницы
        assert self.is_element_text(*FormCreateContractLocators.CONTRACT_TITLE) == "Договор (контракт)"

        # Проверяем автоматическое предзаполнение от пресейла
        assert user_data_dict["customer"] in self.is_element_text(
            *FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Заказчик"

        assert user_data_dict["salesUnit"] in self.is_element_text(
            *FormCreateContractLocators.SALES_UNIT_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"

        assert user_data_dict["salesManager"] in \
               self.is_element_text(*FormCreateContractLocators.SALES_MANAGER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"

        assert user_data_dict["executiveUnit"] in self.is_element_text(
            *FormCreateContractLocators.EXECUTIVE_UNIT_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-исполнитель"

        assert user_data_dict["executiveManager"] in self.is_element_text(
            *FormCreateContractLocators.EXECUTIVE_MANAGER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"

        assert user_data_dict["executiveUnitLegal"] in self.is_element_text(
            *FormCreateContractLocators.EXECUTIVE_UNIT_LEGAL_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Исполнитель (юридическое лицо)"

        assert user_data_dict["fullName"] in self.is_element_text(
            *FormCreateContractLocators.PRESALE_SELECT), \
            "Некорректная информация в поле Пресейловые активности"

        # assert user_data_dict["fullName"] in self.is_element_text(*FormCreateContractLocators.ZAKUP_SELECT), \
        # "Некорректная информация в поле Связанная закупочная процедура"

        # Заполняем поле Номер
        self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).send_keys(
            user_data_dict["numberContract"])

        # Заполняем поле "Дата заключения"
        # Для типа "Тендерная заявка" и "Коммерческое предложение" поле "Дата заключения" предзаполняется
        if user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            self.browser.find_element(*FormCreateContractLocators.START_DATE_CONTRACT).send_keys(
                user_data_dict["startDate"])

        # Для типа "Тендерная заявка" поля "номер закупки" и "Ссылка на закупку" предзаполняются
        if user_data_dict["contractorType"] != "Тендерная заявка":
            # Заполняем поле "Номер закупки"
            self.browser.find_element(*FormCreateContractLocators.EIS_PURCHASE_NUMBER_CONTRACT).send_keys(
                user_data_dict["purchaseNumber"])

            # Заполняем поле "Ссылка на закупку"
            self.browser.find_element(*FormCreateContractLocators.EIS_PURCHSE_LINK_CONTRACT).send_keys(
                user_data_dict["purchaseLink"])

        # Заполняем поле Ссылка на договор/контракт на Официальном сайте ЕИС
        self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).send_keys(
            user_data_dict["eisContractLink"])

        # Жмем кнопку "Поиск допустимого варианта" у поля "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)

        # Выбираем значения во фрейме "Территория применения"
        self.select_elements_in_frame_territory(user_data_dict["territory"])

        # Проверяем заполнение поля "Территория применения"
        territory_value = ''
        for territory in user_data_dict["territory"]:
            territory_value = territory_value + territory + '; '
        territory_value = territory_value.strip()
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TERRITORY_ELEMENT, territory_value)

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)

        self.select_elements_in_frame(user_data_dict["technologies"], 1)

        # Проверяем, строку
        technologies_value = ''
        for technologies in user_data_dict["technologies"]:
            technologies_value = technologies_value + technologies + '; '
        technologies_value = technologies_value.strip()
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT, technologies_value)

        # заполняем поле Количественные показатели реализации проекта
        self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).send_keys(
            user_data_dict["quantitativeIndicatorsProject"])

        # Уникальный код проекта
        self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).send_keys(
            user_data_dict["projectUniqueCode"])

        # Выбираем связанный проект
        self.browser.find_element(*FormCreateContractLocators.PROJECT_ELEMENT).click()
        # self.browser.find_element(*FormCreateContractLocators.PROJECT_FIND_ELEMENT).send_keys(
        # user_data_dict["project"])
        how, what = FormCreateContractLocators.PROJECT_DROPDOWN_ELEMENT
        what = what.replace("project_name", user_data_dict["project"])
        self.browser.find_element(how, what).click()

        # Переходим в низ страницы к кнопке "Создать"
        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON))

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

        if user_data_dict["jointBidding"] == "Да":
            # Заполняем таблицу "Добавленные договоры/контракты"
            sum_joint_bidding = 0
            count_joint_contracts_row = len(user_data_dict["jointBiddingContracts"])
            print(f'\nКоличество строчек Добавленных договор/контрактов: {count_joint_contracts_row}')
            current_row = 0
            while current_row < count_joint_contracts_row:
                # Заполняем поле "Заказчик"
                customer_field = self.browser.find_elements(*FormCreateContractLocators.JOINT_BIDDING_CUSTOMER)[
                    current_row]
                customer_field.click()
                how, what = FormCreateContractLocators.JOINT_BIDDING_CUSTOMER_DROPDOWN
                what = what.replace('customer_name', user_data_dict["jointBiddingContracts"][current_row]["customer"])
                self.browser.find_element(how, what).click()

                # Заполняем поле "Номер"
                number_field = self.browser.find_elements(*FormCreateContractLocators.JOINT_BIDDING_NUMBER)[current_row]
                number_field.send_keys(user_data_dict["jointBiddingContracts"][current_row]["number"])

                # Заполняем поле "Дата заключения"
                startDate_field = self.browser.find_elements(*FormCreateContractLocators.JOINT_BIDDING_START_DATE)[
                    current_row]
                startDate_field.send_keys(user_data_dict["jointBiddingContracts"][current_row]["startDate"])

                # Заполняем поле "Дата окончания"
                endDate_field = self.browser.find_elements(*FormCreateContractLocators.JOINT_BIDDING_END_DATE)[
                    current_row]
                endDate_field.send_keys(user_data_dict["jointBiddingContracts"][current_row]["endDate"])

                # Заполняем поле "Сумма"
                summa_field = self.browser.find_elements(*FormCreateContractLocators.JOINT_BIDDING_SUMMA)[current_row]
                summa_field.send_keys(user_data_dict["jointBiddingContracts"][current_row]["sum"])

                sum_joint_bidding += user_data_dict["jointBiddingContracts"][current_row]["sum"]
                current_row += 1
        # Жмем кнопку создать
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON).click()
        # Подтверждаем внесение изменений  в связанный проект
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CHANGE_PROJECT_BUTTON).click()

    def form_create_contract(self, user_data_dict):
        time.sleep(3)

        # Заполняем поле "Предмет контракта"
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).send_keys(
            user_data_dict["fullName"])

        # Заполняем поле "Заказчик"
        self.browser.find_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT).click()
        how, what = FormCreateContractLocators.CUSTOMER_DROPDOWN_CONTRACT_ELEMENT
        if isinstance(user_data_dict["customer"], list):
            customer = user_data_dict["customer"][0]
        else:
            customer = user_data_dict["customer"]
        what = what.replace("customer_name", customer)
        self.browser.find_element(*FormCreateContractLocators.CUSTOMER_SEARCH_FIELD).send_keys(customer)
        self.browser.find_element(how, what).click()

        # Заполняем поле "Подразделение-продавец"
        self.browser.find_element(*FormCreateContractLocators.SALES_UNIT_CONTRACT_ELEMENT).click()
        how, what = FormCreateContractLocators.SALES_UNIT_DROPDOWN_CONTRACT_ELEMENT
        what = what.replace("salesUnit_name", user_data_dict["salesUnit"])
        self.browser.find_element(how, what).click()

        # Заполняем поле "Ответственный менеджер подразделения-продавца"
        self.browser.find_element(*FormCreateContractLocators.SALES_MANAGER_CONTRACT_ELEMENT).click()
        how, what = FormCreateContractLocators.SALES_MANAGER_CONTRACT_DROPDOWN_ELEMENT
        what = what.replace("salesManager_name", user_data_dict["salesManager"])
        self.browser.find_element(how, what).click()

        # Заполняем поле "Подразделение-исполнитель"
        self.browser.find_element(*FormCreateContractLocators.EXECUTIVE_UNIT_CONTRACT_ELEMENT).click()
        time.sleep(1)
        how, what = FormCreateContractLocators.EXECUTIVE_UNIT_CONTRACT_DROPDOWN_ELEMENT
        what = what.replace("executiveUnit_name", user_data_dict["executiveUnit"])
        self.browser.find_element(how, what).click()

        # Заполняем поле "Ответственный менеджер подразделения-исполнителя"
        self.browser.find_element(*FormCreateContractLocators.EXECUTIVE_MANAGER_CONTRACT_ELEMENT).click()
        how, what = FormCreateContractLocators.EXECUTIVE_MANAGER_DROPDOWN_CONTRACT_ELEMENT
        what = what.replace("executiveManager_name", user_data_dict["executiveManager"])
        self.browser.find_element(how, what).click()

        # Заполняем поле "Исполнитель (юридическое лицо)"
        self.browser.find_element(*FormCreateContractLocators.EXECUTIVE_UNIT_LEGAL_CONTRACT_ELEMENT).click()
        how, what = FormCreateContractLocators.EXECUTIVE_UNIT_LEGAL_DROPDOWN_CONTRACT_ELEMENT
        what = what.replace("executiveUnitLegal_name", user_data_dict["executiveUnitLegal"])
        self.browser.find_element(how, what).click()

        # Ищем кнопку "Тип работ и услуг"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TYPE_AND_SERVICES_ELEMENT).click()
        time.sleep(2)

        # Работем во фрейме "Тип работ и услуг"
        self.select_in_frame_type_work_and_services(user_data_dict["typeOfWorkServices"])

        # Заполняем поле "Сумма договора/контракта"
        self.browser.find_element(*FormCreateContractLocators.SUM_ELEMENT).send_keys(user_data_dict["sum"])

        # Заполняем поле "Валюта договора/контракта "
        Select(self.browser.find_element(*FormCreateContractLocators.CURRENCY_ELEMENT)).select_by_value(
            user_data_dict["currency"])

        # Заполняем поле "Номер"
        self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).send_keys(
            user_data_dict["numberContract"])

        # Заполняем поле "Дата заключения"
        self.browser.find_element(*FormCreateContractLocators.START_DATE_CONTRACT).send_keys(
            user_data_dict["startDate"])

        # Заполняем поле "Дата окончания"
        self.browser.find_element(*FormCreateContractLocators.END_DATE_CONTRACT).send_keys(
            user_data_dict["endDate"])

        # Заполняем поле "Номер закупки"
        self.browser.find_element(*FormCreateContractLocators.EIS_PURCHASE_NUMBER_CONTRACT).send_keys(
            user_data_dict["purchaseNumber"])

        # Заполняем поле " Ссылка на закупку "
        self.browser.find_element(*FormCreateContractLocators.EIS_PURCHSE_LINK_CONTRACT).send_keys(
            user_data_dict["purchaseLink"])

        # Заполняем поле Ссылка на договор/контракт на Официальном сайте ЕИС
        self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).send_keys(
            user_data_dict["eisContractLink"])

        # Жмем кнопку "Поиск допустимого варианта" у поля "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        # Выбираем значения во фрейме "Территория применения"
        self.select_elements_in_frame_territory(user_data_dict["territory"])

        # Жмем кнопку "Поиск допустимого варианта" у поля "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        # Работаем во фрейме "Ключевые технологии"
        self.select_elements_in_frame(user_data_dict["technologies"], 3)

        # Заполняем поле "Цели и задачи"
        self.browser.find_element(*FormCreateContractLocators.DESCRIPTION_PLAIN_TEXT_ELEMENT).send_keys(
            user_data_dict["descriptionText"])

        # заполняем поле Количественные показатели реализации проекта
        self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).send_keys(
            user_data_dict["quantitativeIndicatorsProject"])

        # Уникальный код проекта
        self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).send_keys(
            user_data_dict["projectUniqueCode"])

        # Выбираем связанный проект
        self.browser.find_element(*FormCreateContractLocators.PROJECT_ELEMENT).click()
        # self.browser.find_element(*FormCreateContractLocators.PROJECT_FIND_ELEMENT).send_keys(
        # user_data_dict["project"])
        how, what = FormCreateContractLocators.PROJECT_DROPDOWN_ELEMENT
        what = what.replace("project_name", user_data_dict["project"])
        self.browser.find_element(how, what).click()

        # Заполняем строки плановых платежей
        payments_sum = 0
        count_payments_line = len(user_data_dict["payments"])
        print(f'\nКоличество строчек плановых платежей: {count_payments_line}')
        current_line = 0
        while current_line < count_payments_line:
            # Заполняем поле "Сумма"
            sum_field = self.browser.find_elements(*FormCreateContractLocators.SUMTABLE)[current_line]
            sum_field.send_keys(user_data_dict["payments"][current_line]["sum"])

            # Заполняем поле "Год"
            year_field = self.browser.find_elements(*FormCreateContractLocators.YEARTABLE)[current_line]
            year_field.send_keys(user_data_dict["payments"][current_line]["year"])

            # Заполняем поле "Квартал"
            quarter_field = self.browser.find_elements(*FormCreateContractLocators.QUARTERTABLE)[current_line]
            Select(quarter_field).select_by_visible_text(
                f'{user_data_dict["payments"][current_line]["quarter"]} квартал')

            payments_sum += user_data_dict["payments"][current_line]["sum"]
            current_line += 1

        # Переходим вниз страницы к кнопке "Создать"
        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON))

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

        # Если сумма платежей не совпадает появляется алерт, при подтверждении сущность создается
        if payments_sum != user_data_dict["sum"]:
            alert = self.browser.switch_to.alert
            alert.accept()

    def form_edit_contract(self, old_user_data_dict, new_user_data_dict):

        # Заполняем поле "Предмет контракта"
        if old_user_data_dict["fullName"] != new_user_data_dict["fullName"]:
            # Ищем поле "Предмет контракта" и очищаем его
            self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).clear()
            self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).send_keys(
                new_user_data_dict["fullName"])

        # Ищем поле "Заказчик" и выбираем значение
        if old_user_data_dict["customer"] != new_user_data_dict["customer"]:
            self.browser.find_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT).click()
            how, what = FormCreateContractLocators.CUSTOMER_DROPDOWN_CONTRACT_ELEMENT
            if isinstance(new_user_data_dict["customer"], list):
                customer = new_user_data_dict["customer"][0]
            else:
                customer = new_user_data_dict["customer"]
            what = what.replace("customer_name", customer)
            self.browser.find_element(*FormCreateContractLocators.CUSTOMER_SEARCH_FIELD).send_keys(customer)
            self.browser.find_element(how, what).click()

        # Ищем поле "Подразделение-продавец" и выбираем значение
        if old_user_data_dict["salesUnit"] != new_user_data_dict["salesUnit"]:
            self.browser.find_element(*FormCreateContractLocators.SALES_UNIT_CONTRACT_ELEMENT).click()
            how, what = FormCreateContractLocators.SALES_UNIT_DROPDOWN_CONTRACT_ELEMENT
            what = what.replace("salesUnit_name", new_user_data_dict["salesUnit"])
            self.browser.find_element(how, what).click()

        # Заполняем поле "Ответственный менеджер подразделения-продавца"
        if old_user_data_dict["salesManager"] != new_user_data_dict["salesManager"]:
            self.browser.find_element(*FormCreateContractLocators.SALES_MANAGER_CONTRACT_ELEMENT).click()
            how, what = FormCreateContractLocators.SALES_MANAGER_CONTRACT_DROPDOWN_ELEMENT
            what = what.replace("salesManager_name", new_user_data_dict["salesManager"])
            self.browser.find_element(how, what).click()

        # Заполняем поле "Подразделение-исполнитель"
        if old_user_data_dict["executiveUnit"] != new_user_data_dict["executiveUnit"]:
            self.browser.find_element(*FormCreateContractLocators.EXECUTIVE_UNIT_CONTRACT_ELEMENT).click()
            time.sleep(1)
            how, what = FormCreateContractLocators.EXECUTIVE_UNIT_CONTRACT_DROPDOWN_ELEMENT
            what = what.replace("executiveUnit_name", new_user_data_dict["executiveUnit"])
            self.browser.find_element(how, what).click()

        # Заполняем поле "Ответственный менеджер подразделения-исполнителя"
        if old_user_data_dict["executiveManager"] != new_user_data_dict["executiveManager"]:
            self.browser.find_element(*FormCreateContractLocators.EXECUTIVE_MANAGER_CONTRACT_ELEMENT).click()
            how, what = FormCreateContractLocators.EXECUTIVE_MANAGER_DROPDOWN_CONTRACT_ELEMENT
            what = what.replace("executiveManager_name", new_user_data_dict["executiveManager"])
            self.browser.find_element(how, what).click()

        # Заполняем поле "Исполнитель (юридическое лицо)"
        if old_user_data_dict["executiveUnitLegal"] != new_user_data_dict["executiveUnitLegal"]:
            self.browser.find_element(*FormCreateContractLocators.EXECUTIVE_UNIT_LEGAL_CONTRACT_ELEMENT).click()
            how, what = FormCreateContractLocators.EXECUTIVE_UNIT_LEGAL_DROPDOWN_CONTRACT_ELEMENT
            what = what.replace("executiveUnitLegal_name", new_user_data_dict["executiveUnitLegal"])
            self.browser.find_element(how, what).click()

        # Заполняем новыми значениями поле "Тип работ и услуг"
        if len(set(new_user_data_dict["typeOfWorkServices"]) - set(old_user_data_dict["typeOfWorkServices"])) > 0:
            # Очищаем поле "Тип работ и услуг"
            self.browser.find_element(*FormCreateContractLocators.TYPE_WORK_SERVICES_ELEMENT).clear()
            self.browser.find_element(*FormCreateContractLocators.SEARCH_TYPE_AND_SERVICES_ELEMENT).click()
            time.sleep(2)
            self.select_in_frame_type_work_and_services(new_user_data_dict["typeOfWorkServices"])

        # Очищаем поле "Сумма"
        if old_user_data_dict["sum"] != new_user_data_dict["sum"]:
            self.browser.find_element(*FormCreateContractLocators.SUM_ELEMENT).clear()
            # Заполняем новым значением поле "Сумма"
            self.browser.find_element(*FormCreateContractLocators.SUM_ELEMENT).send_keys(new_user_data_dict["sum"])

        # Ищем поле "Валюта" и выбираем значение
        if old_user_data_dict["currency"] != new_user_data_dict["currency"]:
            Select(self.browser.find_element(*FormCreateContractLocators.CURRENCY_ELEMENT)).select_by_value(
                new_user_data_dict["currency"])

        # Заполняем поле "Номер"
        if old_user_data_dict["numberContract"] != new_user_data_dict["numberContract"]:
            self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).clear()
            self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).send_keys(
                new_user_data_dict["numberContract"])

        # Заполняем поле "Дата заключения"
        if old_user_data_dict["startDate"] != new_user_data_dict["startDate"]:
            self.browser.find_element(*FormCreateContractLocators.START_DATE_CONTRACT).clear()
            # Заполняем поле "Дата заключения"
            self.browser.find_element(*FormCreateContractLocators.START_DATE_CONTRACT).send_keys(
                new_user_data_dict["startDate"])

        # Заполняем поле "Дата окончания"
        if old_user_data_dict["endDate"] != new_user_data_dict["endDate"]:
            self.browser.find_element(*FormCreateContractLocators.END_DATE_CONTRACT).clear()
            self.browser.find_element(*FormCreateContractLocators.END_DATE_CONTRACT).send_keys(
                new_user_data_dict["endDate"])

        # Заполняем поле "Номер закупки"
        if old_user_data_dict["purchaseNumber"] != new_user_data_dict["purchaseNumber"]:
            self.browser.find_element(*FormCreateContractLocators.EIS_PURCHASE_NUMBER_CONTRACT).clear()
            self.browser.find_element(*FormCreateContractLocators.EIS_PURCHASE_NUMBER_CONTRACT).send_keys(
                new_user_data_dict["purchaseNumber"])

        # Заполняем поле " Ссылка на закупку "
        if old_user_data_dict["purchaseLink"] != new_user_data_dict["purchaseLink"]:
            self.browser.find_element(*FormCreateContractLocators.EIS_PURCHSE_LINK_CONTRACT).clear()
            self.browser.find_element(*FormCreateContractLocators.EIS_PURCHSE_LINK_CONTRACT).send_keys(
                new_user_data_dict["purchaseLink"])

        # Заполняем поле Ссылка на договор/контракт на Официальном сайте ЕИС
        if old_user_data_dict["eisContractLink"] != new_user_data_dict["eisContractLink"]:
            self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).clear()
            self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).send_keys(
                new_user_data_dict["eisContractLink"])

        # Ищем поле "Статус контракта" и выбираем значение
        Select(self.browser.find_element(*FormCreateContractLocators.CONTRACT_STATUS_ELEMENT)).select_by_value(
            new_user_data_dict["contractStatus"])

        # Заполнение поля "Территория применения"
        if len(set(new_user_data_dict["territory"]) - set(old_user_data_dict["territory"])) > 0:
            # Очищаем поле "Территория применения"
            self.browser.find_element(*FormCreateContractLocators.TERRITORY_ELEMENT).clear()
            # Жмем кнопку "Поиск допустимого варианта" у поля "Территория применения"
            self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
            time.sleep(2)
            # Выбираем значения во фрейме "Территория применения"
            self.select_elements_in_frame_territory(new_user_data_dict["territory"])

        # Заполнение поля "Ключевые технологии"
        if len(set(new_user_data_dict["technologies"]) - set(old_user_data_dict["technologies"])) > 0:
            # Очищаем поле "Ключевые технологии"
            self.browser.find_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT).clear()
            # Жмем кнопку "Поиск допустимого варианта" у поля "Ключевые технологии"
            self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
            time.sleep(2)
            # Работаем во фрейме "Ключевые технологии"
            self.select_elements_in_frame(new_user_data_dict["technologies"], 2)

        # Заполняем поле "Цели и задачи"
        if old_user_data_dict["descriptionText"] != new_user_data_dict["descriptionText"]:
            self.browser.find_element(*FormCreateContractLocators.DESCRIPTION_PLAIN_TEXT_ELEMENT).clear()
            self.browser.find_element(*FormCreateContractLocators.DESCRIPTION_PLAIN_TEXT_ELEMENT).send_keys(
                new_user_data_dict["descriptionText"])

        # Заполняем поле Количественные показатели реализации проекта
        if old_user_data_dict["quantitativeIndicatorsProject"] != new_user_data_dict["quantitativeIndicatorsProject"]:
            self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).clear()
            self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).send_keys(
                new_user_data_dict["quantitativeIndicatorsProject"])

        # Уникальный код проекта
        if old_user_data_dict["projectUniqueCode"] != new_user_data_dict["projectUniqueCode"]:
            self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).clear()
            self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).send_keys(
                new_user_data_dict["projectUniqueCode"])

        # Удаляем старые строки плановых платежей
        count_old_payments_line = len(old_user_data_dict["payments"])
        delete_line = 0
        while delete_line < count_old_payments_line:
            self.browser.find_element(*FormCreateContractLocators.DELETE_ROW_BUTTON).click()
            confirm_delete = self.browser.switch_to.alert
            confirm_delete.accept()
            delete_line += 1

        # Заполняем строки плановых платежей
        payments_sum = 0
        count_payments_line = len(new_user_data_dict["payments"])
        print(f'\nКоличество строчек плановых платежей: {count_payments_line}')
        current_line = 0
        while current_line < count_payments_line:
            # Заполняем поле "Сумма"
            sum_field = self.browser.find_elements(*FormCreateContractLocators.SUMTABLE)[current_line]
            sum_field.send_keys(new_user_data_dict["payments"][current_line]["sum"])

            # Заполняем поле "Год"
            year_field = self.browser.find_elements(*FormCreateContractLocators.YEARTABLE)[current_line]
            year_field.send_keys(new_user_data_dict["payments"][current_line]["year"])

            # Заполняем поле "Квартал"
            quarter_field = self.browser.find_elements(*FormCreateContractLocators.QUARTERTABLE)[current_line]
            Select(quarter_field).select_by_visible_text(
                f'{new_user_data_dict["payments"][current_line]["quarter"]} квартал')

            payments_sum += new_user_data_dict["payments"][current_line]["sum"]
            current_line += 1

        # Жмем кнопку сохранить
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_EDIT_CONTRACT_BUTTON).click()

    def verify_prefill_department_manager(self, user_data_dict):
        # Проверяем предзаполнение полей:
        # "Ответственный менеджер подразделения-продавца" и "Ответственный менеджер подразделения-исполнителя" для УЗ продавца
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller":
            delayed_assert.expect(self.is_element_text(*FormCreateContractLocators.SALES_MANAGER_ELEMENT_VALUE) ==
                                  user_data_dict["executiveManager"],
                                  f'Для роли {user_data_dict["createAccount"]} '
                                  f'поле "Ответственный менеджер подразделения-продавца" '
                                  f'должно быть предзаполненно значением: "{user_data_dict["executiveManager"]}"')
            delayed_assert.expect(
                self.is_element_text(*FormCreateContractLocators.EXECUTIVE_MANAGER_ELEMENT_VALUE) ==
                user_data_dict["executiveManager"],
                f'Для роли {user_data_dict["createAccount"]} '
                f'поле "Ответственный менеджер подразделения-исполнителя" '
                f'должно быть предзаполненно значением: "{user_data_dict["executiveManager"]}"')
        elif user_data_dict["createAccount"] == "Mr_KSUP_Seller2":
            delayed_assert.expect(self.is_element_text(*FormCreateContractLocators.SALES_MANAGER_ELEMENT_VALUE) ==
                                  user_data_dict["salesManager"],
                                  f'Для роли {user_data_dict["createAccount"]} '
                                  f'поле "Ответственный менеджер подразделения-продавца" '
                                  f'должно быть предзаполненно значением: "{user_data_dict["salesManager"]}"')
            delayed_assert.expect(self.is_element_text(*FormCreateContractLocators.EXECUTIVE_MANAGER_ELEMENT_VALUE) ==
                                  user_data_dict["salesManager"],
                                  f'Для роли {user_data_dict["createAccount"]} '
                                  f'поле "Ответственный менеджер подразделения-исполнителя" '
                                  f'должно быть предзаполненно значением: "{user_data_dict["salesManager"]}"')
