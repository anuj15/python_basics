# rahul179877 / 99$inmediA
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_UP = 100
PROMISED_DOWN = 100
TWITTER_MAIL = 'rahul179877'
TWITTER_PASS = '99$inmediA'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(5)
        self.driver.find_element(By.ID, value='onetrust-accept-btn-handler').click()
        sleep(5)
        self.driver.find_element(By.XPATH, value="//span[text()='Go']").click()
        sleep(60)
        down = self.driver.find_element(By.XPATH, value="(//div[@class='result-data u-align-left']/span)[1]").text
        up = self.driver.find_element(By.XPATH, value="(//div[@class='result-data u-align-left']/span)[2]").text
        return [float(down), float(up)]

    def tweet_at_provider(self, message):
        self.driver.get('https://x.com/')
        sleep(5)
        self.driver.find_element(By.XPATH, value="//button[@data-testid='xMigrationBottomBar']").click()
        sleep(5)
        self.driver.find_element(By.XPATH, value="//span[text()='Sign in']").click()
        sleep(5)
        self.driver.find_element(By.XPATH, value="//input[@autocomplete='username']").send_keys('rahul179877')
        self.driver.find_element(By.XPATH, value="//span[text()='Next']").click()
        sleep(5)
        self.driver.find_element(By.NAME, value='password').send_keys('99$inmediA')
        self.driver.find_element(By.XPATH, value="//button[@data-testid='LoginForm_Login_Button']").click()
        sleep(5)
        self.driver.find_element(By.XPATH, value="//div[@data-testid='tweetTextarea_0']").send_keys(message)
        sleep(5)
        self.driver.find_element(By.XPATH, value="//button[@data-testid='tweetButtonInline']").click()
        sleep(5)


bot = InternetSpeedTwitterBot()
data = bot.get_internet_speed()
if data[0] < PROMISED_DOWN or data[1] < PROMISED_UP:
    msg = (f'Message sent from a bot:\nPromised download speed: {PROMISED_DOWN} MBPS\nActual download speed: {data[0]} '
           f'MBPS\nPromised upload speed: {PROMISED_UP} MBPS\nActual upload speed: {data[1]} MBPS')
    bot.tweet_at_provider(msg)
