import time

from pages.base_page import BasePage
from pages.locators import ContractElementLocators
from userdata.user_data import UserData
from selenium.webdriver.support.color import Color


class ContractElementPage(BasePage):
    def verify_general_information_contract(self, user_data_dict):
        # Проверяем титул карточки который соответствует названию сущности
        assert self.is_element_text(*ContractElementLocators.TITLE_IN_CONTRACT) == user_data_dict["fullName"], \
            'Название карточки "Договор/контракт" не соответствует входным данным'
        print('Название карточки "Договор/контракт" успешно проверено')

        # Проверяем поле "Заказчик"
        assert self.is_element_text(*ContractElementLocators.CUSTOMER_IN_CONTRACT) == user_data_dict["customer"], \
            f'\nНекорректное значение в поле "Заказчик".' \
            f'\nОжидаемый результат:{user_data_dict["customer"]}'
        print('Значение в поле "Заказчик" успешно проверено')

        # Проверяем поле "Подразделение-продавец"
        assert self.is_element_text(*ContractElementLocators.SALES_UNIT_IN_CONTRACT) == user_data_dict["salesUnit"], \
            f'\nНекорректное значение в поле "Подразделение-продавец". ' \
            f'\nОжидаемый результат:{user_data_dict["salesUnit"]}'
        print('Значение в поле "Подразделение-продавец" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-продавца"
        assert self.is_element_text(*ContractElementLocators.SALES_MANAGER_IN_CONTRACT) == user_data_dict[
            "salesManager"], \
            f'\nНекорректное значение в поле "Ответственный менеджер подразделения-продавца".' \
            f'\nОжидаемый результат:{user_data_dict["salesManager"]}'
        print('Значение в поле "Ответственный менеджер подразделения-продавца" успешно проверено')

        # Проверяем поле "Подразделение-исполнитель"
        assert self.is_element_text(*ContractElementLocators.EXECUTIVE_UNIT_IN_CONTRACT) == user_data_dict[
            "executiveUnit"], \
            f'\nНекорректное значение в поле "Подразделение-исполнитель". ' \
            f'\nОжидаемый результат:{user_data_dict["executiveUnit"]}'
        print('Значение в поле "Подразделение-исполнитель" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-исполнителя"
        assert self.is_element_text(*ContractElementLocators.EXECUTIVE_MANAGER_IN_CONTRACT) == user_data_dict[
            "executiveManager"], \
            f'\nНекорректное значение в поле "Ответственный менеджер подразделения-исполнителя".' \
            f'\nОжидаемый результат:{user_data_dict["executiveManager"]}'
        print('Значение в поле "Ответственный менеджер подразделения-исполнителя" успешно проверено')

        # Проверяем поле "Исполнитель (юридическое лицо)"
        assert self.is_element_text(*ContractElementLocators.EXECUTIVE_UNIT_LEGAL_IN_CONTRACT) == \
               user_data_dict["executiveUnitLegal"], \
            f'\nНекорректное значение в поле "Исполнитель (юридическое лицо)".' \
            f'\nОжидаемый результат:{user_data_dict["executiveUnitLegal"]}'
        print('Значение в поле "Исполнитель (юридическое лицо)" успешно проверено')

        # Проверяем поле "Тип работ и услуг"
        work_services_value = ''
        for category in user_data_dict["typeOfWorkServices"]:
            work_services_value = work_services_value + category + '; '
        work_services_value = work_services_value.strip()
        assert self.is_element_text(*ContractElementLocators.TYPE_OF_WORK_SERVCICES_IN_CONTRACT) == work_services_value, \
            f'\nНекорректное значение в поле "Тип работ и услуг".' \
            f'\n Ожидаемый результат: {work_services_value}'
        print('Значение в поле "Тип работ и услуг" успешно проверено')

        assert self.is_element_text(*ContractElementLocators.PRICE_CATEGORY_IN_CONTRACT) == \
               user_data_dict["priceCategory"], "Ценовая категория контракта не корректна"

        # Проверяем поле "Сумма договора/контракта"
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
            assert self.is_element_text(*ContractElementLocators.SUM_IN_CONTRACT) == sum_value, \
                f'\nНекорректное значение в поле "Начальная (максимальная) цена контракта" ' \
                f'\nОжидаемый результат: {sum_value}"'
            print('Значение в поле "Сумма договора/контракта" успешно проверено')

        # Проверяем поле "Валюта договора/контракта"
        assert self.is_element_text(*ContractElementLocators.CURRENCY_IN_CONTRACT) == user_data_dict[
            "currency"], \
            f'\nНекорректное значение в поле "Валюта договора/контракта".' \
            f'\nОжидаемый результат:{user_data_dict["currency"]}'
        print('Значение в поле "Валюта договора/контракта" успешно проверено')

        # Проверяем поле "Категория проекта"
        assert self.is_element_text(*ContractElementLocators.PRICE_CATEGORY_IN_CONTRACT) == \
               user_data_dict["priceCategory"], \
            f'Ценовая категория договор/контракта не корректна.' \
            f'\n Ожидаемый результат: {user_data_dict["priceCategory"]}'
        print('Значение в поле "Категория проекта" успешно проверено')

        # Проверяем поле "Номер"
        if len(str(user_data_dict["numberContract"])) > 0:
            assert self.is_element_text(*ContractElementLocators.CONTRACT_NUMBER_IN_CONTRACT) == \
                   user_data_dict["numberContract"], \
                f'Значение в поле "Номер" не корректно.' \
                f'\n Ожидаемый результат: {user_data_dict["numberContract"]}'
            print('Значение в поле "Категория проекта" успешно проверено')
        else:
            assert self.browser.find_element(
                *ContractElementLocators.CONTRACT_NUMBER_IN_CONTRACT).is_displayed() is False, \
                'Отображено пустое поле "Номер"'
            print('Пустое поле "Номер" успешно не отображено')

        # Проверяем поле "Дата заключения"
        assert user_data_dict["startDate"] in \
               str(self.is_element_text(*ContractElementLocators.START_DATE_IN_CONTRACT)).strip(), \
            f'\nНекорректное значение в поле "Дата заключения договора/контракта".' \
            f'\nОжидаемый результат: {user_data_dict["startDate"]}'
        print('Значение в поле "Дата заключения договора/контракта" успешно проверено')

        # Проверяем поле "Дата окончания"
        assert user_data_dict["endDate"] in \
               str(self.is_element_text(*ContractElementLocators.END_DATE_IN_CONTRACT)).strip(), \
            f'\nНекорректное значение в поле "Дата окончания договора/контракта".' \
            f'\nОжидаемый результат: {user_data_dict["endDate"]}'
        print('Значение в поле "Дата окончания договора/контракта" успешно проверено')

        # Проверяем поле "Номер закупки"
        if len(str(user_data_dict["purchaseNumber"])) > 0:
            assert self.is_element_text(*ContractElementLocators.PURCHASE_NUMBER_IN_CONTRACT) == \
                   user_data_dict["purchaseNumber"], \
                f'\nНекорректное значение в поле "Номер закупки".' \
                f'\nОжидаемый результат:{user_data_dict["purchaseNumber"]}'
            print('Значение в поле "Номер закупки" успешно проверено')
        else:
            assert self.browser.find_element(
                *ContractElementLocators.PURCHASE_NUMBER_IN_CONTRACT).is_displayed() is False, \
                'Отображено пустое поле "Номер закупки"'
            print('Пустое поле "Номер закупки" успешно не отображено')

        # Проверяем поле "Статус контракта"
        assert "Проект" in self.is_element_text(*ContractElementLocators.CONTRACT_STATUS), \
            f'\nНекорректное значение в поле "Статус контракта".' \
            f'\nОжидаемый результат: Проект'
        print('Значение в поле "Статус контракта" успешно проверено')

        # Проверяем поле "Территория применения"
        territory_value = ''
        for territory in user_data_dict["territory"]:
            territory_value = territory_value + territory + '; '
        territory_value = territory_value.strip()
        assert self.is_element_text(*ContractElementLocators.TERRITORY_IN_CONTRACT) == territory_value, \
            f'\nНекорректное значение в поле "Территория применения".' \
            f'\n Ожидаемый результат: {territory_value}'
        print('Значение в поле "Территория применения" успешно проверено')

        # Проверяем поле "Ключевые технологии"
        technologies_value = ''
        for technologies in user_data_dict["technologies"]:
            technologies_value = technologies_value + technologies + '; '
        technologies_value = technologies_value.strip()
        assert self.is_element_text(*ContractElementLocators.TECHNOLOGIES_IN_CONTRACT) == technologies_value, \
            f'\nНекорректное значение в поле "Ключевые технологии".' \
            f'\n Ожидаемый результат: {technologies_value}'
        print('Значение в поле "Ключевые технологии" успешно проверено')

        # Проверяем поле "Уникальный код проекта"
        if len(str(user_data_dict["projectUniqueCode"])) > 0:
            assert self.is_element_text(*ContractElementLocators.PROJECT_UNIQUE_CODE_IN_CONTRACT) == \
                   user_data_dict["projectUniqueCode"], \
                f'\nНекорректное значение в поле "Уникальный код проекта".' \
                f'\nОжидаемый результат:{user_data_dict["projectUniqueCode"]}'
            print('Значение в поле "Уникальный код проекта" успешно проверено')
        else:
            assert self.browser.find_element(
                *ContractElementLocators.PROJECT_UNIQUE_CODE_IN_CONTRACT).is_displayed() is False, \
                'Отображено пустое поле "Уникальный код проекта"'
            print('Пустое поле "Уникальный код проекта" успешно не отображено')

        # Проверяем поле "Связанный проект"
        assert self.is_element_text(*ContractElementLocators.PROJECT_IN_CONTRACT) == user_data_dict["project"], \
            f'Значение в поле "Связанный проект" не корректно.' \
            f'\nОжидаемый результат: {user_data_dict["project"]}' \
            f'\nФактический результат: {self.is_element_text(*ContractElementLocators.PROJECT_IN_CONTRACT)}'
        print('Значение в поле "Связанный проект" успешно проверено')

        # Проверяем поле "Ссылка на закупку"
        if len(str(user_data_dict["purchaseLink"])) > 0:
            assert self.is_element_text(*ContractElementLocators.PURCHASE_LINK_IN_CONTRACT) == \
                   user_data_dict["purchaseLink"], \
                f'Значение в поле "Ссылка на закупку" не корректно.' \
                f'\n Ожидаемый результат: {user_data_dict["purchaseLink"]}'
            print('Значение в поле "Ссылка на закупку" успешно проверено')
        else:
            assert self.browser.find_element(
                *ContractElementLocators.PURCHASE_LINK_IN_CONTRACT).is_displayed() is False, \
                'Отображено пустое поле "Ссылка на закупку"'
            print('Пустое поле "Ссылка на закупку" успешно не отображено')

        # Проверяем поле "Ссылка на договор/контракт на Официальном сайте ЕИС"
        if len(str(user_data_dict["eisContractLink"])) > 0:
            assert self.is_element_text(*ContractElementLocators.EIS_CONTRACT_LINK_IN_CONTRACT) == \
                   user_data_dict["eisContractLink"], \
                f'Значение в поле "Ссылка на договор/контракт на Официальном сайте ЕИС" не корректно.' \
                f'\n Ожидаемый результат: {user_data_dict["eisContractLink"]}'
            print('Значение в поле "Ссылка на договор/контракт на Официальном сайте ЕИС" успешно проверено')
        else:
            assert self.browser.find_element(
                *ContractElementLocators.EIS_CONTRACT_LINK_IN_CONTRACT).is_displayed() is False, \
                'Отображено пустое поле "Ссылка на договор/контракт на Официальном сайте ЕИС"'
            print('Пустое поле "Ссылка на договор/контракт на Официальном сайте ЕИС" успешно не отображено')

        # Проверяем поле "Цели и задачи"
        assert self.is_element_text(*ContractElementLocators.DESCRIPTION_TEXT_IN_CONTRACT) == \
               user_data_dict["descriptionText"], \
            f'Значение в поле "Цели и задачи" не корректно.' \
            f'\n Ожидаемый результат: {user_data_dict["descriptionText"]}'
        print('Значение в поле "Цели и задачи" успешно проверено')

        # Проверяем поле "Количественные показатели реализации проекта"
        if len(str(user_data_dict["quantitativeIndicatorsProject"])) > 0:
            assert self.is_element_text(*ContractElementLocators.QUANTITATIVE_INDICATORS_PROJECT) == \
                   user_data_dict["quantitativeIndicatorsProject"], \
                f'Значение в поле "Количественные показатели реализации проекта" не корректно.' \
                f'\n Ожидаемый результат: {user_data_dict["quantitativeIndicatorsProject"]}'
            print('Значение в поле "Количественные показатели реализации проекта" успешно проверено')
        else:
            assert self.browser.find_element(
                *ContractElementLocators.QUANTITATIVE_INDICATORS_PROJECT).is_displayed() is False, \
                'Отображено пустое поле "Количественные показатели реализации проекта"'
            print('Пустое поле "Количественные показатели реализации проекта" успешно не отображено')

    def verify_joint_bidding_inform_contract(self, user_data_dict):
        # Переходим на вкладку "Заключенные договоры/контракты"
        self.browser.find_element(*ContractElementLocators.JOINT_BIDDING_CONTRACT_TABS).click()
        time.sleep(2)
        # Проверяем заполнение информации в таблице
        sum_joint_bidding = 0
        current_row = 0
        count_joint_contracts_row = len(user_data_dict["jointBiddingContracts"])
        while current_row < count_joint_contracts_row:
            # Проверяем значение в поле "Заказчик"
            customer_value = (self.browser.find_elements(*ContractElementLocators.JOINT_BIDDING_CUSTOMER_VALUE)[current_row]).text
            assert customer_value == user_data_dict["jointBiddingContracts"][current_row]["customer"], \
                f'Не корректное значение в поле "Заказчик" в строке {current_row}' \
                f'\n Ожидаемый результат: {user_data_dict["jointBiddingContracts"][current_row]["customer"]}' \
                f'\n Фактический результат: {customer_value}'

            # Проверяем значение в поле "Номер"
            number_value = (self.browser.find_elements(*ContractElementLocators.JOINT_BIDDING_NUMBER_VALUE)[current_row]).text
            assert number_value == user_data_dict["jointBiddingContracts"][current_row]["number"], \
                f'Не корректное значение в поле "Номер" в строке {current_row}' \
                f'\n Ожидаемый результат: {user_data_dict["jointBiddingContracts"][current_row]["number"]}' \
                f'\n Фактический результат: {number_value}'

            # Проверяем значение в поле "Дата заключения"
            start_date_value = (self.browser.find_elements(*ContractElementLocators.JOINT_BIDDING_START_DATE_VALUE)[current_row]).text
            assert start_date_value == user_data_dict["jointBiddingContracts"][current_row]["startDate"], \
                f'Не корректное значение в поле "Дата заключения" в строке {current_row}' \
                f'\n Ожидаемый результат: {user_data_dict["jointBiddingContracts"][current_row]["startDate"]}' \
                f'\n Фактический результат: {start_date_value}'

            # Проверяем значение в поле "Дата завершения"
            end_date_value = (self.browser.find_elements(*ContractElementLocators.JOINT_BIDDING_END_DATE_VALUE)[current_row]).text
            assert end_date_value == user_data_dict["jointBiddingContracts"][current_row]["endDate"], \
                f'Не корректное значение в поле "Дата завершения" в строке {current_row}' \
                f'\n Ожидаемый результат: {user_data_dict["jointBiddingContracts"][current_row]["endDate"]}' \
                f'\n Фактический результат: {end_date_value}'

            # Проверяем значение в поле "Сумма договора/контракта"
            sum_value = (self.browser.find_elements(*ContractElementLocators.JOINT_BIDDING_SUM_VALUE)[current_row]).text
            sum_value_exception = ('{:,d}'.format(user_data_dict["jointBiddingContracts"][current_row]["sum"])).replace(",", " ") + ',00'
            assert sum_value == sum_value_exception, \
                f'Не корректное значение в поле "Сумма договора/контракта" в строке {current_row}' \
                f'\n Ожидаемый результат: {sum_value_exception}' \
                f'\n Фактический результат: {sum_value}'
            sum_joint_bidding += user_data_dict["jointBiddingContracts"][current_row]["sum"]
            current_row += 1
        # Проверяем значение в Поле "Итого"
        sum_joint_bidding_exception = ('{:,d}'.format(sum_joint_bidding)).replace(",", " ") + ',00'
        total_sum_joint_bidding = self.is_element_text(*ContractElementLocators.JOINT_BIDDING_TOTAL_SUM_VALUE)
        assert sum_joint_bidding_exception == total_sum_joint_bidding, \
            f'Некорректное значение в поле "Итого"' \
            f'\nОжидаемый результат: {sum_joint_bidding_exception}' \
            f'\nФактический результат: {total_sum_joint_bidding}'

    def send_contract_for_approval(self):
        self.is_element_clickable(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.CONFIRM_SEND_APPROVAL_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.CONFIRM_SEND_APPROVAL_CONTRACT).click()

    def verify_unvisibility_approval_button(self):
        assert self.is_element_clickable(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT) is False, \
            'Кнопка "Отправить на согласование" доступна для нажатия после отклонения ККП'

    def verify_visibility_button_send_to_approval_contract(self):

        assert self.is_visibility_of_element_located(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT, 3), \
            'Кнопка "Отправить на согласование(Договор/контракт)" не отобрежена'

    def verify_contract_waiting_status_approval_legal(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        assert self.is_text_to_be_present_in_element(
            *ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT, "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

    def verify_contract_successfully_status_approval_legal(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

    def verify_contract_reject_status_approval_leagal(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

    def verify_contract_waiting_status_approval_count(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

    def verify_contract_successfully_status_approval_count(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

    def verify_contract_reject_status_approval_count(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

    def verify_contract_waiting_status_approval_fin(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

    def verify_contract_successfully_status_approval_fin(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

    def verify_contract_reject_status_approval_fin(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

    def verify_contract_waiting_status_approval_udprpo(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

    def verify_contract_successfully_status_approval_udprpo(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

    def verify_contract_reject_status_approval_udprpo(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

    def verify_contract_waiting_status_approval_kkp(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

    def verify_contract_successfully_status_approval_kkp(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

    def verify_contract_reject_status_approval_kkp(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

    def verify_contract_revision_status_approval_kkp(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отправлено на доработку"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

        # Проверяем цвет статуса "Отправлено на доработку"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отправлено на доработку" в строке согласования со службой ККП'

    def approval_contract_legal(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_legal)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_count(self):

        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_count)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_fin(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_fin)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_excel)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_udprpo(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_udprpo)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_kkp(self):

        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_kkp)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def reject_contract_legal(self):
        self.is_element_clickable(*ContractElementLocators.REJECT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REJECT_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_reject_legal)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REJECT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def reject_contract_count(self):

        self.is_element_clickable(*ContractElementLocators.REJECT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REJECT_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_reject_count)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REJECT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def reject_contract_fin(self):
        self.is_element_clickable(*ContractElementLocators.REJECT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REJECT_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_reject_fin)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_excel)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REJECT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def reject_contract_udprpo(self):
        self.is_element_clickable(*ContractElementLocators.REJECT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REJECT_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_reject_udprpo)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REJECT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def reject_contract_kkp(self):
        self.is_element_clickable(*ContractElementLocators.REJECT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REJECT_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_reject_kkp)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REJECT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def escalate_contract_on_kkp(self):
        self.is_element_clickable(*ContractElementLocators.ESCALATE_CONTRACT)
        self.browser.find_element(*ContractElementLocators.ESCALATE_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_escalation_kkp)
        self.browser.find_element(*ContractElementLocators.CONFIRM_ESCALATE_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def revision_contract_from_kkp(self):
        self.is_element_clickable(*ContractElementLocators.REVISION_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REVISION_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_escalation_kkp)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REVISION_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()
