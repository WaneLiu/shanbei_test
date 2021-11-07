import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.shanbay.com/")
time.sleep(45)

print(driver.get_cookies())

driver.quit()