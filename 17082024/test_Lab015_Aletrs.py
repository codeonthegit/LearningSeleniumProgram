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

def TestAlerts:
    @pytest.fixture(scope="class")
    def setup(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        yield #Return self.driver
        self.driver.quit()

@pytest.mark.qa
def test_alerts_tc1(self, setup):
    self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    self.driver.maximize.window()
    element_prompt = self.driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_prompt.click()
    wait = WebDriverWait(driver=self.driver,timeout=5)
    wait.until(EC.alert_is_present())

    alert = Alert(self.driver)
    print(alert.text)
    alert.accept()

    result = self.driver.find_element(By.ID,"result").text
    assert result == "You successfully clicked an alert"

