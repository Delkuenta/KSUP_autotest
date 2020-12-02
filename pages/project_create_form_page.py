import time

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import FormCreateProjectLocators


class ProjectFormCreate(BasePage):

    # Форма создания пресейла
    def form_create_project(self, user_data_dict):
        # Ищем поле "Название проекта *" и заполняем
        self.browser.find_element(*FormCreateProjectLocators.NAME_PROJECT_ELEMENT).send_keys(user_data_dict["fullName"])

        # Ищем поле "Ссылка на закупку на Официальном сайте ЕИС" и заполняем его
        self.browser.find_element(*FormCreateProjectLocators.EIS_PURCHSE_LINK_CONTRACT).send_keys(user_data_dict["eisPriceLink"])

        # Заполняем поле "Заказчик *"
        for customer in user_data_dict["customer"]:
            self.browser.find_element(*FormCreateProjectLocators.CUSTOMER_ELEMENT).click()
            self.browser.find_element(*FormCreateProjectLocators.CUSTOMER_SEARCH_FIELD).send_keys(customer)
            how, what = FormCreateProjectLocators.CUSTOMER_DROPDOWN_ELEMENT
            what = what.replace("customer_name", customer)
            self.browser.find_element(how, what).click()

        # Жмем кнопку "Поиск допустимого вариант" у поля "Отрасль *"
        self.browser.find_element(*FormCreateProjectLocators.SEARCH_INDUSTRY_ELEMENT).click()
        time.sleep(2)

        # Работаем во фрейме "Отрасль"
        self.select_elements_in_frame(user_data_dict["industry"], 3)

        # Ищем кнопку "Тип работ и услуг *"
        self.browser.find_element(*FormCreateProjectLocators.SEARCH_TYPE_AND_SERVICES_ELEMENT).click()
        time.sleep(2)
        # Работаем во фрейме "Тип работ и услуг"
        self.select_in_frame_type_work_and_services(user_data_dict["typeOfWorkServices"])

        # Ищем и заполняем поле "Исполнитель (юридическое лицо) *"
        self.browser.find_element(*FormCreateProjectLocators.EXECUTIVE_UNIT_LEGAL_PROJECT_ELEMENT).click()
        how, what = FormCreateProjectLocators.EXECUTIVE_UNIT_LEGAL_DROPDOWN_PROJECT_ELEMENT
        what = what.replace("executiveUnitLegal_name", user_data_dict["executiveUnitLegal"])
        self.browser.find_element(how, what).click()

        # Заполняем поле "Исполнитель основной *"
        self.browser.find_element(*FormCreateProjectLocators.EXECUTIVE_UNIT_PROJECT_ELEMENT).click()
        how, what = FormCreateProjectLocators.EXECUTIVE_UNIT_PROJECT_DROPDOWN_ELEMENT
        what = what.replace("executiveUnit_name", user_data_dict["executiveUnit"])
        self.browser.find_element(how, what).click()

        # Заполняем поле "Соисполнители"
        if len(user_data_dict["salesUnit"]) > 0:
            for salesUnit in user_data_dict["salesUnit"]:
                self.browser.find_element(*FormCreateProjectLocators.SALES_UNIT_ELEMENT).click()
                how, what = FormCreateProjectLocators.SALES_UNIT_DROPDOWN_ELEMENT
                what = what.replace("salesUnit_name", salesUnit)
                self.browser.find_element(how, what).click()

        # Ищем поле "Стадия проекта *" и выбираем значение
        Select(self.browser.find_element(*FormCreateProjectLocators.PROJECT_STAGE_ELEMENT)).select_by_value(
            user_data_dict["projectStage"])

        # Ищем поле "Связанные договоры/контракты"
        if len(user_data_dict["contracts"]) > 0:
            for contracts in user_data_dict["contracts"]:
                self.browser.find_element(*FormCreateProjectLocators.CONTRACTS_ELEMENT).click()
                how, what = FormCreateProjectLocators.CONTRACTS_DROPDOWN_ELEMENT
                what = what.replace("contract_name", contracts)
                self.browser.find_element(how, what).click()

        # Ищем поле "Срок начала *" и заполняем
        self.browser.find_element(*FormCreateProjectLocators.START_DATE_ELEMENT).send_keys(user_data_dict["startDate"])

        # Выбираем значение в поле "Вендоры"
        if len(user_data_dict["vendors"]) > 0:
            self.browser.find_element(*FormCreateProjectLocators.SEARCH_VENDORS_BUTTON).click()
            time.sleep(2)
            self.select_elements_in_frame(user_data_dict["vendors"], 3)

        # Выбираем значение в поле "Теги"
        if len(user_data_dict["tags"]) > 0:
            self.browser.find_element(*FormCreateProjectLocators.SEARCH_TAGS_BUTTON).click()
            time.sleep(2)
            self.select_elements_in_frame(user_data_dict["tags"], 1)

        # Ищем поле "Менеджеры проекта *" и заполняем его
        for manager in user_data_dict["salesManager"]:
            self.browser.find_element(*FormCreateProjectLocators.SALES_MANAGER_ELEMENT).click()
            how, what = FormCreateProjectLocators.SALES_MANAGER_DROPDOWN_ELEMENT
            what = what.replace("manager_name", manager)
            self.browser.find_element(how, what).click()

        # Ищем поле "Контактное лицо от ЛАНИТ *"
        # self.browser.find_element(*FormCreateProjectLocators.RP_LANIT_ELEMENT).click()
        self.browser.find_element(*FormCreateProjectLocators.RP_LANIT_ELEMENT).send_keys(user_data_dict["rpLanit"])
        how, what = FormCreateProjectLocators.RP_LANIT_DROPDOWN_ELEMENT
        what = what.replace("name", user_data_dict["rpLanit"])
        self.browser.find_element(how, what).click()

        # Ищем поле "Срок начала *" и заполняем
        self.browser.find_element(*FormCreateProjectLocators.END_DATE_ELEMENT).send_keys(user_data_dict["endDate"])

        # Ищем поле "Сумма по всем договорам/контрактам" и выбираем значение
        Select(self.browser.find_element(*FormCreateProjectLocators.SUM_ELEMENT)).select_by_value(
            user_data_dict["sum"])

        # Выбираем значение в поле "Территория применения"
        self.browser.find_element(*FormCreateProjectLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        self.select_elements_in_frame_territory(user_data_dict["territory"])

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateProjectLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        self.select_elements_in_frame(user_data_dict["technologies"], 1)

        # Ищем поле "Категория" и выбираем значение
        Select(self.browser.find_element(*FormCreateProjectLocators.PROJECT_CATEGORY_ELEMENT)).select_by_value(
            user_data_dict["projectCategory"])
        # Необходимо дописать блок проверки отображения текстового поля при выборе значений "Инновационный",
        # "Импортозамещение", "Социально-значимый" и заполнение этого поля

        # Ищем поле "Цели и задачи *" и заполняем его
        self.browser.find_element(*FormCreateProjectLocators.DESCRIPTION_TEXT_ELEMENT).send_keys(user_data_dict["descriptionText"])

        # Ищем поле "Ожидаемые результаты проекта" и заполняем его
        if len(user_data_dict["quantitativeIndicatorsProject"]) > 0:
            self.browser.find_element(*FormCreateProjectLocators.PROJECT_RESULT_ELEMENT).send_keys(
                user_data_dict["quantitativeIndicatorsProject"])

        # Ищем поле "Информация о заинтересованности" и заполняем его
        if len(user_data_dict["interestInformation"]) > 0:
            self.browser.find_element(*FormCreateProjectLocators.INTEREST_INFORMATION_ELEMENT).send_keys(
                user_data_dict["interestInformation"])

        # Ищем поле "Описание" и заполняем его
        if len(user_data_dict["description"]) > 0:
            self.browser.find_element(*FormCreateProjectLocators.DESCRIPTION_ELEMENT).send_keys(
                user_data_dict["description"])
        # Жмем кнопку "Создать"
        self.browser.find_element(*FormCreateProjectLocators.CONFIRM_PROJECT_BUTTON).click()

        # Ждем пока исчезнет надпись "Мы работаем над этим"
        time.sleep(2)
        self.is_disappeared(*FormCreateProjectLocators.CREATE_WAITING_TITLE)





