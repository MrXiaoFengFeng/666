import json
import unittest

import jmespath
import requests


class HttpClient:
    # key = None
    def __init__(self, request_desc):
        self.request = request_desc.get("request")
        self.case_desc = request_desc.get("case_desc")
        self.validate = request_desc.get("validate")

        response = self.send_request()
        print(response.json())
        print(f"返回header为{response.headers}")
        print(f"返回cookies为{response.cookies}")
        new_response = ResponseObject(response)

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
                    key, actual_data_expression = actual_data.split(".", 1)

                except Exception:

                    # 实际结果值等于实际切割后的值
                    key = actual_data
                    # global key
                    # 表达式为None
                    actual_data_expression = None



                print(actual_data_expression)
                """
                {'message': 'ok', 'nu': 'SF1631643020688', 'ischeck': '1', 'condition': 'G40', 'com': 'shunfeng', 'status': '200', 'state': '4', 'data': [{'time': '2023-02-25 17:56:28', 'ftime': '2023-02-25 17:56:28', 'context': '快件已被退回商家/发件人如有疑问可咨询商家或联系（051885928473），感谢使用申通快递，期待再次为您服务！', 'location': ''},]}
                """
                data = new_response.__getattr__(key)
                #
                # r = data[actual_data_expression]
                r = jmespath.search(actual_data_expression, data)
                print(type(r))

                print(f"返回的r的值为：{r}")
                print(f"预期的值为：{expect_data}")

                # 断言：
                key_word = validate.get("key_word")
                if key_word == 'eq':
                    unittest.TestCase().assertEqual(r, expect_data, msg=validate.get("msg"))

    def send_request(self):
        resp = requests.request(**self.request)
        return resp

"""
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

                    print(f"__property:{__property}")
                    print(f"expect_data:{expect_data}")"""





        # print(response.json())
        # print(f"返回header为{response.headers}")
        # print(f"返回cookies为{response.cookies}")


    # 根据request关键字定义参数模板





class ResponseObject(object):

    def __init__(self, resp_obj):
        """ initialize with a requests.Response object

        Args:
            resp_obj (instance): requests.Response instance

        """
        self.resp_obj: requests.Response = resp_obj

    def __getattr__(self, key):
        try:
            if key == "json":
                value = self.resp_obj.json()
            elif key == "cookies":
                value = self.resp_obj.cookies.get_dict()
            elif key == "request_body":
                body = self.resp_obj.request.__dict__.get("body").decode("utf-8")
                value = json.loads(body)
            elif key == "request_cookies":
                cookie = dict(self.resp_obj.request.__dict__.get("_cookies"))
                value = cookie
            elif key == "request_headers":
                headers = self.resp_obj.request.__dict__.get("headers")
                value = headers
            else:
                value = getattr(self.resp_obj, key)

            self.__dict__[key] = value
            return value
        except AttributeError:
            err_msg = "ResponseObject does not have attribute: {}".format(key)
            # logger.log_error(err_msg)
            raise Exception(err_msg)




    # # 根据request关键字定义参数模板
    # def send_request(self):
    #
    #     resp = requests.request(**self.request)
    #
    #     return resp



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
