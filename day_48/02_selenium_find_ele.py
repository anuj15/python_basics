from selenium import webdriver
from selenium.webdriver.common.by import By

data = {}
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://python.org/')
date_xpath = "//div[h2[text()='Upcoming Events']]/ul/li/time"
link_xpath = "//div[h2[text()='Upcoming Events']]/ul/li/a"
dates = [x.text for x in driver.find_elements(by=By.XPATH, value=date_xpath)]
links = [x.text for x in driver.find_elements(by=By.XPATH, value=link_xpath)]
for i in range(len(dates)):
    data[i] = {'time': dates[i], 'name': links[i]}
print(data)
driver.quit()
