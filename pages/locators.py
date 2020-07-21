from userdata.user_data import UserData
from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_NAME = (By.CSS_SELECTOR, ".o365cs-me-tile-nophoto-username.o365cs-me-bidi")


class PresalePageLocators:
    PRESALE_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    FIND_ELEMENT_IN_LIST = (By.XPATH, f"//a[@class= 'ms-listlink' and contains(text(),'{UserData.name_presale}')]")


class FormCreatePresaleLocators:
    # Предмет контракта
    NAME_PRESALE_ELEMENT = (By.ID, "KsupFullName_1cb78896-92f2-4cb9-a3ad-b45e0f9932a6_$TextField")
    # Ответственный менеджер подразделения-продавца (уже предзаполнено)
    SELLER_RESPONSIBLE_ELEMENT = (By.CSS_SELECTOR, '#select2-wcfLookupControl_KsupSeller-container')
    # Способ определения поставщика
    TYPE_PRESALE_ELEMENT = (By.ID, "KsupContractorType_c208b1d8-b8f1-417e-83de-32d7be2864be_$DropDownChoice")
    # Заказчик
    CUSTOMER_ELEMENT = (By.XPATH, "//div[@id='div-wcfLookupControl_KsupEgr_Customer']/span/span/span")
    CUSTOMER_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), '{UserData.customer}')]")

    # Подразделение-продавец
    DIVISIONS_ELEMENT = (By.ID, "div-wcfLookupControl_KsupDivisions")
    DIVISIONS_DROPDOWN_ELEMENT = (By.XPATH, f"//li[normalize-space(.)='{UserData.divisions_seller}']")

    # Подразделение-исполнитель
    DIVISIONS_PERFORMER_ELEMENT = (By.ID, "div-wcfLookupControl_KsupDivisionPerformer")
    DIVISIONS_PERFORMER_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.division_performer}']")

    # Ответственный менеджер подразделения-исполнителя
    PERFORMER_RESPONSIBLE_ELEMENT = (By.ID, "div-wcfLookupControl_KsupPerformerResponsible")
    PERFORMER_RESPONSIBLE_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.performer_responsible}']")

    # Исполнитель (юридическое лицо)
    PERFORMER_LEGAL_ELEMENT = (By.ID, "div-wcfLookupControl_KsupEgr_PerformerLegal")
    PERFORMER_LEGAL_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), '{UserData.performer_legal}')]")

    # Порядок проведения закупочной процедуры
    SALE_LAW_TYPE_ELEMENT = (By.ID, "KsupSaleLawType_59c9adb5-ad0e-4308-b136-1f1006e5f9f6_$DropDownChoice")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    SEARCH_VALID_OPTION_ELEMENT = (By.CLASS_NAME, "ms-taxonomy-browser-button")

    # Элементы во фрейме "Тип работ и услуг"
    # Группа категории
    GROUP_CATEGORY_ELEMENT = (By.ID, f"{UserData.group_category}")
    # Позиция в группе
    CATEGORY_ELEMENT = (By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{UserData.category}']")
    # Кнопка "Выбор"
    CHOICE_IFRAME_BUTTON = (By.ID,
                            "ctl00_PlaceHolderDialogBodySection_PlaceHolderDialogBodyFooterMainSection_AddToFieldEditor")
    # Кнопка подтверждения (ОК)
    CONFIRM_IFRAME_BUTTON = (By.ID, "ctl00_OkButton")
    # Строка "Тип работ и услуг"
    TYPE_WORK_SERVICES_ELEMENT = (By.CSS_SELECTOR, "span.valid-text")

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
    COMPETITION_DEADLINE_FROM_ELEMENT = (By.XPATH,
                                         "//input[@id='KsupCompetitionDeadlineFrom_5b28696f-6ae9-4765-bb8d-b26513cd0e78_$DateTimeFieldDate']")

    # Плановая дата заключения договора/контракта *
    PLAN_DATE_CONTRACT_CONCLUSION_ELEMENT = (By.XPATH,
                                             "//input[@id='KsupPlanDateContractConclusion_536f5d8c-9e22-4878-9d4c-49c433c82c0d_$DateTimeFieldDate']")

    # Плановая дата окончания договора/контракта
    PLAN_DATE_CONTRACT_FINISH_ELEMENT = (By.XPATH,
                                         "//input[@id='KsupPlanDateContractFinish_aaf043ca-d88d-4e99-bcfe-7c15cbb8ba33_$DateTimeFieldDate']")

    # Вероятность заключения договора/контракта
    PROJECT_PROBABILITY_ELEMENT = (By.ID, "KsupProjectProbability_5bded577-c24a-41f7-ae50-0b1b234d8c21_$NumberField")

    # Краткое описание
    DESCRIPTION_PLAIN_TEXT_ELEMENT = (By.ID, "KsupDescriptionPlainText_18b11f3d-f4ae-4a8f-ba29-62366bd13e66_$TextField")

    # Риски
    RISKS_ELEMENT = (By.ID, "KsupRisks_32ca3c22-b19a-430b-8a16-dbe340b6867a_$TextField")

    # 1 строка Плановых платежей -  Сумма
    SUMTABLE1_ELEMENT = (By.XPATH, "//tr[3]/td[2]/input")

    # 1 строка Плановых платежей - Год
    YEARTABLE1 = (By.XPATH, "//td[4]/input")

    # 1 строка Плановых платежей - Квартал
    QUARTERTABLE1_ELEMENT = (By.XPATH, "//td[5]/select")

    # 2 строка Плановых платежей -  Сумма
    SUMTABLE2_ELEMENT = (By.XPATH, "//tr[4]/td[2]/input")

    # 2 строка Плановых платежей - Год
    YEARTABLE2 = (By.XPATH, "//tr[4]/td[4]/input")

    # 2 строка Плановых платежей - Квартал
    QUARTERTABLE2_ELEMENT = (By.XPATH, "//tr[4]/td[5]/select")

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
    CREATE_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "#CreateContractOnBasedElement\.OnBased-Large")


class FormCreateZpLocators:
    #Титул-название формы создания закупочной процедуры
    TITLE_ZP = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea .die")

    # Тип закупочной процедуры
    PRESALE_TYPE_ELEMENT = (By.CSS_SELECTOR, "#presaleTypes")

    # Предмет контракта
    NAME_ZP_ELEMENT = (By.ID, "KsupFullName_1cb78896-92f2-4cb9-a3ad-b45e0f9932a6_$TextField")

    # Подразделение-продавец
    DIVISIONS_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupDivisionSeller-container")
    DIVISIONS_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, f"//li[normalize-space(.)='{UserData.divisions_seller}']")

    # Ответственный менеджер подразделения-продавца
    SELLER_RESPONSIBLE_IN_ZP_ELEMENT = (By.CSS_SELECTOR, '#select2-wcfLookupControl_KsupSeller-container')

    # Подразделение-исполнитель
    DIVISIONS_PERFORMER_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupDivisionPerformer-container")
    DIVISIONS_PERFORMER_IN_ZP_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.division_performer}']")

    # Ответственный менеджер подразделения-исполнителя
    PERFORMER_RESPONSIBLE_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupPerformerResponsible-container")
    PERFORMER_RESPONSIBLE_IN_ZP_DROPDOWN_ELEMENT = (
        By.XPATH, f"//li[normalize-space(.)='{UserData.performer_responsible}']")

    # чек-бокс Совместные торги
    JOINT_BIDDING_ELEMENT = (
    By.CSS_SELECTOR, "#KsupPresaleJointBidding_d87bbac9-74b3-46c4-9372-38feb12d67f9_\$BooleanField")

    # Заказчик
    CUSTOMER_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupEgr_Customer-container")
    CUSTOMER_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), '{UserData.customer}')]")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    SEARCH_VALID_OPTION_ELEMENT = (By.CLASS_NAME, "ms-taxonomy-browser-button")

    # Элементы во фрейме "Тип работ и услуг"
    # Группа категории
    GROUP_CATEGORY_ELEMENT = (By.ID, f"{UserData.group_category}")
    # Позиция в группе
    CATEGORY_ELEMENT = (By.XPATH, f"//*[normalize-space(text()) and normalize-space(.)='{UserData.category}']")
    # Кнопка "Выбор"
    CHOICE_IFRAME_BUTTON = (By.ID,
                            "ctl00_PlaceHolderDialogBodySection_PlaceHolderDialogBodyFooterMainSection_AddToFieldEditor")
    # Кнопка подтверждения (ОК)
    CONFIRM_IFRAME_BUTTON = (By.ID, "ctl00_OkButton")
    # Строка "Тип работ и услуг"
    TYPE_WORK_SERVICES_ELEMENT = (By.CSS_SELECTOR, "span.valid-text")

    # Исполнитель (юридическое лицо)
    PERFORMER_LEGAL_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupEgr_PerformerLegal-container")
    PERFORMER_LEGAL_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), '{UserData.performer_legal}')]")

    SUM_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#KsupContractSum_8729d9c3-d84d-4132-97dc-27457724cf36_\$NumberField")

    # Валюта
    CURRENCY_IN_ZP_ELEMENT = (By.ID, "KsupCurrency_9cb5cce6-1d98-4146-a2df-c05c4635dd8d_$DropDownChoice")

    # Порядок проведения закупочной процедуры
    SALE_LAW_TYPE_IN_ZP_ELEMENT = (By.ID, "KsupTenderLowType_ea75ed3b-3361-4f0e-ad36-dcd5aba52908_$DropDownChoice")

    # Размер обеспечения заявки
    APPLICATION_SIZE_IN_ZP_ELEMENT = (By.ID, "KsupApplicationSize_1117d974-3a17-4f6f-9104-8cf28be18914_$NumberField")

    # Размер обеспечения договора/контракта
    CONTRACT_SIZE_IN_ZP_ELEMENT = (By.ID, "KsupContractSize_20253d6d-468d-443e-9179-3f20e0c2533e_$NumberField")
    # Плановый срок подачи на конкурс
    COMPETITION_DEADLINE_IN_ZP_FROM_ELEMENT = (By.XPATH,
                                               "//input[@id='KsupCompetitionDeadlineFrom_5b28696f-6ae9-4765-bb8d-b26513cd0e78_$DateTimeFieldDate']")

    # Плановая дата заключения договора/контракта *
    PLAN_DATE_CONTRACT_CONCLUSION_IN_ZP_ELEMENT = (By.XPATH,
                                                   "//input[@id='KsupContractPlanDateFrom_4b3ff310-7fe8-4e4f-b23c-6d570282fedd_$DateTimeFieldDate']")

    # Плановая дата окончания договора/контракта
    PLAN_DATE_CONTRACT_FINISH_IN_ZP_ELEMENT = (By.XPATH,
                                               "//input[@id='KsupContractPlanFinishDateFrom_ba6c4eb8-f5a5-4a43-8c07-d230571e83dc_$DateTimeFieldDate']")

    # Вероятность заключения договора/контракта
    PROJECT_PROBABILITY_ELEMENT = (By.ID, "KsupContractProbability_f7fc8405-e077-4ebf-bf9c-50153beb4378_$NumberField")

    # Номер закупки
    EIS_PURCHASE_NUMBER = (By.CSS_SELECTOR, "#KsupEisPurchaseNumber_8afdb894-e496-4d71-9e54-a1bf0e0a5fb6_$TextField")

    # Ссылка на закупку
    EIS_PURCHASE_LINK = (By.CSS_SELECTOR, "#KsupEisPurchaseLink_39dc12ef-bb5e-46a5-a469-5d687be8ab91_$TextField")

    # Связанные продажи
    SALES_WITH_OP = (By.XPATH, "//div[@id='div-wcfLookupControl_KsupSalesWithOp']/span/span/span/ul/li[2]/input")
    SALES_WITH_OP_FOR_VERIFY = (By.CSS_SELECTOR, ".select2-selection__choice:nth-child(1)")

    # Результаты работ
    DESCRIPTION_PLAIN_IN_ZP_ELEMENT = (By.ID, "KsupPaDescription_81c0defa-82c4-4dec-a6f1-556818457fd6_$TextField")

    # Тендерная заявка
    FILE_TENDER_REQUEST = (By.XPATH, "// div[ @ id = 'File_TenderRequest'] / div / input")

    # Тендерная документация
    FILE_TENDER_DOCS_FROM_CUSTOMER = (By.XPATH, "//div[@id='File_TenderDocsFromCustomer']/div/input")

    # Бюджет проекта
    FILE_BUDGET_OF_PROJECT = (By.XPATH, "//div[@id='File_BudgetOfProject']/div/input")

    # Пояснительная служебная записка
    FILE_EXPLANATORY_MEMORANUM = (By.XPATH, "//div[@id='File_ExplanatoryMemoranum']/div/input")

    # Проект контракта
    FILE_PROJECT_OF_CONTRACT = (By.XPATH, "//div[@id='File_ProjectOfContract']/div/input")

    # Риски проекта с точки зрения Департамента
    PROJECT_RISK_DEPARTMENT_PERSPEC = (
    By.ID, "KsupProjectRiskDepartmentPerspec_2c6333aa-aa0b-4e97-aab8-b89e7aa7f0c6_$TextField")

    # Документы с описанием рисков
    FILE_RISK_MAP_AND_REGISTRY = (By.XPATH, "//div[@id='File_RiskMapAndRegistry']/div/input")

    # Иное
    FILE_OTHER = (By.XPATH, "//div[@id='File_Other']/div/input")

    # Кнопка создания сущности закупочная процедура
    CONFIRM_ZP_BUTTON = (By.CSS_SELECTOR, '[value="Создать"].ms-ButtonHeightWidth')
