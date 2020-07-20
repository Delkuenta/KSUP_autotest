from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_NAME = (By.CSS_SELECTOR, ".o365cs-me-tile-nophoto-username.o365cs-me-bidi")



class PresalePageLocators:
    PRESALE_CREATE_BUTTON = (By.CSS_SELECTOR, "#idHomePageNewItem")


class MainPageLocators:
    pass


class LoginPageLocators:
    pass

class BasketPageLocators:
    pass