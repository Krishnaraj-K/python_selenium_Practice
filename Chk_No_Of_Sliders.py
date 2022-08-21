from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\SeleniumDrivers\geckodriver-v0.31.0-win64\geckodriver")
driver = webdriver.Firefox(service=serv_obj)

driver.get("http://automationpractice.com/")
driver.maximize_window()
sliders = driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(sliders)) #Total number of sliders in the webpage
driver.close()