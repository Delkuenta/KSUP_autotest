from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME_ELEMENT = (By.CSS_SELECTOR, "#userNameInput")
    PASSWORD_ELEMENT = (By.CSS_SELECTOR, "#passwordInput")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submitButton")


class BasePageLocators:
    USER_NAME = (By.CSS_SELECTOR, "span[class*='me-tile-nophoto-username']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[id$='SubLink_ShellSignout']")
    PRESALE_LIST_LINK = "/SalesManagement/Lists/Sale/All.aspx"
    PRESALE_LIST_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    ZAKUP_LIST_LINK = "/SalesManagement/Lists/PresaleActivity/All.aspx"
    ZAKUP_LIST_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    CONTRACT_LIST_LINK = "/SalesManagement/Lists/Contract/All.aspx"
    CONTRACT_LIST_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    KNOWLEDGE_SEARCH_LINK = "/Pages/KnowledgeBaseSearch.aspx"
    KNOWLEDGE_SEARCH_TITLE = (By.CSS_SELECTOR, ".title.title--main")
    PROJECT_LIST_LINK = "/KnowledgeBase/Project/Forms/All.aspx"
    PROJECT_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    CUSTOMER_LIST_LINK = "/KnowledgeBase/Lists/Egrul/All.aspx"
    CUSTOMER_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    OPERPLAN_DEPARTMENT_LINK = "/SalesManagement/Lists/OperationalPlanDivision/All.aspx"
    OPERPLAN_DEPARTMENT_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")
    OPERPLAN_DIRECTION_LINK = "/SalesManagement/Lists/OperationalPlanDirectorate/All.aspx"
    OPERPLAN_DIRECTION_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea a")


    # Локаторы во фрейме "Тип работ и услуг"
    # Группы категорий
    GROUP_CATEGORY_ELEMENT1 = (By.CSS_SELECTOR, "#TIE_3")
    GROUP_CATEGORY_ELEMENT2 = (By.CSS_SELECTOR, "#TIE_4")
    GROUP_CATEGORY_ELEMENT3 = (By.CSS_SELECTOR, "#TIE_5")
    GROUP_CATEGORY_ELEMENT4 = (By.CSS_SELECTOR, "#TIE_6")
    GROUP_CATEGORY_ELEMENT5 = (By.CSS_SELECTOR, "#TIE_7")

    # Кнопка прокрутки вниз у категории Программное обеспечение
    SCROLL_DOWN_SOFTWARE_BUTTON = (By.CSS_SELECTOR, "#PGD_6")

    # Кнопка  элемента //*[normalize-space(text()) and normalize-space(.)='name_type_works']
    WORK_SERVICE_ELEMENT = (By.XPATH, "//*[contains(text(), 'name_type_works')]")

    # Кнопка "Выбор" //button[contains(@id, 'AddToFieldEditor')]
    CHOICE_IFRAME_BUTTON = (By.CSS_SELECTOR, "button[id$='AddToFieldEditor']")
    # Кнопка подтверждения (ОК) //button[contains(@id, 'OkButton')]
    CONFIRM_IFRAME_BUTTON = (By.CSS_SELECTOR, "[id$='OkButton']")

    # Локаторы во фрейме "Территория применения"
    # Группа территорий во фрейме
    GROUP_TERRITORY_ELEMENT = (By.CSS_SELECTOR, "#TIE_3")
    # Элемент территории //*[normalize-space(text()) and normalize-space(.)='territory_name']
    TERRITORY_ELEMENT = (By.XPATH, "//*[contains(text(), 'territory_name')]")

    SCROLL_DOWN_BUTTON_TERRITORY = (By.CSS_SELECTOR, "#PGD_3")

    # Кнопка прокрутки в технологиях
    SCROLL_DOWN_BUTTON = (By.CSS_SELECTOR, "#PGD_1")

    # Выбор технологии //*[normalize-space(text()) and normalize-space(.)='name']
    ELEMENT_IN_FRAME = (By.XPATH, "//*[contains(text(), 'name')]")


class PresaleListLocators:
    PRESALE_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    FIND_ELEMENT_IN_PRESALE_LIST = (By.XPATH, f"//a[@class= 'ms-listlink' and contains(text(),'Test_name')]")

    # Вкладки на листе сущности "Пресейловая активность"
    ALL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewAll']")
    MINE_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewMy']")
    SENT_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewSent']")
    APPROVAL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewApproval']")
    IN_OP_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewInOp']")
    OUT_OP_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewOutOp']")

    # Поле "Статус согласования" множественный результат
    APPROVAL_STATUS_VALUES = (By.CSS_SELECTOR, "[class^='colKsupSaleApproveStatus ms-cellstyle ms-vb2']")

    # Кнопка Пагинатора "Далее"
    PAGINATOR_NEXT_BUTTON = (By.CSS_SELECTOR, "[class^='ms-commandLink'][title='Далее']")


class FormCreatePresaleLocators:
    # Предмет контракта  //textarea[contains(@id, 'KsupFullName')]
    NAME_PRESALE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupFullName']")

    # Способ определения поставщика //select[contains(@id, '')]
    CONTRACTOR_TYPE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupContractorType']")

    # Заказчик * //div[@id='div-wcfLookupControl_KsupEgr_Customer']/span/span/span
    CUSTOMER_ELEMENT = (By.CSS_SELECTOR, "[aria-labelledby*='wcfLookupControl_KsupEgr_Customer']")
    CUSTOMER_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'customer_name')]")

    # Подразделение-продавец *f"//li[normalize-space(.)='salesUnit_name']"
    SALES_UNIT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupDivisions")
    SALES_UNIT_DROPDOWN_ELEMENT = (By.XPATH, "//*[contains(@id, 'KsupDivisions')]//li[contains(text(), 'salesUnit_name')]")

    # Ответственный менеджер подразделения-продавца * //li[normalize-space(.)='salesManager_name']
    SALES_MANAGER_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupSeller")
    SALES_MANAGER_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'salesManager_name')]")
    SALES_MANAGER_ELEMENT_VALUE = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupSeller-container")

    # Подразделение-исполнитель  //li[contains(text(), 'executiveUnit_name')]
    EXECUTIVE_UNIT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupDivisionPerformer")
    # //li[contains(text(), '')]
    EXECUTIVE_UNIT_DROPDOWN_ELEMENT = (
        By.XPATH, "//*[contains(@id, 'KsupDivisionPerformer')]//li[contains(text(), 'executiveUnit_name')]")

    # Ответственный менеджер подразделения-исполнителя //li[normalize-space(.)='executiveManager_name']
    EXECUTIVE_MANAGER_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupPerformerResponsible")
    EXECUTIVE_MANAGER_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'executiveManager_name')]")
    EXECUTIVE_MANAGER_ELEMENT_VALUE = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupPerformerResponsible-container")

    # Исполнитель (юридическое лицо)
    EXECUTIVE_UNIT_LEGAL_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_PerformerLegal")
    EXECUTIVE_UNIT_LEGAL_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), 'executiveUnitLegal_name')]")

    # Порядок проведения закупочной процедуры //select[contains(@id, 'KsupSaleLawType')]
    SALE_LAW_TYPE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupSaleLawType']")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    # //div[contains(@id,'KsupWorkServicesTypeMetadata')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_VALID_OPTION_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupWorkServicesType']>[class='ms-taxonomy-browser-button']")

    # Строка "Тип работ и услуг"
    # //div[contains(@id,'KsupWorkServicesTypeMetadata') and contains(@class,'ms-taxonomy-writeableregion')]
    # [id^='KsupWorkServicesType'][class^='ms-taxonomy-writeableregion']
    TYPE_WORK_SERVICES_ELEMENT = (By.XPATH, "//div[contains(@id,'KsupWorkServicesTypeMetadata') and contains(@class,'ms-taxonomy-writeableregion')]")


    # Сумма //input[starts-with(@id,'KsupSum')]
    SUM_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupSum']")

    # Валюта //select[starts-with(@id, 'KsupCurrency')]
    CURRENCY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupCurrency']")

    # Размер обеспечения заявки //input[starts-with(@id,'KsupApplicationSize')]
    APPLICATION_SIZE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupApplicationSize']")

    # Размер обеспечения договора/контракта //input[starts-with(@id,'KsupContractSize')]
    CONTRACT_SIZE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupContractSize']")

    # Самостоятельная продажа //select[starts-with(@id, 'KsupSeparateSale')]
    SEPARATE_SALE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupSeparateSale']")

    # Плановый срок подачи на конкурс //input[starts-with(@id, 'KsupCompetitionDeadlineFrom')]
    COMPETITION_DEADLINE_FROM_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupCompetitionDeadlineFrom'][class='ms-input']")

    # Плановая дата заключения договора/контракта * //input[starts-with(@id, 'KsupPlanDateContractConclusion')]
    PLAN_DATE_CONTRACT_CONCLUSION_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupPlanDateContractConclusion'][class='ms-input']")

    # Плановая дата окончания договора/контракта //input[starts-with(@id, 'KsupPlanDateContractFinish')]
    PLAN_DATE_CONTRACT_FINISH_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupPlanDateContractFinish'][class='ms-input']")

    # Вероятность заключения договора/контракта //input[starts-with(@id, 'KsupProjectProbability')]
    PROJECT_PROBABILITY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupProjectProbability']")

    # Краткое описание //textarea[starts-with(@id, 'KsupDescriptionPlainText')]
    DESCRIPTION_PLAIN_TEXT_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupDescriptionPlainText']")

    # Риски //textarea[starts-with(@id, 'KsupRisks')]
    RISKS_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupRisks']")

    # Поля плановых платежей, возможно множество элементов
    SUMTABLE = (By.CSS_SELECTOR, ".payplan-summa-field")
    YEARTABLE = (By.CSS_SELECTOR, ".payplan-year-field")
    QUARTERTABLE = (By.CSS_SELECTOR, ".payplan-cell.table__td select")
    DELETE_ROW_BUTTON = (By.CSS_SELECTOR, "[class*='payplan-cell-delete'][data-member='delete']")

    # Кнопка создания сущности пресейл
    CONFIRM_PRESALE_BUTTON = (By.CSS_SELECTOR, '[value="Создать"].ms-ButtonHeightWidth')

    # Кнопка сохранения сущности после изменений
    CONFIRM_EDIT_PRESALE_BUTTON = (By.CSS_SELECTOR, "[id$='ctl00_ctl00_diidIOSaveItem'].ms-ButtonHeightWidth")

    # Элементы модульного окна при отправке на согласование внутри формы создания ПА
    iframe = (By.CSS_SELECTOR, ".ms-dlgFrame")

    # Поле для выбора подразделения //span[@id='select2-directionItems-container']
    APPROVAL_DEPARTMENT_ELEMENT = (By.XPATH, "//span[contains(@id, 'directionItems')]")
    APPROVAL_DEPARTMENT_ELEMENT_DROPDOWN = (By.XPATH,
                                            "//*[contains(@id, 'directionItems-results')]//li[contains(text(), 'deparment_value')]")

    # Кнопка "Отправить" на согласование //input[contains(@id, 'PlaceHolderMain_btnSend')]
    APPROVAL_CONFIRM_SEND_BUTTON = (By.CSS_SELECTOR, "[id*='PlaceHolderMain_btnSend']")

    # Кнопка "Отмена" в модульном окне отправки на согласование //input[contains(@id, 'PlaceHolderMain_btnCancel')]
    APPROVAL_CANCEL_SEND_BUTTON = (By.CSS_SELECTOR, "[id*='PlaceHolderMain_btnCancel']")


class PresaleElementLocators:
    # Титул в карточке "Пресейловая активность"
    TITLE_IN_PRESALE = (By.CSS_SELECTOR, "#pageTitle")

    # Кнопка изменения элемента
    EDIT_ITEM_BUTTON = (By.CSS_SELECTOR, "[id='Ribbon.ListForm.Display.Manage.EditItem-Large']")

    # Кнопка "Внести информацию о конкурсе"
    TENDER_APPLICATION_BUTTON = (By.CSS_SELECTOR, "#createPresaleActivityBasedOnSale_TenderApplication-Large")

    # Кнопка "Внести информацию о запросе цен"
    PRESALE_ACT_BUTTON = (By.CSS_SELECTOR, "#createPresaleActivityBasedOnSale_PresaleAct-Large")

    # Кнопка "Внести информацию о коммерческом предложении"
    COMMERCIAL_OFFER_BUTTON = (By.CSS_SELECTOR, "#createPresaleActivityBasedOnSale_CommercialOffer-Large")

    # Кнопка "Внести информацию о договоре/контракте"
    CREATE_CONTRACT_BUTTON = (By.CSS_SELECTOR, "[id='Ribbon.ListForm.Display.ContractGroup-LargeLarge']")

    # Кнопка "Отправить продавцу" //a[contains(@id, 'Approve.ToDirection')]
    SEND_APPROVE_TO_DIRECTION_BUTTON = (By.CSS_SELECTOR, "[id^='Approve.ToDirection']")

    # Кнопка "Отправить исполнителю/продавцу" //a[contains(@id, 'Approve.ToDepartment')]
    SEND_APPROVE_TO_DEPARTMENT_BUTTON = (By.CSS_SELECTOR, "[id^='Approve.ToDepartment']")

    # Элементы модульного окна при отправке на согласование
    # Название(титул фрейма)
    TITLE_APPROVAL_FRAME_PRESALE = (By.CSS_SELECTOR, "#dialogTitleSpan")

    # Поле для выбора подразделения
    APPROVAL_DEPARTMENT_ELEMENT = (By.XPATH, "//span[contains(@id, 'directionItems')]")
    # Выбор из выпадающего списка //li[normalize-space(.)='Unit_name']
    UNIT_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), 'Unit_name')]")
    # Кнопка "Отправить" на согласование //input[contains(@id, 'PlaceHolderMain_btnSend')]
    APPROVAL_CONFIRM_SEND_BUTTON = (By.CSS_SELECTOR, "[id*='PlaceHolderMain_btnSend']")
    # Кнопка "Отмена" (работает в модульных окнах: отправки, согласования, отклоенения)
    # //input[contains(@id, 'PlaceHolderMain_btnCancel')]
    APPROVAL_CANCEL_SEND_BUTTON = (By.CSS_SELECTOR, "[id*='PlaceHolderMain_btnCancel']")

    # Кнопка согласования пресейла //a[@id='Approve.Approve-Large']
    CONFIRM_APPROVAL_BUTTON = (By.CSS_SELECTOR, "[id^='Approve.Approve']")

    # Кнопка  отклонения согласования //a[@id='Approve.Reject-Large']
    CANCEL_APPROVAL_BUTTON = (By.CSS_SELECTOR, "[id^='Approve.Reject']")

    # Окно iframe
    iframe = (By.CSS_SELECTOR, ".ms-dlgFrame")

    # Поле выбора менеджера в окне согласования
    APPROVAL_MANAGER_ELEMENT = (By.XPATH, "//span[contains(@id, 'PlaceHolderMain_ddlResponsbileManager')]")

    # Выбор значения продавца //li[normalize-space(.)='salesManager_name']
    CHANGE_SELLER_RESPONSIBLE_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'salesManager_name')]")

    # Выбор значения продавца //li[normalize-space(.)='executiveManager_name']
    CHANGE_SELLER_PERFORMER_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'executiveManager_name')]")

    # Кнопка подтверждения согласования в модульном окне //input[contains(@id, 'PlaceHolderMain_btnApprove')]
    APPROVAL_BUTTON_IN_FRAME = (By.CSS_SELECTOR, "[id*='PlaceHolderMain_btnApprove']")

    # Кнопка отклонения согласования в модульном окне //input[contains(@id, 'PlaceHolderMain_btnReject')]
    REJECT_BUTTON_IN_FRAME = (By.CSS_SELECTOR, "[id*='PlaceHolderMain_btnReject']")

    # Поле "Причина" в модульном окне отклонения
    REASON_TEXT_ELEMENT = (By.CSS_SELECTOR, ".agreement-direction-reason")

    # Кнопка ок в модульном окне "Сообщения" после отклонения/согласования //input[@value='OK']
    MESSAGE_OK_BUTTON = (By.CSS_SELECTOR, "[value='OK']")

    # Элементы на вкладке "Общие сведения"
    CONTRACTOR_TYPE_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupContractorType #SPFieldChoice")
    # Поле "Заказчик"
    CUSTOMER_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupEgr_Customer #SPFieldWcfLookup")
    # Поле "Подразделение-продавец"
    SALES_UNIT_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupDivisions #SPFieldWcfLookup")
    # Поле "Ответственный менеджер подразделения-продавца"
    SALES_MANAGER_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupSeller #SPFieldWcfLookup")
    # Поле "Подразделение-исполнитель"
    EXECUTIVE_UNIT_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupDivisionPerformer #SPFieldWcfLookup")
    # Поле "Ответственный менеджер подразделения-исполнителя"
    EXECUTIVE_MANAGER_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupPerformerResponsible #SPFieldWcfLookup")
    # Поле "Исполнитель (юридическое лицо)"
    EXECUTIVE_UNIT_LEGAL_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupEgr_PerformerLegal #SPFieldWcfLookup")
    # Поле "Порядок проведения закупочной процедуры" для Тендер
    SALE_LAW_TYPE_TENDER_PRESALE = (By.CSS_SELECTOR, ".fldKsupSaleLawType  #SPFieldChoice")
    # Поле "Тип работ и услуг"
    TYPE_OF_WORK_SERVCICES_IN_PRESALE = (By.CSS_SELECTOR, "#SPFieldTaxonomyFieldTypeMulti")
    # Поле "Начальная (максимальная) цена контракта"
    SUM_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupSumPlan #SPFieldNumber")
    # Поле "Валюта договора/контракта"
    CURRENCY_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupCurrency #SPFieldChoice")
    # Поле "Размер обеспечения заявки"
    APPLICATION_SIZE_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupApplicationSize #SPFieldNumber")
    # Поле "Размер обеспечения договора/контракта"
    CONTRACT_SIZE_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupContractSize #SPFieldNumber")
    # Поле "Статус продажи"
    PRESALE_STATUS = (By.CSS_SELECTOR, ".fldKsupSaleStatus #SPFieldChoice")
    # Поле "Самостоятельная продажа"
    SEPARATE_SALE_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupSeparateSale #SPFieldChoice")
    # Поле "Плановый срок подачи на конкурс"
    COMPETITION_DEAD_LINE_FROM_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupCompetitionDeadlineFrom #SPFieldDateTime")
    # Поле "Плановая дата заключения договора/контракта"
    START_DATE_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupPlanDateContractConclusion #SPFieldDateTime")
    # Поле "Плановая дата окончания договора/контракта"
    END_DATE_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupPlanDateContractFinish #SPFieldDateTime")
    # Поле "Вероятность заключения договора/контракта"
    PROJECT_PROBABILITY_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupProjectProbability  #SPFieldNumber")
    # Поле "Статус согласования с подразделением"
    PRESALE_APPROVAL_STATUS = (By.CSS_SELECTOR, ".fldKsupSaleApproveStatus #SPFieldChoice")
    # Поле "Краткое описание"
    DESCRIPTION_TEXT_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupDescriptionPlainText #SPFieldNote")
    # Поле "Риски"
    RISKS_IN_PRESALE = (By.CSS_SELECTOR, ".fldKsupRisks #SPFieldNote")


class FormCreateZakupLocators:
    # Общие поля для всех типов
    TITLE_ZP = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea .die")

    # Тип закупочной процедуры
    CONTRACTOR_TYPE_ELEMENT = (By.CSS_SELECTOR, "[id='presaleTypes']")

    # Предмет контракта  //textarea[contains(@id, 'KsupFullName')]
    NAME_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupFullName']")

    # Подразделение-продавец *f"//li[normalize-space(.)='salesUnit_name']"
    SALES_UNIT_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupDivisionSeller")
    SALES_UNIT_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'salesUnit_name')]")

    # Ответственный менеджер подразделения-продавца
    SALES_MANAGER_IN_ZP_ELEMENT = (By.CSS_SELECTOR, '#div-wcfLookupControl_KsupSeller')
    SALES_MANAGER_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'salesManager_name')]")

    # Подразделение-исполнитель
    EXECUTIVE_UNIT_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupDivisionPerformer")
    EXECUTIVE_UNIT_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'executiveUnit_name')]")

    # Ответственный менеджер подразделения-исполнителя
    EXECUTIVE_MANAGER_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupPerformerResponsible")
    EXECUTIVE_MANAGER_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'executiveManager_name')]")

    # Заказчик
    CUSTOMER_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_Customer")
    CUSTOMER_IN_ZP_DROPDOWN_ELEMENT = (By.XPATH, f"//li[contains(text(), 'customer_name')]")
    # Название поля "Заказчик" при активации "Совмсетные торги" меняет название
    CUSTOMER_FIELD_NAME = (By.XPATH, "//*[@class='fldKsupEgr_Customer ']//*[@class='ms-h3 ms-standardheader']")

    # Исполнитель (юридическое лицо)
    EXECUTIVE_LEGAL_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_PerformerLegal")
    EXECUTIVE_LEGAL_DROPDOWN_IN_ZP_ELEMENT = (By.XPATH, f"//li[contains(text(), 'executiveUnitLegal_name')]")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    # //div[contains(@id,'KsupWorkServicesTypeMetadata')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_VALID_OPTION_ELEMENT = (By.CSS_SELECTOR, "[id^=KsupWorkServicesType]>[class='ms-taxonomy-browser-button']")

    # Элементы во фрейме "Тип работ и услуг"
    # Строка "Тип работ и услуг"
    # //div[contains(@id,'KsupWorkServicesTypeMetadata') and contains(@class,'ms-taxonomy-writeableregion')]
    TYPE_WORK_SERVICES_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupWorkServicesType'][class^='ms-taxonomy-writeableregion']")

    # Сумма //input[starts-with(@id, 'KsupContractSum')]
    SUM_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^=KsupContractSum]")

    # Валюта //select[starts-with(@id, 'KsupCurrency')]
    CURRENCY_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^=KsupCurrency]")

    # Плановая дата окончания договора/контракта //input[starts-with(@id, 'KsupContractPlanFinishDateFrom')]
    PLAN_DATE_CONTRACT_FINISH_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupContractPlanFinishDateFrom'][class='ms-input']")

    # Вероятность заключения договора/контракта //input[starts-with(@id, 'KsupContractProbability')]
    PROJECT_PROBABILITY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupContractProbability']")

    # Связанные продажи //div[@id='div-wcfLookupControl_KsupSalesWithOp']/span/span/span/ul/li[2]/input
    SALES_WITH_OP = (By.XPATH, "//div[starts-with(@id,'div-wcfLookupControl_KsupSalesWithOp')]/span[starts-with(@class,'select2')]")
    SALES_WITH_OP_FOR_VERIFY = (By.CSS_SELECTOR, ".select2-selection__choice:nth-child(1)")

    # Результаты работ //textarea[starts-with(@id, 'KsupPaDescription')]
    DESCRIPTION_PLAIN_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupPaDescription']")

    # Риски проекта с точки зрения Департамента //textarea[starts-with(@id, 'KsupProjectRiskDepartmentPerspec')]
    PROJECT_RISK_DEPARTMENT_PERSPEC = (By.CSS_SELECTOR, "[id^='KsupProjectRiskDepartmentPerspec']")

    # Документы с описанием рисков //div[@id='File_RiskMapAndRegistry']/div/input
    # //div[@id='File_RiskMapAndRegistry']//input[@type='file']
    FILE_RISK_MAP_AND_REGISTRY = (By.CSS_SELECTOR, "[id='File_RiskMapAndRegistry']>div>input")
    # fileField_File_RiskMapAndRegistry_NameLink_
    FILE_RISK_MAP_AND_REGISTRY_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_RiskMapAndRegistry_NameLink_']")

    # Иное //div[@id='File_Other']/div/input
    FILE_OTHER = (By.CSS_SELECTOR, "[id='File_Other']>div>input")
    # fileField_File_Other_NameLink_
    FILE_OTHER_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_Other_NameLink_']")

    # Общие поля для типа "Тендерная заявка" и "Коммчерческое предложение"
    # Плановая дата заключения договора/контракта * //input[starts-with(@id, 'KsupContractPlanDateFrom')]
    PLAN_DATE_CONTRACT_CONCLUSION_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupContractPlanDateFrom'][class='ms-input']")

    # Бюджет проекта //div[@id='File_BudgetOfProject']/div/input
    FILE_BUDGET_OF_PROJECT = (By.CSS_SELECTOR, "[id='File_BudgetOfProject']>div>input")
    # fileField_File_BudgetOfProject_NameLink_
    FILE_BUDGET_OF_PROJECT_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_BudgetOfProject_NameLink_']")

    # Пояснительная служебная записка //div[@id='File_ExplanatoryMemoranum']/div/input
    FILE_EXPLANATORY_MEMORANUM = (By.CSS_SELECTOR, "[id='File_ExplanatoryMemoranum']>div>input")
    FILE_EXPLANATORY_MEMORANUM_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_ExplanatoryMemoranum_NameLink_']")

    # Проект контракта //div[@id='File_ProjectOfContract']/div/input
    FILE_PROJECT_OF_CONTRACT = (By.CSS_SELECTOR, "[id='File_ProjectOfContract']>div>input")
    FILE_PROJECT_OF_CONTRACT_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_ProjectOfContract_NameLink_']")

    # Общие поля для типа "Тендерная заявка" и "Запрос, цен, товаров и услуг"
    # Порядок проведения закупочной процедуры (Тендерная заявка) //select[starts-with(@id, 'KsupTenderLowType')]
    CONTRACTOR_TYPE_TENDER_ZP = (By.CSS_SELECTOR, "[id^= 'KsupTenderLowType']")

    # Порядок проведения закупочной процедуры (Тендерная заявка) //select[starts-with(@id, 'KsupRequestLowType')]
    CONTRACTOR_TYPE_ZAPROS_CEN_ZP = (By.CSS_SELECTOR, "[id^= 'KsupRequestLowType']")

    # Размер обеспечения заявки //input[starts-with(@id, 'KsupApplicationSize')]
    APPLICATION_SIZE_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^= 'KsupApplicationSize']")

    # Размер обеспечения договора/контракта //input[starts-with(@id, 'KsupContractSize')]
    CONTRACT_SIZE_IN_ZP_ELEMENT = (By.CSS_SELECTOR, "[id^= 'KsupContractSize']")

    # Уникальные поля для типа "Тендерная заявка"
    # чек-бокс Совместные торги //input[starts-with(@id, 'KsupPresaleJointBidding')]
    JOINT_BIDDING_CHECKBOX = (By.CSS_SELECTOR, "[id^='KsupPresaleJointBidding']")

    # Срок подачи на конкурс //input[starts-with(@id, 'KsupCompetitionDeadlineFrom')]
    COMPETITION_DEADLINE_IN_ZP_FROM_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupCompetitionDeadlineFrom'][class='ms-input']")

    # Номер закупки //input[starts-with(@id, 'KsupEisPurchaseNumber')]
    EIS_PURCHASE_NUMBER = (By.CSS_SELECTOR, "[id^='KsupEisPurchaseNumber']")

    # Ссылка на закупку //textarea[starts-with(@id, 'KsupEisPurchaseLink')]
    EIS_PURCHASE_LINK = (By.CSS_SELECTOR, "[id^='KsupEisPurchaseLink']")

    # Тендерная заявка //div[@id='File_TenderRequest']/div/input
    FILE_TENDER_REQUEST = (By.CSS_SELECTOR, "[id='File_TenderRequest']>div>input")
    FILE_TENDER_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_TenderRequest_NameLink_']")

    # Тендерная документация //div[@id='File_TenderDocsFromCustomer']/div/input
    FILE_TENDER_DOCS_FROM_CUSTOMER = (By.CSS_SELECTOR, "[id='File_TenderDocsFromCustomer']>div>input")
    FILE_TENDER_DOCS_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_TenderDocsFromCustomer_NameLink_']")

    # Уникальные поля для типа "Коммерческое предложение"

    # Официальный запрос от Заказчика на КП //div[@id='File_KPRequestFromCustomer']/div/input
    FILE_KP_REQUEST_FROM_CUSTOMER = (By.CSS_SELECTOR, "[id='File_KPRequestFromCustomer']>div>input")
    FILE_KP_REQUEST_FROM_CUSTOMER_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_KPRequestFromCustomer_NameLink_']")

    # Коммерческое предложение по официальному запросу //div[@id='File_OfferByRequest']/div/input
    FILE_OFFER_BY_REQUEST = (By.CSS_SELECTOR, "[id='File_OfferByRequest']>div>input")
    FILE_OFFER_BY_REQUEST_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_OfferByRequest_NameLink_']")

    # Уникальные поля для типа "Запрос цена, товаров и услуг"

    # Срок предоставления ценовой информации //input[starts-with(@id, 'KsupPriceInformationDeadlineFrom')]
    PRICE_INFORMATION_DEADLINE_FROM = (By.CSS_SELECTOR, "[id^='KsupPriceInformationDeadlineFrom'][class='ms-input']")

    # Предполагаемая дата начала проведения закупки с //input[starts-with(@id, 'KsupPurchaseStartDateFrom')]
    PURCHASE_START_DATE_FROM = (By.CSS_SELECTOR, "[id^='KsupPurchaseStartDateFrom'][class='ms-input']")

    # Предполагаемая дата начала проведения закупки по //input[starts-with(@id, 'KsupPurchaseStartDateTo')]
    PURCHASE_START_DATE_TO = (By.CSS_SELECTOR, "[id^='KsupPurchaseStartDateTo'][class='ms-input']")

    # Номер запроса цен на Официальном сайте ЕИС //input[starts-with(@id, 'KsupEisPriceNumber')]
    EIS_PRICE_NUMBER = (By.CSS_SELECTOR, "[id^='KsupEisPriceNumber']")

    # Ссылка на запрос на Официальном сайте ЕИС //textarea[starts-with(@id, 'KsupEisPriceLink')]
    EIS_PRICE_LINK = (By.CSS_SELECTOR, "[id^='KsupEisPriceLink']")

    # Запрос НМЦК //div[@id='File_NMCKRequest']/div/input
    FILE_NMCK_REQUEST = (By.CSS_SELECTOR, "[id='File_NMCKRequest']>div>input")
    FILE_NMCK_REQUEST_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_NMCKRequest_NameLink_']")

    # Ответ на запрос НМЦК //div[@id='File_NMCKResponse']/div/input
    FILE_NMCK_RESPONSE = (By.CSS_SELECTOR, "[id='File_NMCKResponse']>div>input")
    FILE_NMCK_RESPONSE_NAME_LINK = (By.CSS_SELECTOR, "[class='fileField_File_NMCKResponse_NameLink_']")

    # Кнопка создания сущности закупочная процедура
    CONFIRM_ZP_BUTTON = (By.CSS_SELECTOR, "[id*='diidIOSaveItem'][value='Создать']")


class ZakupListLocators:
    ZAKUP_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    FIND_ELEMENT_IN_ZAKUP_LIST = (By.XPATH, f"//a[@class= 'ms-listlink' and contains(text(),'Test_name')]")

    # Вкладки на листе сущности "Закупочная процедура"
    ALL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewAll']")
    MINE_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewMy']")
    APPROVAL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewApproval']")
    REJECTED_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewRejected']")
    APPROVED_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewApproved']")

    # Поле "Статус согласования" множественный результат
    APPROVAL_STATUS_VALUES = (By.CSS_SELECTOR, "[class^='colKsupPresaleApproveStatus ms-cellstyle ms-vb2']")

    # Кнопка Пагинатора "Далее"
    PAGINATOR_NEXT_BUTTON = (By.CSS_SELECTOR, "[class^='ms-commandLink'][title='Далее']")


class ZakupElementLocators:
    # Титул в карточке "Закупочная процедура"
    TITLE_IN_ZP = (By.CSS_SELECTOR, "#pageTitle")

    # Кнопка создания Контракта на основе закупочной процедуры //a[starts-with(@id, 'CreateContractBasedOnPresaleActivity')]
    CREATE_CONTRACT_BASED_ON_ZAKUP = (By.CSS_SELECTOR, "[id^='CreateContractBasedOnPresaleActivity']")

    # Кнопка Отправить на согласование ЗП  //a[contains(@id, 'ApprovePresaleActivity.ToApprove')]
    SEND_APPROVAL_BUTTON = (By.CSS_SELECTOR, "[id^='ApprovePresaleActivity.ToApprove']")
    # Всплывающее окно подтверждения/отмены отправки закупочной процедуры
    CONFIRM_SEND_APPROVAL_BUTTON = (By.XPATH, "//button[@type = 'button' and (text() = 'Отправить')]")
    CANCEL_SEND_APPROVAL_BUTTON = (By.XPATH, "//button[@type = 'button' and (text() = 'Отмена')]")
    # Кнопка согласования и отклонения закупочной процедуры //a[starts-with(@id, 'ApprovePresaleActivity.Approve')]
    APPROVAL_ZAKUP_BUTTON = (By.CSS_SELECTOR, "[id^='ApprovePresaleActivity.Approve']")
    REJECT_ZAKUP_BUTTON = (By.CSS_SELECTOR, "[id^='ApprovePresaleActivity.Reject']")
    # Кнопка эскалирования на ККП
    ESCALATE_ZAKUP_BUTTON = (By.CSS_SELECTOR, "[id^='ApprovePresaleActivity.Escalate']")
    # Кнопка отправка на доработку
    REVISION_ZAKUP_BUTTON = (By.CSS_SELECTOR, "[id^='ApprovePresaleActivity.Revision']")
    # Кнопка Отзыв с внутренного согласования
    WITHDRAW_FROM_APPROVAL_BUTTON = (By.CSS_SELECTOR, "[id^='Approve.Cancel']")

    # элементы внутри окна подтверждения/отклонения //textarea[@id ='dialogComment']
    COMMENT_TO_APPROVAL_ZAKUP = (By.CSS_SELECTOR, "[id='dialogComment']")
    # //input[@name='filefield']
    FILE_TO_APPROVAL_ZAKUP = (By.CSS_SELECTOR, "[name='filefield']")
    CONFIRM_APPROVAL_ZAKUP = (By.XPATH, "//button[@type = 'button' and (text() = 'Согласовать')]")
    CONFIRM_REJECT_ZAKUP = (By.XPATH, "//button[@type = 'button' and (text() = 'Отклонить')]")
    CONFIRM_ESCALATE_ZAKUP = (By.XPATH, "//button[@type = 'button' and (text() = 'Эскалировать')]")
    CONFIRM_REVISION_ZAKUP = (By.XPATH, "//button[@type = 'button' and (text() = 'Отправить на доработку')]")
    CANCEL_APPROVAL_ZAKUP = (By.XPATH, "//button[@type = 'button' and (text() = 'Отмена')]")
    ClOSE_ALLERT_ZAKUP = (By.CSS_SELECTOR, "#dlgTitleBtns")
    START_WITH_ELEMENT = (By.CSS_SELECTOR, "#dialogRestartStatus")

    # Вкладки в карточке
    GENERAL_INFORMATION_ELEMENT = (By.XPATH, "//a[contains(@href, '#tabCommon')]")
    ATTACHED_FILES_ELEMENT = (By.XPATH, "//a[contains(@href, '#tabFiles')]")
    APPROVAL_HISTORY_ELEMENT = (By.XPATH, "//a[contains(@href, '#tabApprovingHistory')]")

    # Строки статус согласования
    APPROVAL_LEGAL_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование юридической службой']/following::span[1]")
    APPROVAL_COUNT_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование бухгалтерией']/following::span[1]")
    APPROVAL_FIN_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование финансовой службой']/following::span[1]")
    APPROVAL_UDPRPO_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование Директором по разработке ПО']/following::span[1]")
    APPROVAL_KKP_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование ККП']/following::span[1]")

    # Все элементы со статусом согласования
    RESULT_APPROVAL_LIST = (By.CSS_SELECTOR, "[role^= 'result']")

    # Элементы на вкладке "Общие сведения"
    # Поле "Статус согласования"
    APPROVAL_MAIN_STATUS_IN_ZP = (By.CSS_SELECTOR, ".fldKsupPresaleApproveStatus #SPFieldChoice")
    # Значение в Поле "Тип закупочной процедуры" //td[contains(@id, 'ContentTypeFieldDisplay')]
    CONTRACTOR_TYPE_IN_ZP = (By.CSS_SELECTOR, "[id$='tdContentTypeFieldDisplay']")
    # Значение в Поле "Подразделение-продавец"
    SALES_UNIT_IN_ZP = (By.CSS_SELECTOR, ".fldKsupDivisionSeller #SPFieldWcfLookup")
    # Значение в Поле "Ответственный менеджер подразделения-продавца"
    SALES_MANAGER_IN_ZP = (By.CSS_SELECTOR, ".fldKsupSeller #SPFieldWcfLookup")
    # Значение в Поле "Подразделение-исполнитель"
    EXECUTIVE_UNIT_IN_ZP = (By.CSS_SELECTOR, ".fldKsupDivisionPerformer #SPFieldWcfLookup")
    # Значение в Поле "Ответственный менеджер подразделения-исполнителя"
    EXECUTIVE_MANAGER_IN_ZP = (By.CSS_SELECTOR, ".fldKsupPerformerResponsible #SPFieldWcfLookup")
    # Значение в Поле "Совместные торги"
    JOINT_BIDDING_IN_ZP = (By.CSS_SELECTOR, ".fldKsupPresaleJointBidding  #SPFieldBoolean")
    # Название поля "Заказчик"
    CUSTOMER_FIELD_NAME = (By.CSS_SELECTOR, ".fldKsupEgr_Customer .ms-h3")
    # Значение в Поле "Заказчик"
    CUSTOMER_IN_ZP = (By.CSS_SELECTOR, ".fldKsupEgr_Customer #SPFieldWcfLookup")
    # Значение в Поле "Тип работ и услуг"
    TYPE_OF_WORK_SERVCICES_IN_ZP = (By.CSS_SELECTOR, "#SPFieldTaxonomyFieldTypeMulti")
    # Значение в Поле "Исполнитель (юридическое лицо)"
    EXECUTIVE_UNIT_LEGAL_IN_ZP = (By.CSS_SELECTOR, ".fldKsupEgr_PerformerLegal #SPFieldWcfLookup")
    # Значение в Поле "Начальная (максимальная) цена контракта"
    SUM_IN_ZP = (By.CSS_SELECTOR, ".fldKsupContractSum #SPFieldNumber")
    # Значение в Поле "Валюта договора/контракта"
    CURRENCY_IN_ZP = (By.CSS_SELECTOR, ".fldKsupCurrency #SPFieldChoice")
    # Значение в Поле "Категория проекта" (ценовая)
    PRICE_CATEGORY_IN_ZP = (By.CSS_SELECTOR, ".fldKsupProjectCategoryBySum #SPFieldChoice")
    # Значние в Поле "Порядок проведения закупочной процедуры" для Тендер
    SALE_LAW_TYPE_TENDER_ZP = (By.CSS_SELECTOR, ".fldKsupTenderLowType #SPFieldChoice")
    # Значение в Поле "Порядок проведения закупочной процедуры" для Запрос цен
    SALE_LAW_TYPE_ZAPROS_ZP = (By.CSS_SELECTOR, ".fldKsupRequestLowType #SPFieldChoice")
    # Значение в Поле "Размер обеспечения заявки"
    APPLICATION_SIZE_IN_ZP = (By.CSS_SELECTOR, ".fldKsupApplicationSize #SPFieldNumber")
    # Значение в Поле "Размер обеспечения договора/контракта"
    CONTRACT_SIZE_IN_ZP = (By.CSS_SELECTOR, ".fldKsupContractSize #SPFieldNumber")
    # Значение в Поле "Срок подачи на конкурс"
    COMPETITION_DEAD_LINE_FROM_IN_ZP = (By.CSS_SELECTOR, ".fldKsupCompetitionDeadlineFrom #SPFieldDateTime")
    # Значение в Поле "Срок представления ценовой информации"
    PRICE_INFORMATION_DEAD_LINE_FROM_IN_ZP = (By.CSS_SELECTOR, ".fldKsupPriceInformationDeadlineFrom #SPFieldDateTime")
    # Значение в Поле "Предполагаемая дата начала проведения закупки с"
    PURCHASE_START_DATE_FROM = (By.CSS_SELECTOR, ".fldKsupPurchaseStartDateFrom #SPFieldDateTime")
    # Значение в Поле "Предполагаемая дата начала проведения закупки по"
    PURCHASE_START_DATE_TO = (By.CSS_SELECTOR, ".fldKsupPurchaseStartDateTo #SPFieldDateTime")
    # Значение в Поле "Плановая дата заключения договора/контракта"
    START_DATE_IN_ZP = (By.CSS_SELECTOR, ".fldKsupContractPlanDateFrom #SPFieldDateTime")
    # Значение в Поле "Плановая дата окончания договора/контракта"
    END_DATE_IN_ZP = (By.CSS_SELECTOR, ".fldKsupContractPlanFinishDateFrom #SPFieldDateTime")
    # Значение в Поле "Вероятность заключения договора/контракта"
    PROJECT_PROBABILITY_IN_ZP = (By.CSS_SELECTOR, ".fldKsupContractProbability #SPFieldNumber")
    # Значение в Поле "Номер закупки"
    PURCHASE_NUMBER_IN_ZP = (By.CSS_SELECTOR, ".fldKsupEisPurchaseNumber #SPFieldText")
    # Значение в Поле "Номер запроса цен на Официальном сайте ЕИС"
    EIS_PRICE_NUMBER_IN_ZP = (By.CSS_SELECTOR, ".fldKsupEisPriceNumber #SPFieldText")
    # Значение в Поле "Связанные продажи"
    RELATED_SALES_IN_ZP = (By.CSS_SELECTOR, ".fldKsupSalesWithOp #SPFieldWcfLookup")
    # Значение в Поле "Статус продажи"
    PRESALE_STATUS_IN_ZP = (By.CSS_SELECTOR, ".fldKsupPaSaleStatus #SPFieldChoice")
    # Значение в Поле "Ссылка на закупку"
    PURCHASE_LINK_IN_ZP = (By.CSS_SELECTOR, ".fldKsupEisPurchaseLink #SPFieldNote")
    # Значение в Поле "Результаты работ"
    DESCRIPTION_TEXT_IN_ZP = (By.CSS_SELECTOR, ".fldKsupPaDescription #SPFieldNote")
    # Значение в Поле "Риски проекта с точки зрения Департамента"
    PROJECT_RISKS_DEPARTMENT_IN_ZP = (By.CSS_SELECTOR, ".fldKsupProjectRiskDepartmentPerspec #SPFieldNote")
    # Значение в Поле "Ссылка на запрос на Официальном сайте ЕИС"
    EIS_PRICE_LINK_IN_ZP = (By.CSS_SELECTOR, ".fldKsupEisPriceLink #SPFieldNote")


class FormCreateContractLocators:
    CONTRACT_TITLE = (By.CSS_SELECTOR, "#DeltaPlaceHolderPageTitleInTitleArea .die")
    # Предмет контракта //textarea[starts-with(@id, 'KsupFullName')]
    NAME_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupFullName']")

    # Заказчик
    CUSTOMER_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_Customer")
    CUSTOMER_SEARCH_FIELD = (By.XPATH, "//*[@class='select2-search select2-search--dropdown']//input[@class='select2-search__field']")
    CUSTOMER_DROPDOWN_CONTRACT_ELEMENT = (By.XPATH, f"//li[contains(text(), 'customer_name')]")

    # Подразделение-продавец //li[normalize-space()='salesUnit_name']
    SALES_UNIT_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupDivisions")
    SALES_UNIT_DROPDOWN_CONTRACT_ELEMENT = (By.XPATH, "//*[contains(@id, 'KsupDivisions')]//li[contains(text(), 'salesUnit_name')]")

    # Ответственный менеджер подразделения-продавца
    SALES_MANAGER_CONTRACT_ELEMENT = (By.CSS_SELECTOR, '#div-wcfLookupControl_KsupSeller')
    SALES_MANAGER_CONTRACT_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'salesManager_name')]")
    SALES_MANAGER_ELEMENT_VALUE = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupSeller-container")

    # Подразделение-исполнитель
    EXECUTIVE_UNIT_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupDivisionPerformer")
    EXECUTIVE_UNIT_CONTRACT_DROPDOWN_ELEMENT = (By.XPATH, "//*[contains(@id, 'KsupDivisionPerformer')]//li[contains(text(), 'executiveUnit_name')]")

    # Ответственный менеджер подразделения-исполнителя
    EXECUTIVE_MANAGER_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupPerformerResponsible")
    EXECUTIVE_MANAGER_DROPDOWN_CONTRACT_ELEMENT = (By.XPATH, "//li[contains(text(), 'executiveManager_name')]")
    EXECUTIVE_MANAGER_ELEMENT_VALUE = (By.CSS_SELECTOR, "#select2-wcfLookupControl_KsupPerformerResponsible-container")

    # Исполнитель (юридическое лицо)
    EXECUTIVE_UNIT_LEGAL_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_PerformerLegal")
    EXECUTIVE_UNIT_LEGAL_DROPDOWN_CONTRACT_ELEMENT = (By.XPATH, f"//li[contains(text(), 'executiveUnitLegal_name')]")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    # //div[contains(@id,'KsupWorkServicesTypeMetadata')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_TYPE_AND_SERVICES_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupWorkServicesType']>[class='ms-taxonomy-browser-button']")

    # Строка "Тип работ и услуг"
    # //div[contains(@id,'KsupWorkServicesTypeMetadata') and contains(@class,'ms-taxonomy-writeableregion')]
    # [id^='KsupWorkServicesType'][class^='ms-taxonomy-writeableregion']
    TYPE_WORK_SERVICES_ELEMENT = (By.XPATH, "//div[contains(@id,'KsupWorkServicesTypeMetadata') and contains(@class,'ms-taxonomy-writeableregion')]")

    # Сумма //input[starts-with(@id,'KsupSum')]
    SUM_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupSum']")

    # Валюта //select[starts-with(@id,'KsupCurrency')]
    CURRENCY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupCurrency']")

    # связанная Пресейловые активности
    PRESALE_SELECT = (By.XPATH, "//div[@id='div-wcfLookupControl_KsupSales']")
    PRESALE_SELECT_DROPDOWN = (By.XPATH, "//*[normalize-space(.)='fullName_name']")

    # Связанная закупочная процедура
    ZAKUP_SELECT = (By.XPATH, "//span[@id='select2-wcfLookupControl_KsupPresaleActivity-container']")
    ZAKUP_SELECT_DROPDOWN = (By.XPATH, ".//*[normalize-space(.)='fullName']")

    # Номер договора //input[starts-with(@id,'KsupContractNumber')]
    NUMBER_CONTRACT_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupContractNumber']")

    # Чек-бокс Догвоор не заключается //input[starts-with(@id,'KsupContractIsNetting')]
    CONTRACT_IS_NETTING = (By.CSS_SELECTOR, "[id^='KsupContractIsNetting']")

    # Дата заключения договор/контракта //input[starts-with(@id,'KsupConclusionDate')]
    START_DATE_CONTRACT = (By.CSS_SELECTOR, "[id^='KsupConclusionDate'][class='ms-input']")

    # Дата завершение договор/контракта //input[starts-with(@id,'KsupDateEnd')]
    END_DATE_CONTRACT = (By.CSS_SELECTOR, "[id^='KsupDateEnd'][class='ms-input']")

    # Номер закупки //input[starts-with(@id,'KsupEisPurchaseNumber')]
    EIS_PURCHASE_NUMBER_CONTRACT = (By.CSS_SELECTOR, "[id^='KsupEisPurchaseNumber']")

    # Ссылка на закупку //textarea[starts-with(@id,'KsupOffEisPurchaseLink')]
    EIS_PURCHSE_LINK_CONTRACT = (By.CSS_SELECTOR, "[id^='KsupOffEisPurchaseLink']")

    # Ссылка на договор/контракт на Официальном сайте ЕИС //textarea[starts-with(@id,'KsupEisContractLink')]
    EIS_CONTRACT_LINK = (By.CSS_SELECTOR, "[id^='KsupEisContractLink']")

    # Статус контракта
    CONTRACT_STATUS_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupContractStatus']")

    # Кнопка поиск вариантов у поля "Территория применения"
    # //div[contains(@id,'KsupApplicationTerritory')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_TERRITORY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupApplicationTerritory']>[class='ms-taxonomy-browser-button']")

    # Строка Территория применения
    # //div[contains(@id,'KsupApplicationTerritory') and contains(@class,'ms-taxonomy-writeableregion')]
    TERRITORY_ELEMENT = (By.XPATH, "//div[contains(@id,'KsupApplicationTerritory') and contains(@class,'ms-taxonomy-writeableregion')]")

    # Кнопка поиск вариантов у поля "Технологии"
    # //div[contains(@id,'KsupKeyTechnologies')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_TECHNOLOGIES_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupKeyTechnologies']>[class='ms-taxonomy-browser-button']")

    # Строка Ключевые технологии
    # //div[contains(@id,'KsupKeyTechnologies') and contains(@class,'ms-taxonomy-writeableregion')]
    TECHNOLOGIES_ELEMENT = (By.XPATH, "//div[contains(@id,'KsupKeyTechnologies') and contains(@class,'ms-taxonomy-writeableregion')]")

    # Поле Цели и задачи //textarea[starts-with(@id,'KsupDescriptionPlainText')]
    DESCRIPTION_PLAIN_TEXT_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupDescriptionPlainText']")

    # Количественные показатели реализации проекта //textarea[starts-with(@id,'KsupQuantitativeIndicatorsProjec')]
    QUANTITATIVE_INDICATORS_PROJECT_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupQuantitativeIndicatorsProjec']")

    # Уникальный код проекта //input[starts-with(@id,'KsupContractProjectUniqueCode')]
    PROJECT_UNIQUE_CODE = (By.CSS_SELECTOR, "[id^='KsupContractProjectUniqueCode']")

    # Поле "Связанный проект" //div[@id='div-wcfLookupControl_KsupProject'] #div-wcfLookupControl_KsupProject
    PROJECT_ELEMENT = (By.XPATH, "//*[@id='div-wcfLookupControl_KsupProject']//span[contains(@class,'select2-container')]")
    # //span[contains(@class, 'select2-search')]//input
    PROJECT_FIND_ELEMENT = (By.CSS_SELECTOR, "[class$='select2-search--dropdown']>input")
    # //li[normalize-space(.)='project_name']
    PROJECT_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'project_name')]")

    # Поля Плановых платежей
    SUMTABLE = (By.CSS_SELECTOR, ".payplan-summa-field")
    YEARTABLE = (By.CSS_SELECTOR, ".payplan-year-field")
    QUARTERTABLE = (By.CSS_SELECTOR, ".payplan-cell.table__td select")
    DELETE_ROW_BUTTON = (By.CSS_SELECTOR, "[class*='payplan-cell-delete'][data-member='delete']")

    # поле для вставки файла Контракт //div[@id='File_Contract']/div/input
    FILE_CONTRACT = (By.CSS_SELECTOR, "[id='File_Contract']>div>input")
    FILE_CONTRACT_NAME = (By.CSS_SELECTOR, "[class='fileField_File_Contract_NameLink_']")

    # Бюджет проекта //div[@id='File_BudgetOfProject']/div/input
    FILE_BUDGET_OF_PROJECT = (By.CSS_SELECTOR, "[id='File_BudgetOfProject']>div>input")
    FILE_BUDGET_OF_PROJECT_NAME = (By.CSS_SELECTOR, "[class='fileField_File_BudgetOfProject_NameLink_']")

    # Пояснительная служебная записка //div[@id='File_ExplanatoryMemoranum']/div/input
    FILE_EXPLANATORY_MEMORANUM = (By.CSS_SELECTOR, "[id='File_ExplanatoryMemoranum']>div>input")
    FILE_EXPLANATORY_MEMORANUM_NAME = (By.CSS_SELECTOR, "[class='fileField_File_ExplanatoryMemoranum_NameLink_']")

    # Реестр рисков, Карта рисков //div[@id='File_RiskMapAndRegistry']/div/input
    FILE_RISK_MAP_AND_REGISTERY = (By.CSS_SELECTOR, "[id='File_RiskMapAndRegistry']>div>input")
    FILE_RISK_MAP_AND_REGISTERY_NAME = (By.CSS_SELECTOR, "[class='fileField_File_RiskMapAndRegistry_NameLink_']")

    # Иное //div[@id='File_Other']/div/input
    FILE_OTHER = (By.CSS_SELECTOR, "[id='File_Other']>div>input")
    FILE_OTHER_NAME = (By.CSS_SELECTOR, "[class='fileField_File_Other_NameLink_']")

    # Кнопка создания ДК
    CONFIRM_CONTRACT_BUTTON = (By.CSS_SELECTOR, "[id*='diidIOSaveItem'][value='Создать']")

    # Кнопка сохранения сущности после изменений
    CONFIRM_EDIT_CONTRACT_BUTTON = (By.CSS_SELECTOR, "[id$='ctl00_ctl00_diidIOSaveItem'].ms-ButtonHeightWidth")

    # Кнопка подтверждения внесения правок в Связанный проект
    CONFIRM_CHANGE_PROJECT_BUTTON = (By.XPATH, "//input[@value='OK']")

    # Кнопка "Отмена" в окне подтверждения внесения правок в Связанный проект
    CANCEL_CHANGE_PROJECT_BUTTON = (By.XPATH, "//input[@value='Отмена']")

    # Добавленные договоры/контракты
    # Поле "Заказчик" множественный результат
    JOINT_BIDDING_CUSTOMER = (By.XPATH, "//*[@data-member='customer']//*[contains(@class, 'select2-selection--single')]")
    JOINT_BIDDING_CUSTOMER_DROPDOWN = (By.XPATH, "//li[contains(text(), 'customer_name')]")
    # Поле "Номер" множественный результат
    JOINT_BIDDING_NUMBER = (By.XPATH, "//*[@data-member='number']//input[contains(@class,'number-field')]")

    # Поле "Дата заключения"
    JOINT_BIDDING_START_DATE = (By.XPATH, "//*[@data-member='imprisonmentDate']//input[contains(@class,'imprisonment-date')]")

    # Поле "Дата окончания"
    JOINT_BIDDING_END_DATE = (By.XPATH, "//*[@data-member='expirationDate']//input[contains(@class,'expriration-date')]")

    # Поле "Сумма договора/контракта"
    JOINT_BIDDING_SUMMA = (By.XPATH, "//*[@data-member='summa']//input[contains(@class,'jointbidding-summa')]")

    # Кнопка Удаления строки в табилце "Добавленные договоры контракты"
    JOINT_BIDDING_DELETE_ROW = (By.XPATH, "//td[@data-member='delete' and contains(@class, 'jointbidding-cell-delete')]")


class ContractListLocators:
    CONTRACT_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    FIND_ELEMENT_IN_CONTRACT_LIST = (By.XPATH, f"//a[@class= 'ms-listlink' and contains(text(),'Test_name')]")

    # Вкладки на листе сущности "Договор/контракт"
    ALL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewAll']")
    MINE_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewMy']")
    APPROVAL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewApproval']")
    REJECTED_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewRejected']")
    APPROVED_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewApproved']")

    # Поле "Статус согласования" множественный результат
    APPROVAL_STATUS_VALUES = (By.CSS_SELECTOR, "[class^='colKsupContractApproveStatus ms-cellstyle ms-vb2']")


class ContractElementLocators:
    # Титул в карточке "Пресейловая активность"
    TITLE_IN_CONTRACT = (By.CSS_SELECTOR, "#pageTitle")

    # Кнопки на риббоне SP
    # Отправить на согласование //a[starts-with(@id, 'Approve.ToApprove')]
    SEND_APPROVAL_CONTRACT_CONTRACT = (By.CSS_SELECTOR, "[id^='Approve.ToApprove']")
    CONFIRM_SEND_APPROVAL_CONTRACT = (By.XPATH, "//button[@type = 'button' and (text() = 'Отправить')]")
    CANCEL_SEND_APPROVAL_CONTRACT = (By.XPATH, "//button[@type = 'button' and (text() = 'Отмена')]")
    CONFIRM_REJECT_CONTRACT = (By.XPATH, "//button[@type = 'button' and (text() = 'Отклонить')]")
    CONFIRM_ESCALATE_CONTRACT = (By.XPATH, "//button[@type = 'button' and (text() = 'Эскалировать')]")
    CONFIRM_REVISION_CONTRACT = (By.XPATH, "//button[@type = 'button' and (text() = 'Отправить на доработку')]")

    # Кнопка согласования и отклонения контракта
    APPROVAL_CONTRACT = (By.CSS_SELECTOR, "[id^='Approve.Approve']")
    REJECT_CONTRACT = (By.CSS_SELECTOR, "[id^='Approve.Reject']")
    ESCALATE_CONTRACT = (By.CSS_SELECTOR, "[id^='Approve.Escalate']")
    REVISION_CONTRACT = (By.CSS_SELECTOR, "[id^='Approve.Revision']")

    # Кнопка изменения элемента
    EDIT_ITEM_BUTTON = (By.CSS_SELECTOR, "[id='Ribbon.ListForm.Display.Manage.EditItem-Large']")

    # Вкладка "Общие сведения"
    GENERAL_INFORMATION_ELEMENT = (By.XPATH, "//a[contains(@href, '#tabCommon')]")

    # Элементы на вкладке "Статус Согласования"
    # Вкладка "Статус согласования"
    APPROVAL_HISTORY_CONTRACT_TABS = (By.XPATH, "//a[contains(@href, '#tabApprovingHistory')]")
    # Строка согласование с юридической службой
    APPROVAL_LEGAL_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование юридической службой']/following::span[1]")
    # Строка согласование с бухгалтерией
    APPROVAL_COUNT_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование бухгалтерией']/following::span[1]")
    # Строка согласование с финансовой службой
    APPROVAL_FIN_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование финансовой службой']/following::span[1]")
    # Строка согласование с Директором по разработке ПО
    APPROVAL_UDPRPO_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование Директором по разработке ПО']/following::span[1]")
    # Строка согласование с ККП
    APPROVAL_KKP_STATUS_ELEMENT = (By.XPATH, "//*[text() ='Согласование ККП']/following::span[1]")

    # Вкладка "Заключенные договоры/контракты"
    JOINT_BIDDING_CONTRACT_TABS = (By.CSS_SELECTOR, "a[href='#tabJointBidding']")

    # Элементы внутри окна подтверждения/отклонения //textarea[@id='dialogComment']
    COMMENT_TO_APPROVAL_CONTRACT = (By.CSS_SELECTOR, "[id='dialogComment']")
    # Прикрепление файла  //input[@name='filefield']
    FILE_TO_APPROVAL_CONTRACT = (By.CSS_SELECTOR, "[name='filefield']")
    CONFIRM_APPROVAL_CONTRACT = (By.XPATH, "//button[@type = 'button' and (text() = 'Согласовать')]")
    CANCEL_APPROVAL_CONTRACT = (By.XPATH, "//button[@type = 'button' and (text() = 'Отмена')]")
    ClOSE_ALLERT_CONTRACT = (By.CSS_SELECTOR, "#dlgTitleBtns")
    START_WITH_ELEMENT = (By.CSS_SELECTOR, "#dialogRestartStatus")

    # Элементы на вкладке "Общие сведения"
    # Поле "Статус согласования"
    APPROVAL_MAIN_STATUS_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupContractApproveStatus #SPFieldChoice")
    # Поле "Заказчик"
    CUSTOMER_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupEgr_Customer #SPFieldWcfLookup")
    # Поле "Подразделение-продавец"
    SALES_UNIT_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupDivisions #SPFieldWcfLookup")
    # Поле "Ответственный менеджер подразделения-продавца"
    SALES_MANAGER_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupSeller #SPFieldWcfLookup")
    # Поле "Подразделение-исполнитель"
    EXECUTIVE_UNIT_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupDivisionPerformer #SPFieldWcfLookup")
    # Поле "Ответственный менеджер подразделения-исполнителя"
    EXECUTIVE_MANAGER_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupPerformerResponsible #SPFieldWcfLookup")
    # Поле "Исполнитель (юридическое лицо)"
    EXECUTIVE_UNIT_LEGAL_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupEgr_PerformerLegal #SPFieldWcfLookup")
    # Поле "Тип работ и услуг"
    TYPE_OF_WORK_SERVCICES_IN_CONTRACT = (
        By.CSS_SELECTOR, ".fldKsupWorkServicesTypeMetadata #SPFieldTaxonomyFieldTypeMulti")
    # Поле "Начальная (максимальная) цена контракта"
    SUM_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupSum #SPFieldNumber")
    # Поле "Валюта договора/контракта"
    CURRENCY_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupCurrency #SPFieldChoice")
    # Поле "Категория проекта(ценовая)"
    PRICE_CATEGORY_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupProjectCategoryBySum #SPFieldChoice")
    # Поле "Номер"
    CONTRACT_NUMBER_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupContractNumber #SPFieldText")
    # Поле "Дата заключения договора/контракта"
    START_DATE_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupConclusionDate #SPFieldDateTime")
    # Поле "Дата окончания договора/контракта"
    END_DATE_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupDateEnd #SPFieldDateTime")
    # Поле "Номер закупки"
    PURCHASE_NUMBER_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupEisPurchaseNumber #SPFieldText")
    # Поле "Статус контракта"
    CONTRACT_STATUS = (By.CSS_SELECTOR, ".fldKsupContractStatus #SPFieldChoice")
    # Поле "Пресейловые активности"
    RELATED_PRESALE = (By.CSS_SELECTOR, ".fldKsupSales #SPFieldWcfLookup")
    # Поле "Закупочная процедура"
    RELATED_ZAKUP = (By.CSS_SELECTOR, ".fldKsupPresaleActivity #SPFieldWcfLookup")
    # Поле "Территория применения"
    TERRITORY_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupApplicationTerritory #SPFieldTaxonomyFieldType")
    # Поле "Ключевые технологии"
    TECHNOLOGIES_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupKeyTechnologies #SPFieldTaxonomyFieldTypeMulti")
    # Поле "Уникальный код проекта"
    PROJECT_UNIQUE_CODE_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupContractProjectUniqueCode #SPFieldText")
    # Поле "Связанный проект"
    PROJECT_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupProject #SPFieldWcfLookup")
    # Поле "Ссылка на закупку"
    PURCHASE_LINK_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupOffEisPurchaseLink #SPFieldNote")
    # Поле "Ссылка на договор/контракт на Официальном сайте ЕИС"
    EIS_CONTRACT_LINK_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupEisContractLink #SPFieldNote")
    # Поле "Цели и задачи"
    DESCRIPTION_TEXT_IN_CONTRACT = (By.CSS_SELECTOR, ".fldKsupDescriptionPlainText #SPFieldNote")
    # Поле "Количественные показатели реализации проекта"
    QUANTITATIVE_INDICATORS_PROJECT = (By.CSS_SELECTOR, ".fldKsupQuantitativeIndicatorsProjec #SPFieldNote")

    # Вкладка "Заключенные договоры/контракты"
    # Значнеие в поле "Заказчик" Множественный результат
    JOINT_BIDDING_CUSTOMER_VALUE = (By.CSS_SELECTOR, "[data-member='customer'][class^='jointbidding']")

    # Значение в поле "Номер" Множественный результат
    JOINT_BIDDING_NUMBER_VALUE = (By.CSS_SELECTOR, "[data-member='number'][class^='jointbidding']")

    # Значение в поле "Дата заключения" Множественный результат
    JOINT_BIDDING_START_DATE_VALUE = (By.CSS_SELECTOR, "[data-member='imprisonmentDate'][class^='jointbidding']")

    # Значение в поле "Дата окончания" Множественный результат
    JOINT_BIDDING_END_DATE_VALUE = (By.CSS_SELECTOR, "[data-member=''][class^='jointbidding']")

    # Значение в поле "Дата окончания" Множественный результат
    JOINT_BIDDING_SUM_VALUE = (By.CSS_SELECTOR, "[data-member='summa'][class^='jointbidding']")

    JOINT_BIDDING_TOTAL_SUM_VALUE = (By.CSS_SELECTOR, "[class^='payplan-cell']>span")


class KnowledgeSearchLocators:

    # Локаторы в области "Быстрые фильтры"
    # Элемент "Названия блока фильтра" в быстрых фильтрах (множественный результат)
    ALL_TITLE_IN_FAST_FILTER = (By.CSS_SELECTOR, ".search-filter h3")

    # Шаблон для поиска значения чек-бокса
    TEMPLATE_CHECKBOX = (By.XPATH, "//*[@role = 'checkbox' and (text() = 'name' or . = 'name')]")

    # Кнопка "Сбросить"
    RESET_BUTTON = (By.XPATH, "//*[@type = 'button' and (text() = 'Сбросить' or . = 'Сбросить')]")

    # Кнопка "Весь список" в блоке "Заказчик"
    ALL_LIST_CUSTOMER_BLOCK = (By.XPATH, "//h3[contains(text(), 'Заказчик')]/following::*[1]")

    # Кнопка "Весь список" в блоке "Юр.лицо-исполнитель"
    ALL_LIST_LEGAL_BLOCK = (By.XPATH, "//h3[contains(text(), 'Юр.лицо-исполнитель')]/following::*[1]")

    # Кнопка "Весь список" в блоке "Подразделение-исполнитель"
    ALL_LIST_PERFORMER_BLOCK = (By.XPATH, "//h3[contains(text(), 'Подразделение-исполнитель')]/following::*[1]")

    # Кнопка "Весь список" в блоке "Тип работ и услуг"
    ALL_LIST_TYPEWORKS_BLOCK = (By.XPATH, "//h3[contains(text(), 'Тип работ и услуг')]/following::*[1]")

    # Кнопка "Весь список" в блоке "Технологии"
    ALL_LIST_TECHNOLOGIES_BLOCK = (By.XPATH, "//h3[contains(text(), 'Технологии')]/following::*[1]")

    # Cтрока поиска  в блоке фильтра
    SEARCH_LINE_IN_BLOCK_FILTER = (By.XPATH, "//input[@class = 'options-filter__input']")

    # Поле "Стоимость проекта (руб.) ОТ" в блоке фильтрации
    SUM_FROM = (By.XPATH, "//input[@name='projectSum_number-from']")

    # Поле "Стоимость проекта (руб.) ДО" в блоке фильтрации
    SUM_TO = (By.XPATH, "//input[@name='projectSum_number-to']")

    # Поле "Дата заключения" в блоке фильтрации(множественный резульатат: 2 элемента От И До).
    START_DATE = (By.XPATH, "//div[3]/div/div/div/div/input")

    # Поле "Дата завершения" в блоке фильтрации (множественный резульатат: 2 элемента От И До).
    END_DATE = (By.XPATH, "//div[4]/div/div/div/div/input")



    # Локаторы в строке поиска и около того
    # Строка поиска
    SEARCH_LINE = (By.XPATH, "//input[@name='searchText']")

    # Кнопка очистки строки поиска
    CLEAR_LINE_BUTTON = (By.XPATH, "//*[@class = 'clearable__clear']")

    # Локаторы в области результатов поиска
    # Элемент "Тип сущности" в результатах поиска (множественный результат)
    TYPES_OF_ALL_FOUND_ELEMENT = (By.CSS_SELECTOR, ".search-result__title h6")

    # Элемент "Название сущности" в результатах поиска (множественный результат)
    NAMES_OF_ALL_FOUND_ELEMENT = (By.CSS_SELECTOR, ".search-result__title h2")

    # Значение в поле "Заказчик"
    CUSTOMER_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Заказчик']/following::p[1]")

    # Значение в поле "Подразделение"
    DEPARTMENT_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Подразделение']/following::p[1]")

    # Значение в поле "Технологии"
    TECHNOLOGIES_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Технологии']/following::p[1]")

    # Значение в поле "Исполнитель"
    LEGAL_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Исполнитель']/following::p[1]")

    # Значение в поле "Категория"
    CATEGORY_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Категория']/following::p[1]")

    # Значение в поле "Сумма контракта (руб.)"
    SUM_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Сумма контракта (руб.)']/following::p[1]")

    # Значение в поле "Тип работ и услуг"
    TYPE_WORKS_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Тип работ и услуг']/following::p[1]")

    # Значение в поле "Дата заключения"
    START_DATE_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Дата заключения']/following::p[1]")

    # Значение в поле "Дата завершения"
    END_DATE_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Дата завершения']/following::p[1]")

    # Значение в поле "Номер контракта"
    CONTRACT_NUMBER_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Номер контракта']/following::p[1]")

    # Значение в поле "Отрасль"
    INDUSTRY_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='Отрасль']/following::p[1]")

    # Значение в поле "ОГРН"
    OGRN_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='ОГРН']/following::p[1]")

    # Значение в поле "ИНН"
    INN_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='ИНН']/following::p[1]")

    # Значение в поле "КПП"
    KPP_VALUE_IN_RESULT = (By.XPATH, "//*[text() ='КПП']/following::p[1]")

    # Кнопка "загрузить еще" в результатах поиска
    LOAD_MORE_BUTTON = (By.XPATH, "//a[contains(text(),'Загрузить еще')]")

    # Надпись "Конец поисковой выдачи" в результатах поиска
    END_LOAD_BUTTON = (By.XPATH, "//a[contains(text(),'Конец поисковой выдачи')]")

    NOT_FOUND_RESULT = (By.XPATH, "//a[contains(text(),'Результаты не найдены')]")


class ProjectListLocators:
    PROJECT_CREATE_BUTTON = (By.CSS_SELECTOR, "#QCB1_Button1")
    FIND_ELEMENT_IN_PROJECT_LIST = (By.XPATH, f"//a[contains(text(),'Test_name')]")

    # Вкладки на листе сущности "Договор/контракт"
    ALL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewAll']")
    WAITING_INTEREST_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewMarketingWaitingInformation']")
    INTERESTED_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewMarketingInterested']")
    NOT_INTERESTED_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewMarketingNotInterested']")
    WAITING_INFORM_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewMarketingWaitingInformation']")
    INFORMATION_ENOUGH_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewInformationEnough']")
    INFORMATION_NOT_ENOUGH_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewInformationNotEnough']")


class FormCreateProjectLocators:
    # Название проекта //textarea[starts-with(@id, 'KsupProjectFullName')]
    NAME_PROJECT_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupProjectFullName']")

    # Ссылка на закупку на Официальном сайте ЕИС //textarea[starts-with(@id, 'KsupLinkPurchase')]
    EIS_PURCHSE_LINK_CONTRACT = (By.CSS_SELECTOR, "[id^='KsupLinkPurchase']")

    # Заказчик //div[@id='div-wcfLookupControl_KsupEgr_Customers']/span/span/span
    CUSTOMER_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_Customers")
    CUSTOMER_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='select2-search__field']")
    CUSTOMER_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'customer_name')]")

    # Кнопка "Поиск допустимого варианта" у поля "Отрасль"
    # //div[contains(@id,'KsupIndustry')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_INDUSTRY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupIndustry']>[class='ms-taxonomy-browser-button']")

    # Кнопка поиск допустимого варианта в категории "Тип работ и услуг"
    # //div[contains(@id,'KsupWorkServicesType')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_TYPE_AND_SERVICES_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupWorkServicesType']>[class='ms-taxonomy-browser-button']")
    # Строка "Тип работ и услуг"
    TYPE_WORK_SERVICES_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupWorkServicesType'][class*='ms-taxonomy-writeableregion']")

    # Исполнитель (юридическое лицо) //div[@id='div-wcfLookupControl_KsupEgr_PerformerLegal']/span/span/span
    EXECUTIVE_UNIT_LEGAL_PROJECT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_PerformerLegal")
    EXECUTIVE_UNIT_LEGAL_DROPDOWN_PROJECT_ELEMENT = (By.XPATH, "//li[contains(text(), 'executiveUnitLegal_name')]")

    # Подразделение-исполнитель //div[@id='div-wcfLookupControl_KsupPerformerDivision']/span/span/span
    EXECUTIVE_UNIT_PROJECT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupPerformerDivision")
    # //li[normalize-space(.)='executiveUnit_name']
    EXECUTIVE_UNIT_PROJECT_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'executiveUnit_name')]")

    # Cоисполнители //div[@id='div-wcfLookupControl_KsupPerformerDivisions']/span/span/span
    SALES_UNIT_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupPerformerDivisions")
    # //li[normalize-space(.)='salesUnit_name']
    SALES_UNIT_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'salesUnit_name')]")

    # Стадия проекта //select[starts-with(@id, 'KsupProjectStage')]
    PROJECT_STAGE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupProjectStage']")

    # Связанный договор/контракт //div[@id='div-wcfLookupControl_KsupContracts']/span/span/span
    CONTRACTS_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupContracts")
    CONTRACTS_DROPDOWN_ELEMENT = (By.XPATH, "//li[normalize-space(.)='contract_name']")

    # Срок начала //input[starts-with(@id, 'KsupStartDatePlan')]
    START_DATE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupStartDatePlan'][class='ms-input']")

    # Кнопка "Поиск допустимого варианта" у поля "Вендоры"
    # //div[contains(@id,'KsupVendors')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_VENDORS_BUTTON = (By.CSS_SELECTOR, "[id^='KsupVendors']>[class='ms-taxonomy-browser-button']")

    # Кнопка "Поиск допустимого варианта" у поля "Теги"
    # //div[contains(@id,'KsupTag')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_TAGS_BUTTON = (By.CSS_SELECTOR, "[id^='KsupTag']>[class='ms-taxonomy-browser-button']")

    # Менеджеры проекта //div[@id='div-wcfLookupControl_KsupSellers']/span/span/span
    SALES_MANAGER_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupSellers")
    # //li[normalize-space(.)='manager_name']
    SALES_MANAGER_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'manager_name')]")

    # Контактное лицо от ЛАНИТ #KsupRpLanit_c9f28b10-e6a1-4b8e-b4b0-f5dc0565045e_\$ClientPeoplePicker_EditorInput
    RP_LANIT_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupRpLanit'][class*='editorInput']")
    RP_LANIT_DROPDOWN_ELEMENT = (By.XPATH, "//*[(text() = 'name' or . = 'name')]")

    # Дата реализации //input[starts-with(@id, 'KsupDuePlan')]
    END_DATE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupDuePlan'][class='ms-input']")

    # Сумма по всем договорам/контрактам //select[starts-with(@id, 'KsupPrice')]
    SUM_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupPrice']")

    # Кнопка поиск вариантов у поля "Территория применения"
    # //div[contains(@id,'KsupApplicationTerritory')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_TERRITORY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupApplicationTerritory']>[class='ms-taxonomy-browser-button']")

    # Строка Территория применения
    # //div[contains(@id,'KsupApplicationTerritory') and contains(@class,'ms-taxonomy-writeableregion')]
    TYPE_TERRITORY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupApplicationTerritory'][class*='ms-taxonomy-writeableregion']")

    # Кнопка поиск вариантов у поля "Технологии"
    # //div[contains(@id,'KsupTechnology')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_TECHNOLOGIES_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupTechnology']>[class='ms-taxonomy-browser-button']")

    # Строка Ключевые технологии
    # //div[contains(@id,'KsupTechnology') and contains(@class,'ms-taxonomy-writeableregion')]
    TYPE_TECHNOLOGIES_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupTechnology'][class*='ms-taxonomy-writeableregion']")

    # Категория //select[starts-with(@id, 'KsupProjectCategory')]
    PROJECT_CATEGORY_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupProjectCategory']")

    # Цели и задачи //textarea[starts-with(@id, 'KsupServices')]
    DESCRIPTION_TEXT_ELEMENT = (By.CSS_SELECTOR, "textarea[id^='KsupServices']")

    # Ожидаемые результаты проекта //textarea[starts-with(@id, 'KsupProjectResult')]
    PROJECT_RESULT_ELEMENT = (By.CSS_SELECTOR, "textarea[id^='KsupProjectResult']")

    # Информация о заинтересованности //textarea[starts-with(@id, 'KsupInterestInformation')]
    INTEREST_INFORMATION_ELEMENT = (By.CSS_SELECTOR, "textarea[id^='KsupInterestInformation']")

    # Описание //textarea[starts-with(@id, 'KsupDescription')]
    DESCRIPTION_ELEMENT = (By.CSS_SELECTOR, "textarea[id^='KsupDescription']")

    # Кнопка "Сохранить"(создать проект) //*[@type = 'submit' and @value = 'Сохранить']
    CONFIRM_PROJECT_BUTTON = (By.CSS_SELECTOR, "[id$='RptControls_btnOK']")

    # Титул на странице "Мы работаем над этим"
    CREATE_WAITING_TITLE = (By.XPATH, "//h1[contains(text(), 'Мы работаем над этим...')]")


class ProjectElementLocators:
    TITLE_VALUE = (By.CSS_SELECTOR, ".title.title--main")

    SLIDE_CONTENT_ELEMENT = (By.CSS_SELECTOR, ".slide-content__toggler")

    # Значение в поле "Заказчик"
    CUSTOMER_VALUE = (By.CSS_SELECTOR, ".fldKsupEgr_Customers #SPFieldWcfLookup")

    # Значение в поле "Отрасль"
    INDUSTRY_VALUE = (By.CSS_SELECTOR, ".fldKsupIndustry #SPFieldTaxonomyFieldTypeMulti")

    # Значение в поле "Тип работ и услуг"
    WORK_SERVICES_TYPE_VALUE = (By.CSS_SELECTOR, ".fldKsupWorkServicesTypeMetadata #SPFieldTaxonomyFieldTypeMulti")

    # Значение в поле "Исполнитель основной"
    PERFOMER_DIVISION_VALUE = (By.CSS_SELECTOR, ".fldKsupPerformerDivision #SPFieldWcfLookup")

    # Значение в поле "Стадия проекта"
    PROJECT_STAGE_VALUE = (By.CSS_SELECTOR, ".fldKsupProjectStage #SPFieldChoice")

    # Значение в поле "Контактное лицо от ЛАНИТ"
    RP_LANIT_VALUE = (By.CSS_SELECTOR, ".fldKsupRpLanit #SPFieldUser")

    # Значение в поле "Территория применения"
    TERRITORY_VALUE = (By.CSS_SELECTOR, ".fldKsupApplicationTerritory #SPFieldTaxonomyFieldType")

    # Значение в поле "Технологии"
    TECHNOLOGIES_VALUE = (By.CSS_SELECTOR, ".fldKsupTechnology #SPFieldTaxonomyFieldTypeMulti")

    # Значение в поле "Исполнитель (юридическое лицо)"
    PERFORMER_LEGAL_VALUE = (By.CSS_SELECTOR, ".fldKsupEgr_PerformerLegal #SPFieldWcfLookup")

    # Значение в поле "Соисполнители"
    PERFOMER_DIVISIONS_VALUE = (By.CSS_SELECTOR, ".fldKsupPerformerDivisions #SPFieldWcfLookup")

    # Значение в поле "Связанные договоры/контракты"
    CONTRACTS_VALUE = (By.CSS_SELECTOR, ".fldKsupContracts #SPFieldWcfLookup")

    # Значение в поле "Срок начала"
    START_DATE_VALUE = (By.CSS_SELECTOR, ".fldKsupStartDatePlan #SPFieldDateTime")

    # Значение в поле "Вендоры"
    VENDORS_VALUE = (By.CSS_SELECTOR, ".fldKsupVendors #SPFieldTaxonomyFieldType")

    # Значение в поле "Теги"
    TAGS_VALUE = (By.CSS_SELECTOR, ".fldKsupTag  #SPFieldTaxonomyFieldType")

    # Значение в поле "Менеджеры проекта"
    MANAGERS_PROJECT_VALUE = (By.CSS_SELECTOR, ".fldKsupSellers #SPFieldWcfLookup")

    # Значение в поле "Дата реализации"
    END_DATE_VALUE = (By.CSS_SELECTOR, ".fldKsupDuePlan #SPFieldDateTime")

    # Значение в поле "Сумма по всем договорам/контрактам"
    SUM_VALUE = (By.CSS_SELECTOR, ".fldKsupPrice_x0421_ategory #SPFieldChoice")

    # Значение в поле "Категория"
    PROJECT_CATEGORY_VALUE = (By.CSS_SELECTOR, ".fldKsupProjectCategory #SPFieldChoice")

    # Значение в поле "Цели и задачи"
    SERVICES_VALUE = (By.CSS_SELECTOR, ".fldKsupServices #SPFieldNote")

    # Значение в поле "Ожидаемые результаты проекта"
    PROJECT_RESULT_VALUE = (By.CSS_SELECTOR, ".fldKsupProjectResult #SPFieldNote")

    # Значение в поле "Информация о заинтересованности"
    INTEREST_INFORMATION_VALUE = (By.CSS_SELECTOR, ".fldKsupInterestInformation #SPFieldNote")

    # Значение в поле "Описание"
    DESCRIPTION_VALUE = (By.CSS_SELECTOR, ".fldKsupDescription #SPFieldNote")


class OpListLocators:
    OPERPLAN_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    CREATE_IFRAME = (By.CSS_SELECTOR, "[id^='DlgFrame']")
    YEAR_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupYear']")
    CONFIRM_CREATE_OPERPLAN = (By.CSS_SELECTOR, "[id$='ctl00_ctl00_diidIOSaveItem']")
    CANCEL_CREATE_OPERPLAN = (By.CSS_SELECTOR, "[id$='ctl01_ctl00_diidIOGoBack']")
    CREATE_WAITING_TITLE = (By.XPATH, "//h2[contains(text(), 'Пожалуйста, подождите')]")

    FIND_ELEMENT_IN_OPERPLAN_LIST = (By.XPATH, f"//a[contains(text(),'Test_name')]")

    YEAR_DROPDOWN_FILTER = (By.XPATH, "//*[contains(@class, 'colKsupYear ms-vh2')]//a[@class='ms-headerSortArrowLink']")
    YEAR_CLEAR_FILTER = (By.CSS_SELECTOR, "[id='fmi_clr']")
    YEAR_CLOSE_FILTER = (By.CSS_SELECTOR, "[id='fmi_cls']")


class OpElementLocators:
    ROW_ELEMENT_IN_OPERPLAN = (By.XPATH, "//*[contains(text(), 'fullName')]/ancestor::tr[contains(@class, 'ms-itmHoverEnabled ms-itmhover')]")
    ALL_FIELD_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>td")
    CUSTOMER_VALUE_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupEgr_Customer']")
    EXECUTIVE_UNIT_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupDepartment']>a")
    START_DATE_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupDateStart']")
    END_DATE_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupDateEnd']")
    SUM_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupSumYear']")
    PROBABILITY_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupProjectProbability']")
    SUM_PROBABILITY_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupSumProbabilityYear']")
    CONTRACT_NUMBER_IN_ROW = (By.CSS_SELECTOR, "[id='idElementInOpp']>[class^='colKsupContractNumber']")

    # Отправить на согласование
    SEND_TO_APPROVAL = (By.CSS_SELECTOR, "a[id*='OpPlanApprovalButtonsGroup']")

    # Обновить оперплан
    UPDATE_OPERPLAN_BUTTON = (By.CSS_SELECTOR, "a[id*='OpPlanRefreshButtonsGroup']")

    # Ожидание поиск обновленных элементов
    FIND_UPDATED_ELEMENT = (By.XPATH, "//p[contains(text(), 'Выполняется загрузка...')]")

    # Выбрать все элементы в обновлении(множественный результат)
    ADD_ALL_ELEMENT = (By.CSS_SELECTOR, "[class='checkbox checkbox--light']")
    # Элементы в окне обновления НОВЫЕ ЭЛЕМЕНТЫ
    CHECKBOX_NEW_ELEMENT_IN_UPDATE = (By.XPATH, "//span[contains(text(), 'fullName')]/preceding::label[1]")
    CUSTOMER_NEW_ELEMENT_IN_UPDATE = (By.XPATH, "//span[contains(text(), 'fullName')]/following::td[1]")
    PROBABILITY_NEW_ELEMENT_IN_UPDATE = (By.XPATH, "//span[contains(text(), 'fullName')]/following::td[2]")
    SUM_NEW_ELEMENT_IN_UPDATE = (By.XPATH, "//*[contains(text(), 'fullName')]/following::td[3]/div")
    SUM_YEAR_NEW_ELEMENT_IN_UPDATE = (By.XPATH, "//*[contains(text(), 'fullName')]/following::td[4]/div")
    SUM_WITH_PROBABILITY_NEW_ELEMNT_IN_UPDATE = (By.XPATH, "//*[contains(text(), 'fullName')]/following::td[5]/div")
    CREATOR_NEW_ELEMENT_IN_UPDATE = (By.XPATH, "//*[contains(text(), 'fullName')]/following::td[6]/div/p")

    OLD_STATUS_CONTRACT_UPDATE_ELEMENT = (By.XPATH,
                                          "//span[contains(text(), 'statusContract')]/../following::td[contains(text(), 'Статус контракта')]/following::td[1]")
    NEW_STATUS_CONTRACT_UPDATE_ELEMENT = (By.XPATH,
                                          "//span[contains(text(), 'statusContract')]/../following::td[contains(text(), 'Статус контракта')]/following::td[2]")

    CANCEL_BUTTON = (By.CSS_SELECTOR, "[class='btn btn--bordered']")
    CONFIRM_UPDATE_OPERPLAN = (By.CSS_SELECTOR, "[class='btn']")


class CustomerListLocators:
    CUSTOMER_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")
    FIND_ELEMENT_IN_CUSTOMER_LIST = (By.XPATH, f"//a[@class= 'ms-listlink' and contains(text(),'Test_name')]")

    # Вкладки на листе сущности "Заказчики и исполнители"
    ALL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewAll']")
    GK_LANIT_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewlanit']")
    IP_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewip']")
    UL_ELEMENTS_TAB = (By.CSS_SELECTOR, "a[class^='viewul']")


class FormCreateCustomerLocators:
    # Титул в карточке "Пресейловая активность"
    TITLE_IN_CUSTOMER_FORM = (By.CSS_SELECTOR, "#pageTitle")

    OGRN_ELEMENT = (By.CSS_SELECTOR, "[aria-labelledby*='selectEgrulViewOgrnSelect']")
    SEARCH_OGRN_ELEMENT = (By.CSS_SELECTOR, "input[class='select2-search__field']")
    OGRN_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'customer_ogrn')]")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "[value='OK']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "[value='Закрыть']")

    # Поле "Полное наименование *"(только у ЮР.лица)
    FULL_NAME_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_FullName']")

    # Поле "ФИО" (только для ИП)
    FIO_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Fio']")

    # Поле "Название"
    TITLE_NAME_FIELD = (By.CSS_SELECTOR, "[id^='Title']")

    # Поле "ОГРН/ОГРНИП"
    OGRN_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Ogrn']")

    # Поле "ИНН"
    INN_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Inn']")

    # Поле "ККП" (только у ЮР.лица)
    KKP_FIELD =(By.CSS_SELECTOR, "[id^='KsupEgr_Kpp']")

    # Поле "Адрес" (только у ЮР.лица)
    ADDRESS_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Address']")

    # Поле "Дата ликвидации" (только у ЮР.лица)
    LIQUIDATION_DATE_FIELD = (By.CSS_SELECTOR, "input[id^='KsupEgr_LiquidationDate']")

    # Кнопка "Поиск допустимого варианта" у поля "Отрасль"
    # //div[contains(@id,'KsupEgr_Industry')]/img[@class='ms-taxonomy-browser-button']
    SEARCH_INDUSTRY_BUTTON = (By.CSS_SELECTOR, "[id^='KsupEgr_Industry']>[class='ms-taxonomy-browser-button']")
    INDUSTRY_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Industry']>[class='valid-text']")

    # Поле "Значимость"
    SIGNIFICANCE_ELEMENT = (By.CSS_SELECTOR, "[id^='KsupEgr_Significance']")

    # Поле "Описание"
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Description']")

    # Поле "Контактные лица"
    CONTACT_PERSONS_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_ContactPersons']")

    # Поле "Конкуренты ЛАНИТ"
    COMPETITORS_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Competitors']")

    # Поле "Сайт"
    SITE_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_Site']")

    # Поле "Статус Взаимодействия"
    INTERACTION_STATUS_FIELD = (By.CSS_SELECTOR, "[id^='KsupEgr_InteractionStatus']")

    # Поле "Дирекция, ответственная за взаимодействие" (отображено только под Admin)
    DIRECTION_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_Direction")
    DIRECTION_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='select2-search__field']")
    DIRECTION_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'direction_name')]")

    # Поле "Департаменты, ответственные за взаимодействие" (отображено только под Admin)
    DIVISION_ELEMENT = (By.CSS_SELECTOR, "#div-wcfLookupControl_KsupEgr_Divisions")
    DIVISION_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='select2-search__field']")
    DIVISION_DROPDOWN_ELEMENT = (By.XPATH, "//li[contains(text(), 'division_name')]")

    # Чек-бокс "ГК ЛАНИТ" (отображено только под Admin)
    IS_LANIT_CHECKBOX = (By.CSS_SELECTOR, "[id^='KsupEgr_IsLanit']")

    # Поле "Руководители" (отображено только под Admin)
    CUSTOMER_HEAD_FIELD = (By.CSS_SELECTOR, "input[id^='KsupEgrHead_EgrulHead'][class*='editorInput']")
    CUSTOMER_HEAD_DROPDOWN_ELEMENT = (By.XPATH, "//a[@class='ms-core-menu-link']//div[contains(text(), 'name')]")

    # Чек-бокс "Уведомлять руководителя" (отображено только под Admin)
    SHOULD_NOTIFY_CHECKBOX = (By.CSS_SELECTOR, "[id^='KsupEgrHead_ShouldNotify']")

    # Поле "Уведомлять о"
    NOTIFY_ABOUT_FIELD =(By.CSS_SELECTOR, "[class^='fldKsupEgrHead_NotifyAbout']")
    # Чек-боксы в блоке "Уведомлять о" (отображено только под Admin)
    NOTIFY_ABOUT_CHECKBOX = (By.XPATH, "//*[contains(@for, 'KsupEgrHead_NotifyAbout') and normalize-space(.)= 'name']")

    # Кнопка создания
    CONFIRM_CREATE_BUTTON = (By.XPATH, "//*[contains(@id, 'diidIOSaveItem') and @value='Создать']")
