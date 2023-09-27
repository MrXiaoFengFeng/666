import os

import pytest
from selenium import webdriver


class TestBaseBrowser:
    def setup(self):
        browser = os.getenv("browser").lower()  # 转换成小写字母
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Edge()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def teadown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.get("https://baidu.com")


if __name__ == '__main__':
    pytest.main(["-v", "-s", os.path.abspath(__file__)])
