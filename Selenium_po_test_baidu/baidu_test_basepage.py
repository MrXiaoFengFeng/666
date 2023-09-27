# from selenium import webdriver



class BasePage:

    def __init__(self, driver:None):
        self.driver = driver


    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, keyword, *loc):
        self.driver.find_element(*loc).send_keys(keyword)

    def click(self, *loc):
        self.driver.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

