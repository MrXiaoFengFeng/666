import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.get("https://sahitest.com/demo/alertTest.htm?t1=Alert+Message6%2B6")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='t1']").send_keys("这是我写的一个alert文案")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='b1']").click()

        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()

        sleep(5)


if __name__ == '__main__':
    pytest.main(["-vs", os.path.abspath(__file__)])
