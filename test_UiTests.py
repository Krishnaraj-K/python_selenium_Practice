from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

def test_check_no_of_links():
    serv_obj = Service("C:\SeleniumDrivers\geckodriver-v0.31.0-win64\geckodriver")
    driver = webdriver.Firefox(service=serv_obj)
    # serv_obj = Service("C:\SeleniumDrivers\chromedriver_win32\chromedriver")
    # driver = webdriver.Chrome(service=serv_obj)

    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    total_links = driver.find_elements(By.TAG_NAME,'a')
    print(len(total_links)) # Total Number of Links in the Webpage
    driver.close()

test_check_no_of_links()
def test_chk_no_of_sliders():
    serv_obj = Service("C:\SeleniumDrivers\geckodriver-v0.31.0-win64\geckodriver")
    driver = webdriver.Firefox(service=serv_obj)

    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    sliders = driver.find_elements(By.CLASS_NAME,'homeslider-container')
    print(len(sliders)) #Total number of sliders in the webpage
    driver.close()
test_chk_no_of_sliders()
