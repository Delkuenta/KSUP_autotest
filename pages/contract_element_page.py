from pages.base_page import BasePage
from pages.locators import ContractElementLocators
from userdata.user_data import UserData


class ContractElementPage(BasePage):
    def verify_price_category_contract(self):
        assert self.is_element_text(*ContractElementLocators.PRICE_CATEGORY_ELEMENT_IN_CONTRACT) == \
               UserData.user_data_dict["price_category"], "Ценовая категория контракта не корректна"

    def send_contract_for_approval(self):
        self.is_element_clickable(*ContractElementLocators.SEND_APPROVAL_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.SEND_APPROVAL_CONTRACT_ELEMENT).click()
        self.is_element_present(*ContractElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT)
        self.browser.find_element(*ContractElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT).click()

    def verify_contract_waiting_status_approval_legal(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT, "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

    def verify_contract_successfully_status_approval_legal(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

    def verify_contract_waiting_status_approval_count(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

    def verify_contract_successfully_status_approval_count(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

    def verify_contract_waiting_status_approval_fin(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

    def verify_contract_successfully_status_approval_fin(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

    def verify_contract_waiting_status_approval_udprpo(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

    def verify_contract_successfully_status_approval_udprpo(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

    def verify_contract_waiting_status_approval_kkp(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()

        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

    def verify_contract_successfully_status_approval_kkp(self):
        self.is_element_present(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_HISTORY_CONTRACT_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ContractElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

    def approval_contract_legal(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_legal)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_element_present(*ContractElementLocators.ClOSE_ALLERT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_count(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_count)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_element_present(*ContractElementLocators.ClOSE_ALLERT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_fin(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_fin)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_excel)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_element_present(*ContractElementLocators.ClOSE_ALLERT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_udprpo(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_udprpo)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_element_present(*ContractElementLocators.ClOSE_ALLERT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()

    def approval_contract_kkp(self):
        self.is_element_clickable(*ContractElementLocators.APPROVAL_CONTRACT)
        self.browser.find_element(*ContractElementLocators.APPROVAL_CONTRACT).click()
        self.browser.find_element(*ContractElementLocators.COMMENT_TO_APPROVAL_CONTRACT).send_keys(
            UserData.comment_approval_kkp)
        self.browser.find_element(*ContractElementLocators.FILE_TO_APPROVAL_CONTRACT).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ContractElementLocators.CONFIRM_APPROVAL_CONTRACT).click()
        self.is_element_present(*ContractElementLocators.ClOSE_ALLERT_CONTRACT)
        self.browser.find_element(*ContractElementLocators.ClOSE_ALLERT_CONTRACT).click()
