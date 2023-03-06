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

        case = data_demo.pop('case')  # pop('key') , 根据你传入的key ,返回你弹出的value，
        expect = data_demo.pop('expect')  # pop('key') , 根据你传入的key ,返回你弹出的value，
        # 等价于，expect = data_demo.get('expect')
        # del data_demo['expect']
        num1 = data_demo.get('num1')
        num2 = data_demo.get('num2')

        ret = add(**data_demo)

        logger.info('\n'
                    f'ret: {ret}\n'
                    f'')

# add函数是一个接口 ,相当于服务端的一个接口
def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    unittest.main()

'''
先定义，后开发

'''