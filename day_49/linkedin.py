import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = (
    'https://www.linkedin.com/jobs/search/?currentJobId=3954676201&distance=25&f_AL=true&geoId=115884833&keywords'
    '=manual%20tester&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true')
username = 'anujgupta90210@gmail.com'
password = '99$inmediA'
driver.get(url)
time.sleep(5)
driver.find_element(By.XPATH, value="//a[contains(text(),'Sign in')]").click()
time.sleep(5)
driver.find_element(By.ID, value='username').send_keys(username)
driver.find_element(By.ID, value='password').send_keys(password)
driver.find_element(By.XPATH, value="//button[@type='submit']").click()
time.sleep(5)
driver.get(url)
time.sleep(5)
companies = driver.find_elements(By.XPATH, value="//li[contains(@class, 'ember')]//a")
for x in companies:
    x.click()
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, value="(//span[text()='Easy Apply'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="//form//span[text()='Next']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="//form//span[text()='Review']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="//span[text()='Submit application']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="(//button[@aria-label='Dismiss'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="//span[text()='Discard']").click()
        time.sleep(5)
    except NoSuchElementException:
        driver.find_element(By.XPATH, value="(//button[@aria-label='Dismiss'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, value="//span[text()='Discard']").click()
        time.sleep(5)
        continue

driver.quit()
