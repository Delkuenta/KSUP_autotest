from pages.locators import PresaleListLocators
from userdata.user_data import UserData


def test_new(browser):
    print(*PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST)
    how, what = PresaleListLocators.FIND_ELEMENT_IN_PRESALE_LIST
    what = what.replace("Тестовое имя", UserData.user_data_dict["fullName"])
    print(what)
    print(how)