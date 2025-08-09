from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.close()