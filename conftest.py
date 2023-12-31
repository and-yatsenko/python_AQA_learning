import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language")


@pytest.fixture(scope="class")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument("--headless") # open a browser window in headless
    options.add_argument("--window-size=%s" % "1920,1080")
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
