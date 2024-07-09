from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

# keep the browser opens after the program finishes
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://amazon.com/')
driver.quit()
