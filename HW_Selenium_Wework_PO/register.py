from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:

    def __init__(self, driver:WebDriver):
        self._driver = driver

    def register(self):
        # 发送内容
        # 点击元素
        # 企业名称
        # 管理员姓名
        sleep(2)
        self._driver.find_element(By.ID, 'corp_name').send_keys('One11')
        self._driver.find_element(By.ID, 'manager_name').send_keys('FDD')
        sleep(5)
        self._driver.quit()
        return True

