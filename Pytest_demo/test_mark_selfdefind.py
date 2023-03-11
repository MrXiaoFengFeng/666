import pytest


@pytest.mark.search
def test_search1():
    print('1')


@pytest.mark.search
def test_search2():
    print('2')


@pytest.mark.search
def test_search3():
    print('3')


@pytest.mark.login
def test_login1():
    print('1')


@pytest.mark.login
def test_login2():
    print('2')


@pytest.mark.login
def test_login3():
    print('3')
    assert 2 == 3


if __name__ == '__main__':
    pytest.main()
