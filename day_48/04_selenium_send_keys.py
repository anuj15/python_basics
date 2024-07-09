import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://secure-retreat-92358.herokuapp.com/')
driver.find_element(by=By.NAME, value='fName').send_keys('test')
driver.find_element(by=By.NAME, value='lName').send_keys('test')
driver.find_element(by=By.NAME, value='email').send_keys('test@test.test')
driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
time.sleep(5)
driver.quit()
