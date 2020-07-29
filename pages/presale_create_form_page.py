from pages.base_page import BasePage
from .locators import PresalePageLocators
from .locators import FormCreatePresaleLocators
from .locators import FormCreateZakupLocators
from userdata.user_data import UserData
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class PresaleFormCreate(BasePage):
    # Форма создания пресейла
    def form_create_presale_all_type(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreatePresaleLocators.SELLER_RESPONSIBLE_FOR_VERIFY_ELEMENT,
                                              UserData.performer_responsible)
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

        # Ищем поле "Ответственный менеджер подразделения-продавца" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.SELLER_RESPONSIBLE_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.SELLER_RESPONSIBLE_DROPDOWN_ELEMENT).click()

        # Ищем поле "Подразделение-исполнитель" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.DIVISIONS_PERFORMER_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.DIVISIONS_PERFORMER_DROPDOWN_ELEMENT).click()

        # Ищем поле "Ответственный менеджер подразделения-исполнителя" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_RESPONSIBLE_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_RESPONSIBLE_DROPDOWN_ELEMENT).click()

        # Ищем поле "Исполнитель (юридическое лицо)" и выбираем значение
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_LEGAL_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.PERFORMER_LEGAL_DROPDOWN_ELEMENT).click()

        if UserData.type_presale == "Тендерная заявка" or UserData.type_presale == "Запрос цен товаров, работ, услуг":
            assert self.is_visibility_of_element_located(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT), \
                "Ошибка: При выбранном Способе определения поставщика не отображено поле Порядок проведения закупочной процедуры"

            # Ищем поле "Порядок проведения закупочной процедуры" и выбираем значение из выпадающего списка
            sale_law_type_element = Select(
                self.browser.find_element(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT))
            sale_law_type_element.select_by_value(UserData.sale_law_type)

        if UserData.type_presale == "Коммерческое предложение" or UserData.type_presale == "Информация отсутствует":
            assert self.is_visibility_of_element_located(*FormCreatePresaleLocators.SALE_LAW_TYPE_ELEMENT) == False, \
                "Ошибка: При выбранном Способе определения поставщика поле Порядок проведения закупочной процедуры не должно отображаться"

        # Ищем кнопку "Тип работ и услуг"
        self.browser.find_element(*FormCreatePresaleLocators.SEARCH_VALID_OPTION_ELEMENT).click()
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
            *FormCreatePresaleLocators.TYPE_WORK_SERVICES_ELEMENT, f'{UserData.category}')

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
        competition_deadline_from_element = self.browser.find_element(
            *FormCreatePresaleLocators.COMPETITION_DEADLINE_FROM_ELEMENT)
        competition_deadline_from_element.send_keys(UserData.competition_deadline_From)

        # Ищем поле "Плановая дата заключения договора/контракта" и вводим значение
        plan_date_contract_conclusion_element = self.browser.find_element(
            *FormCreatePresaleLocators.PLAN_DATE_CONTRACT_CONCLUSION_ELEMENT)
        plan_date_contract_conclusion_element.send_keys(UserData.plan_date_contract_conclusion)

        # Ищем поле "Плановая дата окончания договора/контракта" и вводим значение
        plan_date_contract_finish_element = self.browser.find_element(
            *FormCreatePresaleLocators.PLAN_DATE_CONTRACT_FINISH_ELEMENT)
        plan_date_contract_finish_element.send_keys(UserData.plan_Date_contract_finish)

        # Ищем поле "Вероятность заключения договора/контракта" и вводим значение
        project_probability_element = self.browser.find_element(*FormCreatePresaleLocators.PROJECT_PROBABILITY_ELEMENT)
        project_probability_element.send_keys(UserData.project_probability)

        # Ищем поле "Краткое описание" и вводим значение
        description_plain_text_element = self.browser.find_element(
            *FormCreatePresaleLocators.DESCRIPTION_PLAIN_TEXT_ELEMENT)
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

    def send_presale_to_approval_in_form_create(self):
        confirm = self.browser.switch_to.alert
        confirm.accept()
        self.browser.switch_to.frame(self.browser.find_element(*FormCreatePresaleLocators.iframe))
        self.browser.find_element(*FormCreatePresaleLocators.APPROVAL_DIRECTION_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.DIVISIONS_DROPDOWN_ELEMENT).click()
        self.browser.find_element(*FormCreatePresaleLocators.APPROVAL_CONFIRM_SEND_BUTTON).click()

    def abort_send_presale_to_approval_in_form_create(self):
        confirm = self.browser.switch_to.alert
        confirm.dismiss()



