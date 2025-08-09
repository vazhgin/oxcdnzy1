import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.instagram.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Ваши тесты
try:
    driver.get(url=url)
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()