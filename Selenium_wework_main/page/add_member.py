import time


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Add_member:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.implicitly_wait(3)


    def add_member(self):
        self._driver.find_element(By.ID, 'username').send_keys('aHO2')
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('13000000005')
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('aHO2')
        self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        return True

    def get_member(self):
        # self._driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        # 获取用户名列表
        elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        list1 = []
        for element in elements:
            list.append(element.get_attribute('title'))
        print(list1)
        return list1

