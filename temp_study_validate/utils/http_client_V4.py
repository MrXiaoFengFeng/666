import allure
import requests
import jmespath
import unittest


class HttpClient():

    def __init__(self, request_desc):
        """
        请求初始化
        :param request_desc:
        """
        """
        初始化参数获取
        """
        self.request = request_desc.get("request")
        self.case_desc = request_desc.get("case_desc")
        allure.dynamic.title(self.case_desc)
        self.validate = request_desc.get("validate")


    # 根据requests关键字参数定义数据模板
    def send_request(self):
        resp = requests.request(**self.request)
        # print(resp.text)
        return resp

    # 断言方法封装
    def validate(self, response):
        if self.validate:
            for validate in self.validate:
                """
                 validate =   {
                      "key_word": "eq",
                      "actual_data": "json.json.key1",
                      "expect_data": 1,
                      "msg": "POST请求响应key1断言失败"
                    }
                """
                expect_data: str = validate.get("expect_data")
                actual_data: str = validate.get("actual_data")

                try:
                    # 切割，如果不存在表达式，走异常逻辑
                    actual_data_key_word, actual_data_expression = actual_data.split(".", 1)
                except Exception:
                    actual_data_key_word = actual_data
                    # 表达式为None
                    actual_data_expression = None

                # 通过反射 找到repsonse里面的方法或者属性
                # status_code：HTTP响应状态码。
                # headers：HTTP响应头。
                # json()：返回HTTP响应内容的JSON格式。
                # Cookies: 响应缓存

                if hasattr(response, actual_data_key_word):
                    property_or_func = getattr(response, actual_data_key_word)
                    # 判断方法是否可被调用，俗称+括号
                    if callable(property_or_func):
                        _property = property_or_func()
                    else:
                        _property = property_or_func

                    # 判断是否存在表达式，
                    if actual_data_expression:
                        # 如果表达式存在 则用jmespath寻找表达式的对应的内容
                        __property = jmespath.search(actual_data_expression, _property)
                    else:
                        # 否则，等于response反射的属性值
                        __property = _property

                    print(f"__property:{__property}")
                    print(f"expect_data:{expect_data}")

                    # 断言
                    key_word = validate.get("key_word")
                    if key_word == "eq":
                        unittest.TestCase().assertEqual(__property, expect_data, msg=validate.get('msg'))

    # 跑http数据驱动
    def run(self):
        """
        数据驱动流程
        :return:
        """
        # 发送http请求
        response = self.send_request()

        # 验证
        self.validate((response))


if __name__ == '__main__':
    # 测试get请求体
    import os
    import pytest

    pytest.main(["-s", "-v", os.path.abspath(__file__)])
