# 进入首页，根据功能 组装 新建 goto login 和goto free
from time import sleep

from selenium.webdriver.common.by import By
from .basepage import Base
from .free import Free
from .login import Login


class Index(Base):
    def goto_login(self):
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        return Login(self.driver)

    def goto_free(self):
        self.driver.find_element(By.LINK_TEXT, "免费试用").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        return Free(self.driver)