import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys

def test_016_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(5)
    first_name = driver.find_element(By.NAME, "firstname")
    #first_name.send_keys("testinghere")

    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "thetesting").key_up(Keys.SHIFT).perform()

    time.sleep(5)
    driver.quit()

