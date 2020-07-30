from .base_page import BasePage
from .locators import PresalePageLocators
from .locators import PresaleElementLocators


class PresaleElementPage(BasePage):
    # Проверка отображения кнопки "Внести информацию о запросе цен"
    def verify_visibility_button_create_zp_tender_based_on_presale(self):
        assert self.is_visibility_of_element_located(
            *PresaleElementLocators.TENDER_APPLICATION_ELEMENT), \
            'Кнопка "Внести информацию о конкурсе" не отобрежена'

    # Проверка отображения кнопки "Внести информацию о запросе цен"
    def verify_visibility_button_create_zp_presale_act_based_on_presale(self):
        assert self.is_visibility_of_element_located(
            *PresaleElementLocators.PRESALE_ACT_ELEMENT), \
            'Кнопка Внести информацию о запросе цен" не отображена'

    # Проверка отображения кнопки "Внести информацию о коммерческом предложении"
    def verify_visibility_button_create_zp_commercial_offer_based_on_presale(self):
        assert self.is_visibility_of_element_located(
            *PresaleElementLocators.COMMERCIAL_OFFER_ELEMENT), \
            'Кнопка "Внести информацию о коммерческом предложении" не отображена'

    # Проверка отображения кнопки создания контракта на основне Пресейла
    def verify_visibility_button_create_contract_based_on_presale(self):
        assert self.is_visibility_of_element_located(
            *PresaleElementLocators.CREATE_CONTRACT_ELEMENT), \
            'Кнопка "Внести информацию о договор/контракте" не доступна для нажатия'


    # Кнопка внутри пресейла для создания ЗП типа тендер (проверяем доступность и нажимаем)
    def go_to_create_zp_tender_based_on_presale(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.TENDER_APPLICATION_ELEMENT), \
            'Кнопка "Внести информацию о конкурсе" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.TENDER_APPLICATION_ELEMENT).click()

    # Кнопка внутри пресейла для создания ЗП типа "Внести информацию о запросе цен" (проверяем доступность и нажимаем)
    def go_to_create_zp_presale_act_based_on_presale(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.PRESALE_ACT_ELEMENT), \
            'Кнопка Внести информацию о запросе цен" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.PRESALE_ACT_ELEMENT).click()

    # Кнопка внутри пресейла для создания ЗП типа "Внести информацию о коммерческом предложении" (проверяем
    # доступность и нажимаем)
    def go_to_create_zp_commercial_offer_based_on_presale(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.COMMERCIAL_OFFER_ELEMENT), \
            'Кнопка "Внести информацию о коммерческом предложении" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.COMMERCIAL_OFFER_ELEMENT).click()

    # Кнопка создания контракта на основне Пресейла
    def go_to_create_contract_based_on_presale(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.CREATE_CONTRACT_ELEMENT), \
            'Кнопка "Внести информацию о договор/контракте" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.CREATE_CONTRACT_ELEMENT).click()

    # Проверка статуса сущности с атрибутом самостоятельная продажа да
    def verify_self_sale_status_approval(self):
        assert self.is_element_text(*PresaleElementLocators.STATUS_APPROVAL_ELEMENT) == "Не требуется согласование", \
            'Некорректный статус сущности с атрибутом "Cамостоятельная продажа"=да'

    # Проверка статуса сущности отправленной на согласование
    def verify_separate_sale_status_was_send_approval(self):
        assert self.is_text_to_be_present_in_element(*PresaleElementLocators.STATUS_APPROVAL_ELEMENT, "На согласовании"), \
            'Некорректный статус сущности с атрибутом "Cамостоятельная продажа"=нет и уже отправленной на согласование'

    # Проверка статуса сущности не отправленной на согласование из формы создания
    def verify_separate_sale_status_dont_send_approval(self):
        assert self.is_element_text(*PresaleElementLocators.STATUS_APPROVAL_ELEMENT) == "Не отправлено", \
            'Некорректный статус сущности с атрибутом "Cамостоятельная продажа"=нет не отправленное на согласование'

    def verify_separate_sale_successfully_status_approval(self):
        assert self.is_element_text(*PresaleElementLocators.STATUS_APPROVAL_ELEMENT) == "Согласовано", \
            'Некорректный статус сущности с атрибутом "Cамостоятельная продажа"=нет после успешного согласования'

    def go_to_approval_presale_in_direction(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.SEND_APPROVAL_IN_DIRECTION_BUTTON), \
            'Кнопка "Отправить на согласование" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.SEND_APPROVAL_IN_DIRECTION_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))
        self.browser.find_element(*PresaleElementLocators.UNIT_SELECTION_FIELD_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.DIVISIONS_DROPDOWN_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.CONFIRM_BUTTON_IN_FRAME).click()
        self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()
        self.is_frame_to_parent()

    def go_to_approval_presale_in_department(self):
        assert self.is_element_clickable(
            *PresaleElementLocators.SEND_APPROVAL_IN_DEPARTMENT_BUTTON), \
            'Кнопка "Отправить на согласование" не доступна для нажатия'
        self.browser.find_element(*PresaleElementLocators.SEND_APPROVAL_IN_DEPARTMENT_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))
        self.browser.find_element(*PresaleElementLocators.UNIT_SELECTION_FIELD_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.DIVISIONS_PERFORMER_DROPDOWN_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.CONFIRM_BUTTON_IN_FRAME).click()
        self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()
        self.is_frame_to_parent()

    def approval_presale_in_direction(self):
        self.is_element_clickable(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON)
        self.browser.find_element(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))
        self.browser.find_element(*PresaleElementLocators.APPROVAL_MANAGER_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.CHANGE_SELLER_RESPONSIBLE_DROPDOWN_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.APPROVAL_BUTTON_IN_FRAME).click()
        self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()

    def approval_presale_in_department(self):
        self.is_element_clickable(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON)
        self.browser.find_element(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))
        self.browser.find_element(*PresaleElementLocators.APPROVAL_MANAGER_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.CHANGE_SELLER_PERFORMER_DROPDOWN_ELEMENT).click()
        self.browser.find_element(*PresaleElementLocators.APPROVAL_BUTTON_IN_FRAME).click()
        self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()



