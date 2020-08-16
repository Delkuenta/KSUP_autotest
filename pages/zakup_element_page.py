from pages.base_page import BasePage
from pages.locators import ZakupElementLocators
from userdata.user_data import UserData


class ZakupElementPage(BasePage):

    def verify_price_category_zakup(self):
        assert self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_ELEMENT_IN_ZP) == \
               UserData.user_data_dict["price_category"], "Ценовая категория закупочной процедуры не корректна"

    def verify_visibility_approval_button_zp(self):
        assert self.is_visibility_of_element_located(*ZakupElementLocators.SEND_APPROVAL_ELEMENT), \
            'Кнопка "Отправить на согласование" не отобрежена'

    def verify_visibility_button_create_contract(self):
        assert self.is_visibility_of_element_located(
            *ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP), \
            'Кнопка "Внести информацию о договоре/контракте" не отобрежена'

    def send_zakup_for_approval(self):
        self.is_element_clickable(*ZakupElementLocators.SEND_APPROVAL_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.SEND_APPROVAL_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT).click()

    def verify_zakup_waiting_status_approval_legal(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

    def verify_zakup_successfully_status_approval_legal(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

    def verify_zakup_waiting_status_approval_count(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

    def verify_zakup_successfully_status_approval_count(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

    def verify_zakup_waiting_status_approval_fin(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

    def verify_zakup_successfully_status_approval_fin(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

    def verify_zakup_waiting_status_approval_udprpo(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

    def verify_zakup_successfully_status_approval_udprpo(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

    def verify_zakup_waiting_status_approval_kkp(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

    def verify_zakup_successfully_status_approval_kkp(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

    def verify_zakup_not_require_status_approval(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "Внутреннее согласование не требуется"), \
            'Некорректный статус или отсутствует статус в строке "Статус согласования"'

    def approval_zakup_legal(self):
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_legal)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_count(self):
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_count)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_fin(self):
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_fin)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_udprpo(self):
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_udprpo)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def approval_zakup_kkp(self):
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_kkp)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def go_to_create_contract_based_on_zp(self):
        self.is_element_present(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP).click()
