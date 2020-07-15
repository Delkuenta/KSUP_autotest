import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Login_Seller = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_windows/default.aspx?ReturnUrl=%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F%255Fwindows%252Fdefault%252Easpx&Source=%2f_windows%2fdefault.aspx"


def test_create_presale(browser):
    browser.get(Login_Seller)
    browser.implicitly_wait(10)
    # Переход на страницу пресейловых активностей
    # Ищем кнопку "Cоздать" на вкладке Пресейловые активности
    button_create_presale = browser.find_element_by_xpath("//a[@id='idHomePageNewItem']")
    button_create_presale.click()

    #Ждем загрузки страницы по последнему загружаемому объекту
    wait = WebDriverWait(browser, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'select2-wcfLookupControl_KsupSeller-container'),
                                                'Бравосов Андрей Игоревич'))

    # Ищем поле "Предмет контракта" и заполняем
    name_presale = browser.find_element_by_css_selector("#KsupFullName_1cb78896-92f2-4cb9-a3ad-b45e0f9932a6_\$TextField")
    name_presale.send_keys("тест_ПА_тендер_самостПрод_катА")

    #Ищем поле "Способ определения поставщика" и выбираем значение
    type_presale = Select(browser.find_element_by_id("KsupContractorType_c208b1d8-b8f1-417e-83de-32d7be2864be_$DropDownChoice"))
    type_presale.select_by_value("Тендерная заявка")

    #Ищем поле "Заказчик" и выбираем значение
    browser.find_element_by_xpath("//div[@id='div-wcfLookupControl_KsupEgr_Customer']/span/span/span").click()
    #Costumer = browser.find_element_by_xpath('//li[text()="КАЗНАЧЕЙСТВО РОССИИ"]').click
    browser.find_element_by_xpath("//li[normalize-space(.)='КАЗНАЧЕЙСТВО РОССИИ']").click()

    #Ищем поле "Подразделение-продавец" и выбираем значение
    browser.find_element_by_id("div-wcfLookupControl_KsupDivisions").click()
    browser.find_element_by_xpath("//li[normalize-space(.)='ОНЛАНТА']").click()

    time.sleep(20)
