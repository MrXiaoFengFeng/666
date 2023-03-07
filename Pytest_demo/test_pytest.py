import pytest


class TestDemo1():
    def test_one(self):
        print('开始运行test_one方法')
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print('开始运行test_two方法')
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print('开始运行test_three方法')
        a = 'hello'
        b = 'hello world'
        # assert a not in b
        pytest.assume(a not in b)
        pytest.assume(1 == 2)
        pytest.assume(4 == 4)


class TestDemo2():
    def test_a(self):
        print('开始运行test_a方法')
        x = 'this'
        assert 'h' in x

    def test_b(self):
        print('开始运行test_b方法')
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print('开始运行test_c方法')
        a = 'hello'
        b = 'hello world'
        assert a in b


if __name__ == '__main__':
    # pytest.main("-v -s test_pytest.py::TestDemo1")
    pytest.main(['-v', 'test_pytest.py::TestDemo1'])

