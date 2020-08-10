from userdata.user_data import UserData
from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_NAME = (By.CSS_SELECTOR, ".o365cs-me-tile-nophoto-username.o365cs-me-bidi")
    PRESALE_LIST_LINK = "https://ksup-tst.lanit/SalesManagement/Lists/Sale/All.aspx"
    PRESALE_LIST_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    ZAKUP_LIST_LINK = "https://ksup-tst.lanit/SalesManagement/Lists/PresaleActivity/All.aspx"
    ZAKUP_LIST_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    CONTRACT_LIST_LINK = "https://ksup-tst.lanit/SalesManagement/Lists/Contract/All.aspx"
    CONTRACT_LIST_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")


class PresaleListLocators:
    PRESALE_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    FIND_ELEMENT_IN_PRESALE_LIST = (
        By.XPATH, f"//a[@class= 'ms-listlink' and contains(text(),'{UserData.user_data_dict['fullName']}')]")


class FormCreatePresaleLocators:
    # Предмет контракта
    NAME_PRESALE_ELEMENT = (By.ID, "KsupFullName_1cb78896-92f2-4cb9-a3ad-b45e0f9932a6_$TextField")

    # Способ определения поставщика
    CONTRACTOR_TYPE_ELEMENT = (By.ID, "KsupContractorType_c208b1d8-b8f1-417e-83de-32d7be2864be_$DropDownChoice")

    # Заказчик *
    CUSTOMER_ELEMENT = (By.XPATH, "//div[@id='div-wcfLookupControl_KsupEgr_Customer']/span/span/span")
    CUSTOMER_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), '{UserData.user_data_dict['customer']}')]")

    # Подразделение-продавец *
    SALES_UNIT_ELEMENT = (By.ID, "div-wcfLookupControl_KsupDivisions")
    SALES_UNIT_DROPDOWN_ELEMENT = (By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['salesUnit']}']")

    # Ответственный менеджер подразделения-продавца *
    SALES_MANAGER_ELEMENT = (By.ID, "div-wcfLookupControl_KsupSeller")
    SALES_MANAGER_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['salesManager']}']")

    # Подразделение-исполнитель
    EXECUTIVE_UNIT_ELEMENT = (By.ID, "div-wcfLookupControl_KsupDivisionPerformer")
    EXECUTIVE_UNIT_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['executiveUnit']}']")

    # Ответственный менеджер подразделения-исполнителя
    EXECUTIVE_MANAGER_ELEMENT = (By.ID, "div-wcfLookupControl_KsupPerformerResponsible")
    EXECUTIVE_MANAGER_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['executiveManager']}']")

    # Исполнитель (юридическое лицо)
    EXECUTIVE_UNIT_LEGAL_ELEMENT = (By.ID, "div-wcfLookupControl_KsupEgr_PerformerLegal")
    EXECUTIVE_UNIT_LEGAL_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[contains(text(), '{UserData.user_data_dict['executiveUnitLegal']}')]")

    # Порядок проведения закупочной процедуры
    SALE_LAW_TYPE_ELEMENT = (By.ID, "KsupSaleLawType_59c9adb5-ad0e-4308-b136-1f1006e5f9f6_$DropDownChoice")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    SEARCH_VALID_OPTION_ELEMENT = (
        By.CSS_SELECTOR, r"#KsupWorkServicesTypeMetadata_\$containercontrolHolder .ms-taxonomy-browser-button")

    # Элементы во фрейме "Тип работ и услуг"

    # Группы категорий
    GROUP_CATEGORY_ELEMENT1 = (By.ID, "TIE_3")
    GROUP_CATEGORY_ELEMENT2 = (By.ID, "TIE_4")
    GROUP_CATEGORY_ELEMENT3 = (By.ID, "TIE_5")
    GROUP_CATEGORY_ELEMENT4 = (By.ID, "TIE_6")
    GROUP_CATEGORY_ELEMENT5 = (By.ID, "TIE_7")

    # Категория
    CATEGORY_ELEMENT = (By.XPATH,
                        f"//*[normalize-space(.)='{UserData.user_data_dict['typeOfWorkServices']}']")
    # Кнопка "Выбор"
    CHOICE_IFRAME_BUTTON = (By.ID,
                            "ctl00_PlaceHolderDialogBodySection_PlaceHolderDialogBodyFooterMainSection_AddToFieldEditor")
    # Кнопка подтверждения (ОК)
    CONFIRM_IFRAME_BUTTON = (By.ID, "ctl00_OkButton")
    # Строка "Тип работ и услуг"
    TYPE_WORK_SERVICES_ELEMENT = (By.ID, "KsupWorkServicesTypeMetadata_$containereditableRegion")

    # Сумма
    SUM_ELEMENT = (By.ID, "KsupSumPlan_9901571e-b38b-42cf-bb3c-f8f7977f1555_$NumberField")

    # Валюта
    CURRENCY_ELEMENT = (By.ID, "KsupCurrency_9cb5cce6-1d98-4146-a2df-c05c4635dd8d_$DropDownChoice")

    # Размер обеспечения заявки
    APPLICATION_SIZE_ELEMENT = (By.ID, "KsupApplicationSize_1117d974-3a17-4f6f-9104-8cf28be18914_$NumberField")

    # Размер обеспечения договора/контракта
    CONTRACT_SIZE_ELEMENT = (By.ID, "KsupContractSize_20253d6d-468d-443e-9179-3f20e0c2533e_$NumberField")

    # Самостоятельная продажа
    SEPARATE_SALE_ELEMENT = (By.ID, "KsupSeparateSale_bf818721-7daf-4db6-b7b9-54ba73429ea5_$DropDownChoice")

    # Плановый срок подачи на конкурс
    COMPETITION_DEADLINE_FROM_ELEMENT = (
    By.ID, "KsupCompetitionDeadlineFrom_5b28696f-6ae9-4765-bb8d-b26513cd0e78_$DateTimeFieldDate")

    # Плановая дата заключения договора/контракта *
    PLAN_DATE_CONTRACT_CONCLUSION_ELEMENT = (
    By.ID, "KsupPlanDateContractConclusion_536f5d8c-9e22-4878-9d4c-49c433c82c0d_$DateTimeFieldDate")

    # Плановая дата окончания договора/контракта
    PLAN_DATE_CONTRACT_FINISH_ELEMENT = (
    By.ID, "KsupPlanDateContractFinish_aaf043ca-d88d-4e99-bcfe-7c15cbb8ba33_$DateTimeFieldDate")

    # Вероятность заключения договора/контракта
    PROJECT_PROBABILITY_ELEMENT = (
        By.ID, "KsupProjectProbability_5bded577-c24a-41f7-ae50-0b1b234d8c21_$NumberField")

    # Краткое описание
    DESCRIPTION_PLAIN_TEXT_ELEMENT = (
        By.ID, "KsupDescriptionPlainText_18b11f3d-f4ae-4a8f-ba29-62366bd13e66_$TextField")

    # Риски
    RISKS_ELEMENT = (By.ID, "KsupRisks_32ca3c22-b19a-430b-8a16-dbe340b6867a_$TextField")

    # 1 строка Плановых платежей
    SUMTABLE1 = (By.XPATH, "//tr[3]/td[2]/input")
    YEARTABLE1 = (By.XPATH, "//td[4]/input")
    QUARTERTABLE1 = (By.XPATH, "//td[5]/select")

    # 2 строка Плановых платежей
    SUMTABLE2 = (By.XPATH, "//tr[4]/td[2]/input")
    YEARTABLE2 = (By.XPATH, "//tr[4]/td[4]/input")
    QUARTERTABLE2 = (By.XPATH, "//tr[4]/td[5]/select")

    # 3 строка Плановых платежей
    SUMTABLE3 = (By.XPATH, "//tr[5]/td[2]/input")
    YEARTABLE3 = (By.XPATH, "//tr[5]/td[4]/input")
    QUARTERTABLE3 = (By.XPATH, "//tr[5]/td[5]/select")

    # 4 строка Плановых платежей
    SUMTABLE4 = (By.XPATH, "//tr[6]/td[2]/input")
    YEARTABLE4 = (By.XPATH, "//tr[6]/td[4]/input")
    QUARTERTABLE4 = (By.XPATH, "//tr[6]/td[5]/select")

    # 5 строка Плановых платежей
    SUMTABLE5 = (By.XPATH, "//tr[7]/td[2]/input")
    YEARTABLE5 = (By.XPATH, "//tr[7]/td[4]/input")
    QUARTERTABLE5 = (By.XPATH, "//tr[7]/td[5]/select")

    # Кнопка создания сущности пресейл
    CONFIRM_PRESALE_BUTTON = (By.CSS_SELECTOR, '[value="Создать"].ms-ButtonHeightWidth')


class PresaleElementLocators:
    # Кнопка изменения элемента
    EDIT_ITEM_ELEMENT = (By.ID, "Ribbon.ListForm.Display.Manage.EditItem-Large")

    # Кнопка "Внести информацию о конкурсе"
    TENDER_APPLICATION_ELEMENT = (By.CSS_SELECTOR, "#createPresaleActivityBasedOnSale_TenderApplication-Large")

    # Кнопка "Внести информацию о запросе цен"
    PRESALE_ACT_ELEMENT = (By.CSS_SELECTOR, "#createPresaleActivityBasedOnSale_PresaleAct-Large")

    # Кнопка "Внести информацию о коммерческом предложении"
    COMMERCIAL_OFFER_ELEMENT = (By.CSS_SELECTOR, "#createPresaleActivityBasedOnSale_CommercialOffer-Large")

    # Кнопка "Внести информацию о договоре/контракте"
    CREATE_CONTRACT_ELEMENT = (By.ID, "Ribbon.ListForm.Display.ContractGroup-LargeLarge")


class FormCreateZakupLocators:
    # Общие поля для всех типов
    TITLE_ZP = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea .die")

    # Тип закупочной процедуры
    PRESALE_TYPE_ELEMENT = (By.CSS_SELECTOR, "#presaleTypes")

    # Предмет контракта
    NAME_ZP_ELEMENT = (By.ID, "KsupFullName_1cb78896-92f2-4cb9-a3ad-b45e0f9932a6_$TextField")

    # Подразделение-продавец
    SALES_UNIT_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupDivisionSeller-container")
    SALES_UNIT_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['salesUnit']}']")

    # Ответственный менеджер подразделения-продавца
    SALES_MANAGER_IN_ZP_ELEMENT = (By.CSS_SELECTOR, '#select2-wcfLookupControl_KsupSeller-container')

    # Подразделение-исполнитель
    EXECUTIVE_UNIT_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupDivisionPerformer-container")
    EXECUTIVE_UNIT_IN_ZP_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['executiveUnit']}']")

    # Ответственный менеджер подразделения-исполнителя
    EXECUTIVE_MANAGER_IN_ZP_ELEMENT = (
        By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupPerformerResponsible-container")
    EXECUTIVE_MANAGER_IN_ZP_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.user_data_dict['executiveManager']}']")

    # Заказчик
    CUSTOMER_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupEgr_Customer-container")
    CUSTOMER_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), '{UserData.user_data_dict['customer']}')]")

    # Исполнитель (юридическое лицо)
    EXECUTIVE_LEGAL_IN_ZP_ELEMENT = (By.ID, "div-wcfLookupControl_KsupEgr_PerformerLegal")
    EXECUTIVE_LEGAL_DROPDOWN_IN_ZP_ELEMENT = (
    By.XPATH, f"//li[contains(text(), '{UserData.user_data_dict['executiveUnitLegal']}')]")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    SEARCH_VALID_OPTION_ELEMENT = (
        By.CSS_SELECTOR, r"#KsupWorkServicesTypeMetadata_\$containercontrolHolder .ms-taxonomy-browser-button")

    # Элементы во фрейме "Тип работ и услуг"

    # Группы категорий
    GROUP_CATEGORY_ELEMENT1 = (By.ID, "TIE_3")
    GROUP_CATEGORY_ELEMENT2 = (By.ID, "TIE_4")
    GROUP_CATEGORY_ELEMENT3 = (By.ID, "TIE_5")
    GROUP_CATEGORY_ELEMENT4 = (By.ID, "TIE_6")
    GROUP_CATEGORY_ELEMENT5 = (By.ID, "TIE_7")

    # Категория
    CATEGORY_ELEMENT = (By.XPATH,
                        f"//*[normalize-space(.)='{UserData.user_data_dict['typeOfWorkServices']}']")
    # Кнопка "Выбор"
    CHOICE_IFRAME_BUTTON = (By.ID,
                            "ctl00_PlaceHolderDialogBodySection_PlaceHolderDialogBodyFooterMainSection_AddToFieldEditor")
    # Кнопка подтверждения (ОК)
    CONFIRM_IFRAME_BUTTON = (By.ID, "ctl00_OkButton")
    # Строка "Тип работ и услуг"
    TYPE_WORK_SERVICES_ELEMENT = (By.ID, "KsupWorkServicesTypeMetadata_$containereditableRegion")

    # Сумма
    SUM_IN_ZP_ELEMENT = (By.ID, "KsupContractSum_8729d9c3-d84d-4132-97dc-27457724cf36_$NumberField")

    # Валюта
    CURRENCY_IN_ZP_ELEMENT = (By.ID, "KsupCurrency_9cb5cce6-1d98-4146-a2df-c05c4635dd8d_$DropDownChoice")

    # Плановая дата окончания договора/контракта
    PLAN_DATE_CONTRACT_FINISH_IN_ZP_ELEMENT = (By.XPATH,
                                               "//input[@id='KsupContractPlanFinishDateFrom_ba6c4eb8-f5a5-4a43-8c07-d230571e83dc_$DateTimeFieldDate']")

    # Вероятность заключения договора/контракта
    PROJECT_PROBABILITY_ELEMENT = (By.ID, "KsupContractProbability_f7fc8405-e077-4ebf-bf9c-50153beb4378_$NumberField")

    # Связанные продажи
    SALES_WITH_OP = (By.XPATH, "//div[@id='div-wcfLookupControl_KsupSalesWithOp']/span/span/span/ul/li[2]/input")
    SALES_WITH_OP_FOR_VERIFY = (By.CSS_SELECTOR, ".select2-selection__choice:nth-child(1)")

    # Результаты работ
    DESCRIPTION_PLAIN_IN_ZP_ELEMENT = (By.ID, "KsupPaDescription_81c0defa-82c4-4dec-a6f1-556818457fd6_$TextField")

    # Риски проекта с точки зрения Департамента
    PROJECT_RISK_DEPARTMENT_PERSPEC = (
        By.ID, "KsupProjectRiskDepartmentPerspec_2c6333aa-aa0b-4e97-aab8-b89e7aa7f0c6_$TextField")

    # Документы с описанием рисков
    FILE_RISK_MAP_AND_REGISTRY = (By.XPATH, "//div[@id='File_RiskMapAndRegistry']/div/input")
    FILE_RISK_MAP_AND_REGISTRY_NAME_LINK = (By.CLASS_NAME, "fileField_File_RiskMapAndRegistry_NameLink_")

    # Иное
    FILE_OTHER = (By.XPATH, "//div[@id='File_Other']/div/input")
    FILE_OTHER_NAME_LINK = (By.CLASS_NAME, "fileField_File_Other_NameLink_")

    # Общие поля для типа "Тендерная заявка" и "Коммчерческое предложение"
    # Плановая дата заключения договора/контракта *
    PLAN_DATE_CONTRACT_CONCLUSION_IN_ZP_ELEMENT = (By.XPATH,
                                                   "//input[@id='KsupContractPlanDateFrom_4b3ff310-7fe8-4e4f-b23c-6d570282fedd_$DateTimeFieldDate']")
    # Бюджет проекта
    FILE_BUDGET_OF_PROJECT = (By.XPATH, "//div[@id='File_BudgetOfProject']/div/input")
    FILE_BUDGET_OF_PROJECT_NAME_LINK = (By.CLASS_NAME, "fileField_File_BudgetOfProject_NameLink_")

    # Пояснительная служебная записка
    FILE_EXPLANATORY_MEMORANUM = (By.XPATH, "//div[@id='File_ExplanatoryMemoranum']/div/input")
    FILE_EXPLANATORY_MEMORANUM_NAME_LINK = (By.CLASS_NAME, "fileField_File_ExplanatoryMemoranum_NameLink_")

    # Проект контракта
    FILE_PROJECT_OF_CONTRACT = (By.XPATH, "//div[@id='File_ProjectOfContract']/div/input")
    FILE_PROJECT_OF_CONTRACT_NAME_LINK = (By.CLASS_NAME, "fileField_File_ProjectOfContract_NameLink_")

    # Общие поля для типа "Тендерная заявка" и "Запрос, цен, товаров и услуг"
    # Порядок проведения закупочной процедуры (Тендерная заявка)
    CONTRACTOR_TYPE_TENDER_ZP = (By.ID, "KsupTenderLowType_ea75ed3b-3361-4f0e-ad36-dcd5aba52908_$DropDownChoice")

    # Порядок проведения закупочной процедуры (Тендерная заявка)
    CONTRACTOR_TYPE_ZAPROS_CEN_ZP = (By.ID, "KsupRequestLowType_c021af9e-7150-4f51-b854-a2f0140ef257_$DropDownChoice")

    # Размер обеспечения заявки
    APPLICATION_SIZE_IN_ZP_ELEMENT = (By.ID, "KsupApplicationSize_1117d974-3a17-4f6f-9104-8cf28be18914_$NumberField")

    # Размер обеспечения договора/контракта
    CONTRACT_SIZE_IN_ZP_ELEMENT = (By.ID, "KsupContractSize_20253d6d-468d-443e-9179-3f20e0c2533e_$NumberField")

    # Уникальные поля для типа "Тендерная заявка"
    # чек-бокс Совместные торги
    JOINT_BIDDING_ELEMENT = (
        By.CSS_SELECTOR, "#KsupPresaleJointBidding_d87bbac9-74b3-46c4-9372-38feb12d67f9_$BooleanField")

    # Срок подачи на конкурс
    COMPETITION_DEADLINE_IN_ZP_FROM_ELEMENT = (By.XPATH,
                                                   "//input[@id='KsupCompetitionDeadlineFrom_5b28696f-6ae9-4765-bb8d-b26513cd0e78_$DateTimeFieldDate']")
    # Номер закупки
    EIS_PURCHASE_NUMBER = (By.ID, "KsupEisPurchaseNumber_8afdb894-e496-4d71-9e54-a1bf0e0a5fb6_$TextField")

    # Ссылка на закупку
    EIS_PURCHASE_LINK = (By.ID, "KsupEisPurchaseLink_39dc12ef-bb5e-46a5-a469-5d687be8ab91_$TextField")

    # Тендерная заявка
    FILE_TENDER_REQUEST = (By.XPATH, "//div[@id='File_TenderRequest']/div/input")
    FILE_TENDER_NAME_LINK = (By.CLASS_NAME, "fileField_File_TenderRequest_NameLink_")

    # Тендерная документация
    FILE_TENDER_DOCS_FROM_CUSTOMER = (By.XPATH, "//div[@id='File_TenderDocsFromCustomer']/div/input")
    FILE_TENDER_DOCS_NAME_LINK = (By.CLASS_NAME, "fileField_File_TenderDocsFromCustomer_NameLink_")

    # Уникальные поля для типа "Коммерческое предложение"

    # Официальный запрос от Заказчика на КП
    FILE_KP_REQUEST_FROM_CUSTOMER = (By.XPATH, "//div[@id='File_KPRequestFromCustomer']/div/input")
    FILE_KP_REQUEST_FROM_CUSTOMER_NAME_LINK = (By.CLASS_NAME, "fileField_File_KPRequestFromCustomer_NameLink_")

    # Коммерческое предложение по официальному запросу
    FILE_OFFER_BY_REQUEST = (By.XPATH, "//div[@id='File_OfferByRequest']/div/input")
    FILE_OFFER_BY_REQUEST_NAME_LINK =  (By.CLASS_NAME, "fileField_File_OfferByRequest_NameLink_")

    # Уникальные поля для типа "Запрос цена, товаров и услуг"

    # Срок предоставления ценовой информации
    PRICE_INFORMATION_DEADLINE_FROM = (By.XPATH, "//input[@id='KsupPriceInformationDeadlineFrom_8ec338f0-a8c3-4c1a-8b36-892c98be55a7_$DateTimeFieldDate']")

    # Предполагаемая дата начала проведения закупки с
    PURCHASE_START_DATE_FROM = (By.XPATH, "//input[@id='KsupPurchaseStartDateFrom_f6f725b7-1c54-4d4c-a087-39f89853714f_$DateTimeFieldDate']")

    # Предполагаемая дата начала проведения закупки по
    PURCHASE_START_DATE_TO = (By.XPATH, "//input[@id='KsupPurchaseStartDateTo_c8e972e8-b7ad-4de5-afca-78c2103ca3bb_$DateTimeFieldDate']")

    # Номер запроса цен на Официальном сайте ЕИС
    EIS_PRICE_NUMBER = (By.ID, "KsupEisPriceNumber_0c8b9e99-9c3a-421a-8f14-c03b006f4231_$TextField")

    # Ссылка на запрос на Официальном сайте ЕИС
    EIS_PRICE_LINK = (By.ID, "KsupEisPriceLink_deebb51e-29c0-4543-9290-d801cfafcb4c_$TextField")

    # Запрос НМЦК
    FILE_NMCK_REQUEST = (By.XPATH, "//div[@id='File_NMCKRequest']/div/input")
    FILE_NMCK_REQUEST_NAME_LINK = (By.CLASS_NAME, "fileField_File_NMCKRequest_NameLink_")

    # Ответ на запрос НМЦК
    FILE_NMCK_RESPONSE = (By.XPATH, "//div[@id='File_NMCKResponse']/div/input")
    FILE_NMCK_RESPONSE_NAME_LINK = (By.CLASS_NAME, "fileField_File_NMCKResponse_NameLink_")

    # Кнопка создания сущности закупочная процедура
    CONFIRM_ZP_BUTTON = (By.CSS_SELECTOR, '[value="Создать"].ms-ButtonHeightWidth')


class ZakupListLocators:
    ZAKUP_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    FIND_ELEMENT_IN_ZAKUP_LIST = (
    By.XPATH, f"//a[@class= 'ms-listlink' and contains(text(),'{UserData.user_data_dict['fullName']}')]")

class ZakupElementLocators:

    PRICE_CATEGORY_ELEMENT_IN_ZP = (By.CSS_SELECTOR, ".fldKsupProjectCategoryBySum #SPFieldChoice")


