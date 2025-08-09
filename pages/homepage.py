from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com')

    def click_product(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.browser.find_element(By.LINK_TEXT, value='Monitors')
        monitor_link.click()

    def check_product_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, value='.card')
        assert len(monitors) == count