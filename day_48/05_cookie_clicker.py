import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://orteil.dashnet.org/experiments/cookie/')
xpath = "//div[@id='store']/div[@class!='grayed']"
cookie = driver.find_element(by=By.XPATH, value="//div[@id='cookie']")
five_minute_timer = time.time() + 5 * 60
while time.time() < five_minute_timer:
    five_second_timer = time.time() + 5
    while time.time() < five_second_timer:
        cookie.click()
        power_ups = driver.find_elements(By.XPATH, value=xpath)
        if len(power_ups) > 0:
            driver.find_element(By.XPATH, value=f'{xpath}[{len(power_ups)}]').click()
cookie_per_second = driver.find_element(By.ID, value='cps').text
print(cookie_per_second)
driver.quit()
