import pytest
from selenium import webdriver
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
        options.add_argument("start-maximized")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        #browser.maximize_window()

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        # browser.maximize_window()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(autouse=True)
def calc_price_category():

    # Определяем валюту и переводим в рубли
    raw_sum = UserData.user_data_dict["sum"]
    if UserData.user_data_dict["currency"] == "Доллар":
        sum_in_rub = raw_sum * 70
    elif UserData.user_data_dict["currency"] == "Евро":
        sum_in_rub = raw_sum * 80
    else:
        sum_in_rub = raw_sum

    # Присваиваем категорию на основе суммы в рублях
    price_category = ""
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
def identification_group_type_work():
    i = 0
    for category in UserData.user_data_dict["typeOfWorkServices"]:
        if category in UserData.group_software:
            i += 1
    if i >= 1:
        group_type_dict = {"groupTypeWork": "Software"}

    else:
        group_type_dict = {"groupTypeWork": "Other"}
    UserData.user_data_dict.update(group_type_dict)

@pytest.fixture(autouse=True)
def sort_territory_list():
    UserData.user_data_dict["territory"].sort()