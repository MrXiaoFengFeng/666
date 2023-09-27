import os
from time import sleep

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestBarScroll:

    def setup(self):
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option('w3c', 'false')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 页面内元素滚动
    def test_touchaction_scroll(self):
        self.driver.get("https://music.163.com/#/song?id=64293")
        # hand_element = self.driver.find_element(By.CSS_SELECTOR, ".bg")
        self.driver.find_element(By.CSS_SELECTOR, "a[data-action='lock']").click()

        radio_element = self.driver.find_element(By.CSS_SELECTOR, ".cur")
        bar_element = self.driver.find_element(By.CSS_SELECTOR, ".rdy")

        action = ActionChains(self.driver)

        # action.move_to_element(hand_element)

        # 播放进度条滑动
        # 移动按钮可以
        action.click_and_hold(radio_element).move_by_offset(400, 0).release()
        action.pause(3)
        # 进度条栏也可以
        action.click_and_hold(bar_element).move_by_offset(600, 0).release()

        # action.click_and_hold(radio_element)
        # action.move_by_offset(200, 0)
        # action.release()
        action.perform()
        sleep(5)


if __name__ == '__main__':
    pytest.main(["-vs", os.path.abspath(__file__)])
