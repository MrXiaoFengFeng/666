import pytest

def setup_module():
    print('模块级，这是setup_module方法')

def teardown_module():
    print('模块级，这是teardown_module方法')


def setup_function():
    print('函数级，这是setup_fuction方法')

def teardown_function():
    print('函数级，这是teardown_function方法')

def test_login():
    print('这个外部的方法')


class TestDemo:
    def setup_class(self):
        print('类级，这是setup_class方法')

    def teardown_class(self):
        print('类级，这是teardown_class方法')


    def setup_method(self):
        print('方法级，这是setup_class方法')

    def setup(self):
        print('类里面的case，这是setup方法')

    def teardown(self):
        print('类里面的case，这是teardown方法')

    def teardown_method(self):
        print('方法级，这是teardown_method方法')

    def test_0(self):
        print('0000类里的case0方法')
        assert 1 == 1

    def test_1(self):
        print('0000类里的case1方法')
        assert 1 == 1






if __name__ == '__main__':
    pytest.main()