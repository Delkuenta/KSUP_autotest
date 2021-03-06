import time

import pytest_check as check
from pages.base_page import BasePage
from pages.locators import PresaleElementLocators
from userdata.user_data import UserData
import delayed_assert


class PresaleElementPage(BasePage):
    # Проверка отображения кнопки "Внести информацию о запросе цен"
    def verify_visibility_button_create_zp_tender_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.TENDER_APPLICATION_BUTTON, 5), \
            'Кнопка "Внести информацию о конкурсе" не отобрежена'

    # Проверка отображения кнопки "Внести информацию о запросе цен"
    def verify_visibility_button_create_zp_presale_act_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.PRESALE_ACT_BUTTON, 5), \
            'Кнопка Внести информацию о запросе цен" не отображена'

    # Проверка отображения кнопки "Внести информацию о коммерческом предложении"
    def verify_visibility_button_create_zp_commercial_offer_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.COMMERCIAL_OFFER_BUTTON, 5), \
            'Кнопка "Внести информацию о коммерческом предложении" не отображена'

    # Проверка отображения кнопки создания контракта на основне Пресейла
    def verify_visibility_button_create_contract_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.CREATE_CONTRACT_BUTTON, 5), \
            'Кнопка "Внести информацию о договор/контракте" не доступна для нажатия'

    def go_to_create_zp_based_on_presale(self, user_data_dict):
        if user_data_dict["contractorType"] == "Тендерная заявка" or \
                user_data_dict["contractorType"] == "Информация отсутствует":
            PresaleElementPage.go_to_create_zp_tender_based_on_presale(self)
        elif user_data_dict["contractorType"] == "Коммерческое предложение":
            PresaleElementPage.go_to_create_zp_commercial_offer_based_on_presale(self)
        elif user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            PresaleElementPage.go_to_create_zp_presale_act_based_on_presale(self)

    # Кнопка "Внести информацию о кокурсе" (проверяем доступность и нажимаем)
    def go_to_create_zp_tender_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.TENDER_APPLICATION_BUTTON, 5), \
            'Кнопка "Внести информацию о конкурсе" не отображена'
        self.browser.find_element(*PresaleElementLocators.TENDER_APPLICATION_BUTTON).click()

    # Кнопка "Внести информацию о запросе цен" (проверяем доступность и нажимаем)
    def go_to_create_zp_presale_act_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.PRESALE_ACT_BUTTON, 5), \
            'Кнопка Внести информацию о запросе цен" не отображена'
        self.browser.find_element(*PresaleElementLocators.PRESALE_ACT_BUTTON).click()

    # Кнопка "Внести информацию о коммерческом предложении" (проверяем доступность и нажимаем)
    def go_to_create_zp_commercial_offer_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.COMMERCIAL_OFFER_BUTTON, 5), \
            'Кнопка "Внести информацию о коммерческом предложении" не отображена'
        self.browser.find_element(*PresaleElementLocators.COMMERCIAL_OFFER_BUTTON).click()

    # Кнопка создания контракта на основне Пресейла
    def go_to_create_contract_based_on_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.CREATE_CONTRACT_BUTTON, 5), \
            'Кнопка "Внести информацию о договор/контракте" не отображена'
        self.browser.find_element(*PresaleElementLocators.CREATE_CONTRACT_BUTTON).click()

    # Кнопка редактирования пресейла
    def go_to_edit_presale(self):
        assert self.is_visibility_of_element_located(*PresaleElementLocators.EDIT_ITEM_BUTTON, 5), \
            'Кнопка "Изменить элемент" не отображена'
        self.browser.find_element(*PresaleElementLocators.EDIT_ITEM_BUTTON).click()

    def send_to_approval_presale(self, user_data_dict):
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Dir":

            # Проверяем, что кнопка "Отправить исполнителю" не отображена
            delayed_assert.expect(self.browser.find_element(
                *PresaleElementLocators.SEND_APPROVE_TO_DEPARTMENT_BUTTON).is_displayed() is False,
                                  f'Под ролью {user_data_dict["createAccount"]} отображена кнопка "Отправить исполнителю"')

            # Отправляем на согласование продавцу
            self.is_element_clickable(*PresaleElementLocators.SEND_APPROVE_TO_DIRECTION_BUTTON)
            self.browser.find_element(*PresaleElementLocators.SEND_APPROVE_TO_DIRECTION_BUTTON).click()
            self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))

            # Проверяем предзаполнение поля "Подразделение" из поля "Подразделение-продавец"
            delayed_assert.expect(
                self.is_element_text(*PresaleElementLocators.APPROVAL_DEPARTMENT_ELEMENT) == user_data_dict[
                    "salesUnit"],
                f'При отправке на согласование под ролью {user_data_dict["createAccount"]} '
                f'поле "Подразделение" должно предзаполняться значением из поля "Подразделение-продавец"')

            self.browser.find_element(*PresaleElementLocators.APPROVAL_DEPARTMENT_ELEMENT).click()
            how, what = PresaleElementLocators.UNIT_DROPDOWN_ELEMENT
            what = what.replace("Unit_name", user_data_dict["salesUnit"])
            self.browser.find_element(how, what).click()
            self.browser.find_element(*PresaleElementLocators.APPROVAL_CONFIRM_SEND_BUTTON).click()
            self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()
            self.is_frame_to_parent()
        else:
            # Проверяем, что кнопка "Отправить продавцу" не отображена
            delayed_assert.expect(self.browser.find_element(
                *PresaleElementLocators.SEND_APPROVE_TO_DIRECTION_BUTTON).is_displayed() is False,
                                  f'Под ролью {user_data_dict["createAccount"]} отображена кнопка "Отправить продавцу"')

            # Отправляем на согласование исполнителю
            self.is_element_clickable(*PresaleElementLocators.SEND_APPROVE_TO_DEPARTMENT_BUTTON)
            self.browser.find_element(*PresaleElementLocators.SEND_APPROVE_TO_DEPARTMENT_BUTTON).click()
            self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))

            # Проверяем предзаполнение поля "Подразделение"
            delayed_assert.expect(
                self.is_element_text(*PresaleElementLocators.APPROVAL_DEPARTMENT_ELEMENT) == user_data_dict[
                    "executiveUnit"],
                f'При отправке на согласование под ролью {user_data_dict["createAccount"]} '
                f'поле "Подразделение" должно предзаполняться значением из поля "Подразделение-исполнитель"')

            self.browser.find_element(*PresaleElementLocators.APPROVAL_DEPARTMENT_ELEMENT).click()
            how, what = PresaleElementLocators.UNIT_DROPDOWN_ELEMENT
            what = what.replace("Unit_name", user_data_dict["executiveUnit"])
            self.browser.find_element(how, what).click()
            self.browser.find_element(*PresaleElementLocators.APPROVAL_CONFIRM_SEND_BUTTON).click()
            self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()
            self.is_frame_to_parent()

    def approval_presale(self, user_data_dict):
        self.is_element_clickable(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON)
        self.browser.find_element(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))
        self.browser.find_element(*PresaleElementLocators.APPROVAL_MANAGER_ELEMENT).click()
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Dir":
            how, what = PresaleElementLocators.CHANGE_SELLER_RESPONSIBLE_DROPDOWN_ELEMENT
            what = what.replace("salesManager_name", user_data_dict["salesManager"])
            self.browser.find_element(how, what).click()
        else:
            how, what = PresaleElementLocators.CHANGE_SELLER_PERFORMER_DROPDOWN_ELEMENT
            what = what.replace("executiveManager_name", user_data_dict["executiveManager"])
            self.browser.find_element(how, what).click()
        self.browser.find_element(*PresaleElementLocators.APPROVAL_BUTTON_IN_FRAME).click()
        self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()
        self.is_frame_to_parent()
        self.browser.refresh()

    def reject_approval_presale(self, user_data_dict):
        self.is_element_clickable(*PresaleElementLocators.CANCEL_APPROVAL_BUTTON)
        self.browser.find_element(*PresaleElementLocators.CANCEL_APPROVAL_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))
        reason_field = self.browser.find_element(*PresaleElementLocators.REASON_TEXT_ELEMENT)
        if user_data_dict["createAccount"] == "Mr_KSUP_Seller" or user_data_dict["createAccount"] == "Mr_KSUP_Dir":
            reason_field.send_keys(UserData.comment_reject_presale_with_sales)
        else:
            reason_field.send_keys(UserData.comment_reject_presale_with_executive)
        self.browser.find_element(*PresaleElementLocators.REJECT_BUTTON_IN_FRAME).click()
        self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()
        self.is_frame_to_parent()

    def verify_presale_approval_waiting_status(self):
        assert self.is_text_to_be_present_in_element(*PresaleElementLocators.PRESALE_APPROVAL_STATUS,
                                                     "На согласовании"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования с подразделением".' \
            '\nОжидаемый результат: "На согласовании"'

    def verify_presale_approval_successfully_status(self):
        assert self.is_text_to_be_present_in_element(*PresaleElementLocators.PRESALE_APPROVAL_STATUS, "Согласовано"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования с подразделением"' \
            '\nОжидаемый результат: "Согласовано"'

    def verify_presale_approval_reject_status(self):
        assert self.is_text_to_be_present_in_element(*PresaleElementLocators.PRESALE_APPROVAL_STATUS,
                                                     "Не согласовано"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования с подразделением".' \
            '\nОжидаемый результат: "Не согласовано"'

    def verify_presale_not_require_status_approval(self):
        assert self.is_text_to_be_present_in_element(*PresaleElementLocators.PRESALE_APPROVAL_STATUS,
                                                     "Не требуется согласование"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования с подразделением".' \
            '\nОжидаемый результат: "Не требуется согласование"'

    def verify_general_information_in_presale(self, user_data_dict):

        # Проверяем титул карточки который соответствует названию сущности
        assert self.is_element_text(*PresaleElementLocators.TITLE_IN_PRESALE) == user_data_dict["fullName"], \
            'Название карточки "Пресейловой активности" не соответствует входным данным'
        print('Название карточки "Пресейловой активности" успешно проверено')

        # Проверяем поле "Тип закупочной процедуры"
        assert self.is_element_text(*PresaleElementLocators.CONTRACTOR_TYPE_IN_PRESALE) == user_data_dict[
            "contractorType"], \
            f'\nНекорректное значение в поле "Тип закупочной процедуры". ' \
            f'\nОжидаемый результат:{user_data_dict["contractorType"]}'
        print('Значение в поле "Тип закупочной процедуры" успешно проверено')

        # Проверяем поле "Заказчик"
        assert self.is_element_text(*PresaleElementLocators.CUSTOMER_IN_PRESALE) == user_data_dict["customer"], \
            f'\nНекорректное значение в поле "Заказчик".' \
            f'\nОжидаемый результат:{user_data_dict["customer"]}'
        print('Значение в поле "Заказчик" успешно проверено')

        # Проверяем поле "Подразделение-продавец"
        assert self.is_element_text(*PresaleElementLocators.SALES_UNIT_IN_PRESALE) == user_data_dict["salesUnit"], \
            f'\nНекорректное значение в поле "Подразделение-продавец". ' \
            f'\nОжидаемый результат:{user_data_dict["salesUnit"]}'
        print('Значение в поле "Подразделение-продавец" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-продавца"
        if (user_data_dict["createAccount"] == "Mr_KSUP_Seller" or
            user_data_dict["createAccount"] == "Mr_KSUP_Dir") \
                and user_data_dict["separateSale"] == "Нет" \
                and self.is_element_text(*PresaleElementLocators.PRESALE_APPROVAL_STATUS) == "На согласовании":
            assert self.is_element_text(*PresaleElementLocators.SALES_MANAGER_IN_PRESALE) == \
                   user_data_dict["executiveManager"], \
                f'\nНекорректное значение в поле "Ответственный менеджер подразделения-продавца".' \
                f'\nОжидаемый результат:{user_data_dict["executiveManager"]}'
            print('Значение в поле "Ответственный менеджер подразделения-продавца" успешно проверено')
        else:
            assert self.is_element_text(*PresaleElementLocators.SALES_MANAGER_IN_PRESALE) == \
                   user_data_dict["salesManager"], \
                f'\nНекорректное значение в поле "Ответственный менеджер подразделения-продавца".' \
                f'\nОжидаемый результат:{user_data_dict["salesManager"]}'
            print('Значение в поле "Ответственный менеджер подразделения-продавца" успешно проверено')

        # Проверяем поле "Подразделение-исполнитель"
        assert self.is_element_text(*PresaleElementLocators.EXECUTIVE_UNIT_IN_PRESALE) == user_data_dict[
            "executiveUnit"], \
            f'\nНекорректное значение в поле "Подразделение-исполнитель". ' \
            f'\nОжидаемый результат:{user_data_dict["executiveUnit"]}'
        print('Значение в поле "Подразделение-исполнитель" успешно проверено')

        # Проверяем поле "Ответственный менеджер подразделения-исполнителя"
        if (user_data_dict["createAccount"] == "Mr_KSUP_Seller2" or
            user_data_dict["createAccount"] == "Mr_KSUP_Dir2") \
                and user_data_dict["separateSale"] == "Нет" \
                and self.is_element_text(*PresaleElementLocators.PRESALE_APPROVAL_STATUS) == "На согласовании":
            assert self.is_element_text(*PresaleElementLocators.EXECUTIVE_MANAGER_IN_PRESALE) == \
                   user_data_dict["salesManager"], \
                f'\nНекорректное значение в поле "Ответственный менеджер подразделения-исполнителя".' \
                f'\nОжидаемый результат:{user_data_dict["salesManager"]}'
            print('Значение в поле "Ответственный менеджер подразделения-исполнителя" успешно проверено')
        else:
            assert self.is_element_text(*PresaleElementLocators.EXECUTIVE_MANAGER_IN_PRESALE) == \
                   user_data_dict["executiveManager"], \
                f'\nНекорректное значение в поле "Ответственный менеджер подразделения-исполнителя".' \
                f'\nОжидаемый результат:{user_data_dict["executiveManager"]}'
            print('Значение в поле "Ответственный менеджер подразделения-исполнителя" успешно проверено')

        # Проверяем поле "Исполнитель (юридическое лицо)"
        if len(user_data_dict["executiveUnitLegal"]) > 0:
            assert self.is_element_text(*PresaleElementLocators.EXECUTIVE_UNIT_LEGAL_IN_PRESALE) == \
                   user_data_dict["executiveUnitLegal"], \
                f'\nНекорректное значение в поле "Исполнитель (юридическое лицо)".' \
                f'\nОжидаемый результат:{user_data_dict["executiveUnitLegal"]}'
            print('Значение в поле "Исполнитель (юридическое лицо)" успешно проверено')
        else:
            assert self.browser.find_element(
                *PresaleElementLocators.EXECUTIVE_UNIT_LEGAL_IN_PRESALE).is_displayed() is False, \
                'Отображено пустое поле "Исполнитель (юридическое лицо)"'
            print('Пустое поле "Исполнитель (юридическое лицо)" успешно не отображено')

        # Проверяем поле "Порядок проведения закупочной процедуры"
        if user_data_dict["contractorType"] == "Тендерная заявка":
            assert self.is_element_text(*PresaleElementLocators.SALE_LAW_TYPE_TENDER_PRESALE) == \
                   user_data_dict["saleLawType"], \
                f'\nНекорректное значение в поле "Порядок проведения закупочной процедуры".' \
                f'\nОжидаемый результат:{user_data_dict["saleLawType"]}'
            print('Значение в поле "Порядок проведения закупочной процедуры" успешно проверено')

        # Проверяем поле "Тип работ и услуг"
        work_services_value = ''
        for category in user_data_dict["typeOfWorkServices"]:
            work_services_value = work_services_value + category + '; '
        work_services_value = work_services_value.rstrip()
        assert self.is_element_text(*PresaleElementLocators.TYPE_OF_WORK_SERVCICES_IN_PRESALE) == work_services_value, \
            f'\nНекорректное значение в поле "Тип работ и услуг".' \
            f'\n Ожидаемый результат: {work_services_value}'
        print('Значение в поле "Тип работ и услуг" успешно проверено')

        # Проверяем поле "Плановая сумма договора/контракт"
        sum_value = BasePage.to_human_string_sum(self, user_data_dict["sum"], user_data_dict["currency"])
        assert self.is_element_text(*PresaleElementLocators.SUM_IN_PRESALE) == sum_value, \
            f'\nНекорректное значение в поле "Начальная (максимальная) цена контракта" ' \
            f'\nОжидаемый результат: {sum_value}"'
        print('Значение в поле "Сумма договора/контракта" успешно проверено')

        # Проверяем поле "Валюта договора/контракта"
        assert self.is_element_text(*PresaleElementLocators.CURRENCY_IN_PRESALE) == user_data_dict["currency"], \
            f'\nНекорректное значение в поле "Валюта договора/контракта".' \
            f'\nОжидаемый результат:{user_data_dict["currency"]}'
        print('Значение в поле "Валюта договора/контракта" успешно проверено')

        # Проверяем поле "Размер обеспечения заявки"
        if user_data_dict["contractorType"] != "Коммерческое предложение" and \
                len(str(user_data_dict["applicationSize"])) > 0:
            application_size = BasePage.to_human_string_sum(self, user_data_dict["applicationSize"],
                                                            user_data_dict["currency"])
            assert self.is_element_text(*PresaleElementLocators.APPLICATION_SIZE_IN_PRESALE) == application_size, \
                f'\nНекорректное значение в поле "Размер обеспечения заявки" ' \
                f'\nОжидаемый результат: {application_size}"'
            print('Значение в поле "Размер обеспечения заявки" успешно проверено')

        # Проверяем поле "Размер обеспечения договора/контракта"
        if user_data_dict["contractorType"] != "Коммерческое предложение" and \
                len(str(user_data_dict["contractSize"])) > 0:
            contract_size = BasePage.to_human_string_sum(self, user_data_dict["contractSize"],
                                                         user_data_dict["currency"])
            assert self.is_element_text(*PresaleElementLocators.CONTRACT_SIZE_IN_PRESALE) == contract_size, \
                f'\nНекорректное значение в поле "Размер обеспечения договора/контракта" ' \
                f'\nОжидаемый результат: {contract_size}"'
            print('Значение в поле "Размер обеспечения договора/контракта" успешно проверено')

        # Проверяем поле "Статус продажи"
        assert self.is_element_text(*PresaleElementLocators.PRESALE_STATUS) == "В работе", \
            f'\nНекорректное значение в поле "Статус продажи".' \
            f'\nОжидаемый результат: "В работе"'
        print('Значение в поле "Статус продажи" успешно проверено')

        # Проверяем поле "Срок подачи на конкурс"
        if len(user_data_dict["competitionDeadlineFrom"]) > 0:
            assert user_data_dict["competitionDeadlineFrom"] in \
                   str(self.is_element_text(*PresaleElementLocators.COMPETITION_DEAD_LINE_FROM_IN_PRESALE)).strip(), \
                f'\nНекорректное значение в поле "Срок подачи на конкурс".' \
                f'\nОжидаемый результат: {user_data_dict["competitionDeadlineFrom"]}'
            print('Значение в поле "Срок подачи на конкурс" успешно проверено')
        else:
            assert self.browser.find_element(
                *PresaleElementLocators.COMPETITION_DEAD_LINE_FROM_IN_PRESALE).is_displayed() is False, \
                'Отображено пустое поле "Срок подачи на конкурс"'
            print('Пустое поле "Срок подачи на конкурс" успешно не отображено')

        # Проверяем поле "Плановая дата заключения договора/контракта"
        assert user_data_dict["startDate"] in \
               str(self.is_element_text(*PresaleElementLocators.START_DATE_IN_PRESALE)).strip(), \
            f'\nНекорректное значение в поле "Плановая дата заключения договора/контракта".' \
            f'\nОжидаемый результат: {user_data_dict["startDate"]}'
        print('Значение в поле "Плановая дата заключения договора/контракта" успешно проверено')

        # Проверяем поле "Плановая дата окончания договора/контракта"
        if len(str(user_data_dict["endDate"])) > 0:
            assert user_data_dict["endDate"] in \
                   str(self.is_element_text(*PresaleElementLocators.END_DATE_IN_PRESALE)).strip(), \
                f'\nНекорректное значение в поле "Плановая дата окончания договора/контракта".' \
                f'\nОжидаемый результат: {user_data_dict["endDate"]}'
            print('Значение в поле "Плановая дата окончания договора/контракта" успешно проверено')
        else:
            assert self.browser.find_element(*PresaleElementLocators.END_DATE_IN_PRESALE).is_displayed() is False, \
                'Отображено пустое поле "Плановая дата окончания договора/контракта"'
            print('Пустое поле "Плановая дата окончания договора/контракта" успешно не отображено')

        # Проверяем поле "Вероятность заключения договора/контракта"
        assert self.is_element_text(*PresaleElementLocators.PROJECT_PROBABILITY_IN_PRESALE) == \
               str(user_data_dict["projectProbability"]) + "%", \
            f'\nНекорректное значение в поле "Вероятность заключения договора/контракта".' \
            f'\nОжидаемый результат:{user_data_dict["projectProbability"]}'
        print('Значение в поле "Вероятность заключения договора/контракта" успешно проверено')

        # Проверяем поле "Статус согласования с подразделением"
        if user_data_dict["separateSale"] == "Да":
            assert "Не требуется согласование" in self.is_element_text(*PresaleElementLocators.PRESALE_APPROVAL_STATUS), \
                f'\nНекорректное значение в поле "Статус согласования с подразделением".' \
                f'\n Ожидаемый результат: "Не требуется согласование"'

        # Провеоряем поле "Краткое описание"
        assert self.is_element_text(*PresaleElementLocators.DESCRIPTION_TEXT_IN_PRESALE) == \
               user_data_dict["descriptionText"], \
            f'\nНекорректное значение в поле "Краткое описание".' \
            f'\nОжидаемый результат:{user_data_dict["descriptionText"]}'
        print('Значение в поле "Краткое описание" успешно проверено')

        # Проверяем поле "Риски"
        if len(str(user_data_dict["risksText"])) > 0:
            assert self.is_element_text(*PresaleElementLocators.RISKS_IN_PRESALE) == \
                   user_data_dict["risksText"], \
                f'\nНекорректное значение в поле "Риски".' \
                f'\nОжидаемый результат:{user_data_dict["risksText"]}'
            print('Значение в поле "Риски" успешно проверено')

    def verify_payments_information_in_presale(self, user_data_dict):
        # Переходим на вкладку "График платежей"
        self.browser.find_element(*PresaleElementLocators.PAYMENTS_TAB).click()

        # Проверяем титул таблицы плановых платежей
        delayed_assert.expect(
            self.is_element_text(*PresaleElementLocators.PLAN_PAYMENTS_TITLE) == "ПЛАНОВЫЕ ПОСТУПЛЕНИЯ",
            'Некорректное название статуса Таблицы плановых платежей'
            f'\nОжидаемый результат: "ПЛАНОВЫЕ ПОСТУПЛЕНИЯ"'
            f'\nФактический результат: {self.is_element_text(*PresaleElementLocators.PLAN_PAYMENTS_TITLE)}')

        # Проверяем таблицу плановых платежей
        payments_sum = 0
        count_payments_line = len(user_data_dict["payments"])
        current_line = 0
        while current_line < count_payments_line:
            # Проверяем значение в поле "Сумма в валюте контракта" в текущей строке
            sum_fact_value = self.browser.find_elements(*PresaleElementLocators.SUM_VALUE_ROWS)[current_line].text
            sum_expect = BasePage.to_human_string_sum(self, user_data_dict["payments"][current_line]["sum"],
                                                      user_data_dict["currency"])
            assert sum_expect == sum_fact_value, \
                f'Некорректное значение суммы в строке "{current_line + 1}"' \
                f'\nОР: {sum_expect}' \
                f'\nФР: {sum_fact_value}'

            # Проверяем значение в поле "Год" в текущей строке
            year_fact_value = self.browser.find_elements(*PresaleElementLocators.YEAR_VALUE_ROWS)[current_line].text
            year_expect = str(user_data_dict["payments"][current_line]["year"])
            assert year_expect == year_fact_value, \
                f'Некорректное значение года в строке "{current_line + 1}"' \
                f'\nОР: {year_expect}' \
                f'\nФР: {year_fact_value}'

            # Проверяем значение в поле "Квартал" в текущей строке
            quarter_fact_value = self.browser.find_elements(*PresaleElementLocators.QUARTER_VALUE_ROWS)[
                current_line].text
            quarter_expect = f'{user_data_dict["payments"][current_line]["quarter"]} квартал'
            assert quarter_expect == quarter_fact_value, \
                f'Некорректное значение квартала в строке "{current_line + 1}"' \
                f'\nОР: {quarter_expect}' \
                f'\nФР: {quarter_fact_value}'

            payments_sum += user_data_dict["payments"][current_line]["sum"]
            current_line += 1

        # Проверяем значение в поле "Плановая сумма"
        plan_sum_fact_value = self.browser.find_element(*PresaleElementLocators.SUM_IN_PAYMENTS).text
        plan_sum_expect = BasePage.to_human_string_sum(self, user_data_dict["sum"], user_data_dict["currency"])
        assert plan_sum_expect == plan_sum_fact_value, \
            f'Некорректное значение суммы в строке "{current_line + 1}"' \
            f'\nОР: {plan_sum_expect}' \
            f'\nФР: {plan_sum_fact_value}'

        # Проверяем значение в поле "Итого"
        summary_fact_value = self.browser.find_element(*PresaleElementLocators.SUMMARY_IN_PAYMENTS).text
        summary_expect = BasePage.to_human_string_sum(self, payments_sum, user_data_dict["currency"])
        assert summary_expect == summary_fact_value, \
            f'Некорректное значение суммы в строке "{current_line + 1}"' \
            f'\nОР: {summary_expect}' \
            f'\nФР: {summary_fact_value}'
