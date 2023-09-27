from HW_Selenium_Wework_PO.index import Index


class TestRgister:

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register()
        # self.index.goto_login().goto_register().register()
