from pages.base_page import BasePage
from .locators import PresalePageLocators
from .locators import FormCreatePresaleLocators
from .locators import FormCreateZakupLocators
from userdata.user_data import UserData
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class ZakupFormCreate(BasePage):

    # Форма создания ЗП  на основе ПА (с предзаполнением)
    def form_create_zp_based_on_presale_tender(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT,
                                              UserData.customer)
        # Проверяем автоматическое предзаполнение от пресейла
        assert UserData.type_presale in self.is_element_text(*FormCreateZakupLocators.TITLE_ZP), \
            "Некорректное название формы создания"
        assert UserData.divisions_seller in self.is_element_text(*FormCreateZakupLocators.DIVISIONS_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"
        assert UserData.seller_responsible in self.is_element_text(*FormCreateZakupLocators.SELLER_RESPONSIBLE_IN_ZP_ELEMENT),\
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"
        assert UserData.division_performer in self.is_element_text(*FormCreateZakupLocators.DIVISIONS_PERFORMER_IN_ZP_ELEMENT),\
            "Некорректная информация в поле Подразделение-исполнитель"
        assert UserData.performer_responsible in self.is_element_text(*FormCreateZakupLocators.PERFORMER_RESPONSIBLE_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"
        assert UserData.customer in self.is_element_text(*FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Заказчик"
        assert UserData.category in self.is_element_text(*FormCreateZakupLocators.TYPE_WORK_SERVICES_ELEMENT), \
            "Некорректная информация в поле Тип работ и услуг"
        assert UserData.performer_legal in self.is_element_text(*FormCreateZakupLocators.PERFORMER_LEGAL_IN_ZP_ELEMENT),\
            "Некорректная информация в поле Исполнитель Юр.Лицо"
        assert UserData.name_presale in self.is_element_text(*FormCreateZakupLocators.SALES_WITH_OP_FOR_VERIFY), \
            "Некорректная информация в поле Связанные продажи"

        # Ищем поле "Предмет контракта" и меняем в нем значение на новое
        name_zp_basedOn_presale_element = self.browser.find_element(*FormCreateZakupLocators.NAME_ZP_ELEMENT)
        name_zp_basedOn_presale_element.clear()
        name_zp_basedOn_presale_element.send_keys(UserData.name_zp_based_on_presale)
        #Заполняем поле "Номер закупки"
        number_zakup_element = self.browser.find_element(*FormCreateZakupLocators.EIS_PURCHASE_NUMBER)
        number_zakup_element.send_keys(UserData.purchase_number)
        eis_purchase_link_element = self.browser.find_element(*FormCreateZakupLocators.EIS_PURCHASE_LINK)
        eis_purchase_link_element.send_keys(UserData.purchase_link)

        # Заполняем поле "Риски проекта с точки зрения Департамента"
        project_risk_depatment_element = self.browser.find_element(*FormCreateZakupLocators.PROJECT_RISK_DEPARTMENT_PERSPEC)
        project_risk_depatment_element.send_keys(UserData.project_risk_department)

        # Прикрепляем файл в поле Тендерная заявка
        self.browser.find_element(*FormCreateZakupLocators.FILE_TENDER_REQUEST).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_TENDER_NAME_LINK, UserData.name_file_to_link)

        # Тендерная документация
        self.browser.find_element(*FormCreateZakupLocators.FILE_TENDER_DOCS_FROM_CUSTOMER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_TENDER_DOCS_NAME_LINK, UserData.name_file_to_link)

        # Бюджет проекта
        self.browser.find_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT_NAME_LINK, UserData.name_file_to_link)

        # Пояснительная служебная записка
        self.browser.find_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM_NAME_LINK, UserData.name_file_to_link)

        # Проект контракта
        self.browser.find_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT_NAME_LINK, UserData.name_file_to_link)

        #Документы с описанием рисков
        self.browser.find_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY_NAME_LINK, UserData.name_file_to_link)

        #Иное
        self.browser.find_element(*FormCreateZakupLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OTHER_NAME_LINK, UserData.name_file_to_link)

        # Жмем кнопку Создать
        self.browser.find_element(*FormCreateZakupLocators.CONFIRM_ZP_BUTTON).click()

    def form_create_zp_based_on_presale_zaproc_cen(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT,
                                              UserData.customer)
        # Проверяем автоматическое предзаполнение от пресейла
        assert UserData.type_presale in self.is_element_text(*FormCreateZakupLocators.TITLE_ZP), \
            "Некорректное название формы создания"
        assert UserData.divisions_seller in self.is_element_text(*FormCreateZakupLocators.DIVISIONS_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"
        assert UserData.seller_responsible in self.is_element_text(*FormCreateZakupLocators.SELLER_RESPONSIBLE_IN_ZP_ELEMENT),\
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"
        assert UserData.division_performer in self.is_element_text(*FormCreateZakupLocators.DIVISIONS_PERFORMER_IN_ZP_ELEMENT),\
            "Некорректная информация в поле Подразделение-исполнитель"
        assert UserData.performer_responsible in self.is_element_text(*FormCreateZakupLocators.PERFORMER_RESPONSIBLE_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"
        assert UserData.customer in self.is_element_text(*FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Заказчик"
        assert UserData.category in self.is_element_text(*FormCreateZakupLocators.TYPE_WORK_SERVICES_ELEMENT), \
            "Некорректная информация в поле Тип работ и услуг"
        assert UserData.performer_legal in self.is_element_text(*FormCreateZakupLocators.PERFORMER_LEGAL_IN_ZP_ELEMENT),\
            "Некорректная информация в поле Исполнитель Юр.Лицо"
        assert UserData.name_presale in self.is_element_text(*FormCreateZakupLocators.SALES_WITH_OP_FOR_VERIFY), \
            "Некорректная информация в поле Связанные продажи"

        #При выборе     # sale_law_type = "44-ФЗ" появляются четыре дополнительных поля
        # "Предполагаемая дата начала проведения закупки с" и "Предполагаемая дата начала проведения закупки по"
        # проверяем отображения этих полей. При другом типе пропускаем эти проверки
        if UserData.sale_law_type == "44-ФЗ":
            assert self.is_visibility_of_element_located(*FormCreateZakupLocators.PURCHASE_START_DATE_FROM), \
                'Ошибка: Не отображено поле "Предполагаемая дата начала проведения закупки с"'
            assert self.is_visibility_of_element_located(*FormCreateZakupLocators.PURCHASE_START_DATE_TO), \
                'Ошибка: Не отображено поле "Предполагаемая дата начала проведения закупки с"'

            assert self.is_visibility_of_element_located(*FormCreateZakupLocators.EIS_PRICE_NUMBER), \
                'Ошибка: Не отображено поле "Номер запроса цен на Официальном сайте ЕИС"'

            assert self.is_visibility_of_element_located(*FormCreateZakupLocators.EIS_PRICE_LINK), \
                'Ошибка: Не отображено поле "Ссылка на запрос на Официальном сайте ЕИС"'

            # Предполагаемая дата начала проведения закупки с
            self.browser.find_element(*FormCreateZakupLocators.PURCHASE_START_DATE_FROM).send_keys(
                UserData.purchase_start_date_from)

            # Предполагаемая дата начала проведения закупки по
            self.browser.find_element(*FormCreateZakupLocators.PURCHASE_START_DATE_TO).send_keys(
                UserData.purchase_start_date_to)

            # Номер запроса цен на Официальном сайте ЕИС
            self.browser.find_element(*FormCreateZakupLocators.EIS_PRICE_NUMBER).send_keys(UserData.eis_price_number)

            # Ссылка на запрос на Официальном сайте ЕИС
            self.browser.find_element(*FormCreateZakupLocators.EIS_PRICE_LINK).send_keys(UserData.eis_price_link)

        # Ищем поле "Предмет контракта" и меняем в нем значение на новое
        name_zp_basedOn_presale_element = self.browser.find_element(*FormCreateZakupLocators.NAME_ZP_ELEMENT)
        name_zp_basedOn_presale_element.clear()
        name_zp_basedOn_presale_element.send_keys(UserData.name_zp_based_on_presale)

        # Срок предоставления ценовой информации
        self.browser.find_element(*FormCreateZakupLocators.PRICE_INFORMATION_DEADLINE_FROM).send_keys(UserData.price_information_deadline)


        # Заполняем поле "Риски проекта с точки зрения Департамента"
        project_risk_depatment_element = self.browser.find_element(*FormCreateZakupLocators.PROJECT_RISK_DEPARTMENT_PERSPEC)
        project_risk_depatment_element.send_keys(UserData.project_risk_department)

        # Прикрепляем файл в поле Запрос НМЦК
        self.browser.find_element(*FormCreateZakupLocators.FILE_NMCK_REQUEST).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_NMCK_REQUEST_NAME_LINK, UserData.name_file_to_link)

        # Прикрепляем файл в поле Ответ на запрос НМЦК
        self.browser.find_element(*FormCreateZakupLocators.FILE_NMCK_RESPONSE).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_NMCK_RESPONSE_NAME_LINK, UserData.name_file_to_link)

        #Документы с описанием рисков
        self.browser.find_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY_NAME_LINK, UserData.name_file_to_link)

        #Иное
        self.browser.find_element(*FormCreateZakupLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OTHER_NAME_LINK, UserData.name_file_to_link)

        # Жмем кнопку Создать
        self.browser.find_element(*FormCreateZakupLocators.CONFIRM_ZP_BUTTON).click()

    def form_create_zp_based_on_presale_komm_pred(self):

        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT,
                                              UserData.customer)
        # Проверяем автоматическое предзаполнение от пресейла
        assert UserData.type_presale in self.is_element_text(*FormCreateZakupLocators.TITLE_ZP), \
            "Некорректное название формы создания"
        assert UserData.divisions_seller in self.is_element_text(*FormCreateZakupLocators.DIVISIONS_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"
        assert UserData.seller_responsible in self.is_element_text(
            *FormCreateZakupLocators.SELLER_RESPONSIBLE_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"
        assert UserData.division_performer in self.is_element_text(
            *FormCreateZakupLocators.DIVISIONS_PERFORMER_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Подразделение-исполнитель"
        assert UserData.performer_responsible in self.is_element_text(
            *FormCreateZakupLocators.PERFORMER_RESPONSIBLE_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"
        assert UserData.customer in self.is_element_text(*FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Заказчик"
        assert UserData.category in self.is_element_text(*FormCreateZakupLocators.TYPE_WORK_SERVICES_ELEMENT), \
            "Некорректная информация в поле Тип работ и услуг"
        assert UserData.performer_legal in self.is_element_text(*FormCreateZakupLocators.PERFORMER_LEGAL_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Исполнитель Юр.Лицо"
        assert UserData.name_presale in self.is_element_text(*FormCreateZakupLocators.SALES_WITH_OP_FOR_VERIFY), \
            "Некорректная информация в поле Связанные продажи"

        # Ищем поле "Предмет контракта" и меняем в нем значение на новое
        name_zp_basedOn_presale_element = self.browser.find_element(*FormCreateZakupLocators.NAME_ZP_ELEMENT)
        name_zp_basedOn_presale_element.clear()
        name_zp_basedOn_presale_element.send_keys(UserData.name_zp_based_on_presale)

        # Заполняем поле "Риски проекта с точки зрения Департамента"
        project_risk_depatment_element = self.browser.find_element(*FormCreateZakupLocators.PROJECT_RISK_DEPARTMENT_PERSPEC)
        project_risk_depatment_element.send_keys(UserData.project_risk_department)

        # Заполняем поле Официальный запрос от Заказчика на КП
        self.browser.find_element(*FormCreateZakupLocators.FILE_KP_REQUEST_FROM_CUSTOMER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_KP_REQUEST_FROM_CUSTOMER_NAME_LINK, UserData.name_file_to_link)

        # Коммерческое предложение по официальному запросу
        self.browser.find_element(*FormCreateZakupLocators.FILE_OFFER_BY_REQUEST).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OFFER_BY_REQUEST_NAME_LINK, UserData.name_file_to_link)

        # Бюджет проекта
        self.browser.find_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT).send_keys(
            UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT_NAME_LINK,
                                              UserData.name_file_to_link)

        # Пояснительная служебная записка
        self.browser.find_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(
            UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM_NAME_LINK,
                                              UserData.name_file_to_link)

        # Проект контракта
        self.browser.find_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT).send_keys(
            UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT_NAME_LINK,
                                              UserData.name_file_to_link)

        # Документы с описанием рисков
        self.browser.find_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY).send_keys(
            UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY_NAME_LINK,
                                              UserData.name_file_to_link)

        # Иное
        self.browser.find_element(*FormCreateZakupLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OTHER_NAME_LINK, UserData.name_file_to_link)

        # Жмем кнопку Создать
        self.browser.find_element(*FormCreateZakupLocators.CONFIRM_ZP_BUTTON).click()
