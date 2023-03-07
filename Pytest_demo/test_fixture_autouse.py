import pytest



@pytest.fixture(autouse=True)
def open():
    print('打开浏览器')


def test_searche1():
    print('test_searcher1')
    pass

def test_searche2():
    print('test_searcher2')
    pass

def test_searche3():
    print('test_searcher3')
    pass

if __name__ == '__main__':
    pytest.main()