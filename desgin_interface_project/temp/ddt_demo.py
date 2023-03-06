import unittest

from ddt import ddt, data
from loguru import logger

data_demo = [
    {"case": "1号用例", "num1": 1, "num2": 2, "expect": 2},
    {"case": "2号用例", "num1": 3, "num2": 4, "expect": 7},
]


@ddt
class TestDemo(unittest.TestCase):

    @data(*data_demo)  # *列表
    def test_ddt_demo(self, data_demo):
        logger.info(f'\n'
                    f'data_demo: {data_demo}\n'
                    f'')

        case = data_demo.get('case')  # 如果拿不到case不会报错，默认等于None
        num1 = data_demo.get('num1')
        num2 = data_demo.get('num2')

        ret = add(num1, num2)

        logger.info('\n'
                    f'ret: {ret}\n'
                    f'')


def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    unittest.main()
