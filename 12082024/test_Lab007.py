import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@pytest.mark.negative
@allure.title("VWO Invalid Login Page - test_mini_project_2")
@allure.description("Verify that with Invalid Email, Password. Error message came")
def test_mini_project_2():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://app.vwo.com/#/login")
        assert driver.current_url == "https://app.vwo.com/#/login"

        email_web_element = driver.find_element(By.NAME, "username")
        email_web_element.send_keys("admin@admin.com")

        password_web_element = driver.find_element(By.ID, "login-password")
        password_web_element.send_keys("admin@123")

        submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
        submit_btn_web_element.click()

        time.sleep(3)

        error_message_web_element = driver.find_element(By.ID, "js-notification-box-msg")
        assert error_message_web_element.text == "Your email, password, IP address or location did not match"

        time.sleep(5)
        driver.quit()

