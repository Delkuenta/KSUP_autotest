import time

import delayed_assert
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import ContractElementLocators
from userdata.user_data import UserData
from selenium.webdriver.support.color import Color


class ContractElementPage(BasePage):
    # Проверка информации на вкладке "Общие сведения"
    def verify_general_information_contract(self, user_data_dict):
        # Переходим на вкладку "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        time.sleep(1)

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
        if "contractStatus" in user_data_dict:
            assert user_data_dict["contractStatus"] in self.is_element_text(*ContractElementLocators.CONTRACT_STATUS),\
                f'\nНекорректное значение в поле "Статус контракта".' \
                f'\nОжидаемый результат: {user_data_dict["contractStatus"]}'
        else:
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

    # Проверка информации на вкладке "Прикрепленные файлы"
    def verify_attached_files_information(self):
        self.browser.find_element(*ContractElementLocators.ATTACHED_FILES_ELEMENT).click()
        time.sleep(2)

        # Проверяем текст в поле "Контракт"
        actual_text = self.is_element_text(*ContractElementLocators.CONTRACT_FIELD)
        expected_text = UserData.name_doc_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Контракт" на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Проверяем текст в поле "Пояснительная служебная записка"
        actual_text = self.is_element_text(*ContractElementLocators.EXPLANATORY_MEMORANUM_FIELD)
        expected_text = UserData.name_doc_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Пояснительная служебная записка" '
                              'на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Проверяем текст в поле "Реестр рисков, Карта рисков"
        actual_text = self.is_element_text(*ContractElementLocators.RISK_MAP_AND_REGISTRY_FIELD)
        expected_text = UserData.name_jpg_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Реестр рисков, Карта рисков" '
                              'на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Проверяем текст в поле "Иное"
        actual_text = self.is_element_text(*ContractElementLocators.OTHER_FIELD)
        expected_text = UserData.name_doc_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Иное" '
                              'на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

    # Проверка значения в поле "Связанная пресейловая активность"
    def verify_related_presale(self, user_data_dict):
        # Проверяем отображение значения связанной пресейловой активности в поле "Пресейловые активности"
        assert self.is_element_text(*ContractElementLocators.RELATED_PRESALE) == user_data_dict["fullName"],\
            f'Значение в поле "Пресейловые активности" не корректно.\n ' \
            f'Ожидаемый результат: "{user_data_dict["fullName"]}"'
        print('Значение в поле  "Пресейловые активности" успешно проверено')

    # Проверка значения в поле "Связанная закупочная процедура"
    def verify_related_zakup(self, user_data_dict):
        # Проверяем отображение значения связанной закупочной процедуры в поле "Связанная закупочная процедура"
        assert self.is_element_text(*ContractElementLocators.RELATED_ZAKUP) == user_data_dict["fullName"],\
            f'Значение в поле "Связанная закупочная процедура" не корректно.\n ' \
            f'Ожидаемый результат: "{user_data_dict["fullName"]}"'
        print('Значение в поле  "Связанная закупочная процедура" успешно проверено')

    # Проверка информации на вкладке "Заключенные договоры/контракты"
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

    # Отправка контракта на согласования
    def send_contract_for_approval(self):
        self.is_element_clickable(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT).click()

        # Выбираем сотрудника из юридической службы
        self.browser.find_element(*ContractElementLocators.EMPLOYEE_LEGAL_FIELD).click()
        how, what = ContractElementLocators.EMPLOYEE_LEGAL_DROPDOWN_ELEMENT
        what = what.replace("employee_legal", "Mr_KSUP_Legal")
        self.browser.find_element(how, what).click()

        # Выбираем сотрудника из бухгалтерии
        self.browser.find_element(*ContractElementLocators.EMPLOYEE_COUNT_FIELD).click()
        how, what = ContractElementLocators.EMPLOYEE_COUNT_DROPDOWN_ELEMENT
        what = what.replace("employee_count", "Mr_KSUP_Count")
        self.browser.find_element(how, what).click()

        # Выбираем сотрудника из финансовой службы
        self.browser.find_element(*ContractElementLocators.EMPLOYEE_FIN_FIELD).click()
        how, what = ContractElementLocators.EMPLOYEE_FIN_DROPDOWN_ELEMENT
        what = what.replace("employee_fin", "Mr_KSUP_Fin")
        self.browser.find_element(how, what).click()

        # Жмем кнопку отправить
        self.browser.find_element(*ContractElementLocators.CONFIRM_SELECT_EMPLOYEE_BUTTON).click()
        breakpoint()

    # Проверка НЕ отображения кнопки "Отправить на согласования"
    def verify_unvisibility_send_approval_button(self):
        assert self.is_element_clickable(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT) is False, \
            'Кнопка "Отправить на согласование" доступна для нажатия после отклонения ККП'

    # Проверка отображения кнопки "Отправить на согласования"
    def verify_visibility_button_send_to_approval_contract(self):

        assert self.is_visibility_of_element_located(*ContractElementLocators.SEND_APPROVAL_CONTRACT_CONTRACT, 3), \
            'Кнопка "Отправить на согласование(Договор/контракт)" не отобрежена'

    # Проверка отображения кнопки "Добавить бюджет проекта"
    def verify_visibility_budget_button(self):
        assert self.is_visibility_of_element_located(*ContractElementLocators.BUDGET_CONTRACT_BUTTON, 5), \
            'Кнопка "Внести информацию о договоре/контракте" не отобрежена'

    # Проверка отображения статуса "На согласовании с юридической службой"
    def verify_contract_waiting_status_approval_legal(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "На согласовании с юридической службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус согласования на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        """
        assert self.is_text_to_be_present_in_element(
            *ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT, "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'
        """
        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование юридической службой" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования с юридической службой'

    # Проверка отображения статуса "Согласовано юридической службой"
    def verify_contract_successfully_status_approval_legal(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'
        """
        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование юридической службой" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано юридической службой" в строке согласования с юридической службой'

    # Проверка отображения статуса "Не согласовано с юридической службой"
    def verify_contract_reject_status_approval_legal(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "Не согласовано с юридической службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'
        """
        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование юридической службой" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с юридической службой'

    # Проверка отображения статуса "На согласовании с бухгалтерией"
    def verify_contract_waiting_status_approval_count(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "На согласовании с бухгалтерией"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем согласование на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование бухгалтерией" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования с бухгалтерией'

    # Проверка отображения статуса "Согласовано с бухгалтерией"
    def verify_contract_successfully_status_approval_count(self):
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование бухгалтерией" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с бухгалтерией'

    # Проверка отображения статуса "Не согласовано бухгалтерией"
    def verify_contract_reject_status_approval_count(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "Не согласовано бухгалтерией"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с бухгалтерией"'

        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование бухгалтерией" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с бухгалтерией'

    # Проверка отображения статуса "На согласовании с финансовой службой"
    def verify_contract_waiting_status_approval_fin(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "На согласовании с финансовой службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование бухгалтерией" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования с финансовой службой'

    # Проверка отображения статуса "Согласовано с финансовой службой"
    def verify_contract_successfully_status_approval_fin(self, user_data_dict):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (user_data_dict["priceCategory"] == "C") or \
                (user_data_dict["priceCategory"] == "B"
                 and user_data_dict["groupTypeWork"] == "Other"):
            self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
            assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                         "Согласовано с финансовой службой"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()
        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование финансовой службой" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с финансовой службой'

    # Проверка отображения статуса "Не согласовано с финансовой службой"
    def verify_contract_reject_status_approval_fin(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "Не согласовано с финансовой службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'
        """
        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: "Согласование финансовой службой" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с финансовой службой'

    # Проверка отображения статуса "На согласовании Директором по разработке ПО"
    def verify_contract_waiting_status_approval_udprpo(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "На согласовании Директором по разработке ПО"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c Директором по разработке ПО"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: ""Согласование c Директором по разработке ПО" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования со службой Директором по разработке ПО'

    # Проверка отображения статуса "Согласовано Директором по разработке ПО"
    def verify_contract_successfully_status_approval_udprpo(self, user_data_dict):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if user_data_dict["groupTypeWork"] == "Software" and user_data_dict["priceCategory"] == "B":
            self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
            assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                         "Согласовано Директором по разработке ПО"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус на вкладке "Статс согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c Директором по разработке ПО"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: ""Согласование c Директором по разработке ПО" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с Директором по разработке ПО'

    # Проверка отображения статуса "Не согласовано Директором по разработке ПО"
    def verify_contract_reject_status_approval_udprpo(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "Не согласовано Директором по разработке ПО"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано Директором по разработке ПО"'

        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c Директором по разработке ПО"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: ""Согласование c Директором по разработке ПО" - "Отклонено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования со службой Директором по разработке ПО'

    # Проверка отображения статуса "На согласовании в ККП"
    def verify_contract_waiting_status_approval_kkp(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "На согласовании в ККП"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласуется"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласуется", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: ""Согласование c ККП" - "Согласуется"'

        # Проверяем цвет статуса "Согласуется"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(last_result.value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Согласуется" в строке согласования со службой ККП'

    # Проверка отображения статуса "Участие в проекте согласовано в ККП"
    def verify_contract_successfully_status_approval_kkp(self, user_data_dict):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if user_data_dict["priceCategory"] != "A":
            self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
            assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                         "Участие в проекте согласовано в ККП"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Согласовано", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: ""Согласование c ККП" - "Согласовано"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования со службой ККП'

    # Проверка отображения статуса "Участие в проекте не согласовано в ККП"
    def verify_contract_reject_status_approval_kkp(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "Участие в проекте не согласовано в ККП"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Участие в проекте не согласовано в ККП"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'
        
        """
        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Прекращено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: ""Согласование c ККП" - "Прекращено"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования со службой ККП'

    # Проверка отображения статуса "Отправлено на доработку ККП"
    def verify_contract_revision_status_approval_kkp(self):
        # Проверяем статус "Отправлено на доработку" на вкладке "Общие сведения"
        self.browser.find_element(*ContractElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT, 5)
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_MAIN_STATUS_IN_CONTRACT,
                                                     "Отправлено на доработку ККП"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Отправлено на доработку ККП"'

        # Проверяем статус на вкладке "Статус согласования"
        self.is_visibility_of_element_located(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS, 3)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_TABS).click()

        """
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отправлено на доработку"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'
        """

        last_result = self.browser.find_elements(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT)[-1]
        last_result_text = last_result.text
        assert last_result_text == "Отклонено", 'Некорректный статус или отсутствует статус в последней строке. ' \
                                             'Ожидаемый результат: ""Согласование c ККП" - "Отклонено"'

        # Проверяем цвет статуса "Отправлено на доработку"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(last_result.value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отправлено на доработку" в строке согласования со службой ККП'

    # Успешное согласование контракта
    def approval_contract(self, comment, file):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(comment)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(file)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()
        self.browser.refresh()

    # Отклонение контракта с выбором этапа
    def reject_contract(self, comment, file, start_with):
        self.is_element_clickable(*ContractElementLocators.REJECT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REJECT_CONTRACT).click()
        # Выбираем значение в выпадающем списке "При повторном согласовании начать с шага:"
        Select(self.browser.find_element(*ContractElementLocators.START_WITH_ELEMENT)).select_by_value(start_with)
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(comment + ". Начать с: " + start_with)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(file)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REJECT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()
        self.browser.refresh()

    # Отклонение контракта за ККП
    def reject_contract_kkp(self, comment, file):
        self.is_element_clickable(*ContractElementLocators.REJECT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REJECT_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(comment)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(file)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REJECT_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()
        self.browser.refresh()

    # Эскалация контракта на ККП
    def escalate_contract_on_kkp(self):
        self.is_element_clickable(*ContractElementLocators.ESCALATE_CONTRACT)
        self.browser.find_element(*ContractElementLocators.ESCALATE_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_escalation_kkp)
        self.browser.find_element(*ContractElementLocators.CONFIRM_ESCALATE_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    # Отправка на доработку от ККП
    def revision_contract_from_kkp(self, comment, start_with):
        self.is_element_clickable(*ContractElementLocators.REVISION_CONTRACT)
        self.browser.find_element(*ContractElementLocators.REVISION_CONTRACT).click()
        # Выбираем значение в выпадающем списке "При повторном согласовании начать с шага:"
        Select(self.browser.find_element(*ContractElementLocators.START_WITH_ELEMENT)).select_by_value(start_with)
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(comment + ". Начать с: " + start_with)
        self.browser.find_element(*ContractElementLocators.CONFIRM_REVISION_CONTRACT).click()
        self.is_visibility_of_element_located(*ContractElementLocators.ClOSE_ALLERT_CONTRACT, 5)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    # Кнопка изменения элемента
    def go_to_edit_contract(self):
        assert self.is_element_clickable(*ContractElementLocators.EDIT_ITEM_BUTTON), \
            'Кнопка "Изменить элемент" не доступна для нажатия'
        self.browser.find_element(*ContractElementLocators.EDIT_ITEM_BUTTON).click()

    # Добавление файла бюджета проекта
    def add_file_of_budget(self):
        self.browser.find_element(*ContractElementLocators.BUDGET_CONTRACT_BUTTON).click()

        # Проверяем текст заголовка модульного окна
        actual_text = self.is_element_text(*ContractElementLocators.TITLE_BUDGET_ELEMENT)
        expected_text = "Добавить файл бюджета проекта в договор/контракт?"
        delayed_assert.expect(actual_text == expected_text,
                              f'Не корректный текст заголовка в модульном окне добавления файла бюджета\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Проверяем основной текст модульного окна
        actual_text = self.is_element_text(*ContractElementLocators.TEXT_BUDGET_ELEMENT)
        expected_text = "Если файл бюджета проекта был ранее добавлен в договор/контракт, то он будет перезаписан"
        delayed_assert.expect(actual_text == expected_text,
                              f'Не корректный основной текст в модульном окне добавления файла бюджета\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

        # Добавляем файл бюджета
        self.browser.find_element(*ContractElementLocators.FILE_BUDGET_FIELD).send_keys(UserData.file_path_for_link_doc)
        time.sleep(2)
        # Жмем кнопку "Добавить"
        self.browser.find_element(*ContractElementLocators.ADD_BUDGET_FILE_BUTTON).click()

        # Переходим на вкладку "Прикрепленные файлы"
        self.browser.find_element(*ContractElementLocators.ATTACHED_FILES_ELEMENT).click()

        # Проверяем отображение добавленного файла бюджета
        actual_text = self.is_element_text(*ContractElementLocators.BUDGET_OF_PROJECT_FIELD)
        expected_text = UserData.name_doc_to_link
        delayed_assert.expect(actual_text == expected_text,
                              'Не корректное название файла в поле "Бюджет проекта" на вкладке "Прикрепленные файлы"\n'
                              f'Ожидаемый результат: {expected_text}\n'
                              f'Фактический результат: {actual_text}')

