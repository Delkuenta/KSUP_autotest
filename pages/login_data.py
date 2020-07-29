from userdata.user_data import UserData
from pages.base_page import BasePage
import win32com.client
import time
from selenium.webdriver.common.keys import Keys

class LoginData(BasePage):
    link = "https://ksup-tst.lanit"

    def login(self, login, password):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys(login)
        shell.Sendkeys("{TAB}")
        shell.Sendkeys(password)
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

