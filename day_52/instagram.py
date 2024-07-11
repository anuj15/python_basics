import time

from selenium import webdriver
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = 'chefsteps'
USERNAME = 'tanishqmehta90210@gmail.com'
PASSWORD = '99$inmediA'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://instagram.com/')
        time.sleep(5)
        self.driver.find_element(By.NAME, value='username').send_keys('tanishqmehta90210@gmail.com')
        self.driver.find_element(By.NAME, value='password').send_keys('99$inmediA')
        self.driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        time.sleep(5)

    def find_followers(self):
        self.driver.find_element(By.XPATH, value="//span[text()='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//input[@aria-label='Search input']").send_keys(SIMILAR_ACCOUNT)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[text()= 'chefsteps']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Follow')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//a[@href='/chefsteps/followers/']").click()
        time.sleep(5)

    def follow(self):
        followers = self.driver.find_elements(By.XPATH, value="//div[@role='dialog']//button[@class!='_abl-']")
        for follower in followers:
            follower.click()
            time.sleep(2)

    def close(self):
        self.driver.quit()


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
insta.close()
