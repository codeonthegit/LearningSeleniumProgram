from selenium import webdriver
def test_sample():
    driver = webdriver.Chrome()
    # driver =  webdriver.Edge()
    # driver = webdriver.Firefox()
    driver.get("https://www.google.co.in/")
    assert driver.current_url == "https://www.google.co.in/"
