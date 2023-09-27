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

    # 鼠标点击操作
    @pytest.mark.skip
    def test_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")

        click_element = self.driver.find_element(By.CSS_SELECTOR, "input[value='click me']")
        double_click_clement = self.driver.find_element(By.CSS_SELECTOR, "input[value='dbl click me']")
        right_click_clement = self.driver.find_element(By.CSS_SELECTOR, "input[value='right click me']")
        clear_clement = self.driver.find_element(By.CSS_SELECTOR, "input[value='Clear']")

        action = ActionChains(self.driver)
        action.click(click_element)
        action.double_click(double_click_clement)
        action.context_click(right_click_clement)
        action.pause(2)
        action.click(clear_clement)
        action.perform()

    # 鼠标悬浮
    @pytest.mark.skip
    def test_move_to_element(self):
        self.driver.get("https://baidu.com")
        set_element = self.driver.find_element(By.CSS_SELECTOR, "span[id=s-usersetting-top]")

        action = ActionChains(self.driver)
        action.move_to_element(set_element)
        action.perform()

    # 拖拽
    @pytest.mark.skip
    def test_drag_and_drop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.XPATH, "//*[@id='dragger']")
        drop1_element = self.driver.find_element(By.XPATH, "//*[@class='item'][1]")
        drop2_element = self.driver.find_element(By.XPATH, "//*[@class='item'][2]")
        drop3_element = self.driver.find_element(By.XPATH, "//*[@class='item'][3]")

        action = ActionChains(self.driver)
        # 方式1
        action.drag_and_drop(drag_element, drop1_element).perform()
        sleep(3)
        # 方式2
        action.click_and_hold(drag_element).release(drop2_element).perform()
        sleep(3)
        # 方式3
        action.click_and_hold(drag_element).move_to_element(drop3_element).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("https://baidu.com")
        input_element = self.driver.find_element(By.CSS_SELECTOR, "#kw")
        action = ActionChains(self.driver)
        action.click(input_element)
        action.key_down(Keys.SHIFT).send_keys("4").key_up(Keys.SHIFT).send_keys("hello").perform()
        sleep(3)




if __name__ == '__main__':
    pytest.main(["-vs", os.path.abspath(__file__)])
