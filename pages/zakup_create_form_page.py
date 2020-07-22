from pages.base_page import BasePage
from .locators import PresalePageLocators
from .locators import FormCreatePresaleLocators
from .locators import FormCreateZpLocators
from userdata.user_data import UserData
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class ZakupFormCreate(BasePage):

    # Форма создания ЗП  на основе ПА (с предзаполнением)
    def form_create_zp_based_on_presale_tender(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.CUSTOMER_IN_ZP_ELEMENT,
                                              UserData.customer)
        # Проверяем автоматическое предзаполнение от пресейла
        assert self.is_element_text(*FormCreateZpLocators.TITLE_ZP) == UserData.type_presale, \
            "Некорректное название формы создания"
        assert self.is_element_text(*FormCreateZpLocators.DIVISIONS_IN_ZP_ELEMENT) == UserData.divisions_seller, \
            "Некорректная информация в поле Подразделение-продавец"
        assert self.is_element_text(*FormCreateZpLocators.SELLER_RESPONSIBLE_IN_ZP_ELEMENT) == \
               UserData.performer_responsible, \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"
        assert self.is_element_text(*FormCreateZpLocators.DIVISIONS_PERFORMER_IN_ZP_ELEMENT) == UserData.division_performer, \
            "Некорректная информация в поле Подразделение-исполнитель"
        assert self.is_element_text(*FormCreateZpLocators.PERFORMER_RESPONSIBLE_IN_ZP_ELEMENT) == UserData.performer_responsible, \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"
        assert self.is_element_text(*FormCreateZpLocators.CUSTOMER_IN_ZP_ELEMENT) == UserData.customer, \
            "Некорректная информация в поле Заказчик"
        assert self.is_element_text(*FormCreateZpLocators.TYPE_WORK_SERVICES_ELEMENT) == UserData.category, \
            "Некорректная информация в поле Тип работ и услуг"
        assert self.is_element_text(*FormCreateZpLocators.PERFORMER_LEGAL_IN_ZP_ELEMENT) == f'×\n{UserData.performer_legal}', \
            "Некорректная информация в поле Исполнитель Юр.Лицо"
        assert self.is_element_text(*FormCreateZpLocators.SALES_WITH_OP_FOR_VERIFY) == f'×{UserData.name_presale}', \
            "Некорректная информация в поле Связанные продажи"

        # Ищем поле "Предмет контракта" и меняем в нем значение на новое
        name_zp_basedOn_presale_element = self.browser.find_element(*FormCreateZpLocators.NAME_ZP_ELEMENT)
        name_zp_basedOn_presale_element.clear()
        name_zp_basedOn_presale_element.send_keys(UserData.name_zp_basedOn_presale)
        #Заполняем поле "Номер закупки"
        number_zakup_element = self.browser.find_element(*FormCreateZpLocators.EIS_PURCHASE_NUMBER)
        number_zakup_element.send_keys(UserData.purchase_number)
        eis_purchase_link_element = self.browser.find_element(*FormCreateZpLocators.EIS_PURCHASE_LINK)
        eis_purchase_link_element.send_keys(UserData.purchase_link)

        # Заполняем поле "Риски проекта с точки зрения Департамента"
        project_risk_depatment_element = self.browser.find_element(*FormCreateZpLocators.PROJECT_RISK_DEPARTMENT_PERSPEC)
        project_risk_depatment_element.send_keys(UserData.project_risk_department)

        # Прикрепляем файл в поле Тендерная заявка
        self.browser.find_element(*FormCreateZpLocators.FILE_TENDER_REQUEST).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.FILE_TENDER_NAME_LINK, UserData.name_file_to_link)

        # Тендерная документация
        self.browser.find_element(*FormCreateZpLocators.FILE_TENDER_DOCS_FROM_CUSTOMER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.FILE_TENDER_DOCS_NAME_LINK, UserData.name_file_to_link)

        # Бюджет проекта
        self.browser.find_element(*FormCreateZpLocators.FILE_BUDGET_OF_PROJECT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.FILE_BUDGET_OF_PROJECT_NAME_LINK, UserData.name_file_to_link)

        # Пояснительная служебная записка
        self.browser.find_element(*FormCreateZpLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.FILE_EXPLANATORY_MEMORANUM_NAME_LINK, UserData.name_file_to_link)

        # Проект контракта
        self.browser.find_element(*FormCreateZpLocators.FILE_PROJECT_OF_CONTRACT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.FILE_PROJECT_OF_CONTRACT_NAME_LINK, UserData.name_file_to_link)

        #Документы с описанием рисков
        self.browser.find_element(*FormCreateZpLocators.FILE_RISK_MAP_AND_REGISTRY).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.FILE_RISK_MAP_AND_REGISTRY_NAME_LINK, UserData.name_file_to_link)

        #Иное
        self.browser.find_element(*FormCreateZpLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.FILE_OTHER_NAME_LINK, UserData.name_file_to_link)

        # Жмем кнопку Создать
        self.browser.find_element(*FormCreateZpLocators.CONFIRM_ZP_BUTTON).click()