from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Selenium_wework_main.page.add_member import Add_member


class Index:

    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self._driver = webdriver.Chrome(options=options)
        self._driver.implicitly_wait(5)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

    def goto_add_member(self):
        # 点击顶部栏通讯录，跳转后点击添加
        self._driver.find_element(By.ID, 'menu_contacts').click()
        sleep(3)
        # 点击添加成员
        # self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)> .js_add_member').click()

        return Add_member(self._driver)



    def goto_register(self):
        pass

