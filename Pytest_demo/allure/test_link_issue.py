import allure
import pytest

@allure.link('http://www.baidu.com', name = '链接')
def test_with_link():
    print('这是一条添加了链接的测试')
    pass

TEST_CASE_LINK = 'https://fanyi.youdao.com/index.html'

@allure.testcase(TEST_CASE_LINK, '翻译首页用例')
def test_with_case_link():
    print('这是条测试用例的链接，连接到测试用例里面')

# 运行的时候，命令行中加这段命令，140指bug id
#--allure-link-pattern=issue:http://www.baidu.com/issue/{}
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass

if __name__ == '__main__':
    pytest.main()