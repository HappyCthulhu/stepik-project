import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--driver_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru or eng")


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption("driver_name")
    user_language = request.config.getoption('language')
    print('Look at me')
    driver = None
    if driver_name == "chrome":
        print("\nstart chrome driver for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
    elif driver_name == "firefox":
        print("\nstart firefox driver for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--driver_name should be chrome or firefox")
    yield driver
    print("\nquit driver..")
    driver.quit()
