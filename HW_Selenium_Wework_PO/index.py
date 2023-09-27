from selenium import webdriver
from selenium.webdriver.common.by import By

from HW_Selenium_Wework_PO.login import Login
from HW_Selenium_Wework_PO.register import Register


class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')


    def goto_login(self):
        # click login 后跳转到登录页
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)

    def goto_register(self):
        # 点击立即注册，return到理解注册页面

        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)