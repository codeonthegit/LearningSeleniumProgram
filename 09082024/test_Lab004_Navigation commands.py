import time

from selenium import webdriver
def test_open_vwologin():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    driver.refresh()
    driver.back()
    driver.forward()
    time.sleep(10)
    driver.quit()
