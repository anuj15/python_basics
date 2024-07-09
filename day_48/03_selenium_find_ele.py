from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
articles = driver.find_element(by=By.XPATH, value="//a[@title='Special:Statistics']").text
print(articles)
driver.quit()
