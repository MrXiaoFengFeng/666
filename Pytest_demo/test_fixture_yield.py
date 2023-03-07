import pytest


# 作用域：module是在模块之前执行，模块之后执行
@pytest.fixture(scope='module')
def open():
    print('打开浏览器')
    # yield

    print('执行teardown')
    print('最后关闭浏览器')

def test_searche1(open):
    print('test_searcher1')
    raise NameError
    pass

def test_searche2(open):
    print('test_searcher2')
    raise NameError
    pass

if __name__ == '__main__':
    pytest.main()