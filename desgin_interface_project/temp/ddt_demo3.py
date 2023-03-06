import json
import unittest

from ddt import ddt, data
from loguru import logger

from client import RequestHandler


def parse_test_case_from_json(file_path):
    '''
    读取json，返回dict
    :param file_path:
    :return:
    '''
    f = open(file_path, 'r', encoding='utf-8')
    data = json.loads(f.read())

    # with open(file_path, 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    return data


# python不要用相对路径，要用绝对路径，自行拼接绝对路径
CASE_LIST = parse_test_case_from_json('/Users/dengjiajie/Desktop/desgin_interface_project/temp/req_demo.json')
logger.info('\n'
            f'CASE_LIST: {CASE_LIST}')


@ddt
class TestDemo(unittest.TestCase):

    @data(*CASE_LIST)  # *列表
    def test_ddt_demo(self, reqeust_list):
        logger.info(f'\n'
                    f'reqeust_data: {CASE_LIST}\n'
                    f'')

        # 发送请求
        http_client = RequestHandler()  # alt + 回车键
        resp = http_client.send_http(CASE_LIST)

        logger.info('\n'
                    f'响应结果---{resp.text}\n'
                    f'')


if __name__ == '__main__':
    unittest.main()

'''
先定义，后开发

'''

'''
1、get和post有什么不同
2、用postman发送demo例子
3、敲一遍requests快速入门的文档
4、写一个数据驱动demo,实现数据与驱动完全分离

----
家华：
把你的项目改造成今天的数据驱动
'''