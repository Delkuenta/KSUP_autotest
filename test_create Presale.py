import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Login_Seller = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_windows/default.aspx?ReturnUrl=%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F%255Fwindows%252Fdefault%252Easpx&Source=%2f_windows%2fdefault.aspx"
name_presale = "тест_ПА_тендер_самостПрод_катА"
Divisions = "ОНЛАНТА"
DivisionPerformer = "ОНЛАНТА"
PerformerResponsible = "Бравосов Андрей Игоревич"
type_presale = "Тендерная заявка"
SaleLawType = "44-ФЗ"
Currency = "Доллар"
Sum = 52000000
ApplicationSize = "1000"
ContractSize = "2000"
SeparateSale = "Да"
CompetitionDeadlineFrom = "15.07.2020"
PlanDateContractConclusion = "1.07.2020"
PlanDateContractFinish = "30.12.2020"
ProjectProbability = "100"
DescriptionPlainText = "Краткое описание текст"
yeartable = 2020
quarter1 = "1 квартал"
quarter2 = "2 квартал"
quarter3 = "3 квартал"
quarter4 = "4 квартал"

def test_create_presale(browser):
    wait = WebDriverWait(browser, 10)
    browser.get(Login_Seller)
    browser.implicitly_wait(20)
    # Переход на страницу пресейловых активностей
    # Ищем кнопку "Cоздать" на вкладке Пресейловые активности
    time.sleep(2)
    button_create_presale = browser.find_element(By.XPATH, "//a[@id='idHomePageNewItem']")
    button_create_presale.click()
    # Ждем загрузки страницы по последнему загружаемому объекту

    wait.until(EC.text_to_be_present_in_element((By.ID, 'select2-wcfLookupControl_KsupSeller-container'),
                                                f'{PerformerResponsible}'))

    # Ищем поле "Предмет контракта" и заполняем
    name_presale_element = browser.find_element(By.CSS_SELECTOR,
                                                "#KsupFullName_1cb78896-92f2-4cb9-a3ad-b45e0f9932a6_\$TextField")
    name_presale_element.send_keys(name_presale)

    # Ищем поле "Способ определения поставщика" и выбираем значение
    type_presale_element = Select(
        browser.find_element(By.ID, "KsupContractorType_c208b1d8-b8f1-417e-83de-32d7be2864be_$DropDownChoice"))
    type_presale_element.select_by_value(type_presale)

    # Ищем поле "Заказчик" и выбираем значение
    browser.find_element(By.XPATH, "//div[@id='div-wcfLookupControl_KsupEgr_Customer']/span/span/span").click()
    # Costumer = browser.find_element_by_xpath('//li[text()="КАЗНАЧЕЙСТВО РОССИИ"]').click
    browser.find_element(By.XPATH, "//li[contains(text(), 'ООО \"ДЕКОР\"')]").click()

    # Ищем поле "Подразделение-продавец" и выбираем значение
    browser.find_element(By.ID, "div-wcfLookupControl_KsupDivisions").click()
    browser.find_element(By.XPATH, f"//li[normalize-space(.)='{Divisions}']").click()

    # Ищем поле "подразделение-продавец" и выбираем значение
    browser.find_element(By.ID, "div-wcfLookupControl_KsupDivisionPerformer").click()
    browser.find_element(By.XPATH, f"//li[normalize-space(.)='{DivisionPerformer}']").click()

    # Ищем поле "Ответственный менеджер подразделения-исполнителя" и выбираем значение
    browser.find_element(By.ID, "div-wcfLookupControl_KsupPerformerResponsible").click()
    browser.find_element(By.XPATH, f"//li[normalize-space(.)='{PerformerResponsible}']").click()

    # Ищем поле "Исполнитель (юридическое лицо)" и выбираем значение
    browser.find_element(By.ID, "div-wcfLookupControl_KsupEgr_PerformerLegal").click()
    browser.find_element(By.XPATH, "//li[contains(text(), 'ООО \"ОНЛАНТА\"')]").click()

    # Ищем поле "Порядок проведения закупочной процедуры" и выбираем значение из выпадающего списка
    SaleLawType_element = Select(
        browser.find_element(By.ID, "KsupSaleLawType_59c9adb5-ad0e-4308-b136-1f1006e5f9f6_$DropDownChoice"))
    SaleLawType_element.select_by_value(SaleLawType)

    # Ищем кнопку "Тип работ и услуг"
    browser.find_element(By.CLASS_NAME, "ms-taxonomy-browser-button").click()
    time.sleep(2)

    # Работаем во фреймворке и выбираем категории
    frame_category = browser.switch_to_active_element()
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_category))
    browser.find_element(By.ID, "TIE_6").click()
    browser.find_element(By.ID, "LBL_33").click()
    browser.find_element(By.ID,
                         "ctl00_PlaceHolderDialogBodySection_PlaceHolderDialogBodyFooterMainSection_AddToFieldEditor").click()
    browser.find_element(By.ID, "ctl00_OkButton").click()
    # Возврат к форм создания.
    browser.switch_to_default_content()
    time.sleep(1)

    # Ищем поле "Сумма" и вводим значение
    sum_element = browser.find_element(By.ID, "KsupSumPlan_9901571e-b38b-42cf-bb3c-f8f7977f1555_$NumberField")
    sum_element.send_keys(Sum)

    # Ищем поле "Валюта" и выбираем значение
    Currency_element = Select(browser.find_element(By.ID,
                                                   "KsupCurrency_9cb5cce6-1d98-4146-a2df-c05c4635dd8d_$DropDownChoice"))
    Currency_element.select_by_value(Currency)

    # Ищем поле "Размер обеспечения заявки" и вводим значение
    ApplicationSize_element = browser.find_element(By.ID,
                                                   "KsupApplicationSize_1117d974-3a17-4f6f-9104-8cf28be18914_$NumberField")
    ApplicationSize_element.send_keys(ApplicationSize)

    ContractSize_element = browser.find_element(By.ID,
                                                "KsupContractSize_20253d6d-468d-443e-9179-3f20e0c2533e_$NumberField")
    ContractSize_element.send_keys(ContractSize)

    # Ищем поле "Самостоятельная продажа" и выбираем значение
    SeparateSale_element = Select(browser.find_element(By.ID,
                                                       "KsupSeparateSale_bf818721-7daf-4db6-b7b9-54ba73429ea5_$DropDownChoice"))
    SeparateSale_element.select_by_value(SeparateSale)

    # Ищем поле "Плановый срок подачи на конкурс" и вводим значение
    CompetitionDeadlineFrom_element = browser.find_element(By.ID,
                                                           "KsupCompetitionDeadlineFrom_5b28696f-6ae9-4765-bb8d-b26513cd0e78_$DateTimeFieldDate")
    CompetitionDeadlineFrom_element.send_keys(CompetitionDeadlineFrom)

    # Ищем поле "Плановая дата заключения договора/контракта" и вводим значение
    PlanDateContractConclusion_element = browser.find_element(By.ID,
                                                              "KsupPlanDateContractConclusion_536f5d8c-9e22-4878-9d4c-49c433c82c0d_$DateTimeFieldDate")
    PlanDateContractConclusion_element.send_keys(PlanDateContractConclusion)

    # Ищем поле "Плановая дата окончания договора/контракта" и вводим значение
    PlanDateContractFinish_element = browser.find_element(By.ID,
                                                          "KsupPlanDateContractFinish_aaf043ca-d88d-4e99-bcfe-7c15cbb8ba33_$DateTimeFieldDate")
    PlanDateContractFinish_element.send_keys(PlanDateContractFinish)

    # Ищем поле "Вероятность заключения договора/контракта" и вводим значение
    ProjectProbability_element = browser.find_element(By.ID,
                                                      "KsupProjectProbability_5bded577-c24a-41f7-ae50-0b1b234d8c21_$NumberField")
    ProjectProbability_element.send_keys(ProjectProbability)

    # Ищем поле "Краткое описание" и вводим значение
    DescriptionPlainText_element = browser.find_element(By.ID,
                                                        "KsupDescriptionPlainText_18b11f3d-f4ae-4a8f-ba29-62366bd13e66_$TextField")
    DescriptionPlainText_element.send_keys("Краткое описание текст")

    # Ищем поле "Риски" и вводим значение
    Risks = browser.find_element(By.ID, "KsupRisks_32ca3c22-b19a-430b-8a16-dbe340b6867a_$TextField")
    Risks.send_keys("Текст_риски_тест")

    # Заполнение таблицы Плановых платежей 1 строка
    sumtable1_element = browser.find_element(By.XPATH, "//tr[3]/td[2]/input")
    sumtable1_element.send_keys(int(Sum/2))

    yeartable1_element = browser.find_element(By.XPATH, "//td[4]/input")
    yeartable1_element.send_keys(yeartable)

    quartertable1_element = Select(browser.find_element(By.XPATH, "//td[5]/select"))
    quartertable1_element.select_by_visible_text(quarter3)

    # Заполнение таблицы плановых платежей 2 строка
    sumtable2_element = browser.find_element(By.XPATH, "//tr[4]/td[2]/input")
    sumtable2_element.send_keys(int(Sum/2))

    yeartable2_element = browser.find_element(By.XPATH, "//tr[4]/td[4]/input")
    yeartable2_element.send_keys(yeartable)

    quartertable2_element = Select(browser.find_element(By.XPATH, "//tr[4]/td[5]/select"))
    quartertable2_element.select_by_visible_text(quarter4)

    confirm_presale_button = browser.find_element(By.ID,
        "ctl00_ctl69_g_9d59c0d2_6296_467d_9f94_a040ee8d543e_ctl00_toolBarTbl_RightRptControls_ctl00_ctl00_diidIOSaveItem")
    confirm_presale_button.click()

    # Проверка наличия названия сущности в списке Пресейлов
    find_create_presale = browser.find_element_by_css_selector(
                                                ".ms-listviewtable>tbody:nth-child(4)>tr:nth-child(1)>td:nth-child(2)")
    find_create_presale = find_create_presale.text

    assert find_create_presale == name_presale, "Сущность не создана, не найдено такое название"

    time.sleep(20)
