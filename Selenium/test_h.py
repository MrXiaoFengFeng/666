from time import sleep
import pytest
from selenium import webdriver


class TestH:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_h(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团111").click()
        self.driver.find_element_by_link_text("TesterHome内部站务").click()
        print("执行完啦")

if __name__ == '__main__':
    pytest.main()
