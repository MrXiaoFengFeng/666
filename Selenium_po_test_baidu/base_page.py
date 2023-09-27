
import time

from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, keyword, *loc):
        self.driver.find_element(*loc).send_keys(keyword)

    def click(self,*loc):
        self.driver.find_element(*loc).click()

    def get_title(self):
        return self.driver.title


class BaiduPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        driver.get('http://baidu.com')

    def search(self):
        loc = (By.ID, 'kw')
        keyword = 'selenium'
        loc2 = (By.ID, 'su')
        self.input_text(keyword, *loc)
        self.click(*loc2)



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    baidupage = BaiduPage(driver)
    baidupage.search()

