from pages.base_page import BasePage
import time
from pages.locators import BasePageLocators
from userdata.user_data import UserData
from pages.locators import LoginPageLocators
import autoit
import pyautogui


class LoginData(BasePage):
    # ППАК https://ksup.lanit.ru
    # ТПАК https://ksup-test.lanit.ru/
    link = "https://ksup-test.lanit.ru"

    def login(self, login):
        autoit.auto_it_set_option("WinTitleMatchMode", 1)
        autoit.opt("SendKeyDelay", 0)
        if self.browser.name == "chrome":
            autoit.win_wait_active("[TITLE:https://adfs.lan.lanit.ru/; CLASS:Chrome_WidgetWin_1]", 10)
            autoit.send("Lanit" + "\\" + login)
            pyautogui.press("tab")
            autoit.send(UserData.user_account[login])
            pyautogui.press("enter")
        elif self.browser.name == "msedge" or self.browser.capabilities['browserName'] == "internet explorer":
            autoit.win_wait_active("[TITLE:Безопасность Windows; CLASS:Credential Dialog Xaml Host]", 10)
            time.sleep(1)
            autoit.send("Lanit" + "\\" + login)
            pyautogui.press("tab")
            autoit.send(UserData.user_account[login])
            pyautogui.press("enter")
        elif self.browser.name == "firefox":
            self.browser.find_element(*LoginPageLocators.USER_NAME_ELEMENT).send_keys("Lanit" + "\\" + login)
            self.browser.find_element(*LoginPageLocators.PASSWORD_ELEMENT).send_keys(UserData.user_account[login])
            self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        else:
            print(self.browser.capabilities['browserName'])

    def logout(self):
        self.is_visibility_of_element_located(*BasePageLocators.USER_NAME, 5)
        self.browser.find_element(*BasePageLocators.USER_NAME).click()
        time.sleep(1)
        self.is_visibility_of_element_located(*BasePageLocators.LOGOUT_BUTTON, 5)
        self.browser.find_element(*BasePageLocators.LOGOUT_BUTTON).click()
