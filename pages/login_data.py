from pages.base_page import BasePage
import win32com.client
import time
from userdata.user_data import UserData


class LoginData(BasePage):
    link = "https://ksup-tst.lanit"

    def login(self, login):
        account = ""
        shell = win32com.client.Dispatch("WScript.Shell")
        if login == "Mr_KSUP_Seller":
            account = UserData.login_seller
        elif login == "Mr_KSUP_Seller2":
            account = UserData.login_seller2
        elif login == "Mr_KSUP_Dir":
            account = UserData.login_dir
        elif login == "Mr_KSUP_Dir2":
            account = UserData.login_dir2
        elif login == "Mr_KSUP_Legal":
            account = UserData.login_legal
        elif login == "Mr_KSUP_Count":
            account = UserData.login_count
        elif login == "Mr_KSUP_Fin":
            account = UserData.login_fin
        elif login == "Mr_KSUP_UDPRPO":
            account = UserData.login_udprpo
        elif login == "Mr_KSUP_KKP":
            account = UserData.login_kkp
        else:
            print("Не корректное значение переменной 'create_account' в файле json")
        shell.Sendkeys(account[0])
        shell.Sendkeys("{TAB}")
        shell.Sendkeys(account[1])
        time.sleep(2)
        shell.Sendkeys("{ENTER}")
