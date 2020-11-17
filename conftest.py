import pytest
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions



def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="firefox",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language:ru, en,....')


# pytest -s -v --browser_name=chrome test_parser.py
# pytest -s -v --browser_name=firefox test_parser.py

@pytest.fixture()
def browser_function(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("ignore-certificate-errors")
        # options.add_argument("start-maximized")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()

    elif browser_name == "msedge":
        print("\nstart MicrosoftEdge browser for test..")
        options = EdgeOptions()
        options.use_chromium = True
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument("ignore-certificate-errors")
        options.add_argument("start-maximized")
        browser = Edge(options=options)
    elif browser_name == "ie11":
        options = webdriver.IeOptions()
        print('\nstart "Internet Explorer 11" browser for test..')
        browser = webdriver.Ie()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.fixture(scope="session")
def browser_session(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("ignore-certificate-errors")
        #options.add_argument("start-maximized")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        # browser.maximize_window()

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        # browser.maximize_window()

    elif browser_name == "msedge":
        print("\nstart MicrosoftEdge browser for test..")
        options = EdgeOptions()
        options.use_chromium = True
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("ignore-certificate-errors")
        options.add_argument("start-maximized")
        browser = Edge(options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

