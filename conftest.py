import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en,  fr, es")

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\n\nStart browser for test...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    browser.save_screenshot('screenshots/screenshot-%s.png' % now)
    browser.quit()
