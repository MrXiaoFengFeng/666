

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


    def test_upload_files(self):
        self.driver.get("https://baidu.com")
        self.driver.find_element(By.CSS_SELECTOR, ".soutu-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".upload-pic").send_keys("E:\\WorkSpace\\Selenium\\upload.jpg")
        sleep(5)






if __name__ == '__main__':
    pytest.main(["-vs", os.path.abspath(__file__)])
