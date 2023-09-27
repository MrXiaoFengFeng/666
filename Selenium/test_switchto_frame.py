import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSwitchFrame:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


    def test_switch_frame(self):
        self.driver.get("https://mail.163.com/")

        self.driver.find_element(By.CSS_SELECTOR, '.headerLogo')
        # 定位动态frame，然后取出值
        # 以xxx开始
        iframe_id = self.driver.find_element(By.XPATH, "//iframe[starts-with(@id, 'x-URS-iframe')]")
        # 包含xxx
        # frame_id = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'x-URS-iframe')]")
        # 切换到登录框frame
        print(iframe_id)
        self.driver.switch_to.frame(iframe_id)
        name_element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        name_element.send_keys("hello")
        print(name_element.get_attribute("placeholder"))
        # 切回默认iframe1
        # self.driver.switch_to.default_content()
        # 切回父iframe
        self.driver.switch_to.parent_frame()
        print(self.driver.find_element(By.CSS_SELECTOR, ".headerTitle").text)
        sleep(5)


if __name__ == '__main__':
    pytest.main(["-vs", os.path.abspath(__file__)])
