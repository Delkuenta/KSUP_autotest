from pages.base_page import BasePage
from pages.locators import ZakupElementLocators
from userdata.user_data import UserData
from selenium.webdriver.support.color import Color


class ZakupElementPage(BasePage):

    def verify_price_category_zakup(self):
        assert self.is_element_text(*ZakupElementLocators.PRICE_CATEGORY_ELEMENT_IN_ZP) == \
               UserData.user_data_dict["price_category"], "Ценовая категория закупочной процедуры не корректна"

    def verify_draft_status_zakup(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "Черновик"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

    def verify_visibility_approval_button_zp(self):
        assert self.is_visibility_of_element_located(*ZakupElementLocators.SEND_APPROVAL_ELEMENT), \
            'Кнопка "Отправить на согласование" не отобрежена'

    def verify_visibility_button_create_contract(self):
        assert self.is_visibility_of_element_located(
            *ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP), \
            'Кнопка "Внести информацию о договоре/контракте" не отобрежена'

    def verify_unvisibility_approval_button(self):
        assert self.is_element_clickable(*ZakupElementLocators.SEND_APPROVAL_ELEMENT) is False, \
            'Кнопка "Отправить на согласование" доступна для нажатия'

    def send_zakup_for_approval(self):
        self.is_element_clickable(*ZakupElementLocators.SEND_APPROVAL_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.SEND_APPROVAL_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_SEND_APPROVAL_ELEMENT).click()

    def verify_zakup_waiting_status_approval_legal(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "На согласовании с юридической службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        # Проверяем статус "Ожидает согласования"
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования с юридической службой'

    def verify_zakup_successfully_status_approval_legal(self):
        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано юридической службой" в строке согласования с юридической службой'

    def verify_zakup_reject_status_approval_legal(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "Не согласовано с финансовой службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование юридической службой"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_LEGAL_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с юридической службой'

    def verify_zakup_waiting_status_approval_count(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "На согласовании с бухгалтерией"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        # Проверяем статус "Ожидает согласования"
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования с бухгалтерией'

    def verify_zakup_successfully_status_approval_count(self):
        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с бухгалтерией'

    def verify_zakup_reject_status_approval_count(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "Не согласовано с бухгалтерией"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с бухгалтерией"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c бухгалтерией"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_COUNT_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с бухгалтерией'

    def verify_zakup_waiting_status_approval_fin(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "На согласовании с финансовой службой"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()

        # Проверяем статус "Ожидает согласования"
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования с финансовой службой'

    def verify_zakup_successfully_status_approval_fin(self):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (UserData.user_data_dict["contractorType"] == "Тендерная заявка" and UserData.user_data_dict["price_category"] == "C") or \
            (UserData.user_data_dict["contractorType"] == "Тендерная заявка"
                and UserData.user_data_dict["price_category"] == "B"
                and UserData.user_data_dict["groupTypeWork"] == "Other"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                         "Согласовано с финансовой службой"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

        # Проверяем цвет статуса "Согласовано"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования с финансовой службой'

    def verify_zakup_reject_status_approval_fin(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "Не согласовано с финансовой службой"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с финансовой службой"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c финансовой службой"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_FIN_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования с финансовой службой'

    def verify_zakup_waiting_status_approval_udprpo(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "На согласовании УДПР ПО"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Ожидает согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования со службой УДПР ПО'

    def verify_zakup_successfully_status_approval_udprpo(self):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (UserData.user_data_dict["contractorType"] == "Тендерная заявка"
                and UserData.user_data_dict["groupTypeWork"] == "Software"
                and UserData.user_data_dict["price_category"] == "B") \
            or \
                (UserData.user_data_dict["groupTypeWork"] == "Software"
                 and UserData.user_data_dict["price_category"] != "C"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                         "Согласовано УДПР ПО"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования со службой УДПР ПО'

    def verify_zakup_reject_status_approval_udprpo(self):
        # Проверяем статус "Отклонено" на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "Не согласовано с УДПР ПО"), \
            '\nНекорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения" ' \
            '\n Ожидаемый результат: Отображен статус "Не согласовано с УДПР ПО"'

        # Проверяем статус "Отклонено" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c УДПР ПО"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_UDPRPO_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования со службой УДПР ПО'

    def verify_zakup_waiting_status_approval_kkp(self):
        # Проверяем поле статуса на вкладке "Общие сведения"
        self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "На согласовании в ККП"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Ожидает согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Ожидает согласования"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

        # Проверяем цвет статуса "Ожидает согласования"
        waiting_color = "#f5b300"
        color_in_element = (Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))).hex
        assert color_in_element == waiting_color, \
            'Некорректный цвет статуса "Ожидает согласования" в строке согласования со службой ККП'

    def verify_zakup_successfully_status_approval_kkp(self):
        # Проверяем успешный статус согласования во вкладке "Общие сведения"
        if (UserData.user_data_dict["contractorType"] == "Тендерная заявка"
                and UserData.user_data_dict["price_category"] != "A"):
            self.browser.find_element(*ZakupElementLocators.GENERAL_INFORMATION_ELEMENT).click()
            self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
            assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                         "Участие в проекте согласовано в ККП"), \
                'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

        # Проверяем статус "Согласовано" на вкладке "Статус согласования"
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

        # Проверяем цвет статуса "Согласовано" на вкладке "Статус согласования"
        successfully_color = Color.from_string('green')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == successfully_color, \
            'Некорректный цвет статуса "Согласовано" в строке согласования со службой ККП'

    def verify_zakup_reject_status_approval_kkp(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отклонено"), \
            'Некорректный статус или отсутствует статус в строке "Согласование c ККП"'

        # Проверяем цвет статуса "Отклонено"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отклонено" в строке согласования со службой ККП'

    def verify_zakup_not_require_status_approval(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT)
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_MAIN_STATUS_ELEMENT,
                                                     "Внутреннее согласование не требуется"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования" на вкладке "Общие сведения"'

    def verify_zakup_revision_status_approval(self):
        self.is_element_present(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_HISTORY_ELEMENT).click()
        assert self.is_text_to_be_present_in_element(*ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT,
                                                     "Отправлено на доработку"), \
            'Некорректный статус или отсутствует статус в строке "Согласование ККП"'

        # Проверяем цвет статуса "Отправлено на доработку"
        reject_color = Color.from_string('red')
        color_in_element = Color.from_string(self.browser.find_element(
            *ZakupElementLocators.APPROVAL_KKP_STATUS_ELEMENT).value_of_css_property('color'))
        assert color_in_element == reject_color, \
            'Некорректный цвет статуса "Отправлено на доработку" в строке согласования со службой ККП'

    def approval_zakup_legal(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
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
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
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
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
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
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
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
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.APPROVAL_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.APPROVAL_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.APPROVAL_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_approval_kkp)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_legal(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_legal)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_count(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_count)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_jpg)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_fin(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_fin)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_excel)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_udprpo(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_udprpo)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_mp4)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def reject_zakup_kkp(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REJECT_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REJECT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REJECT_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_reject_kkp)
        self.browser.find_element(*ZakupElementLocators.FILE_TO_APPROVAL_ZAKUP).send_keys(
            UserData.file_path_for_link_doc)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def revision_zakup_from_kkp(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.REVISION_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.REVISION_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.REVISION_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_revision_kkp)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def escalate_on_kkp(self):
        count_refresh_page = 0
        while count_refresh_page < 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.ESCALATE_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_clickable(*ZakupElementLocators.ESCALATE_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ESCALATE_ZAKUP).click()
        self.browser.find_element(*ZakupElementLocators.COMMENT_TO_APPROVAL_ZAKUP).send_keys(
            UserData.comment_escalation_kkp)
        self.browser.find_element(*ZakupElementLocators.CONFIRM_APPROVAL_ZAKUP).click()
        self.is_element_present(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.ClOSE_ALLERT_ZAKUP).click()

    def go_to_create_contract_based_on_zp(self):
        count_refresh_page = 0
        while count_refresh_page <= 3:
            if self.is_visibility_of_element_located(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP) is True:
                break
            else:
                self.browser.refresh()
                count_refresh_page += 1
        self.is_element_present(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP)
        self.browser.find_element(*ZakupElementLocators.CREATE_CONTRACT_BASED_ON_ZAKUP).click()
