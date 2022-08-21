from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\SeleniumDrivers\geckodriver-v0.31.0-win64\geckodriver")
driver = webdriver.Firefox(service=serv_obj)

driver.get("http://automationpractice.com/")
driver.maximize_window()
total_links = driver.find_elements(By.TAG_NAME,'a')
print(len(total_links))
driver.close()
