from pages.base_page import BasePage
from pages.locators import ZakupElementLocators
from userdata.user_data import UserData
from selenium.webdriver.support.color import Color
from pages.locators import BasePageLocators


class ZakupElementPage(BasePage):

    def verify_general_information_in_zakup(self):

        # Проверяем титул карточки который соответствует названию сущности
        assert self.is_element_text(*ZakupElementLocators.TITLE_IN_ZP) == UserData.user_data_dict["fullName"], \
            "Название карточки не соответствует входным данным"
        print("Название карточки успешно проверено")

        # Проверяем поле "Тип закупочной процедуры"
        assert self.is_element_text(*ZakupElementLocators.CONTRACTOR_TYPE_IN_ZP) == UserData.user_data_dict[
            "contractorType"], \
            f'\nНекорректное значение в поле "Тип закупочной процедуры". ' \
            f'\nОжидаемый результат:{UserData.user_data_dict["contractorType"]}'
        print('Значение в поле "Тип закупочной процедуры" успешно проверено')

        # Проверяем поле "Подразделение-продавец"
        assert self.is_element_text(*ZakupElementLocators.SALES_UNIT_IN_ZP) == UserData.user_data_dict[
            "salesUnit"], \
            f'\nНекорректное значение в поле "Подразделение-продавец". ' \
            f'\nОжидаемый результат:{UserData.user_data_dict["salesUnit"]}'
        print('Значение в поле "Подразделение-продавец" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-продавца"
        assert self.is_element_text(*ZakupElementLocators.SALES_MANAGER_IN_ZP) == UserData.user_data_dict[
            "salesManager"], \
            f'\nНекорректное значение в поле "Ответственный менеджер подразделения-продавца".' \
            f'\nОжидаемый результат:{UserData.user_data_dict["salesManager"]}'
        print('Значение в поле "Ответственный менеджер подразделения-продавца" успешно проверено')

        # Проверяем поле "Подразделение-исполнитель"
        assert self.is_element_text(*ZakupElementLocators.EXECUTIVE_UNIT_IN_ZP) == UserData.user_data_dict[
            "executiveUnit"], \
            f'\nНекорректное значение в поле "Подразделение-исполнитель". ' \
            f'\nОжидаемый результат:{UserData.user_data_dict["executiveUnit"]}'
        print('Значение в поле "Подразделение-исполнитель" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-исполнителя"
        assert self.is_element_text(*ZakupElementLocators.EXECUTIVE_MANAGER_IN_ZP) == UserData.user_data_dict[
            "executiveManager"], \
            f'\nНекорректное значение в поле "Ответственный менеджер подразделения-исполнителя".' \
            f'\nОжидаемый результат:{UserData.user_data_dict["executiveManager"]}'
        print('Значение в поле "Ответственный менеджер подразделения-исполнителя" успешно проверено')

        # Проверяем поле "Заказчик"
        assert self.is_element_text(*ZakupElementLocators.CUSTOMER_IN_ZP) == UserData.user_data_dict[
            "customer"], \
            f'\nНекорректное значение в поле "Заказчик".' \
            f'\nОжидаемый результат:{UserData.user_data_dict["customer"]}'
        print('Значение в поле "Заказчик" успешно проверено')

        # Проверяем поле "Тип работ и услуг"
        work_services_value = ''
        for category in UserData.user_data_dict["typeOfWorkServices"]:
            work_services_value = work_services_value + category + '; '
        work_services_value = work_services_value.rstrip()
        assert self.is_element_text(*ZakupElementLocators.TYPE_OF_WORK_SERVCICES_IN_ZP) == work_services_value, \
            f'\nНекорректное значение в поле "Тип работ и услуг".' \
            f'\n Ожидаемый результат: {work_services_value}'
        print('Значение в поле "Тип работ и услуг" успешно проверено')

        # Проверяем поле "Исполнитель (юридическое лицо)"
        if len(UserData.user_data_dict["executiveUnitLegal"]) > 0:
            assert self.is_element_text(*ZakupElementLocators.EXECUTIVE_UNIT_LEGAL_IN_ZP) == \
                   UserData.user_data_dict["executiveUnitLegal"], \
                f'\nНекорректное значение в поле "Исполнитель (юридическое лицо)".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["executiveUnitLegal"]}'
            print('Значение в поле "Исполнитель (юридическое лицо)" успешно проверено')
        else:
            assert len(self.browser.find_elements(*ZakupElementLocators.EXECUTIVE_UNIT_LEGAL_IN_ZP)) == 0, \
                'Отображено пустое поле "Исполнитель (юридическое лицо)"'

        # Проверяем поле "Начальная (максимальная) цена контракта"
        sum_value = str(UserData.user_data_dict["sum"])
        if sum_value.find('.') > 0:
            # Преобразование значения с плавающей точкой под необходимый шаблон
            print("Заглушка")
        else:
            # Преобразование целого значения с разделителями пробелами и припиской валюты
            if UserData.user_data_dict["currency"] == "Доллар":
                sum_value = ('{:,d}'.format(UserData.user_data_dict["sum"])).replace(",", " ") + ',00 $'
            elif UserData.user_data_dict["currency"] == "Евро":
                sum_value = ('{:,d}'.format(UserData.user_data_dict["sum"])).replace(",", " ") + ',00 €'
            else:
                sum_value = ('{:,d}'.format(UserData.user_data_dict["sum"])).replace(",", " ") + ',00 ₽'
            assert self.is_element_text(*ZakupElementLocators.SUM_IN_ZP) == sum_value, \
                f'\nНекорректное значение в поле "Начальная (максимальная) цена контракта" ' \
                f'\nОжидаемый результат: {sum_value}"'
            print('Значение в поле "Сумма договора/контракта" успешно проверено')

        # Проверяем поле "Валюта договора/контракта"
        assert self.is_element_text(*ZakupElementLocators.CURRENCY_IN_ZP) == UserData.user_data_dict["currency"], \
            f'\nНекорректное значение в поле "Валюта договора/контракта".' \
            f'\nОжидаемый результат:{UserData.user_data_dict["currency"]}'
        print('Значение в поле "Валюта договора/контракта" успешно проверено')

        # Проверяем поле "Категория проекта"
        assert self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_IN_ZP) == \
               UserData.user_data_dict["price_category"], "Ценовая категория закупочной процедуры не корректна"
        print('Значение в поле "Категория проекта" успешно проверено')

        # Проверяем поле "Порядок проведения закупочной процедуры"
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            assert self.is_element_text(*ZakupElementLocators.SALE_LAW_TYPE_TENDER_ZP) == UserData.user_data_dict[
                "saleLawType"], \
                f'\nНекорректное значение в поле "Порядок проведения закупочной процедуры".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["saleLawType"]}'
            print('Значение в поле "Порядок проведения закупочной процедуры" успешно проверено')
        elif UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            assert self.is_element_text(*ZakupElementLocators.SALE_LAW_TYPE_ZAPROS_ZP) == UserData.user_data_dict[
                "saleLawType"], \
                f'\nНекорректное значение в поле "Порядок проведения закупочной процедуры".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["saleLawType"]}'
            print('Значение в поле "Порядок проведения закупочной процедуры" успешно проверено')

        # Проверяем поле "Размер обеспечения заявки"
        if UserData.user_data_dict["contractorType"] != "Коммерческое предложение" and \
                len(str(UserData.user_data_dict["applicationSize"])) > 0:
            application_size = str(UserData.user_data_dict["applicationSize"])
            if application_size.find('.') > 0:
                # Преобразование значения с плавающей точкой под необходимый шаблон
                print("Заглушка")
            else:
                # Преобразование целого значения с разделителями пробелами и припиской валюты
                if UserData.user_data_dict["currency"] == "Доллар":
                    application_size = ('{:,d}'.format(UserData.user_data_dict["applicationSize"])).replace(",",
                                                                                                            " ") + ',00 $'
                elif UserData.user_data_dict["currency"] == "Евро":
                    application_size = ('{:,d}'.format(UserData.user_data_dict["applicationSize"])).replace(",",
                                                                                                            " ") + ',00 €'
                else:
                    application_size = ('{:,d}'.format(UserData.user_data_dict["applicationSize"])).replace(",",
                                                                                                            " ") + ',00 ₽'
                assert self.is_element_text(*ZakupElementLocators.APPLICATION_SIZE_IN_ZP) == application_size, \
                    f'\nНекорректное значение в поле "Размер обеспечения заявки" ' \
                    f'\nОжидаемый результат: {application_size}"'
                print('Значение в поле "Размер обеспечения заявки" успешно проверено')

        # Проверяем поле "Размер обеспечения договора/контракта"
        if UserData.user_data_dict["contractorType"] != "Коммерческое предложение" and \
                len(str(UserData.user_data_dict["contractSize"])) > 0:
            contract_size = str(UserData.user_data_dict["contractSize"])
            if contract_size.find('.') > 0:
                # Преобразование значения с плавающей точкой под необходимый шаблон
                print("Заглушка")
            else:
                # Преобразование целого значения с разделителями пробелами и припиской валюты
                if UserData.user_data_dict["currency"] == "Доллар":
                    contract_size = ('{:,d}'.format(UserData.user_data_dict["contractSize"])).replace(",",
                                                                                                      " ") + ',00 $'
                elif UserData.user_data_dict["currency"] == "Евро":
                    contract_size = ('{:,d}'.format(UserData.user_data_dict["contractSize"])).replace(",",
                                                                                                      " ") + ',00 €'
                else:
                    contract_size = ('{:,d}'.format(UserData.user_data_dict["contractSize"])).replace(",",
                                                                                                      " ") + ',00 ₽'
                assert self.is_element_text(*ZakupElementLocators.CONTRACT_SIZE_IN_ZP) == contract_size, \
                    f'\nНекорректное значение в поле "Размер обеспечения договора/контракта" ' \
                    f'\nОжидаемый результат: {contract_size}"'
                print('Значение в поле "Размер обеспечения договора/контракта" успешно проверено')

        # Проверяем поле "Срок подачи на конкурс"
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            assert UserData.user_data_dict["competitionDeadlineFrom"] in \
                   str(self.is_element_text(*ZakupElementLocators.COMPETITION_DEAD_LINE_FROM_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Срок подачи на конкурс".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["competitionDeadlineFrom"]}'
            print('Значение в поле "Срок подачи на конкурс" успешно проверено')

        # Проверяем поле "Предполагаемая дата начала проведения закупки с"
        if UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                UserData.user_data_dict["saleLawType"] == "44-ФЗ":
            assert UserData.user_data_dict["purchase_start_date_from"] in \
                   str(self.is_element_text(*ZakupElementLocators.PURCHASE_START_DATE_FROM)).strip(), \
                f'\nНекорректное значение в поле "Предполагаемая дата начала проведения закупки с".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["purchase_start_date_from"]}'
            print('Значение в поле "Предполагаемая дата начала проведения закупки с" успешно проверено')

        # Проверяем поле "Предполагаемая дата начала проведения закупки по"
        if UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                UserData.user_data_dict["saleLawType"] == "44-ФЗ":
            assert UserData.user_data_dict["purchase_start_date_to"] in \
                   str(self.is_element_text(*ZakupElementLocators.PURCHASE_START_DATE_TO)).strip(), \
                f'\nНекорректное значение в поле "Предполагаемая дата начала проведения закупки по".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["purchase_start_date_to"]}'
            print('Значение в поле "Предполагаемая дата начала проведения закупки по" успешно проверено')

        # Проверяем поле "Срок предоставления ценовой информации"
        if UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                len(str(UserData.user_data_dict["price_information_deadline"])) > 0:
            assert UserData.user_data_dict["price_information_deadline"] in \
                   str(self.is_element_text(*ZakupElementLocators.PRICE_INFORMATION_DEAD_LINE_FROM_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Срок предоставления ценовой информации".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["price_information_deadline"]}'
            print('Значение в поле "Срок предоставления ценовой информации" успешно проверено')

        # Проверяем поле "Плановая дата заключения договора/контракта"
        if UserData.user_data_dict["contractorType"] != "Запрос цен товаров, работ, услуг":
            assert UserData.user_data_dict["startDate"] in \
                   str(self.is_element_text(*ZakupElementLocators.START_DATE_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Плановая дата заключения договора/контракта".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["startDate"]}'
            print('Значение в поле "Плановая дата заключения договора/контракта" успешно проверено')

        # Проверяем поле "Плановая дата окончания договора/контракта"
        if UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            if len(str(UserData.user_data_dict["endDate"])) > 0:
                assert UserData.user_data_dict["endDate"] in \
                       str(self.is_element_text(*ZakupElementLocators.END_DATE_IN_ZP)).strip(), \
                    f'\nНекорректное значение в поле "Плановая дата окончания договора/контракта".' \
                    f'\nОжидаемый результат: {UserData.user_data_dict["endDate"]}'
                print('Значение в поле "Плановая дата окончания договора/контракта" успешно проверено')
        else:
            assert UserData.user_data_dict["endDate"] in \
                   str(self.is_element_text(*ZakupElementLocators.END_DATE_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Плановая дата окончания договора/контракта".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["endDate"]}'
            print('Значение в поле "Плановая дата окончания договора/контракта" успешно проверено')

        # Проверяем поле "Вероятность заключения договора/контракта"
        assert self.is_element_text(*ZakupElementLocators.PROJECT_PROBABILITY_IN_ZP) == str(UserData.user_data_dict[
                                                                                                "projectProbability"]) + "%", \
            f'\nНекорректное значение в поле "Вероятность заключения договора/контракта".' \
            f'\nОжидаемый результат:{UserData.user_data_dict["projectProbability"]}'
        print('Значение в поле "Вероятность заключения договора/контракта" успешно проверено')

        # Проверяем поле "Номер закупки"
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            assert self.is_element_text(*ZakupElementLocators.PURCHASE_NUMBER_IN_ZP) == \
                   UserData.user_data_dict["purchase_number"], \
                f'\nНекорректное значение в поле "Номер закупки".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["purchase_number"]}'
            print('Значение в поле "Номер закупки" успешно проверено')

        # Проверяем поле "Номер запроса цен на Официальном сайте ЕИС"
        if UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                UserData.user_data_dict["saleLawType"] == "44-ФЗ":
            assert UserData.user_data_dict["eis_price_number"] in \
                   str(self.is_element_text(*ZakupElementLocators.EIS_PRICE_NUMBER_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Номер запроса цен на Официальном сайте ЕИС".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["eis_price_number"]}'
            print('Значение в поле "Номер запроса цен на Официальном сайте ЕИС" успешно проверено')

        # Проверяем поле "Ссылка на запрос на Официальном сайте ЕИС"
        if UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг" and \
                UserData.user_data_dict["saleLawType"] == "44-ФЗ":
            assert UserData.user_data_dict["eis_price_link"] in \
                   str(self.is_element_text(*ZakupElementLocators.EIS_PRICE_LINK_IN_ZP)).strip(), \
                f'\nНекорректное значение в поле "Ссылка на запрос на Официальном сайте ЕИС".' \
                f'\nОжидаемый результат: {UserData.user_data_dict["eis_price_link"]}'
            print('Значение в поле "Ссылка на запрос на Официальном сайте ЕИС" успешно проверено')

        # Проверяем поле "Связанные продажи"
        if self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Seller" or \
                self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Seller2" or \
                self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Dir" or \
                self.is_element_text(*BasePageLocators.USER_NAME) == "Mr_KSUP_Dir2":
            assert self.is_element_text(*ZakupElementLocators.RELATED_SALES_IN_ZP) == \
                   UserData.user_data_dict["fullName"], \
                f'\nНекорректное значение в поле "Связанные продажи".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["fullName"]}'
            print('Значение в поле "Связанные продажи" успешно проверено')

        # Проверяем поле "Статус продажи"
        assert self.is_element_text(*ZakupElementLocators.PRESALE_STATUS_IN_ZP) == "В работе", \
            f'\nНекорректное значение в поле "Статус продажи".' \
            f'\nОжидаемый результат: "В работе"'
        print('Значение в поле "Статус продажи" успешно проверено')

        # Проверяем поле "Ссылка на закупку"
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка":
            assert self.is_element_text(*ZakupElementLocators.PURCHASE_LINK_IN_ZP) == \
                   UserData.user_data_dict["purchase_link"], \
                f'\nНекорректное значение в поле "Ссылка на закупку".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["purchase_link"]}'
            print('Значение в поле "Ссылка на закупку" успешно проверено')

        # Проверяем поле "Результаты работ"
        if len(UserData.user_data_dict["descriptionText"]) > 0:
            assert self.is_element_text(*ZakupElementLocators.DESCRIPTION_TEXT_IN_ZP) == \
                   UserData.user_data_dict["descriptionText"], \
                f'\nНекорректное значение в поле "Результаты работ".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["descriptionText"]}'
            print('Значение в поле "Результаты работ')
        else:
            assert len(self.browser.find_elements(*ZakupElementLocators.DESCRIPTION_TEXT_IN_ZP)) == 0, \
                'Отображено пустое поле "Результаты работ"'
            print('Пустое поле "Результаты работ" успешно не отображено')

        # Проверяем поле "Риски проекта с точки зрения Департамента"
        if len(UserData.user_data_dict["project_risk_department"]) > 0:
            assert self.is_element_text(*ZakupElementLocators.PROJECT_RISKS_DEPARTMENT_IN_ZP) == \
                   UserData.user_data_dict["project_risk_department"], \
                f'\nНекорректное значение в поле "Риски проекта с точки зрения Департамента".' \
                f'\nОжидаемый результат:{UserData.user_data_dict["project_risk_department"]}'
            print('Значение в поле "Риски проекта с точки зрения Департамента')
        else:
            assert len(self.browser.find_elements(*ZakupElementLocators.PROJECT_RISKS_DEPARTMENT_IN_ZP)) == 0, \
                'Отображено пустое поле "Риски проекта с точки зрения Департамента"'
            print('Пустое поле "Риски проекта с точки зрения Департамента')

    def verify_draft_status_zakup(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Черновик"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

    def verify_visibility_approval_button_zp(self):
        assert self.is_visibility_of_element_located(*ZakupElementLocators.SEND_APPROVAL_ELEMENT), \
            'Кнопка "Отправить на согласование" не отобрежена'

    def verify_visibility_button_create_contract(self):
        assert self.is_visibility_of_element_located(
            *ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP), \
            'Кнопка "Внести информацию о договоре/контракте" не отобрежена'

    def verify_unvisibility_approval_button(self):
        assert self.is_element_clickable(*ZakupElementLocators.SEND_APPROVAL_ELEMENT) is False, \
            'Кнопка "Отправить на согласование" доступна для нажатия'

    def send_zakup_for_approval(self):
        self.is_element_clickable(*ZakupElementLocators.SEND_APPROVAL_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.SEND_APPROVAL_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT).click()

    def verify_zakup_waiting_status_approval_legal(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании с юридической службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        # Проверяем статус "Ожидает согласования"
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования с юридической службой'

    def verify_zakup_successfully_status_approval_legal(self):
        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано юридической службой" в строке согласования с юридической службой'

    def verify_zakup_reject_status_approval_legal(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано с юридической службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с юридической службой'

    def verify_zakup_waiting_status_approval_count(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании с бухгалтерией"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        # Проверяем статус "Ожидает согласования"
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования с бухгалтерией'

    def verify_zakup_successfully_status_approval_count(self):
        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с бухгалтерией'

    def verify_zakup_reject_status_approval_count(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано бухгалтерией"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с бухгалтерией"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с бухгалтерией'

    def verify_zakup_waiting_status_approval_fin(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании с финансовой службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        # Проверяем статус "Ожидает согласования"
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования с финансовой службой'

    def verify_zakup_successfully_status_approval_fin(self):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (UserData.user_data_dict["contractorType"] == "Тендерная заявка" and UserData.user_data_dict[
            "price_category"] == "C") or \
                (UserData.user_data_dict["contractorType"] == "Тендерная заявка"
                 and UserData.user_data_dict["price_category"] == "B"
                 and UserData.user_data_dict["groupTypeWork"] == "Other"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                         "Согласовано с финансовой службой"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с финансовой службой'

    def verify_zakup_reject_status_approval_fin(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано с финансовой службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с финансовой службой'

    def verify_zakup_waiting_status_approval_udprpo(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании УДПР ПО"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Ожидает согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования со службой УДПР ПО'

    def verify_zakup_successfully_status_approval_udprpo(self):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (UserData.user_data_dict["contractorType"] == "Тендерная заявка"
            and UserData.user_data_dict["groupTypeWork"] == "Software"
            and UserData.user_data_dict["price_category"] == "B") \
                or (UserData.user_data_dict["contractorType"] != "Тендерная заявка"
                    and UserData.user_data_dict["groupTypeWork"] == "Software"
                    and UserData.user_data_dict["price_category"] != "C"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                         "Согласовано УДПР ПО"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования со службой УДПР ПО'

    def verify_zakup_reject_status_approval_udprpo(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Не согласовано УДПР ПО"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с УДПР ПО"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования со службой УДПР ПО'

    def verify_zakup_waiting_status_approval_kkp(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "На согласовании в ККП"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Ожидает согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования со службой ККП'

    def verify_zakup_successfully_status_approval_kkp(self):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (UserData.user_data_dict["contractorType"] == "Тендерная заявка"
                and UserData.user_data_dict["price_category"] != "A"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                         "Участие в проекте согласовано в ККП"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования со службой ККП'

    def verify_zakup_reject_status_approval_kkp(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования со службой ККП'

    def verify_zakup_not_require_status_approval(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_IN_ZP,
                                                     "Внутреннее согласование не требуется"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

    def verify_zakup_revision_status_approval(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отправлено на доработку"), \
            'Некорректный статус или отсутствует статус в строке "Согласование ККП"'

        # Проверяем цвет статуса "Отправлено на доработку"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отправлено на доработку" в строке согласования со службой ККП'

    def approval_zakup_legal(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_legal)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_count(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_count)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_fin(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_fin)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_udprpo(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_udprpo)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_kkp(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_kkp)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_legal(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_legal)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_count(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_count)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_fin(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_fin)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_excel)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_udprpo(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_udprpo)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_mp4)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_kkp(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_kkp)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def revision_zakup_from_kkp(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REVISION_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REVISION_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REVISION_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_revision_kkp)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def escalate_on_kkp(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.ESCALATE_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.ESCALATE_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ESCALATE_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_escalation_kkp)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def go_to_create_contract_based_on_zp(self):
        count_refresh_page = 0
        while count_refresh_page <= 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_present(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP).click()
