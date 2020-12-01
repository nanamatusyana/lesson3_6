import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")

@pytest.fixture()
def browser(request):
    browser_languge = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_languge})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test")
    yield browser
    browser.quit()
