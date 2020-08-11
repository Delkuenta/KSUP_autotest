import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from userdata.user_data import UserData


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language:ru, en,....')


# pytest -s -v --browser_name=chrome test_parser.py
# pytest -s -v --browser_name=firefox test_parser.py

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("ignore-certificate-errors")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(autouse=True)
def calc_price_category():
    price_category = ""
    if UserData.user_data_dict["currency"] == "Доллар":
        sum_in_rub = UserData.user_data_dict["sum"] * 70
    elif UserData.user_data_dict["currency"] == "Евро":
        sum_in_rub = UserData.user_data_dict["sum"] * 80
    else:
        sum_in_rub = UserData.user_data_dict["sum"]

    if sum_in_rub >= 50000000:
        price_category = "A"
    elif 30000000 <= sum_in_rub < 50000000:
        price_category = "B"
    elif sum_in_rub < 30000000:
        price_category = "C"

    # Добавляем в словарь ценовую категорию
    price_category_dict = {"price_category": price_category}
    UserData.user_data_dict.update(price_category_dict)


@pytest.fixture(autouse=True)
def calc_group_type_work():
    i = 0
    for item in UserData.user_data_dict["typeOfWorkServices"]:
        if item in UserData.group_software:
            i += 1
    if i >= 1:
        group_type_dict = {"groupTypeWork": "Software"}

    else:
        group_type_dict = {"groupTypeWork": "Other"}
    UserData.user_data_dict.update(group_type_dict)
