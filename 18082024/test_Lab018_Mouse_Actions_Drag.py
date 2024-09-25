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

def test_018_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(2)

    #draggable
    element_to_hold= driver.find_element(By.ID, "draggable")
    time.sleep(5)
    #Create an ActionChains object
    actions = ActionChains(driver)

    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(2)
    driver.quit()

