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

def test_vwo_login_16():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/")
        try:
            (WebDriverWait(driver=driver, timeout=10).until
                (EC.element_to_be_clickable((By.ID, "submit"))))
            print("End of the program")
        except TimeoutException as see:
            print(see)
            print("TimeoutException occured!!, 10 Seconds Passed")
        finally:
            driver.quit()
