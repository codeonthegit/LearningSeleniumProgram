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
from selenium.webdriver.common.action_chains import  ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_017_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(4)
    atag = driver.find_element(By.ID, "click")
    atag.click()
    time.sleep(4)

    action_builders = ActionBuilder(driver)
    action_builders.pointer_action.pointer_up(MouseButton.BACK)
    action_builders.perform()

    time.sleep(5)
    driver.quit()

