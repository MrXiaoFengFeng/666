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

        """
        [
        {
          "key_word": "eq",
          "actual_data": "json.key1",
          "expect_data": 1,
          "msg": "POST请求响应key1断言失败"
        },
        {
          "key_word": "eq",
          "actual_data": "json.json.key2",
          "expect_data": 2,
          "msg": "POST请求响应key2断言失败"
        }
      ]
        """
        # 第一种断言需求：通过关键字json获取到响应体的相关数据
        response = self.send_request()
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
                key_word_mapping = {
                    "json": response.json(),
                    "status_code": response.status_code,
                    "headers": response.headers,
                }
                actual_data_key_word, actual_data_expression = actual_data.split(".", 1)
                if actual_data_key_word == "json":
                    # response.json() = json.loads(response.text)
                    # json_data: dict = response.json()
                    json_data: dict = key_word_mapping["json"]
                    # 默认搜索不到为None
                    _actual_data = jmespath.search("json.key1", json_data)

                    # 断言
                    key_word = validate.get("key_word")
                    if key_word == "eq":
                        unittest.TestCase().assertEqual(_actual_data, expect_data, msg=validate.get('msg'))

        print(response.json())



    # 根据requests关键字参数定义数据模板
    def send_request(self):
        resp = requests.request(**self.request)
        # print(resp.text)
        return resp







if __name__ == '__main__':
    # 测试get请求体
    import os
    import pytest

    pytest.main(["-s", "-v", os.path.abspath(__file__)])
