import time
import pytest
from pages.homepage import HomePage
from selenium.webdriver.chrome.options import Options
from pages.product import ProductPage

@pytest.fixture()
def test_open(browser):
    options = Options()
    options.add_argument('--headless')
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_product()
    product_page = ProductPage(browser)
    product_page.check_title('Samsung galaxy s6')


def test_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    # browser.get('https://demoblaze.com')
    homepage.click_monitor()
    # monitor = browser.find_element(By.LINK_TEXT, value='Monitors')
    # monitor.click()
    time.sleep(3)
    homepage.check_product_count(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, value=".card")
    # assert len(monitors) == "2"