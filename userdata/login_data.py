from userdata.user_data import UserData
from pages.base_page import BasePage
import win32com.client
import time
from selenium.webdriver.common.keys import Keys

class LoginData(BasePage):
    link = "https://ksup-tst.lanit"

    def login_seller(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Mr_KSUP_Seller")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("AsdGhj-5681-Sle")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_seller2(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Mr_KSUP_Seller2")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("AsdGhj-5681-2Les")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_dir(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Mr_KSUP_Dir")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("AsdGhj-5681-Dri")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_dir2(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Mr_KSUP_Dir2")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("AsdGhj-5681-2Rid")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_legal(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Mr_KSUP_Legal")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("AsdGhj-5681-Lge")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_count(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Lanit\Mr_KSUP_Count")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("*AF5hcnEfF8D2g8a")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_fin(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Lanit\Mr_KSUP_Fin")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("AsdGhj-5681-Fni")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_udprpo(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Lanit\Mr_KSUP_UDPRPO")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("lPRvCNi9m9zU8gb")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")

    def login_kkp(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(2)
        shell.Sendkeys("Lanit\Mr_KSUP_KKP")
        shell.Sendkeys("{TAB}")
        shell.Sendkeys("su@rMpuYu{^}bOI5Z")
        time.sleep(2)
        shell.Sendkeys("{ENTER}")
