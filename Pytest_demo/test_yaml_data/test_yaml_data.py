import pytest
import yaml


# 直接传值方式：
# class TestData:
#    @pytest.mark.parametrize('a,b',[(1, 2), (3, 4)])
#    def test_data(self, a, b):
#       return a + b
#
# if __name__ == '__main__':
#
#    pytest.main('-vs')

# 引入yaml传值
class TestYamlData:
    @pytest.mark.parametrize('a, b', yaml.safe_load(open('./data.yml', 'r')))
    def test_data(self, a, b):
        return a + b


if __name__ == '__main__':
    pytest.main()
