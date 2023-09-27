import pytest


class Test_ini:
    data = [1, 2, 3]

    # def add(self, a, b, c):
    #     return self.a + self.b = c


    @pytest.mark.parametrize('a, b, c', data)
    @pytest.mark.do
    def test01(self, a, b, c):
        print(a, b, c)

    @pytest.mark.undo
    def test02(self):
        print('test02')

    @pytest.mark.do
    def test03(self):
        print('test03')


if __name__ == '__main__':
    pytest.main(['-v' '-s' 'test01.py'])
