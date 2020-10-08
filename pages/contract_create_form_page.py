import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import FormCreateContractLocators
from userdata.user_data import UserData


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

        assert user_data_dict["fullName"] in self.is_element_text(*FormCreateContractLocators.ZAKUP_SELECT), \
            "Некорректная информация в поле Связанная закупочная процедура"

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

        # Выбираем значение в поле "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()

        # Развернуть узел "Все субъекты если кнопка отображена"
        if len(self.browser.find_elements(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT)) == 1:
            self.browser.find_element(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT).click()
        # Выбираем территории из списка
        for territory in user_data_dict["territory"]:
            how, what = FormCreateContractLocators.TERRITORY_ELEMENT
            what = what.replace("territory_name", territory)
            if self.is_visibility_of_element_located(how, what):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 7
                while self.is_visibility_of_element_located(how, what) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON_TERRITORY).click()
                    scrolls += 1
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_visibility_of_element_located(how, what) is False and scrolls == max_scrolls:
                    print(f"Не найдена территория  с именем {territory}")

        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()

        # возврат к основной форме
        self.is_frame_to_parent()
        territory_value = ''
        for territory in user_data_dict["territory"]:
            territory_value = territory_value + territory + '; '
        territory_value = territory_value.strip()

        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TERRITORY_ELEMENT, territory_value)

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        for technologies in user_data_dict["technologies"]:
            how, what = FormCreateContractLocators.TECHNOLOGIES_ELEMENT
            what = what.replace("technologies_name", technologies)
            if self.is_visibility_of_element_located(how, what):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 3
                while self.is_visibility_of_element_located(how, what) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON_TECHNOLOGIES).click()
                    scrolls += 1

                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_visibility_of_element_located(how, what) is False and scrolls == max_scrolls:
                    print(f"Не найдена технология с именем {technologies}")

        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        self.is_frame_to_parent()
        # Проверяем, строку
        technologies_value = ''
        for technologies in user_data_dict["technologies"]:
            technologies_value = technologies_value + technologies + '; '
        technologies_value = technologies_value.strip()
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TECHNOLOGIES_ELEMENT, technologies_value)

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

        # Жмем кнопку создать
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON).click()
        # Подтверждаем внесение изменений  в связанный проект
        # Не работает до фикса KSUP-1045
        #self.browser.find_element(*FormCreateContractLocators.CONFIRM_CHANGE_PROJECT_BUTTON).click()

    def form_create_contract(self, user_data_dict):
        # Ждем загрузки формы по последнему загруженному элементу
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.SALES_MANAGER_CONTRACT_ELEMENT,
                                              user_data_dict["salesManager"])

        # Заполняем поле "Предмет контракта"
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).send_keys(
            user_data_dict["fullName"])

        # Заполняем поле "Заказчик"
        self.browser.find_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT).click()
        how, what = FormCreateContractLocators.CUSTOMER_DROPDOWN_CONTRACT_ELEMENT
        what = what.replace("customer_name", user_data_dict["customer"])
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

        # Работаем во фрейме и выбираем категории
        self.is_frame_to_be_available_and_switch_to_it()

        # Открываем все доступные категории
        if len(self.browser.find_elements(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT1)) == 1:
            self.browser.find_element(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT1).click()
        if len(self.browser.find_elements(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT2)) == 1:
            self.browser.find_element(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT2).click()
        if len(self.browser.find_elements(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT3)) == 1:
            self.browser.find_element(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT3).click()
        if len(self.browser.find_elements(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT4)) == 1:
            self.browser.find_element(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT4).click()
        if len(self.browser.find_elements(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT5)) == 1:
            self.browser.find_element(*FormCreateContractLocators.GROUP_CATEGORY_ELEMENT5).click()

        # Выбираем нужный элемент
        for item in user_data_dict["typeOfWorkServices"]:
            WORK_SERVICE_ELEMENT = (By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{item}']")
            if self.is_visibility_of_element_located(*WORK_SERVICE_ELEMENT):
                self.browser.find_element(*WORK_SERVICE_ELEMENT).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON).click()
                assert self.is_visibility_of_element_located(*WORK_SERVICE_ELEMENT) is True, \
                    f"Не найден тип работ и услуг с именем {item}"
                self.browser.find_element(*WORK_SERVICE_ELEMENT).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()

        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()

        # Возврат к форм создания.
        self.is_frame_to_parent()
        time.sleep(2)

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

        # Выбираем значение в поле "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        # Развернуть узел "Все субъекты если кнопка отображена"
        if len(self.browser.find_elements(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT)) == 1:
            self.browser.find_element(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT).click()
        for territory in user_data_dict["territory"]:
            how, what = FormCreateContractLocators.TERRITORY_ELEMENT
            what = what.replace("territory_name", territory)
            if self.is_visibility_of_element_located(how, what):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 7
                while self.is_visibility_of_element_located(how, what) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON_TERRITORY).click()
                    scrolls += 1
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_visibility_of_element_located(how, what) is False and scrolls == max_scrolls:
                    print(f"Не найдена территория  с именем {territory}")

        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        # возврат к основной форме
        self.is_frame_to_parent()
        time.sleep(2)

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        for technologies in user_data_dict["technologies"]:
            how, what = FormCreateContractLocators.TECHNOLOGIES_ELEMENT
            what = what.replace("technologies_name", technologies)
            if self.is_visibility_of_element_located(how, what):
                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
            else:
                # количество перелистываний
                scrolls = 0
                # максимум возможных перелистываний
                max_scrolls = 3
                while self.is_visibility_of_element_located(how, what) is False and scrolls <= max_scrolls:
                    self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON_TECHNOLOGIES).click()
                    scrolls += 1

                self.browser.find_element(how, what).click()
                self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
                if self.is_visibility_of_element_located(how, what) is False and scrolls == max_scrolls:
                    print(f"Не найдена технология с именем {technologies}")

        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        self.is_frame_to_parent()
        time.sleep(2)

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

        payments_sum = 0
        count_payments_line = len(user_data_dict["payments"])
        print(f'\nКоличество строчек плановых платежей: {count_payments_line}')

        if count_payments_line == 5:
            # Заполняем 1ую строку из 5
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE1).send_keys(
                user_data_dict["payments"][0]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE1).send_keys(
                user_data_dict["payments"][0]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE1)).select_by_visible_text(
                f'{user_data_dict["payments"][0]["quarter"]} квартал')

            # Заполняем 2ую строку из 5и
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE2).send_keys(
                user_data_dict["payments"][1]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE2).send_keys(
                user_data_dict["payments"][1]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE2)).select_by_visible_text(
                f'{user_data_dict["payments"][1]["quarter"]} квартал')

            # Заполняем 3ью строку из 5и
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE3).send_keys(
                user_data_dict["payments"][2]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE3).send_keys(
                user_data_dict["payments"][2]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE3)).select_by_visible_text(
                f'{user_data_dict["payments"][2]["quarter"]} квартал')

            # Заполняем 4ую строку из 5и
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE4).send_keys(
                user_data_dict["payments"][3]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE4).send_keys(
                user_data_dict["payments"][3]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE4)).select_by_visible_text(
                f'{user_data_dict["payments"][2]["quarter"]} квартал')

            # Заполняем 5ую строку из 5и
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE5).send_keys(
                user_data_dict["payments"][4]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE5).send_keys(
                user_data_dict["payments"][4]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE5)).select_by_visible_text(
                f'{user_data_dict["payments"][4]["quarter"]} квартал')
            payments_sum = user_data_dict["payments"][0]["sum"] + user_data_dict["payments"][1]["sum"] + \
                           user_data_dict["payments"][2]["sum"] + user_data_dict["payments"][3]["sum"] + \
                           user_data_dict["payments"][4]["sum"]

        elif count_payments_line == 4:
            # Заполняем 1ую строку из 4х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE1).send_keys(
                user_data_dict["payments"][0]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE1).send_keys(
                user_data_dict["payments"][0]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE1)).select_by_visible_text(
                f'{user_data_dict["payments"][0]["quarter"]} квартал')

            # Заполняем 2ую строку из 4х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE2).send_keys(
                user_data_dict["payments"][1]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE2).send_keys(
                user_data_dict["payments"][1]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE2)).select_by_visible_text(
                f'{user_data_dict["payments"][1]["quarter"]} квартал')

            # Заполняем 3ью строку из 4х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE3).send_keys(
                user_data_dict["payments"][2]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE3).send_keys(
                user_data_dict["payments"][2]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE3)).select_by_visible_text(
                f'{user_data_dict["payments"][2]["quarter"]} квартал')

            # Заполняем 4ую строку из 4х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE4).send_keys(
                user_data_dict["payments"][3]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE4).send_keys(
                user_data_dict["payments"][3]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE4)).select_by_visible_text(
                f'{user_data_dict["payments"][2]["quarter"]} квартал')
            payments_sum = user_data_dict["payments"][0]["sum"] + user_data_dict["payments"][1]["sum"] + \
                           user_data_dict["payments"][2]["sum"] + user_data_dict["payments"][3]["sum"]

        elif count_payments_line == 3:
            # Заполняем 1ую строку из 3х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE1).send_keys(
                user_data_dict["payments"][0]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE1).send_keys(
                user_data_dict["payments"][0]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE1)).select_by_visible_text(
                f'{user_data_dict["payments"][0]["quarter"]} квартал')

            # Заполняем 2ую строку из 3х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE2).send_keys(
                user_data_dict["payments"][1]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE2).send_keys(
                user_data_dict["payments"][1]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE2)).select_by_visible_text(
                f'{user_data_dict["payments"][1]["quarter"]} квартал')

            # Заполняем 3ью строку из 3х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE3).send_keys(
                user_data_dict["payments"][2]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE3).send_keys(
                user_data_dict["payments"][2]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE3)).select_by_visible_text(
                f'{user_data_dict["payments"][2]["quarter"]} квартал')
            payments_sum = user_data_dict["payments"][0]["sum"] + user_data_dict["payments"][1]["sum"] + \
                           user_data_dict["payments"][2]["sum"]

        elif count_payments_line == 2:
            # Заполняем 1ую строку из 2х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE1).send_keys(
                user_data_dict["payments"][0]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE1).send_keys(
                user_data_dict["payments"][0]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE1)).select_by_visible_text(
                f'{user_data_dict["payments"][0]["quarter"]} квартал')

            # Заполняем 2ую строку из 2х
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE2).send_keys(
                user_data_dict["payments"][1]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE2).send_keys(
                user_data_dict["payments"][1]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE2)).select_by_visible_text(
                f'{user_data_dict["payments"][1]["quarter"]} квартал')
            payments_sum = user_data_dict["payments"][0]["sum"] + user_data_dict["payments"][1]["sum"]

        elif count_payments_line == 1:
            # Заполняем 1ую строку из 1ой
            self.browser.find_element(*FormCreateContractLocators.SUMTABLE1).send_keys(
                user_data_dict["payments"][0]["sum"])
            self.browser.find_element(*FormCreateContractLocators.YEARTABLE1).send_keys(
                user_data_dict["payments"][0]["year"])
            Select(self.browser.find_element(*FormCreateContractLocators.QUARTERTABLE1)).select_by_visible_text(
                f'{user_data_dict["payments"][0]["quarter"]} квартал')
            payments_sum = user_data_dict["payments"][0]["sum"]

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

        # Жмем кнопку создать
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON).click()

        # Подтверждаем внесение изменений  в связанный проект
        #  # Не работает до фикса KSUP-1045
        # self.browser.find_element(*FormCreateContractLocators.CONFIRM_CHANGE_PROJECT_BUTTON).click()

        # Если сумма платежей не совпадает появляется алерт, при подтверждении сущность создается
        if payments_sum != user_data_dict["sum"]:
            alert = self.browser.switch_to.alert
            alert.accept()
