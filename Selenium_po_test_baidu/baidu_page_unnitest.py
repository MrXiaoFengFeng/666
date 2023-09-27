from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class BaiduPage:
    input_element = (By.ID, 'kw')
    sub_element = (By.ID, 'su')

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 测试元素
        # self.input_element = (By.ID, 'kw')
        # self.sub_element = (By.ID, 'su')

    # 测试方法,打开百度
    def goto_link(self, url, ):
        self.driver.get(url)

    #测试方法，输入关键字。点击提交
    def goto_search(self, url, keyword):
        self.goto_link(url)
        self.driver.find_element(*self.input_element).send_keys(keyword)
        self.driver.find_element(*self.sub_element).click()

    time.sleep(5)


class TestBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.baidupage = BaiduPage()


    def test_search(self):
        self.baidupage.goto_link('http://baidu.com')
        self.baidupage.goto_search('http://baidu.com', 'selenium')




    def tearDown(self) -> None:
        self.baidupage.driver.quit()

if __name__ == '__main__':

    unittest.main()