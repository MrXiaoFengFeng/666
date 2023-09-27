import unittest

import jmespath
import requests


class HttpClient:

    def __init__(self, request_desc):
        self.request = request_desc.get("request")
        self.case_desc = request_desc.get("case_desc")
        self.validate = request_desc.get("validate")

        response = self.send_request()

        # 实现断言1：通过关键字json获取到响应体的相关数据
        # 判断用例yaml文件中是否写了断言字段
        if self.validate:
            for validate in self.validate:

                # 如果有断言，获取预期值和实际值
                expect_data: str = validate.get("expect_data")
                actual_data: str = validate.get("actual_data")
                # 判断实际值中是否存在表达式，如果不存在表达式，走异常逻辑
                try:
                    # 切割实际返回结果字段
                    actual_data_key_word, actual_data_expression = actual_data.split(".", 1)
                except Exception:
                    # 实际结果值等于实际切割后的值
                    actual_data_key_word = actual_data
                    # 表达式为None
                    actual_data_expression = None

                if hasattr(response, actual_data_key_word):
                    property_or_func = getattr(response, actual_data_key_word)
                    # 判断方法是否可以被调用，+()
                    if callable(property_or_func):
                        _property = property_or_func()
                    else:
                        _property = property_or_func

                    # 判断是否存在表达式：
                    if actual_data_expression:
                        # 如果表达式存在，则用jmespath寻找表达式对应的内容
                        __property = jmespath.search(actual_data_expression, _property)
                    else:
                        # 如果不存在，等于response反射的属性值
                        __property = _property

                    print(f"__property{__property}")
                    print(f"expect_data:{expect_data}")

                    # 断言：
                    key_word = validate.get("key_word")
                    if key_word == 'eq':
                        unittest.TestCase().assertEqual(__property, expect_data, msg=validate.get("msg"))
                    elif key_word == 'notNull':
                        unittest.TestCase().assertIsNotNone(__property, msg=validate.get("msg"))

        print(response.json())
        print(f"返回header为{response.headers}")
        print(f"返回cookies为{response.cookies}")



    # 根据request关键字定义参数模板
    def send_request(self):

        resp = requests.request(**self.request)

        return resp


# def test_http_client_get():
#     """测试get请求"""
#     """
#     {'test_suite': [{'method': 'get', 'url': 'https://api.apiopen.top/api/getHaoKanVideo',
#     'params': None, 'data': [{'page': 1}, {'size': 5}]}]}
#     """
#     request_desc = {
#         "method": "get",
#         "url": "https://api.apiopen.top/api/getHaoKanVideo",
#         "params": None,
#         "data": {
#             "page": 1,
#             "size": 5,
#         }
#
#     }
#     res = HttpClient(request_desc).send_request()
#
#     assert res.status_code == 200






if __name__ == '__main__':
    import os
    import pytest

    pytest.main(['-vs', os.path.abspath(__file__)])
