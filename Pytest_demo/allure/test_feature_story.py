import pytest
import allure


@allure.feature('登录功能')
class TestLogin:

    @allure.story('登录成功')
    def test_login_succ(self):
        print('登录：测试用例--成功')

    @allure.story('登录失败')
    def test_login_fail_nullname(self):
        print('登录：测试用例--失败-用户名为空')

    @allure.story('登录失败')
    def test_login_fail_erropass(self):
        with allure.step('点击用户名'):
            print('请输入用户名')
        with allure.step('请输入密码'):
            print('请输入密码')
        print('点击登录')
        with allure.step('点击登录后登录失败'):
            assert '1' == 1
            print('登录失败')


if __name__ == '__main__':
    pytest.main()
