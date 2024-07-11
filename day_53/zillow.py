import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

form_link = ('https://docs.google.com/forms/d/e/1FAIpQLSdn0kahLOMoUDXPBX2zTgw1qaMxBjnqf7ve3q9Xvqh91viDYA/viewform?usp'
             '=sf_link')
zillow_url = 'https://appbrewery.github.io/Zillow-Clone/'

contents = requests.get(zillow_url).content
soup = BeautifulSoup(contents, 'html.parser')
addresses = [x.text.strip().replace('| ', '') for x in
             soup.select(selector=".StyledPropertyCardDataWrapper > a > address")]
links = [x.get('href') for x in soup.select(selector=".StyledPropertyCardDataWrapper > a")]
prices = [x.text.split('/')[0].split('+')[0] for x in soup.select(selector=".PropertyCardWrapper__StyledPriceLine")]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
for i in range(len(links) - 1):
    driver.get(form_link)
    time.sleep(1)
    driver.find_element(By.XPATH, value="(//input[@type='text'])[1]").send_keys(addresses[i])
    driver.find_element(By.XPATH, value="(//input[@type='text'])[2]").send_keys(prices[i])
    driver.find_element(By.XPATH, value="(//input[@type='text'])[3]").send_keys(links[i])
    driver.find_element(By.XPATH, value="//span[text()='Submit']").click()
    time.sleep(1)
driver.quit()
