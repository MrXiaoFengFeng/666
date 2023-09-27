from selenium import webdriver


class TestAddCookies:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_add_cookies(self):
        self.driver.get("https://login.feishu.cn/accounts/page/login?app_id=11&redirect_uri=https%3A%2F%2Fwww.feishu.cn%2F&template_id=7159153320657698818")
        self.driver.add_cookie()