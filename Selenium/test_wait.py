from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/thbd")
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # self.driver.find_element(By.XPATH, '//*[@title="社区与测吧遗留问题释疑"]').click()
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, "//*[@class='card-header']")) > 1
        # WebDriverWait(self.driver, 10).until(wait)
        # 是否可以定位到
        expected_conditions.visibility_of_element_located("//*[@class='card-header']")
        print('++++++++')
        # 是否可以点击
        el = expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='card-header']"))
        # 显示等待
        WebDriverWait(self.driver, 10).until(el)
        print('666')
        self.driver.find_element(By.LINK_TEXT, "所有成员...").click()
        print("hello")
        sleep(3)


if __name__ == '__main__':
    pytest.main()
