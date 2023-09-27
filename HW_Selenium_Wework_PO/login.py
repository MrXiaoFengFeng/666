from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from HW_Selenium_Wework_PO.register import Register


class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver


    # 扫码
    def scanf(self):
        pass

    # 企业注册
    def goto_register(self):
        # 点击注册，跳转到注册

        self._driver.find_element(By.LINK_TEXT, '企业注册').click()
        return Register(self._driver)