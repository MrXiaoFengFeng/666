from selenium.webdriver.common.by import By
from .basepage import Base

class Free(Base):
    def free(self):
        self.driver.find_element(By.XPATH, "//div[@class='mobile-input-right']/input").send_keys("13026360000")
        return self