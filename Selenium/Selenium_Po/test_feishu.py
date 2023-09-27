"""
需求：
1、首页点击登录-点击立即注册
2、首页点击免费试用，输入手机号xx
"""
import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFeishu:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://feishu.cn")
        self.driver.find_element(By.CSS_SELECTOR, "div[data-elem-id='he4otsjKQ8']").click()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_case_login(self):
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.XPATH, "//button[contains(@class,'ud__button')]").click()
        sleep(3)

    def test_case_register(self):
        self.driver.find_element(By.LINK_TEXT, "免费试用").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        sleep(3)
        self.driver.find_element(By.XPATH, "//div[@class='mobile-input-right']/input").send_keys("13026360000")
        sleep(3)


if __name__ == '__main__':
    pytest.main(["-vs", os.path.abspath(__file__)])