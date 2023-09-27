from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://baidu.com")
sleep(10)