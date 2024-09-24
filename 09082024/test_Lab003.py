import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    # Create an instance of ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Open incognito
   # chrome_options.add_argument("--window--size=920X680")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    print(driver.page_source)
    time.sleep(10)
    driver.quit()
