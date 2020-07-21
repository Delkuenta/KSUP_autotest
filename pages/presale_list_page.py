from .base_page import BasePage
from .locators import PresalePageLocators
from .locators import FormCreatePresaleLocators
from .locators import FormCreateZpLocators
from .locators import PresaleElementLocators
from userdata.user_data import UserData
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class PresalePage(BasePage):

    def go_to_create_presale(self):
        button_create_presale = self.browser.find_element(*PresalePageLocators.PRESALE_CREATE_BUTTON)
        button_create_presale.click()

    def go_to_presale_element(self):
        self.browser.find_element(*PresalePageLocators.FIND_ELEMENT_IN_LIST).click()

    def go_to_create_zp_tender_based_on_presale(self):
        self.browser.find_element(*PresaleElementLocators.TENDER_APPLICATION_ELEMENT).click()

    def form_create_presale_tender(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreatePresaleLocators.SELLER_RESPONSIBLE_ELEMENT, UserData.performer_responsible)
        # Ищем поле "Предмет контракта" и заполняем
        name_presale_element = self.browser.find_element(*FormCreatePresaleLocators.NAME_PRESALE_ELEMENT)
        name_presale_element.send_keys(*UserData.name_presale)

        # Ищем поле "Способ определения поставщика" и выбираем значение
        type_presale_element = Select(
        self.browser.find_element(*FormCreatePresaleLocators.TYPE_PRESALE_ELEMENT))
        type_presale_element.select_by_value(UserData.type_presale)

        # Ищем поле "Заказчик" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.CUSTOMER_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.CUSTOMER_DROPDOWN_ELEMENT).click()

        # Ищем поле "Подразделение-продавец" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.DIVISIONS_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.DIVISIONS_DROPDOWN_ELEMENT).click()

        # Ищем поле "Подразделение-исполнитель" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.DIVISIONS_PERFORMER_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.DIVISIONS_PERFORMER_DROPDOWN_ELEMENT).click()

        # Ищем поле "Ответственный менеджер подразделения-исполнителя" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_RESPONSIBLE_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_RESPONSIBLE_DROPDOWN_ELEMENT).click()

        # Ищем поле "Исполнитель (юридическое лицо)" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_LEGAL_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_LEGAL_DROPDOWN_ELEMENT).click()

        # Ищем поле "Порядок проведения закупочной процедуры" и выбираем значение из выпадающего списка
        sale_law_type_element = Select(
            self.browser.find_element(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT))
        sale_law_type_element.select_by_value(UserData.sale_law_type)

        # Ищем кнопку "Тип работ и услуг"
        self.browser.find_element(By.CLASS_NAME, "ms-taxonomy-browser-button").click()
        time.sleep(2)

        # Работаем во фрейме и выбираем категории
        self.is_frame_to_be_available_and_switch_to_it()
        self.browser.find_element(*FormCreatePresaleLocators.GROUP_CATEGORY_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.CATEGORY_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.CHOICE_IFRAME_BUTTON).click()
        self.browser.find_element(*FormCreatePresaleLocators.CONFIRM_IFRAME_BUTTON).click()
        # Возврат к форм создания.
        self.is_frame_to_parent()
        self.is_text_to_be_present_in_element(
            *FormCreatePresaleLocators.TYPE_WORK_SERVICES_ELEMENT, UserData.category)

        # Ищем поле "Сумма" и вводим значение
        sum_element = self.browser.find_element(*FormCreatePresaleLocators.SUM_ELEMENT)
        sum_element.send_keys(UserData.sum)

        # Ищем поле "Валюта" и выбираем значение
        currency_element = Select(self.browser.find_element(*FormCreatePresaleLocators.CURRENCY_ELEMENT))
        currency_element.select_by_value(UserData.currency)

        # Ищем поле "Размер обеспечения заявки" и вводим значение
        application_size_element = self.browser.find_element(*FormCreatePresaleLocators.APPLICATION_SIZE_ELEMENT)
        application_size_element.send_keys(UserData.application_size)

        # Ищем поле "Размер обеспечения договора/контракта" и заполняем его
        contract_size_element = self.browser.find_element(*FormCreatePresaleLocators.CONTRACT_SIZE_ELEMENT)
        contract_size_element.send_keys(UserData.contract_size)

        # Ищем поле "Самостоятельная продажа" и выбираем значение
        separate_sale_element = Select(self.browser.find_element(*FormCreatePresaleLocators.SEPARATE_SALE_ELEMENT))
        separate_sale_element.select_by_value(UserData.separate_sale)

        # Ищем поле "Плановый срок подачи на конкурс" и вводим значение
        competition_deadline_from_element = self.browser.find_element(*FormCreatePresaleLocators.COMPETITION_DEADLINE_FROM_ELEMENT)
        competition_deadline_from_element.send_keys(UserData.competition_deadline_From)

        # Ищем поле "Плановая дата заключения договора/контракта" и вводим значение
        plan_date_contract_conclusion_element = self.browser.find_element(*FormCreatePresaleLocators.PLAN_DATE_CONTRACT_CONCLUSION_ELEMENT)
        plan_date_contract_conclusion_element.send_keys(UserData.plan_date_contract_conclusion)

        # Ищем поле "Плановая дата окончания договора/контракта" и вводим значение
        plan_date_contract_finish_element = self.browser.find_element(*FormCreatePresaleLocators.PLAN_DATE_CONTRACT_FINISH_ELEMENT)
        plan_date_contract_finish_element.send_keys(UserData.plan_Date_contract_finish)

        # Ищем поле "Вероятность заключения договора/контракта" и вводим значение
        project_probability_element = self.browser.find_element(*FormCreatePresaleLocators.PROJECT_PROBABILITY_ELEMENT)
        project_probability_element.send_keys(UserData.project_probability)

        # Ищем поле "Краткое описание" и вводим значение
        description_plain_text_element = self.browser.find_element(*FormCreatePresaleLocators.DESCRIPTION_PLAIN_TEXT_ELEMENT)
        description_plain_text_element.send_keys(UserData.description_plain_text)

        # Ищем поле "Риски" и вводим значение
        risks_element = self.browser.find_element(*FormCreatePresaleLocators.RISKS_ELEMENT)
        risks_element.send_keys(UserData.risks)

        # Заполнение таблицы Плановых платежей 1 строка
        sumtable1_element = self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE1_ELEMENT)
        sumtable1_element.send_keys(int(UserData.sum / 2))

        yeartable1_element = self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE1)
        yeartable1_element.send_keys(UserData.yeartable_1line)

        quartertable1_element = Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE1_ELEMENT))
        quartertable1_element.select_by_visible_text(UserData.quarter_1line)

        # Заполнение таблицы плановых платежей 2 строка
        sumtable2_element = self.browser.find_element(*FormCreatePresaleLocators.SUMTABLE2_ELEMENT)
        sumtable2_element.send_keys(int(UserData.sum / 2))

        yeartable2_element = self.browser.find_element(*FormCreatePresaleLocators.YEARTABLE2)
        yeartable2_element.send_keys(UserData.yeartable_2line)

        quartertable2_element = Select(self.browser.find_element(*FormCreatePresaleLocators.QUARTERTABLE2_ELEMENT))
        quartertable2_element.select_by_visible_text(UserData.quarter_2line)

        confirm_presale_button = self.browser.find_element(*FormCreatePresaleLocators.CONFIRM_PRESALE_BUTTON)
        confirm_presale_button.click()
        self.find_element_on_list()

    def form_create_zp_based_on_presale_tender(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateZpLocators.CUSTOMER_IN_ZP_ELEMENT,
                                              UserData.customer)
        # Проверяем предзаполнение
        assert self.is_element_text(*FormCreateZpLocators.TITLE_ZP) == UserData.type_presale, "Некорректное название формы создания"
        assert self.is_element_text(*FormCreateZpLocators.DIVISIONS_IN_ZP_ELEMENT) == UserData.divisions_seller, "Некорректная информация в поле Подразделение-продавец"
        assert self.is_element_text(*FormCreateZpLocators.SELLER_RESPONSIBLE_IN_ZP_ELEMENT) == \
               UserData.performer_responsible, "Некорректная информация в поле Ответственный менеджер подразделения-продавца"
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
        self.browser.find_element(*FormCreateZpLocators.SALES_WITH_OP).click()
        breakpoint()


    def should_be_clickable_create_button(self):
        assert self.is_element_clickable(*PresalePageLocators.PRESALE_CREATE_BUTTON), 'Кнопка "Создать" не доступна для нажатия'

    def should_be_element_on_list(self):
        assert self.is_element_present(*PresalePageLocators.FIND_ELEMENT_IN_LIST), \
            f'Пресейловая активность с именем "{UserData.name_presale}" не найдена в списке'




