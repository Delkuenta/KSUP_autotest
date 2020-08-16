from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import PresaleElementLocators
from userdata.user_data import UserData


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

    def go_to_create_zp_based_on_presale(self):
        if UserData.user_data_dict["contractorType"] == "Тендерная заявка" or \
                UserData.user_data_dict["contractorType"] == "Информация отсутствует":
            PresaleElementPage.go_to_create_zp_tender_based_on_presale(self)
        elif UserData.user_data_dict["contractorType"] == "Коммерческое предложение":
            PresaleElementPage.go_to_create_zp_commercial_offer_based_on_presale(self)
        elif UserData.user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            PresaleElementPage.go_to_create_zp_presale_act_based_on_presale(self)

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

    def approval_presale(self):
        self.is_element_clickable(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON)
        self.browser.find_element(*PresaleElementLocators.CONFIRM_APPROVAL_BUTTON).click()
        self.browser.switch_to.frame(self.browser.find_element(*PresaleElementLocators.iframe))
        self.browser.find_element(*PresaleElementLocators.APPROVAL_MANAGER_ELEMENT).click()
        if UserData.user_data_dict["create_account"] == "Mr_KSUP_Seller" or UserData.user_data_dict["create_account"] == "Mr_KSUP_Dir":
            self.browser.find_element(By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['salesManager']}']").click()
        else:
            self.browser.find_element(By.XPATH,
                                      f"//li[normalize-space(.)='{UserData.user_data_dict['executiveManager']}']").click()
        self.browser.find_element(*PresaleElementLocators.APPROVAL_BUTTON_IN_FRAME).click()
        self.browser.find_element(*PresaleElementLocators.MESSAGE_OK_BUTTON).click()
        self.browser.refresh()

    def verify_presale_approval_waiting_status(self):
        assert self.is_text_to_be_present_in_element(*PresaleElementLocators.PRESALE_APPROVAL_STATUS,
                                                     "На согласовании"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования с подразделением"'

    def verify_presale_approval_successfully_status(self):
        assert self.is_text_to_be_present_in_element(*PresaleElementLocators.PRESALE_APPROVAL_STATUS,
                                                     "Согласовано"), \
            'Некорректный статус или отсутствует статус в поле "Статус согласования с подразделением"'