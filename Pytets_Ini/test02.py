import pytest


class Test_parametrize:
    data0 = [1, 2, 3]

    data1 = ['1234', '446']

    data2 = [(1, 2, 3), (4, 5, 6)]

    @pytest.mark.parametrize('num', data0)
    def test00(self, num):
        print(num)

    @pytest.mark.do
    @pytest.mark.parametrize('nums', data1)
    def test01(self, nums):
        print(nums)


    def add(self,a, b):
        return a + b

    @pytest.mark.do
    @pytest.mark.parametrize('a, b, c', data2)
    def test02(self, a, b, c):
        assert self.add(a, b) == c



if __name__ == '__main__':
    pytest.main(['-v' '-s' 'test02.py'])
