import time

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import ZakupElementLocators
from userdata.user_data import UserData
from selenium.webdriver.support.color import Color
from pages.locators import BasePageLocators
import delayed_assert


class ZakupElementPage(BasePage):

    # Проверка информации на вкладке "Общие сведения"
    def verify_general_information_in_zakup(self, user_data_dict):
        # Переходим на вкладку "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        time.sleep(1)

        # Проверяем титул карточки который соответствует названию сущности
        assert self.is_element_text(*ZakupElementLocators.TITLE_IN_ZP) == user_data_dict["fullName"], \
            "Название карточки не соответствует входным данным"
        print("Название карточки успешно проверено")

        # Проверяем поле "Тип закупочной процедуры"
        assert self.is_element_text(*ZakupElementLocators.CONTRACTOR_TYPE_IN_ZP) == user_data_dict["contractorType"], \
            f'\nНекорректное значение в поле "Тип закупочной процедуры". ' \
            f'\nОжидаемый результат:{user_data_dict["contractorType"]}'
        print('Значение в поле "Тип закупочной процедуры" успешно проверено')

        # Проверяем поле "Подразделение-продавец"
        assert self.is_element_text(*ZakupElementLocators.SALES_UNIT_IN_ZP) == user_data_dict["salesUnit"], \
            f'\nНекорректное значение в поле "Подразделение-продавец". ' \
            f'\nОжидаемый результат:{user_data_dict["salesUnit"]}'
        print('Значение в поле "Подразделение-продавец" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-продавца"
        assert self.is_element_text(*ZakupElementLocators.SALES_MANAGER_IN_ZP) == user_data_dict["salesManager"], \
            f'\nНекорректное значение в поле "Ответственный менеджер подразделения-продавца".' \
            f'\nОжидаемый результат:{user_data_dict["salesManager"]}'
        print('Значение в поле "Ответственный менеджер подразделения-продавца" успешно проверено')

        # Проверяем поле "Подразделение-исполнитель"
        assert self.is_element_text(*ZakupElementLocators.EXECUTIVE_UNIT_IN_ZP) == user_data_dict["executiveUnit"], \
            f'\nНекорректное значение в поле "Подразделение-исполнитель". ' \
            f'\nОжидаемый результат:{user_data_dict["executiveUnit"]}'
        print('Значение в поле "Подразделение-исполнитель" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-исполнителя"
        assert self.is_element_text(*ZakupElementLocators.EXECUTIVE_MANAGER_IN_ZP) == user_data_dict[
            "executiveManager"], \
            f'\nНекорректное значение в поле "Ответственный менеджер подразделения-исполнителя".' \
            f'\nОжидаемый результат:{user_data_dict["executiveManager"]}'
        print('Значение в поле "Ответственный менеджер подразделения-исполнителя" успешно проверено')

        # Проверяем поле "Совместные торги"
        if user_data_dict["contractorType"] == 'Тендерная заявка' and user_data_dict["jointBidding"] == 'Да':
            assert self.is_element_text(*ZakupElementLocators.JOINT_BIDDING_IN_ZP) == user_data_dict["jointBidding"], \
                f'\nНекорректное значение в поле "Совместные торги".' \
                f'\nОжидаемый результат:{user_data_dict["jointBidding"]}'

            # Проверяем название поля "Заказчик" при совместных торгах
            assert self.is_element_text(
                *ZakupElementLocators.CUSTOMER_FIELD_NAME) == "Организация, осуществляющая размещение закупки", \
                f'\nНекорректное название поля "Заказчик" при совместных торгах.' \
                f'\nОжидаемый результат: Организация, осуществляющая размещение закупки' \
                f'\nФактический результат: {self.is_element_text(*ZakupElementLocators.CUSTOMER_FIELD_NAME)}'

        # Проверяем поле "Заказчик"
        assert self.is_element_text(*ZakupElementLocators.CUSTOMER_IN_ZP) == user_data_dict["customer"], \
            f'\nНекорректное значение в поле "Заказчик".' \
            f'\nОжидаемый результат:{user_data_dict["customer"]}'
        print('Значение в поле "Заказчик" успешно проверено')

        # Проверяем поле "Тип работ и услуг"
        work_services_value = ''
        for category in user_data_dict["typeOfWorkServices"]:
            work_services_value = work_services_value + category + '; '
        work_services_value = work_services_value.rstrip()
        assert self.is_element_text(*ZakupElementLocators.TYPE_OF_WORK_SERVCICES_IN_ZP) == work_services_value, \
            f'\nНекорректное значение в поле "Тип работ и услуг".' \
            f'\n Ожидаемый результат: {work_services_value}'
        print('Значение в поле "Тип работ и услуг" успешно проверено')

        # Проверяем поле "Исполнитель (юридическое лицо)"
        if len(user_data_dict["executiveUnitLegal"]) > 0:
            assert self.is_element_text(*ZakupElementLocators.EXECUTIVE_UNIT_LEGAL_IN_ZP) == \
                   user_data_dict["executiveUnitLegal"], \
                f'\nНекорректное значение в поле "Исполнитель (юридическое лицо)".' \
                f'\nОжидаемый результат:{user_data_dict["executiveUnitLegal"]}'
            print('Значение в поле "Исполнитель (юридическое лицо)" успешно проверено')
        else:
            assert self.browser.find_element(*ZakupElementLocators.EXECUTIVE_UNIT_LEGAL_IN_ZP).is_displayed() is False, \
                'Отображено пустое поле "Исполнитель (юридическое лицо)"'
            print('Пустое поле "Исполнитель (юридическое лицо)" успешно не отображено')

        # Проверяем поле "Начальная (максимальная) цена контракта"
        sum_value = str(user_data_dict["sum"])
        if sum_value.find('.') > 0:
            # Преобразование значения с плавающей точкой под необходимый шаблон
            print("Заглушка")
        else:
            # Преобразование целого значения с разделителями пробелами и припиской валюты
            if user_data_dict["currency"] == "Доллар":
                sum_value = ('{:,d}'.format(user_data_dict["sum"])).replace(",", " ") + ',00 $'
            elif user_data_dict["currency"] == "Евро":
                sum_value = ('{:,d}'.format(user_data_dict["sum"])).replace(",", " ") + ',00 €'
            else:
                sum_value = ('{:,d}'.format(user_data_dict["sum"])).replace(",", " ") + ',00 ₽'
            assert self.is_element_text(*ZakupElementLocators.SUM_IN_ZP) == sum_value, \
                f'\nНекорректное значение в поле "Начальная (максимальная) цена контракта" ' \
                f'\nОжидаемый результат: {sum_value}"'
            print('Значение в поле "Сумма договора/контракта" успешно проверено')

        # Проверяем поле "Валюта договора/контракта"
        assert self.is_element_text(*ZakupElementLocators.CURRENCY_IN_ZP) == user_data_dict["currency"], \
            f'\nНекорректное значение в поле "Валюта договора/контракта".' \
            f'\nОжидаемый результат:{user_data_dict["currency"]}'
        print('Значение в поле "Валюта договора/контракта" успешно проверено')

        # Проверяем поле "Категория проекта"
        assert self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_IN_ZP) == \
               user_data_dict["priceCategory"], "Ценовая категория закупочной процедуры не корректна"
        print('Значение в поле "Категория проекта" успешно проверено')

        # Проверяем поле "Порядок проведения закупочной процедуры"
        if user_data_dict["contractorType"] == "Тендерная заявка":
            assert self.is_element_text(*ZakupElementLocators.SALE_LAW_TYPE_TENDER_ZP) == user_data_dict["saleLawType"], \
                f'\nНекорректное значение в поле "Порядок проведения закупочной процедуры".' \
                f'\nОжидаемый результат:{user_data_dict["saleLawType"]}'
            print('Значение в поле "Порядок проведения закупочной процедуры" успешно проверено')
        elif user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            assert self.is_element_text(*ZakupElementLocators.SALE_LAW_TYPE_ZAPROS_ZP) == user_data_dict[
                "saleLawType"], \
                f'\nНекорректное значение в поле "Порядок проведения закупочной процедуры".' \
                f'\nОжидаемый результат:{user_data_dict["saleLawType"]}'
            print('Значение в поле "Порядок проведения закупочной процедуры" успешно проверено')

        # Проверяем поле "Размер обеспечения заявки"
        if user_data_dict["contractorType"] != "Коммерческое предложение" and \
                len(str(user_data_dict["applicationSize"])) > 0:
            application_size = str(user_data_dict["applicationSize"])
            if application_size.find('.') > 0:
                # Преобразование значения с плавающей точкой под необходимый шаблон
                print("Заглушка")
            else:
                # Преобразование целого значения с разделителями пробелами и припиской валюты
                if user_data_dict["currency"] == "Доллар":
                    application_size = ('{:,d}'.format(user_data_dict["applicationSize"])).replace(",", " ") + ',00 $'
                elif user_data_dict["currency"] == "Евро":
                    application_size = ('{:,d}'.format(user_data_dict["applicationSize"])).replace(",", " ") + ',00 €'
                else:
                    application_size = ('{:,d}'.format(user_data_dict["applicationSize"])).replace(",", " ") + ',00 ₽'
                assert self.is_element_text(*ZakupElementLocators.APPLICATION_SIZE_IN_ZP) == application_size, \
                    f'\nНекорректное значение в поле "Размер обеспечения заявки" ' \
                    f'\nОжидаемый результат: {application_size}"'
                print('Значение в поле "Размер обеспечения заявки" успешно проверено')

        # Проверяем поле "Размер обеспечения договора/контракта"
        if user_data_dict["contractorType"] != "Коммерческое предложение" and \
                len(str(user_data_dict["contractSize"])) > 0:
            contract_size = str(user_data_dict["contractSize"])
            if contract_size.find('.') > 0:
                # Преобразование значения с плавающей точкой под необходимый шаблон
                print("Заглушка")
            else:
                # Преобразование целого значения с разделителями пробелами и припиской валюты
                if user_data_dict["currency"] == "Доллар":
                    contract_size = ('{:,d}'.format(user_data_dict["contractSize"])).replace(",", " ") + ',00 $'
                elif user_data_dict["currency"] == "Евро":
                    contract_size = ('{:,d}'.format(user_data_dict["contractSize"])).replace(",", " ") + ',00 €'
                else:
                    contract_size = ('{:,d}'.format(user_data_dict["contractSize"])).replace(",", " ") + ',00 ₽'
                assert self.is_element_text(*ZakupElementLocators.CONTRACT_SIZE_IN_ZP) == contract_size, \
                    f'\nНекорректное значение в поле "Размер обеспечения договора/контракта" ' \
                    f'\nОжидаемый результат: {contract_size}"'
                print('Значение в поле "Размер обеспечения договора/контракта" успешно проверено')

        # Проверяем поле "Срок подачи на конкурс"
        if user_data_dict["contractorType"] == "Тендерная заявка":
            assert user_data_dict["competitionDeadlineFrom"] in \
                   str(self.is_element_text(*ZakupElementLocators.COMPETITION_DEAD_LINE_FROM_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Срок подачи на конкурс".' \
                f'\nОжидаемый результат: {user_data_dict["competitionDeadlineFrom"]}'
            print('Значение в поле "Срок подачи на конкурс" успешно проверено')

        # Проверяем поле "Предполагаемая дата начала проведения закупки с"
        if user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                user_data_dict["saleLawType"] == "44-ФЗ":
            assert user_data_dict["purchaseStartDateFrom"] in \
                   str(self.is_element_text(*ZakupElementLocators.PURCHASE_START_DATE_FROM)).strip(), \
                f'\nНекорректное значение в поле "Предполагаемая дата начала проведения закупки с".' \
                f'\nОжидаемый результат: {user_data_dict["purchaseStartDateFrom"]}'
            print('Значение в поле "Предполагаемая дата начала проведения закупки с" успешно проверено')

        # Проверяем поле "Предполагаемая дата начала проведения закупки по"
        if user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                user_data_dict["saleLawType"] == "44-ФЗ":
            assert user_data_dict["purchaseStartDateTo"] in \
                   str(self.is_element_text(*ZakupElementLocators.PURCHASE_START_DATE_TO)).strip(), \
                f'\nНекорректное значение в поле "Предполагаемая дата начала проведения закупки по".' \
                f'\nОжидаемый результат: {user_data_dict["purchaseStartDateTo"]}'
            print('Значение в поле "Предполагаемая дата начала проведения закупки по" успешно проверено')

        # Проверяем поле "Срок предоставления ценовой информации"
        if user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                len(str(user_data_dict["priceInformationDeadline"])) > 0:
            assert user_data_dict["priceInformationDeadline"] in \
                   str(self.is_element_text(*ZakupElementLocators.PRICE_INFORMATION_DEAD_LINE_FROM_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Срок предоставления ценовой информации".' \
                f'\nОжидаемый результат: {user_data_dict["priceInformationDeadline"]}'
            print('Значение в поле "Срок предоставления ценовой информации" успешно проверено')

        # Проверяем поле "Плановая дата заключения договора/контракта"
        if user_data_dict["contractorType"] != "Запрос цен товаров, работ, услуг":
            assert user_data_dict["startDate"] in \
                   str(self.is_element_text(*ZakupElementLocators.START_DATE_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Плановая дата заключения договора/контракта".' \
                f'\nОжидаемый результат: {user_data_dict["startDate"]}'
            print('Значение в поле "Плановая дата заключения договора/контракта" успешно проверено')

        # Проверяем поле "Плановая дата окончания договора/контракта"
        if user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            if len(str(user_data_dict["endDate"])) > 0:
                assert user_data_dict["endDate"] in \
                       str(self.is_element_text(*ZakupElementLocators.END_DATE_IN_ZP)).strip(), \
                    f'\nНекорректное значение в поле "Плановая дата окончания договора/контракта".' \
                    f'\nОжидаемый результат: {user_data_dict["endDate"]}'
                print('Значение в поле "Плановая дата окончания договора/контракта" успешно проверено')
        else:
            assert user_data_dict["endDate"] in \
                   str(self.is_element_text(*ZakupElementLocators.END_DATE_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Плановая дата окончания договора/контракта".' \
                f'\nОжидаемый результат: {user_data_dict["endDate"]}'
            print('Значение в поле "Плановая дата окончания договора/контракта" успешно проверено')

        # Проверяем поле "Вероятность заключения договора/контракта"
        assert self.is_element_text(*ZakupElementLocators.PROJECT_PROBABILITY_IN_ZP) == str(user_data_dict[
                                                                                                "projectProbability"]) + "%", \
            f'\nНекорректное значение в поле "Вероятность заключения договора/контракта".' \
            f'\nОжидаемый результат:{user_data_dict["projectProbability"]}'
        print('Значение в поле "Вероятность заключения договора/контракта" успешно проверено')

        # Проверяем поле "Номер закупки"
        if user_data_dict["contractorType"] == "Тендерная заявка":
            assert self.is_element_text(*ZakupElementLocators.PURCHASE_NUMBER_IN_ZP) == \
                   user_data_dict["purchaseNumber"], \
                f'\nНекорректное значение в поле "Номер закупки".' \
                f'\nОжидаемый результат:{user_data_dict["purchaseNumber"]}'
            print('Значение в поле "Номер закупки" успешно проверено')

        # Проверяем поле "Номер запроса цен на Официальном сайте ЕИС"
        if user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                user_data_dict["saleLawType"] == "44-ФЗ":
            assert user_data_dict["eisPriceNumber"] in \
                   str(self.is_element_text(*ZakupElementLocators.EIS_PRICE_NUMBER_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Номер запроса цен на Официальном сайте ЕИС".' \
                f'\nОжидаемый результат: {user_data_dict["eisPriceNumber"]}'
            print('Значение в поле "Номер запроса цен на Официальном сайте ЕИС" успешно проверено')

        # Проверяем поле "Ссылка на запрос на Официальном сайте ЕИС"
        if user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                user_data_dict["saleLawType"] == "44-ФЗ":
            assert user_data_dict["eisPriceLink"] in \
                   str(self.is_element_text(*ZakupElementLocators.EIS_PRICE_LINK_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Ссылка на запрос на Официальном сайте ЕИС".' \
                f'\nОжидаемый результат: {user_data_dict["eisPriceLink"]}'
            print('Значение в поле "Ссылка на запрос на Официальном сайте ЕИС" успешно проверено')

        # Проверяем поле "Связанные продажи"
        if self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Seller" or \
                self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Seller2" or \
                self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Dir" or \
                self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Dir2":
            assert self.is_element_text(*ZakupElementLocators.RELATED_SALES_IN_ZP) == \
                   user_data_dict["fullName"], \
                f'\nНекорректное значение в поле "Связанные продажи".' \
                f'\nОжидаемый результат:{user_data_dict["fullName"]}'
            print('Значение в поле "Связанные продажи" успешно проверено')

        # Проверяем поле "Статус продажи"
        assert self.is_element_text(*ZakupElementLocators.PRESALE_STATUS_IN_ZP) == "В работе", \
            f'\nНекорректное значение в поле "Статус продажи".' \
            f'\nОжидаемый результат: "В работе"'
        print('Значение в поле "Статус продажи" успешно проверено')

        # Проверяем поле "Ссылка на закупку"
        if user_data_dict["contractorType"] == "Тендерная заявка":
            assert self.is_element_text(*ZakupElementLocators.PURCHASE_LINK_IN_ZP) == \
                   user_data_dict["purchaseLink"], \
                f'\nНекорректное значение в поле "Ссылка на закупку".' \
                f'\nОжидаемый результат:{user_data_dict["purchaseLink"]}'
            print('Значение в поле "Ссылка на закупку" успешно проверено')

        # Проверяем поле "Результаты работ"
        if len(user_data_dict["descriptionText"]) > 0:
            assert self.is_element_text(*ZakupElementLocators.DESCRIPTION_TEXT_IN_ZP) == \
                   user_data_dict["descriptionText"], \
                f'\nНекорректное значение в поле "Результаты работ".' \
                f'\nОжидаемый результат:{user_data_dict["descriptionText"]}'
            print('Значение в поле "Результаты работ')
        else:
            assert self.browser.find_element(*ZakupElementLocators.DESCRIPTION_TEXT_IN_ZP).is_displayed() is False, \
                'Отображено пустое поле "Результаты работ"'
            print('Пустое поле "Результаты работ" успешно не отображено')

        # Проверяем поле "Риски проекта с точки зрения Департамента"
        if len(user_data_dict["projectRiskDepartment"]) > 0:
            assert self.is_element_text(*ZakupElementLocators.PROJECT_RISKS_DEPARTMENT_IN_ZP) == \
                   user_data_dict["projectRiskDepartment"], \
                f'\nНекорректное значение в поле "Риски проекта с точки зрения Департамента".' \
                f'\nОжидаемый результат:{user_data_dict["projectRiskDepartment"]}'
            print('Значение в поле "Риски проекта с точки зрения Департамента')
        else:
            assert self.browser.find_element(
                *ZakupElementLocators.PROJECT_RISKS_DEPARTMENT_IN_ZP).is_displayed() is False, \
                'Отображено пустое поле "Риски проекта с точки зрения Департамента"'
            print('Пустое поле "Риски проекта с точки зрения Департамента" успешно отображено')

    # Проверка информации на вкладке "Прикрепленные файлы"
    def verify_attached_files_information(self, user_data_dict):
        self.browser.find_element(*ZakupElementLocators.ATTACHED_FILES_TAB).click()
        time.sleep(2)
        if user_data_dict["contractorType"] == "Тендерная заявка":
            # Проверяем текст в поле "Тендерная заявка"
            actual_text = self.is_element_text(*ZakupElementLocators.TENDER_REQUEST_FIELD)
            expected_text = UserData.name_doc_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Тендерная заявка" на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')

            # Проверяем текст в поле "Тендерная документация"
            actual_text = self.is_element_text(*ZakupElementLocators.TENDER_DOCS_FROM_CUSTOMER_FIELD)
            expected_text = UserData.name_excel_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Тендерная документация" на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')

        elif user_data_dict["contractorType"] == "Коммерческое предложение":
            # Проверяем текст в поле "Официальный запрос от Заказчика на КП"
            actual_text = self.is_element_text(*ZakupElementLocators.KP_REQUEST_FROM_CUSTOMER_FIELD)
            expected_text = UserData.name_doc_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Официальный запрос от Заказчика на КП" '
                                  'на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')

            # Проверяем текст в поле "Коммерческое предложение по официальному запросу"
            actual_text = self.is_element_text(*ZakupElementLocators.OFFER_BY_REQUEST_FIELD)
            expected_text = UserData.name_excel_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Коммерческое предложение по официальному запросу" '
                                  'на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')
        else:
            # Проверяем текст в поле "Запрос НМЦК"
            actual_text = self.is_element_text(*ZakupElementLocators.NMCK_REQUEST_FIELD)
            expected_text = UserData.name_doc_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Запрос НМЦК" '
                                  'на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')

            # Проверяем текст в поле "Ответ на запрос НМЦК"
            actual_text = self.is_element_text(*ZakupElementLocators.NMCK_RESPONSE_FIELD)
            expected_text = UserData.name_jpg_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Ответ на запрос НМЦК" '
                                  'на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')

        if user_data_dict["contractorType"] == "Коммерческое предложение" or user_data_dict["contractorType"] == "Тендерная заявка":
            # Проверяем текст в поле "Пояснительная служебная записка"
            actual_text = self.is_element_text(*ZakupElementLocators.EXPLANATORY_MEMORANUM_FIELD)
            expected_text = UserData.name_doc_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Пояснительная служебная записка" '
                                  'на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')

            # Проверяем текст в поле "Проект контракта"
            actual_text = self.is_element_text(*ZakupElementLocators.PROJECT_OF_CONTRACT_FIELD)
            expected_text = UserData.name_excel_to_link
            delayed_assert.expect(actual_text == expected_text,
                                  'Не корректное название файла в поле "Проект контракта" '
                                  'на вкладке "Прикрепленные файлы"\n'
                                  f'Ожидаемый результат: {expected_text}\n'
                                  f'Фактический результат: {actual_text}')

        # Проверяем текст в поле "Документы с описанием рисков"
        actual_text = self.is_element_text(*ZakupElementLocators.RISK_MAP_AND_REGISTRY_FIELD)
        expected_text = UserData.name_jpg_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Документы с описанием рисков" '
                              'на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Проверяем текст в поле "Иное"
        actual_text = self.is_element_text(*ZakupElementLocators.OTHER_FIELD)
        expected_text = UserData.name_doc_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Иное" '
                              'на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

    # Проверка отображения статуса "Черновик"
    def verify_draft_status_zakup(self):
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Черновик"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

    # Проверка отображения кнопки "Отправить на согласование"
    def verify_visibility_approval_send_button_zp(self):
        assert self.is_visibility_of_element_located(*ZakupElementLocators.SEND_APPROVAL_BUTTON, 5), \
            'Кнопка "Отправить на согласование" не отобрежена'

    # Проверка отображения кнопки "Внести информацию о договоре/контракте"
    def verify_visibility_button_create_contract(self):
        assert self.is_visibility_of_element_located(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP, 5), \
            'Кнопка "Внести информацию о договоре/контракте" не отобрежена'

    # Проверка НЕ отображения кнопки "Отправить на согласование"
    def verify_unvisibility_approval_send_button(self):
        assert self.is_element_clickable(*ZakupElementLocators.SEND_APPROVAL_BUTTON) is False, \
            'Кнопка "Отправить на согласование" отображена и доступна для нажатия'

    # Отправка на согласования закупки
    def send_zakup_for_approval(self, user_data_dict):
        self.is_element_clickable(*ZakupElementLocators.SEND_APPROVAL_BUTTON)
        self.browser.find_element(*ZakupElementLocators.SEND_APPROVAL_BUTTON).click()
        if user_data_dict["contractorType"] == "Тендерная заявка":
            # Выбираем сотрудника из юридической службы
            self.browser.find_element(*ZakupElementLocators.EMPLOYEE_LEGAL_FIELD).click()
            how, what = ZakupElementLocators.EMPLOYEE_LEGAL_DROPDOWN_ELEMENT
            what = what.replace("employee_legal", "Mr_KSUP_Legal")
            self.browser.find_element(how, what).click()

            # Выбираем сотрудника из бухгалтерии
            self.browser.find_element(*ZakupElementLocators.EMPLOYEE_COUNT_FIELD).click()
            how, what = ZakupElementLocators.EMPLOYEE_COUNT_DROPDOWN_ELEMENT
            what = what.replace("employee_count", "Mr_KSUP_Count")
            self.browser.find_element(how, what).click()

            # Выбираем сотрудника из финансовой службы
            self.browser.find_element(*ZakupElementLocators.EMPLOYEE_FIN_FIELD).click()
            how, what = ZakupElementLocators.EMPLOYEE_FIN_DROPDOWN_ELEMENT
            what = what.replace("employee_fin", "Mr_KSUP_Fin")
            self.browser.find_element(how, what).click()

            # Жмем кнопку отправить
            self.browser.find_element(*ZakupElementLocators.CONFIRM_SELECT_EMPLOYEE_BUTTON).click()
        else:
            self.is_visibility_of_element_located(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_BUTTON, 5)
            self.browser.find_element(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_BUTTON).click()

    # Проверка отображения статуса "На согласовании с юридической службой"
    def verify_zakup_waiting_status_approval_legal(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании с юридической службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        # Проверяем статус "Согласуется" по имени службы согласования
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'
                """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование юридической службой" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования с юридической службой'

    # Проверка отображения статуса "Согласовано юридической службой"
    def verify_zakup_successfully_status_approval_legal(self):

        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                                'Ожидаемый результат: "Согласование юридической службой" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано юридической службой" в строке согласования с юридической службой'

    # Проверка отображения статуса "Не согласовано юридической службой"
    def verify_zakup_reject_status_approval_legal(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано с юридической службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование юридической службой" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с юридической службой'

    # Проверка отображения статуса "На согласовании с бухгалтерией"
    def verify_zakup_waiting_status_approval_count(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании с бухгалтерией"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        # Проверяем статус "Согласуется" по имени службы
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование бухгалтерией" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования с бухгалтерией'

    # Проверка отображения статуса "Согласовано с бухгалтерией"
    def verify_zakup_successfully_status_approval_count(self):
        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование бухгалтерией" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с бухгалтерией'

    # Проверка отображения статуса "Не согласовано с бухгалтерией"
    def verify_zakup_reject_status_approval_count(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано бухгалтерией"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с бухгалтерией"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование бухгалтерией" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с бухгалтерией'

    # Проверка отображения статуса "На согласовании с финансовой службой"
    def verify_zakup_waiting_status_approval_fin(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании с финансовой службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        # Проверяем статус "Согласуется"
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование финансовой службой" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования с финансовой службой'

    # Проверка отображения статуса "Согласовано с финансовой службой"
    def verify_zakup_successfully_status_approval_fin(self, user_data_dict):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (user_data_dict["contractorType"] == "Тендерная заявка" and user_data_dict["priceCategory"] == "C") or \
                (user_data_dict["contractorType"] == "Тендерная заявка"
                 and user_data_dict["priceCategory"] == "B"
                 and user_data_dict["groupTypeWork"] == "Other"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
            self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                         "Согласовано с финансовой службой"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        # Проверка статуса по имени службы(необходим один элемент этой службы)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование финансовой службой" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с финансовой службой'

    # Проверка отображения статуса "Не согласовано с финансовой службой"
    def verify_zakup_reject_status_approval_fin(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано с финансовой службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование финансовой службой" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с финансовой службой'

    # Проверка отображения статуса "На согласовании Директором по разработке ПО"
    def verify_zakup_waiting_status_approval_udprpo(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании Директором по разработке ПО"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласуется"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c Директором по разработке ПО"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование Директором по разработке ПО" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования со службой Директором по разработке ПО'

    # Проверка отображения статуса "Согласовано Директором по разработке ПО"
    def verify_zakup_successfully_status_approval_udprpo(self, user_data_dict):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (user_data_dict["contractorType"] == "Тендерная заявка"
            and user_data_dict["groupTypeWork"] == "Software"
            and user_data_dict["priceCategory"] == "B") \
                or (user_data_dict["contractorType"] != "Тендерная заявка"
                    and user_data_dict["groupTypeWork"] == "Software"
                    and user_data_dict["priceCategory"] != "C"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
            self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                         "Согласовано Директором по разработке ПО"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование Директором по разработке ПО"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование Директором по разработке ПО" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования со службой Директором по разработке ПО'

    # Проверка отображения статуса "Не согласовано Директором по разработке ПО"
    def verify_zakup_reject_status_approval_udprpo(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано Директором по разработке ПО"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано Директором по разработке ПО"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c Директором по разработке ПО"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование Директором по разработке ПО" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования со службой Директором по разработке ПО'

    # Проверка отображения статуса "На согласовании в ККП"
    def verify_zakup_waiting_status_approval_kkp(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании в ККП"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласуется"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование ККП" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования со службой ККП'

    # Проверка отображения статуса "Участие в проекте согласовано в ККП"
    def verify_zakup_successfully_status_approval_kkp(self, user_data_dict):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (user_data_dict["contractorType"] == "Тендерная заявка"
                and user_data_dict["priceCategory"] != "A"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
            self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                         "Участие в проекте согласовано в ККП"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование ККП" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования со службой ККП'

    # Проверка отображения статуса "Участие в проекте не согласовано в ККП"
    def verify_zakup_reject_status_approval_kkp(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Участие в проекте не согласовано в ККП"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Участие в проекте не согласовано в ККП"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Прекращено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование ККП" - "Прекращено"'

        # Проверяем цвет статуса "Прекращено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Прекращено" в строке согласования со службой ККП'

    # Проверка отображения статуса "Внутреннее согласование не требуется"
    def verify_zakup_not_require_status_approval(self):
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Внутреннее согласование не требуется"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

    # Проверка отображения статуса "Отправлено на доработку ККП"
    def verify_zakup_revision_status_approval(self):
        # Проверяем статус "Отправлено на доработку" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_TAB).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP, 5)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Отправлено на доработку ККП"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Отправлено на доработку ККП"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_HISTORY_TAB, 5)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_TAB).click()
        """
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отправлено на доработку"), \
            'Некорректный статус или отсутствует статус в строке "Согласование ККП"'
        """
        last_result = self.browser.find_elements(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                           'Ожидаемый результат: "Согласование ККП" - "Отправлено на доработку"'

        # Проверяем цвет статуса "Отправлено на доработку"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отправлено на доработку" в строке согласования со службой ККП'

    # Успешное согласование закупочной процедуры
    def approval_zakup(self, comment, file):
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP_BUTTON)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP_BUTTON).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(comment)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(file)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP, 5)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()
        self.browser.refresh()

    # Отклонение закупочной процедуры с выбором этапа
    def reject_zakup(self, comment, file, start_with):
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP_BUTTON)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP_BUTTON).click()
        # Выбираем значение в выпадающем списке "При повторном согласовании начать с шага:"
        Select(self.browser.find_element(*ZakupElementLocators.START_WITH_ELEMENT)).select_by_value(start_with)
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(comment + ". Начать с: " + start_with)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(file)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_REJECT_ZAKUP).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP, 5)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()
        self.browser.refresh()

    # Отклонение закупочной процедуры за ККП
    def reject_zakup_from_kkp(self, comment):
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP_BUTTON)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP_BUTTON).click()

        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(comment)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_REJECT_ZAKUP).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP, 5)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()
        self.browser.refresh()

    # Отправка на доработку от ККП с выбором этапа
    def revision_zakup_from_kkp(self, comment, start_with):
        self.is_element_clickable(*ZakupElementLocators.REVISION_ZAKUP_BUTTON)
        self.browser.find_element(*ZakupElementLocators.REVISION_ZAKUP_BUTTON).click()
        Select(self.browser.find_element(*ZakupElementLocators.START_WITH_ELEMENT)).select_by_value(start_with)
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(comment + ". Начать с: " + start_with)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_REVISION_ZAKUP).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP, 5)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    # Эскалация на ККП
    def escalate_on_kkp(self):
        self.is_element_clickable(*ZakupElementLocators.ESCALATE_ZAKUP_BUTTON)
        self.browser.find_element(*ZakupElementLocators.ESCALATE_ZAKUP_BUTTON).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_escalation_kkp)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_ESCALATE_ZAKUP).click()
        self.is_visibility_of_element_located(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP, 5)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    # Создание контракта на основе закупочной процедуры
    def go_to_create_contract_based_on_zp(self):
        assert self.is_visibility_of_element_located(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP, 5), \
            'Кнопка "Внести информацию о конкурсе" не отображена'
        self.browser.find_element(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP).click()

    # Проверка отобрежения кнопки "Добавить бюджет проекта"
    def verify_visibility_budget_button(self):
        assert self.is_visibility_of_element_located(*ZakupElementLocators.BUDGET_ZAKUP_BUTTON, 5), \
            'Кнопка "Внести информацию о договоре/контракте" не отобрежена'

    # Добавление файла бюджета
    def add_file_of_budget(self):
        self.browser.find_element(*ZakupElementLocators.BUDGET_ZAKUP_BUTTON).click()

        # Проверяем текст заголовка модульного окна
        actual_text = self.is_element_text(*ZakupElementLocators.TITLE_BUDGET_ELEMENT)
        expected_text = "Добавить файл бюджета проекта в закупочную процедуру?"
        delayed_assert.expect(actual_text == expected_text,
                              f'Не корректный текст заголовка в модульном окне добавления файла бюджета\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Проверяем основной текст модульного окна
        actual_text = self.is_element_text(*ZakupElementLocators.TEXT_BUDGET_ELEMENT)
        expected_text = "Если файл бюджета проекта был ранее добавлен в закупочную процедуру, то он будет перезаписан"
        delayed_assert.expect(actual_text == expected_text,
                              f'Не корректный основной текст в модульном окне добавления файла бюджета\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Добавляем файл бюджета
        self.browser.find_element(*ZakupElementLocators.FILE_BUDGET_FIELD).send_keys(UserData.file_path_for_link_doc)
        time.sleep(2)
        # Жмем кнопку "Добавить"
        self.browser.find_element(*ZakupElementLocators.ADD_BUDGET_FILE_BUTTON).click()

        # Переходим на вкладку "Прикрепленные файлы"
        self.browser.find_element(*ZakupElementLocators.ATTACHED_FILES_TAB).click()

        # Проверяем отображение добавленного файла бюджета
        actual_text = self.is_element_text(*ZakupElementLocators.BUDGET_OF_PROJECT_FIELD)
        expected_text = UserData.name_doc_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Бюджет проекта" на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')
