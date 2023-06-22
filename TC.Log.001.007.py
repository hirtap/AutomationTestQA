from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

time.sleep(2)
driver.get("https://www.saucedemo.com/")
element = driver.find_element(By.ID, "user-name").send_keys("usernamebelumterdaftar")
element = driver.find_element(By.ID, "password").send_keys("apalagipasswordnyapastibelumjuga")

time.sleep(2)
element = driver.find_element(By.ID, "login-button").click()

while(True):
    pass