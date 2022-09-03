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

def test_titlecompare():
    driver = webdriver.Firefox()
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"Email").clear()
    driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
    driver.find_element(By.ID,"Password").clear()
    driver.find_element(By.ID,"Password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR,".button-1").click()

    act_title = driver.title
    exp_title = "Dashboard / nopCommerce administration"

    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login Test Failed")

    driver.close()

test_titlecompare()
