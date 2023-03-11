import pytest
# 默认加载统计目录文件conftest.py


def test_case1(login):
    print('case1需登录')
    pass


def test_case2():
    print('case2无需登录')
    pass


def test_case3():
    print('case3')
    pass


def test_case4(login):
    print('case4')
    pass


if __name__ == '__main__':
    pytest.main()