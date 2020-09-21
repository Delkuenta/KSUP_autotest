from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import FormCreateZakupLocators
from userdata.user_data import UserData


class ZakupFormCreate(BasePage):

    def form_create_zakup_all_type(self, user_data_dict):
        self.is_text_to_be_present_in_element(*FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT, user_data_dict["customer"])
        # Проверка заголовка формы создания Закупочной процедуры на основе типа в пользовательских данных
        if user_data_dict["contractorType"] == "Тендерная заявка" or \
                user_data_dict["contractorType"] == "Информация отсутствует":
            # Проверяем заголовок страницы
            assert "Тендерная заявка" in self.is_element_text(*FormCreateZakupLocators.TITLE_ZP), \
                "Некорректное название формы создания закупочной процедуры"
        elif user_data_dict["contractorType"] == "Коммерческое предложение":
            assert "Коммерческое предложение" in self.is_element_text(*FormCreateZakupLocators.TITLE_ZP), \
                "Некорректное название формы создания закупочной процедуры"
        elif user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            assert "Запрос цен товаров, работ, услуг" in self.is_element_text(*FormCreateZakupLocators.TITLE_ZP), \
                "Некорректное название формы создания закупочной процедуры"

        # Проверки заполнения общих полей для всех типов
        assert user_data_dict["salesUnit"] in self.is_element_text(
            *FormCreateZakupLocators.SALES_UNIT_IN_ZP_ELEMENT), "Некорректная информация в поле Подразделение-продавец"
        assert user_data_dict["salesManager"] in self.is_element_text(
            *FormCreateZakupLocators.SALES_MANAGER_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"
        assert user_data_dict["executiveUnit"] in self.is_element_text(
            *FormCreateZakupLocators.EXECUTIVE_UNIT_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Подразделение-исполнитель"
        assert user_data_dict["executiveManager"] in self.is_element_text(
            *FormCreateZakupLocators.EXECUTIVE_MANAGER_IN_ZP_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"
        assert user_data_dict["customer"] in self.is_element_text(
            *FormCreateZakupLocators.CUSTOMER_IN_ZP_ELEMENT), "Некорректная информация в поле Заказчик"
        assert user_data_dict["executiveUnitLegal"] in self.is_element_text(
            *FormCreateZakupLocators.EXECUTIVE_LEGAL_IN_ZP_ELEMENT), "Некорректная информация в поле Исполнитель Юр.Лицо"
        assert user_data_dict["fullName"] in self.is_element_text(*FormCreateZakupLocators.SALES_WITH_OP_FOR_VERIFY), \
            "Некорректная информация в поле Связанные продажи"

        if user_data_dict["contractorType"] == "Тендерная заявка":
            # Заполняем поле "Порядок проведения закупочной процедуры"
            Select(self.browser.find_element(*FormCreateZakupLocators.CONTRACTOR_TYPE_TENDER_ZP)).select_by_value(
                user_data_dict["saleLawType"])
            if user_data_dict["saleLawType"] == "44-ФЗ" or user_data_dict["saleLawType"] == "223-ФЗ":
                assert self.is_visibility_of_element_located(*FormCreateZakupLocators.EIS_PURCHASE_NUMBER), \
                    'Ошибка: Не отображено поле "Номер закупки"'
                # Заполняем поле "Номер закупки *"
                self.browser.find_element(*FormCreateZakupLocators.EIS_PURCHASE_NUMBER).send_keys(
                    user_data_dict["purchaseNumber"])
            # Заполняем поле "Ссылка на закупку *"
            self.browser.find_element(*FormCreateZakupLocators.EIS_PURCHASE_LINK).send_keys(
                user_data_dict["purchaseLink"])
            # Заполняем поле "Риски проекта с точки зрения Департамента"
            self.browser.find_element(*FormCreateZakupLocators.PROJECT_RISK_DEPARTMENT_PERSPEC).\
                send_keys(user_data_dict["projectRiskDepartment"])
            # Добавляем файл в поле "Тендерная заявка"
            self.browser.find_element(*FormCreateZakupLocators.FILE_TENDER_REQUEST).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_TENDER_NAME_LINK,
                                                  UserData.name_doc_to_link)
            # Добавляем файл в поле "Тендерная документация"
            self.browser.find_element(*FormCreateZakupLocators.FILE_TENDER_DOCS_FROM_CUSTOMER).send_keys(
                UserData.file_path_for_link_excel)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_TENDER_DOCS_NAME_LINK,
                                                  UserData.name_excel_to_link)
            # Добавляем файл в поле "Бюджет проекта"
            self.browser.find_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT).send_keys(
                UserData.file_path_for_link_jpg)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT_NAME_LINK,
                                                  UserData.name_jpg_to_link)
            # Добавляем файл в поле "Пояснительная служебная записка"
            self.browser.find_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM_NAME_LINK,
                                                  UserData.name_doc_to_link)
            # Добавляем файл в поле "Проект контракта"
            self.browser.find_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT).send_keys(
                UserData.file_path_for_link_excel)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT_NAME_LINK,
                                                  UserData.name_excel_to_link)
            # Добавляем файл в поле "Документы с описанием рисков"
            self.browser.find_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY_NAME_LINK,
                                                  UserData.name_doc_to_link)
            # Добавляем файл в поле "Иное"
            self.browser.find_element(*FormCreateZakupLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_mp4)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OTHER_NAME_LINK,
                                                  UserData.name_mp4_to_link)

        elif user_data_dict["contractorType"] == "Коммерческое предложение":
            # Заполняем поле "Риски проекта с точки зрения Департамента"
            self.browser.find_element(*FormCreateZakupLocators.PROJECT_RISK_DEPARTMENT_PERSPEC).\
                send_keys(user_data_dict["projectRiskDepartment"])
            # Добавляем файл в поле  "Официальный запрос от Заказчика на КП *"
            self.browser.find_element(*FormCreateZakupLocators.FILE_KP_REQUEST_FROM_CUSTOMER).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_KP_REQUEST_FROM_CUSTOMER_NAME_LINK,
                                                  UserData.name_doc_to_link)
            # Добавляем файл в поле "Коммерческое предложение по официальному запросу *"
            self.browser.find_element(*FormCreateZakupLocators.FILE_OFFER_BY_REQUEST).send_keys(
                UserData.file_path_for_link_excel)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OFFER_BY_REQUEST_NAME_LINK,
                                                  UserData.name_excel_to_link)
            # Добавляем файл в поле "Бюджет проекта"
            self.browser.find_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT).send_keys(
                UserData.file_path_for_link_jpg)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_BUDGET_OF_PROJECT_NAME_LINK,
                                                  UserData.name_jpg_to_link)
            # Добавляем файл в поле "Пояснительная служебная записка"
            self.browser.find_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_EXPLANATORY_MEMORANUM_NAME_LINK,
                                                  UserData.name_doc_to_link)
            # Добавляем файл в поле "Проект контракта"
            self.browser.find_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT).send_keys(
                UserData.file_path_for_link_excel)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_PROJECT_OF_CONTRACT_NAME_LINK,
                                                  UserData.name_excel_to_link)
            # Добавляем файл в поле "Документы с описанием рисков"
            self.browser.find_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY_NAME_LINK,
                                                  UserData.name_doc_to_link)
            # Добавляем файл в поле "Иное"
            self.browser.find_element(*FormCreateZakupLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_mp4)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OTHER_NAME_LINK,
                                                  UserData.name_mp4_to_link)

        elif user_data_dict["contractorType"] == "Запрос цен товаров, работ, услуг":
            Select(self.browser.find_element(*FormCreateZakupLocators.CONTRACTOR_TYPE_ZAPROS_CEN_ZP)).select_by_value(
                user_data_dict["saleLawType"])
            # Заполняем поле "Срок предоставления ценовой информации"
            self.browser.find_element(*FormCreateZakupLocators.PRICE_INFORMATION_DEADLINE_FROM).send_keys(
                user_data_dict["priceInformationDeadline"])

            # Проверяем отображение полей "Предполагаемая дата начала проведения закупки с/по",
            # поля "Номер запроса цен на Официальном сайте ЕИС" и
            # "Ссылка на запрос на Официальном сайте ЕИС" если порядок закупки 44-ФЗ

            if user_data_dict["saleLawType"] == "44-ФЗ":
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
                    user_data_dict["purchaseStartDateFrom"])

                # Предполагаемая дата начала проведения закупки по
                self.browser.find_element(*FormCreateZakupLocators.PURCHASE_START_DATE_TO).send_keys(
                    user_data_dict["purchaseStartDateTo"])

                # Номер запроса цен на Официальном сайте ЕИС
                self.browser.find_element(*FormCreateZakupLocators.EIS_PRICE_NUMBER).send_keys(
                    user_data_dict["eisPriceNumber"])

                # Ссылка на запрос на Официальном сайте ЕИС
                self.browser.find_element(*FormCreateZakupLocators.EIS_PRICE_LINK).send_keys(
                    user_data_dict["eisPriceLink"])

            # Заполняем поле "Риски проекта с точки зрения Департамента"
            self.browser.find_element(*FormCreateZakupLocators.PROJECT_RISK_DEPARTMENT_PERSPEC).\
                send_keys(user_data_dict["projectRiskDepartment"])

            # Прикрепляем файл в поле Запрос НМЦК
            self.browser.find_element(*FormCreateZakupLocators.FILE_NMCK_REQUEST).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_NMCK_REQUEST_NAME_LINK,
                                                  UserData.name_doc_to_link)

            # Прикрепляем файл в поле Ответ на запрос НМЦК
            self.browser.find_element(*FormCreateZakupLocators.FILE_NMCK_RESPONSE).send_keys(
                UserData.file_path_for_link_jpg)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_NMCK_RESPONSE_NAME_LINK,
                                                  UserData.name_jpg_to_link)

            # Добавляем файл в поле "Документы с описанием рисков"
            self.browser.find_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY).send_keys(
                UserData.file_path_for_link_doc)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_RISK_MAP_AND_REGISTRY_NAME_LINK,
                                                  UserData.name_doc_to_link)
            # Добавляем файл в поле "Иное"
            self.browser.find_element(*FormCreateZakupLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_mp4)
            self.is_text_to_be_present_in_element(*FormCreateZakupLocators.FILE_OTHER_NAME_LINK,
                                                  UserData.name_mp4_to_link)

        # Нажимаем кнопку "Создать"
        self.browser.find_element(*FormCreateZakupLocators.CONFIRM_ZP_BUTTON).click()
        self.browser.find_element(*FormCreateZakupLocators.CONFIRM_ZP_BUTTON).click()
