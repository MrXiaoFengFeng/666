import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSwitchWindows:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com")

    # def teardown(self):
    #     pass
        # self.driver.quit()

    def test_switch_windows(self):
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-loginbtn").click()
        # 获取当前窗口
        window1 = self.driver.current_window_handle
        print(window1)
        # 点击注册
        self.driver.find_element(By.CSS_SELECTOR, "#TANGRAM__PSP_11__regLink").click()

        sleep(5)
        windows = self.driver.window_handles
        print(windows)
        # 用windows列表取可以
        # self.driver.switch_to.window((windows[0]))
        # 用定义的起始winsow也可以
        self.driver.switch_to.window(window1)
        # 点击输入用户名
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="userName"]').send_keys("hello")
        sleep(5)


if __name__ == '__main__':
    pytest.main(["-v", "-s", os.path.abspath(__file__)])

