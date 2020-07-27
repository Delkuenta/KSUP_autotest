from pages.base_page import BasePage
from pages.locators import FormCreateContractLocators
from userdata.user_data import UserData
import time


class ContractFormCreate(BasePage):

    # Форма создания Договор контракта  на основе ПА и ЗП-конкурс(с предзаполнением)
    def form_create_contract_based_on_zp_konkurs(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT, UserData.customer)

        # Проверяем заголовок страницы
        assert self.is_element_text(*FormCreateContractLocators.CONTRACT_TITLE) == "Договор (контракт)"

        # Проверяем автоматическое предзаполнение от пресейла
        assert UserData.customer in self.is_element_text(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Заказчик"

        assert UserData.divisions_seller in self.is_element_text(
            *FormCreateContractLocators.DIVISIONS_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"

        assert UserData.performer_responsible in \
               self.is_element_text(*FormCreateContractLocators.SELLER_RESPONSIBLE_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"

        assert UserData.division_performer in self.is_element_text(
            *FormCreateContractLocators.DIVISIONS_PERFORMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-исполнитель"

        assert UserData.performer_responsible in self.is_element_text(
            *FormCreateContractLocators.PERFORMER_RESPONSIBLE_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"

        assert UserData.performer_legal in self.is_element_text(
            *FormCreateContractLocators.PERFORMER_LEGAL_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Исполнитель (юридическое лицо)"

        assert UserData.category in self.is_element_text(*FormCreateContractLocators.TYPE_WORK_SERVICES_ELEMENT), \
            "Некорректная информация в поле Тип работ и услуг"

        assert UserData.name_presale in self.is_element_text(*FormCreateContractLocators.PRESALE_SELECT), \
            "Некорректная информация в поле Пресейловые активности"

        assert UserData.name_zp_based_on_presale in self.is_element_text(*FormCreateContractLocators.ZAKUP_SELECT), \
            "Некорректная информация в поле Связанная закупочная процедура"

        # Изменяем название сущности
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).clear()
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).send_keys(UserData.name_contract_based_on_zakup)
        # Заполняем поле номер договора
        self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).send_keys(
            UserData.number_contract)

        # Заполняем поле Ссылка на договор/контракт на Официальном сайте ЕИС
        self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).send_keys(UserData.eis_contract_link)

        # Выбираем значение в поле "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        self.browser.find_element(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.TERRITORY_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        # возврат к основной форме
        self.is_frame_to_parent()
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TERRITORY_ELEMENT,
                                              f'{UserData.territory};')

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        if self.is_element_present(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT):
            self.browser.find_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT).click()
        else:
            self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON).click()
            assert self.is_element_present(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT) == True, \
                f"Не найдена технология с именем {UserData.technologies}"
            self.browser.find_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        self.is_frame_to_parent()
        # Проверяем, строку
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TECHNOLOGIES_ELEMENT,
                                              f'{UserData.technologies};')
        # заполняем поле Количественные показатели реализации проекта
        self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).send_keys(UserData.quantitative_indicators_project)

        # Уникальный код проекта
        self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).send_keys(UserData.project_unique_code)

        # прикрепляем файл Контракт
        self.browser.find_element(*FormCreateContractLocators.FILE_CONTRACT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_CONTRACT_NAME, UserData.name_file_to_link)

        # прикрепляем файл Бюджет проекта
        self.browser.find_element(*FormCreateContractLocators.FILE_BUDGET_OF_PROJECT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_BUDGET_OF_PROJECT_NAME, UserData.name_file_to_link)

        # прикрепляем файл Пояснительная служебная записка
        self.browser.find_element(*FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM_NAME, UserData.name_file_to_link)

        # прикрепляем файл Реестр рисков, Карта рисков
        self.browser.find_element(*FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY_NAME, UserData.name_file_to_link)

        # прикрепляем файл Иное
        self.browser.find_element(*FormCreateContractLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_OTHER_NAME, UserData.name_file_to_link)

        # Жмем кнопку создать
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON).click()

    # Форма создания Договор контракта  на основе ПА и ЗП-запрос цен товаров и услуг(с предзаполнением)
    def form_create_contract_based_on_zp_zapros_cen(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT, UserData.customer)

        # Проверяем заголовок страницы
        assert self.is_element_text(*FormCreateContractLocators.CONTRACT_TITLE) == "Договор (контракт)"

        # Проверяем автоматическое предзаполнение от пресейла
        assert UserData.customer in self.is_element_text(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Заказчик"

        assert UserData.divisions_seller in self.is_element_text(
            *FormCreateContractLocators.DIVISIONS_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"

        assert UserData.performer_responsible in \
               self.is_element_text(*FormCreateContractLocators.SELLER_RESPONSIBLE_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"

        assert UserData.division_performer in self.is_element_text(
            *FormCreateContractLocators.DIVISIONS_PERFORMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-исполнитель"

        assert UserData.performer_responsible in self.is_element_text(
            *FormCreateContractLocators.PERFORMER_RESPONSIBLE_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"

        assert UserData.performer_legal in self.is_element_text(
            *FormCreateContractLocators.PERFORMER_LEGAL_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Исполнитель (юридическое лицо)"

        assert UserData.category in self.is_element_text(*FormCreateContractLocators.TYPE_WORK_SERVICES_ELEMENT), \
            "Некорректная информация в поле Тип работ и услуг"

        assert UserData.name_presale in self.is_element_text(*FormCreateContractLocators.PRESALE_SELECT), \
            "Некорректная информация в поле Пресейловые активности"

        assert UserData.name_zp_based_on_presale in self.is_element_text(*FormCreateContractLocators.ZAKUP_SELECT), \
            "Некорректная информация в поле Связанная закупочная процедура"

        # Изменяем название сущности
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).clear()
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).send_keys(UserData.name_contract_based_on_zakup)
        # Заполняем поле номер договора
        self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).send_keys(
            UserData.number_contract)

        #Заполняем поле дата заключения договор/контракта
        self.browser.find_element(*FormCreateContractLocators.CONCLUSION_DATE_CONTRACT).send_keys(UserData.plan_date_contract_conclusion)

        # Заполняем поле Номер закупки
        self.browser.find_element(*FormCreateContractLocators.EIS_PURCHASE_NUMBER_CONTRACT).send_keys(
            UserData.purchase_number)

        # Заполняем поле Ссылка на закупку
        self.browser.find_element(*FormCreateContractLocators.EIS_PURCHSE_LINK_CONTRACT).send_keys(
            UserData.purchase_link)

        # Заполняем поле Ссылка на договор/контракт на Официальном сайте ЕИС
        self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).send_keys(UserData.eis_contract_link)

        # Выбираем значение в поле "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        self.browser.find_element(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.TERRITORY_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        # возврат к основной форме
        self.is_frame_to_parent()
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TERRITORY_ELEMENT,
                                              f'{UserData.territory};')

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        if self.is_element_present(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT):
            self.browser.find_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT).click()
        else:
            self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON).click()
            assert self.is_element_present(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT) == True, \
                f"Не найдена технология с именем {UserData.technologies}"
            self.browser.find_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        self.is_frame_to_parent()
        # Проверяем, строку
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TECHNOLOGIES_ELEMENT,
                                              f'{UserData.technologies};')
        # заполняем поле Количественные показатели реализации проекта
        self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).send_keys(UserData.quantitative_indicators_project)

        # Уникальный код проекта
        self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).send_keys(UserData.project_unique_code)

        # прикрепляем файл Контракт
        self.browser.find_element(*FormCreateContractLocators.FILE_CONTRACT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_CONTRACT_NAME, UserData.name_file_to_link)

        # прикрепляем файл Бюджет проекта
        self.browser.find_element(*FormCreateContractLocators.FILE_BUDGET_OF_PROJECT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_BUDGET_OF_PROJECT_NAME, UserData.name_file_to_link)

        # прикрепляем файл Пояснительная служебная записка
        self.browser.find_element(*FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM_NAME, UserData.name_file_to_link)

        # прикрепляем файл Реестр рисков, Карта рисков
        self.browser.find_element(*FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY_NAME, UserData.name_file_to_link)

        # прикрепляем файл Иное
        self.browser.find_element(*FormCreateContractLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_OTHER_NAME, UserData.name_file_to_link)

        # Жмем кнопку создать
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON).click()

    # Форма создания Договор контракта  на основе ПА и ЗП-запрос цен товаров и услуг(с предзаполнением)
    def form_create_contract_based_on_zp_komm_pred(self):
        # Ждем загрузки страницы по последнему загружаемому объекту
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT, UserData.customer)

        # Проверяем заголовок страницы
        assert self.is_element_text(*FormCreateContractLocators.CONTRACT_TITLE) == "Договор (контракт)"

        # Проверяем автоматическое предзаполнение от пресейла
        assert UserData.customer in self.is_element_text(*FormCreateContractLocators.CUSTOMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Заказчик"

        assert UserData.divisions_seller in self.is_element_text(
            *FormCreateContractLocators.DIVISIONS_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-продавец"

        assert UserData.performer_responsible in \
               self.is_element_text(*FormCreateContractLocators.SELLER_RESPONSIBLE_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-продавца"

        assert UserData.division_performer in self.is_element_text(
            *FormCreateContractLocators.DIVISIONS_PERFORMER_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Подразделение-исполнитель"

        assert UserData.performer_responsible in self.is_element_text(
            *FormCreateContractLocators.PERFORMER_RESPONSIBLE_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Ответственный менеджер подразделения-исполнителя"

        assert UserData.performer_legal in self.is_element_text(
            *FormCreateContractLocators.PERFORMER_LEGAL_CONTRACT_ELEMENT), \
            "Некорректная информация в поле Исполнитель (юридическое лицо)"

        assert UserData.category in self.is_element_text(*FormCreateContractLocators.TYPE_WORK_SERVICES_ELEMENT), \
            "Некорректная информация в поле Тип работ и услуг"

        assert UserData.name_presale in self.is_element_text(*FormCreateContractLocators.PRESALE_SELECT), \
            "Некорректная информация в поле Пресейловые активности"

        assert UserData.name_zp_based_on_presale in self.is_element_text(*FormCreateContractLocators.ZAKUP_SELECT), \
            "Некорректная информация в поле Связанная закупочная процедура"

        # Изменяем название сущности
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).clear()
        self.browser.find_element(*FormCreateContractLocators.NAME_CONTRACT_ELEMENT).send_keys(UserData.name_contract_based_on_zakup)

        # Заполняем поле номер договора
        self.browser.find_element(*FormCreateContractLocators.NUMBER_CONTRACT_ELEMENT).send_keys(
            UserData.number_contract)

        # Заполняем поле Номер закупки
        self.browser.find_element(*FormCreateContractLocators.EIS_PURCHASE_NUMBER_CONTRACT).send_keys(
            UserData.purchase_number)

        # Заполняем поле Ссылка на закупку
        self.browser.find_element(*FormCreateContractLocators.EIS_PURCHSE_LINK_CONTRACT).send_keys(
            UserData.purchase_link)

        # Заполняем поле Ссылка на договор/контракт на Официальном сайте ЕИС
        self.browser.find_element(*FormCreateContractLocators.EIS_CONTRACT_LINK).send_keys(UserData.eis_contract_link)

        # Выбираем значение в поле "Территория применения"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TERRITORY_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        self.browser.find_element(*FormCreateContractLocators.GROUP_TERRITORY_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.TERRITORY_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        # возврат к основной форме
        self.is_frame_to_parent()
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TERRITORY_ELEMENT,
                                              f'{UserData.territory};')

        # Выбираем значение в поле "Ключевые технологии"
        self.browser.find_element(*FormCreateContractLocators.SEARCH_TECHNOLOGIES_ELEMENT).click()
        time.sleep(2)
        self.is_frame_to_be_available_and_switch_to_it()
        if self.is_element_present(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT):
            self.browser.find_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT).click()
        else:
            self.browser.find_element(*FormCreateContractLocators.SCROLL_DOWN_BUTTON).click()
            assert self.is_element_present(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT) == True, \
                f"Не найдена технология с именем {UserData.technologies}"
            self.browser.find_element(*FormCreateContractLocators.TECHNOLOGIES_ELEMENT).click()
        self.browser.find_element(*FormCreateContractLocators.CHOICE_IFRAME_BUTTON).click()
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_IFRAME_BUTTON).click()
        self.is_frame_to_parent()
        # Проверяем, строку
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.TYPE_TECHNOLOGIES_ELEMENT,
                                              f'{UserData.technologies};')
        # заполняем поле Количественные показатели реализации проекта
        self.browser.find_element(*FormCreateContractLocators.QUANTITATIVE_INDICATORS_PROJECT_ELEMENT).send_keys(UserData.quantitative_indicators_project)

        # Уникальный код проекта
        self.browser.find_element(*FormCreateContractLocators.PROJECT_UNIQUE_CODE).send_keys(UserData.project_unique_code)

        # прикрепляем файл Контракт
        self.browser.find_element(*FormCreateContractLocators.FILE_CONTRACT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_CONTRACT_NAME, UserData.name_file_to_link)

        # прикрепляем файл Бюджет проекта
        self.browser.find_element(*FormCreateContractLocators.FILE_BUDGET_OF_PROJECT).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_BUDGET_OF_PROJECT_NAME, UserData.name_file_to_link)

        # прикрепляем файл Пояснительная служебная записка
        self.browser.find_element(*FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_EXPLANATORY_MEMORANUM_NAME, UserData.name_file_to_link)

        # прикрепляем файл Реестр рисков, Карта рисков
        self.browser.find_element(*FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_RISK_MAP_AND_REGISTERY_NAME, UserData.name_file_to_link)

        # прикрепляем файл Иное
        self.browser.find_element(*FormCreateContractLocators.FILE_OTHER).send_keys(UserData.file_path_for_link_file)
        self.is_text_to_be_present_in_element(*FormCreateContractLocators.FILE_OTHER_NAME, UserData.name_file_to_link)

        # Жмем кнопку создать
        self.browser.find_element(*FormCreateContractLocators.CONFIRM_CONTRACT_BUTTON).click()