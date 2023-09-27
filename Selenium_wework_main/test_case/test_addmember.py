from time import sleep

from Selenium_wework_main.page.index import Index


class TestAddmember:

    def setup(self):
        self.index = Index()

    def test_addmember(self):
        add_member = self.index.goto_add_member()
        # add_member.add_member()
        get_member = add_member.get_member()
        print(get_member)
        sleep(3)
        assert 'hello' in get_member


# if __name__ == '__main__':
#     TestAddmember.test_add_member()