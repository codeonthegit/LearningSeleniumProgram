import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.positive
def test_mini_project():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://app.vwo.com/#/login")

        email_web_element = driver.find_element(By.NAME, "username")
        email_web_element.send_keys("admin@admin.com")

        password_web_element = driver.find_element(By.ID, "login-password")
        password_web_element.send_keys("admin@123")

        submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
        submit_btn_web_element.click()

        WebDriverWait(driver=driver, timeout=5).until(
                EC.visibility_of_element_located((By.ID,'js-notification-box-msg'))
        )

        error_message_web_element = driver.find_element(By.ID, "js-notification-box-msg")
        print(error_message_web_element.text)
        assert error_message_web_element.text == "Your email, password, IP address or location did not match"

        time.sleep(5)
        driver.quit()

