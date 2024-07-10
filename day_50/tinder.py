import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://tinder.com/app/recs')
time.sleep(5)
driver.find_element(By.XPATH, value="//div[text()='I accept']").click()
time.sleep(5)
driver.find_element(By.XPATH, value="//div[text()='Log in']").click()
time.sleep(5)
driver.find_element(By.XPATH, value="//div[text()='Log in with Facebook']").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.find_element(By.ID, value='email').send_keys('anuj.nits@gmail.com')
driver.find_element(By.ID, value='pass').send_keys('anuj#101001')
driver.find_element(By.XPATH, value="//input[@type='submit']").click()
time.sleep(15)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.find_element(By.XPATH, value="//div[text()='Allow']").click()
time.sleep(5)
driver.find_element(By.XPATH, value="//div[text()='Notify me']").click()
time.sleep(5)
for _ in range(100):
    xpath = "//*[@id='u-1419960890']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button"
    try:
        driver.find_element(By.XPATH, value=xpath).click()
        time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
driver.quit()
