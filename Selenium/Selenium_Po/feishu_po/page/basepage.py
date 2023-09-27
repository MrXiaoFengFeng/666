# 是所有page页父类，公共方法，初始化driver 退出driver
# __init__ 初始化
from time import sleep

from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    def __init__(self, driver: WebDriver=None):
        # driver进行复用，不存在就创建新的
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get("https://feishu.cn")
            self.driver.find_element(By.CSS_SELECTOR, "div[data-elem-id='he4otsjKQ8']").click()
        else:
            self.driver = driver


    def close(self):
        sleep(5)
        self.driver.quit()