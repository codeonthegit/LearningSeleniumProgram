import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_mini_project_1():
     driver = webdriver.Chrome()
     driver.get("https://katalon-demo-cura.herokuapp.com/")
     make_appointment_element = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
     make_appointment_element.click()

     time.sleep(5)

     # Verify that URL changes
     assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
     driver.quit()
