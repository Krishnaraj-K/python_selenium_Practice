# TestCase:
#     Open Browser
#     Open URL - https://admin-demo.nopcommerce.com/
#     Enter Username - admin@yourstore.com
#     Enter Password - admin
#     Click On Login.
#     Capture title of the homepage. (Actual Title)
#     Verify title of the page OrangeHRM (Expected)
#     Close Browser


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox()
driver.get("https://admin-demo.nopcommerce.com/")
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