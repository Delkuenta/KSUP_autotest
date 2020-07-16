import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json

Login_Seller = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_windows/default.aspx?ReturnUrl=%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F%255Fwindows%252Fdefault%252Easpx&Source=%2f_windows%2fdefault.aspx"


def test_create_presale(browser):
    wait = WebDriverWait(browser, 10)
    browser.get(Login_Seller)
    browser.implicitly_wait(10)
    # Переход на страницу пресейловых активностей
    # Ищем кнопку "Cоздать" на вкладке Пресейловые активности
    time.sleep(2)
    button_create_presale = browser.find_element_by_xpath("//a[@id='idHomePageNewItem']")
    button_create_presale.click()
    # Ждем загрузки страницы по последнему загружаемому объекту

    wait.until(EC.text_to_be_present_in_element((By.ID, 'select2-wcfLookupControl_KsupSeller-container'),
                                                'Бравосов Андрей Игоревич'))

    # Ищем поле "Предмет контракта" и заполняем
    name_presale = browser.find_element_by_css_selector(
        "#KsupFullName_1cb78896-92f2-4cb9-a3ad-b45e0f9932a6_\$TextField")
    name_presale.send_keys("тест_ПА_тендер_самостПрод_катА")

    # Ищем поле "Способ определения поставщика" и выбираем значение
    type_presale = Select(
        browser.find_element_by_id("KsupContractorType_c208b1d8-b8f1-417e-83de-32d7be2864be_$DropDownChoice"))
    type_presale.select_by_value("Тендерная заявка")

    # Ищем поле "Заказчик" и выбираем значение
    browser.find_element_by_xpath("//div[@id='div-wcfLookupControl_KsupEgr_Customer']/span/span/span").click()
    # Costumer = browser.find_element_by_xpath('//li[text()="КАЗНАЧЕЙСТВО РОССИИ"]').click
    browser.find_element_by_xpath("//li[contains(text(), 'ООО \"ДЕКОР\"')]").click()

    # Ищем поле "Подразделение-продавец" и выбираем значение
    browser.find_element_by_id("div-wcfLookupControl_KsupDivisions").click()
    browser.find_element_by_xpath("//li[normalize-space(.)='ОНЛАНТА']").click()

    #Ищем поле "подразделение-продавец" и выбираем значение
    browser.find_element_by_id("div-wcfLookupControl_KsupDivisionPerformer").click()
    browser.find_element_by_xpath("//li[normalize-space(.)='ОНЛАНТА']").click()

    #Ищем поле "Ответственный менеджер подразделения-исполнителя" и выбираем значение
    browser.find_element_by_id("div-wcfLookupControl_KsupPerformerResponsible").click()
    browser.find_element_by_xpath("//li[normalize-space(.)='Бравосов Андрей Игоревич']").click()

    #Ищем поле "Исполнитель (юридическое лицо)" и выбираем значение
    browser.find_element_by_id("div-wcfLookupControl_KsupEgr_PerformerLegal").click()
    browser.find_element_by_xpath("//li[contains(text(), 'ООО \"ОНЛАНТА\"')]").click()

    #Ищем поле "Порядок проведения закупочной процедуры" и выбираем значение из выпадающего списка
    KsupSaleLawType = Select(
        browser.find_element_by_id("KsupSaleLawType_59c9adb5-ad0e-4308-b136-1f1006e5f9f6_$DropDownChoice"))
    KsupSaleLawType.select_by_value("44-ФЗ")

    #Ищем кнопку "Тип работ и услуг"
    browser.find_element_by_class_name("ms-taxonomy-browser-button").click()
    time.sleep(2)

    iframe = browser.switch_to_active_element()
    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe))
    browser.find_element(By.ID, "TIE_6").click()
    browser.find_element(By.ID, "LBL_33").click()
    browser.find_element(By.ID,
                             "ctl00_PlaceHolderDialogBodySection_PlaceHolderDialogBodyFooterMainSection_AddToFieldEditor").click()
    browser.find_element(By.ID, "ctl00_OkButton").click()
    parent_frame = browser.switch_to_default_content()
    time.sleep(1)
    sum = browser.find_element_by_id("KsupSumPlan_9901571e-b38b-42cf-bb3c-f8f7977f1555_$NumberField")
    sum.send_keys("52000000")

    time.sleep(20)
