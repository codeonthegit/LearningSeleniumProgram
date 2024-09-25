import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_mini_project_1():
     driver = webdriver.Chrome()
     driver.get("https://katalon-demo-cura.herokuapp.com/")
     make_appointment_element = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
     make_appointment_element.click()

     WebDriverWait(driver=driver, timeout=10).until(
          EC.url_contains("profile.php#login")
     )

     username = driver.find_element(By.ID, "txt-username")
     username.send_keys("John Doe")



