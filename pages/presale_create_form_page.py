import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import FormCreatePresaleLocators
from userdata.user_data import UserData


class PresaleFormCreate(BasePage):
    # Форма создания пресейла
    def form_create_presale_all_type(self):
        global payments_sum

        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreatePresaleLocators.SALES_MANAGER_ELEMENT,
                                              UserData.user_data_dict["salesManager"])
        # Ищем поле "Предмет контракта" и заполняем
        self.browser.find_element(*FormCreatePresaleLocators.NAME_PRESALE_ELEMENT).send_keys(
            UserData.user_data_dict["fullName"])

        # Ищем поле "Способ определения поставщика" и выбираем значение
        Select(self.browser.find_element(*FormCreatePresaleLocators.CONTRACTOR_TYPE_ELEMENT)).select_by_value(
            UserData.user_data_dict["contractorType"])

        # Ищем поле "Заказчик" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.CUSTOMER_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.CUSTOMER_DROPDOWN_ELEMENT).click()

        # Ищем поле "Подразделение-продавец" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.SALES_UNIT_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.SALES_UNIT_DROPDOWN_ELEMENT).click()

        # Ищем поле "Ответственный менеджер подразделения-продавца" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.SALES_MANAGER_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.SALES_MANAGER_DROPDOWN_ELEMENT).click()

        # Ищем поле "Подразделение-исполнитель" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_UNIT_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_UNIT_DROPDOWN_ELEMENT).click()

        # Ищем поле "Ответственный менеджер подразделения-исполнителя" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_MANAGER_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_MANAGER_DROPDOWN_ELEMENT).click()

        # Ищем поле "Исполнитель (юридическое лицо)" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_UNIT_LEGAL_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.EXECUTIVE_UNIT_LEGAL_DROPDOWN_ELEMENT).click()

        # Проверка отображения поля Порядок проведения закупочной процедуры
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка" or UserData.user_data_dict[
            "contractorType"] == "Запрос цен товаров, работ, услуг":
            assert self.is_visibility_of_element_located(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT), \
                "Ошибка: При выбранном способе определения поставщика не отображено поле Порядок проведения " \
                "закупочной процедуры "

            # Ищем поле "Порядок проведения закупочной процедуры" и выбираем значение из выпадающего списка
            sale_law_type_element = Select(
                self.browser.find_element(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT))
            sale_law_type_element.select_by_value(UserData.user_data_dict["saleLawType"])

        if UserData.user_data_dict["contractorType"] == "Коммерческое предложение" or UserData.user_data_dict[
            "contractorType"] == "Информация отсутствует":
            assert self.is_visibility_of_element_located(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT) == False, \
                "Ошибка: При выбранном Способе определения поставщика поле Порядок проведения закупочной процедуры не должно отображаться"

        # Ищем кнопку "Тип работ и услуг"
        self.browser.find_element(*FormCreatePresaleLocators.SEARCH_VALID_OPTION_ELEMENT).click()
        time.sleep(2)

        # Работаем во фрейме и выбираем категории
        self.is_frame_to_be_available_and_switch_to_it()

        # Открываем все доступные категории
        self.browser.find_element(*FormCreatePresaleLocators.GROUP_CATEGORY_ELEMENT1).click()
        self.browser.find_element(*FormCreatePresaleLocators.GROUP_CATEGORY_ELEMENT2).click()
        self.browser.find_element(*FormCreatePresaleLocators.GROUP_CATEGORY_ELEMENT3).click()
        self.browser.find_element(*FormCreatePresaleLocators.GROUP_CATEGORY_ELEMENT4).click()
        self.browser.find_element(*FormCreatePresaleLocators.GROUP_CATEGORY_ELEMENT5).click()

        # Выбираем нужный элемент
        for item in UserData.user_data_dict["typeOfWorkServices"]:
            if self.is_element_present(By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{item}']"):
                self.browser.find_element(By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{item}']").click()
                self.browser.find_element(*FormCreatePresaleLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                self.browser.find_element(*FormCreatePresaleLocators.SCROLL_DOWN_BUTTON).click()
                assert self.is_element_present(By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{item}']") == True, \
                    f"Не найден тип работ и услуг с именем {item}"
                self.browser.find_element(By.XPATH,
                                          f"//*[normalize-space(text()) and normalize-space(.)='{item}']").click()
                self.browser.find_element(*FormCreatePresaleLocators.CHOICE_IFRAME_BUTTON).click()

        self.browser.find_element(*FormCreatePresaleLocators.CONFIRM_IFRAME_BUTTON).click()
        # Возврат к форм создания.
        self.is_frame_to_parent()
        time.sleep(2)

        # Ищем поле "Сумма" и вводим значение
        self.browser.find_element(*FormCreatePresaleLocators.SUM_ELEMENT).send_keys(UserData.user_data_dict["sum"])

        # Ищем поле "Валюта" и выбираем значение
        Select(self.browser.find_element(*FormCreatePresaleLocators.CURRENCY_ELEMENT)).select_by_value(
            UserData.user_data_dict["currency"])

        # Ищем поле "Размер обеспечения заявки" и вводим значение
        self.browser.find_element(*FormCreatePresaleLocators.APPLICATION_SIZE_ELEMENT).send_keys(
            UserData.user_data_dict["applicationSize"])

        # Ищем поле "Размер обеспечения договора/контракта" и заполняем его
        self.browser.find_element(*FormCreatePresaleLocators.CONTRACT_SIZE_ELEMENT).send_keys(
            UserData.user_data_dict["contractSize"])

        # Ищем поле "Самостоятельная продажа" и выбираем значение
        Select(self.browser.find_element(*FormCreatePresaleLocators.SEPARATE_SALE_ELEMENT)).select_by_value(
            UserData.user_data_dict["separateSale"])

        # Ищем поле "Плановый срок подачи на конкурс" и вводим значение
        competition_deadline_from_element = self.browser.find_element(
            *FormCreatePresaleLocators.COMPETITION_DEADLINE_FROM_ELEMENT)
        competition_deadline_from_element.send_keys(UserData.user_data_dict["competitionDeadlineFrom"])

        # Ищем поле "Плановая дата заключения договора/контракта" и вводим значение
        plan_date_contract_conclusion_element = self.browser.find_element(
            *FormCreatePresaleLocators.PLAN_DATE_CONTRACT_CONCLUSION_ELEMENT)
        plan_date_contract_conclusion_element.send_keys(UserData.user_data_dict["startDate"])

        # Ищем поле "Плановая дата окончания договора/контракта" и вводим значение
        plan_date_contract_finish_element = self.browser.find_element(
            *FormCreatePresaleLocators.PLAN_DATE_CONTRACT_FINISH_ELEMENT)
        plan_date_contract_finish_element.send_keys(UserData.user_data_dict["endDate"])

        # Ищем поле "Вероятность заключения договора/контракта" и вводим значение
        project_probability_element = self.browser.find_element(*FormCreatePresaleLocators.PROJECT_PROBABILITY_ELEMENT)
        project_probability_element.send_keys(UserData.user_data_dict["projectProbability"])

        # Ищем поле "Краткое описание" и вводим значение
        description_plain_text_element = self.browser.find_element(
            *FormCreatePresaleLocators.DESCRIPTION_PLAIN_TEXT_ELEMENT)
        description_plain_text_element.send_keys(UserData.user_data_dict["descriptionText"])

        # Ищем поле "Риски" и вводим значение
        risks_element = self.browser.find_element(*FormCreatePresaleLocators.RISKS_ELEMENT)
        risks_element.send_keys(UserData.user_data_dict["risksText"])

        payments = UserData.user_data_dict["payments"]
        count_payments_line = len(UserData.user_data_dict["payments"])
        print(f'\nКоличество строчек плановых платежей: {count_payments_line}')

        if count_payments_line == 5:
            line1 = dict(payments[0])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE1).send_keys(line1["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE1).send_keys(line1["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE1)).select_by_visible_text(
                f"{line1['quarter']} квартал")

            line2 = dict(payments[1])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE2).send_keys(line2["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE2).send_keys(line2["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE2)).select_by_visible_text(
                f"{line2['quarter']} квартал")

            line3 = dict(payments[2])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE3).send_keys(line3["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE3).send_keys(line3["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE3)).select_by_visible_text(
                f"{line3['quarter']} квартал")

            line4 = dict(payments[3])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE4).send_keys(line4["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE4).send_keys(line4["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE4)).select_by_visible_text(
                f"{line4['quarter']} квартал")

            line5 = dict(payments[4])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE5).send_keys(line5["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE5).send_keys(line5["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE5)).select_by_visible_text(
                f"{line5['quarter']} квартал")
            payments_sum = line1["sum"] + line2["sum"] + line3["sum"] + line4["sum"] + line5["sum"]

        elif count_payments_line == 4:
            line1 = dict(payments[0])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE1).send_keys(line1["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE1).send_keys(line1["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE1)).select_by_visible_text(
                f"{line1['quarter']} квартал")

            line2 = dict(payments[1])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE2).send_keys(line2["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE2).send_keys(line2["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE2)).select_by_visible_text(
                f"{line2['quarter']} квартал")

            line3 = dict(payments[2])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE3).send_keys(line3["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE3).send_keys(line3["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE3)).select_by_visible_text(
                f"{line3['quarter']} квартал")

            line4 = dict(payments[3])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE4).send_keys(line4["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE4).send_keys(line4["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE4)).select_by_visible_text(
                f"{line4['quarter']} квартал")
            payments_sum = line1["sum"] + line2["sum"] + line3["sum"] + line4["sum"]

        elif count_payments_line == 3:
            line1 = dict(payments[0])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE1).send_keys(line1["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE1).send_keys(line1["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE1)).select_by_visible_text(
                f"{line1['quarter']} квартал")

            line2 = dict(payments[1])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE2).send_keys(line2["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE2).send_keys(line2["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE2)).select_by_visible_text(
                f"{line2['quarter']} квартал")

            line3 = dict(payments[2])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE3).send_keys(line3["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE3).send_keys(line3["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE3)).select_by_visible_text(
                f"{line3['quarter']} квартал")
            payments_sum = line1["sum"] + line2["sum"] + line3["sum"]

        elif count_payments_line == 2:
            line1 = dict(payments[0])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE1).send_keys(line1["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE1).send_keys(line1["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE1)).select_by_visible_text(
                f"{line1['quarter']} квартал")

            line2 = dict(payments[1])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE2).send_keys(line2["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE2).send_keys(line2["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE2)).select_by_visible_text(
                f"{line2['quarter']} квартал")
            payments_sum = line1["sum"] + line2["sum"]

        elif count_payments_line == 1:
            line1 = dict(payments[0])
            self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE1).send_keys(line1["sum"])
            self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE1).send_keys(line1["year"])
            Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE1)).select_by_visible_text(
                f"{line1['quarter']} квартал")
            payments_sum = line1["sum"]

        if payments_sum != UserData.user_data_dict["sum"]:
            confirm_presale_button = self.browser.find_element(*FormCreatePresaleLocators.CONFIRM_PRESALE_BUTTON)
            confirm_presale_button.click()
            time.sleep(1)
            alert = self.browser.switch_to.alert
            alert.accept()
            alert.accept()
        else:
            confirm_presale_button = self.browser.find_element(*FormCreatePresaleLocators.CONFIRM_PRESALE_BUTTON)
            confirm_presale_button.click()
