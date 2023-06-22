from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

time.sleep(2)
driver.get("https://www.saucedemo.com/")
element = driver.find_element(By.ID, "user-name").send_keys("standard_user")
element = driver.find_element(By.ID, "password").send_keys("secret_sauce")

time.sleep(2)
element = driver.find_element(By.ID, "login-button").click()

time.sleep(2)
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
element = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

time.sleep(2)
element = driver.find_element(By.ID, "shopping_cart_container").click()

time.sleep(2)
element = driver.find_element(By.ID, "checkout").click()

time.sleep(2)
element = driver.find_element(By.ID, "first-name").send_keys("")
element = driver.find_element(By.ID, "last-name").send_keys("")
element = driver.find_element(By.ID, "postal-code").send_keys("")

time.sleep(2)
element = driver.find_element(By.ID, "continue").click()

while(True):
    pass