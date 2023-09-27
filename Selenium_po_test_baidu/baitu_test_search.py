import pytest
import yaml
from selenium.webdriver.common.by import By
from .baidu_test_basepage import BasePage
# from selenium import webdriver
# from .data_handler import get_data

class Test_search(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get('https://baiduc.com')



    @pytest.mark.parametrize('type, value', )
    def test_search(self, type, value):
        self.input_text()
        # self.click(By.ID, 'su')

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    test = Test_search(driver)
    test.test_search()