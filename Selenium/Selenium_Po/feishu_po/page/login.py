from selenium.webdriver.common.by import By

from .basepage import Base
from .free import Free


class Login(Base):
    def login(self):
        self.driver.find_element(By.XPATH, "//button[contains(@class,'ud__button')]").click()
        return Free(self.driver)