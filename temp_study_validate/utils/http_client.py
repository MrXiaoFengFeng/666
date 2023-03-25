import allure
import requests
import jmespath
import unittest


# 有培训班这么写
# class HttpClient():
#
#     def get(self, url, params, headers):
#         resp = requests.get(url=url, params=params, headers=headers)
#
#     def post(self, url, data=None, json=None, headers=None):
#         if data:
#             resp = requests.post(url=url, data=data, headers=headers)
#         elif json:
#             resp = requests.post(url=url, json=json, headers=headers)

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
                actual_data_key_word, actual_data_expression = actual_data.split(".", 1)
                if actual_data_key_word == "json":
                    # response.json() = json.loads(response.text)
                    json_data: dict = response.json()
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


def test_http_client_get():
    request_desc = {
        "method": "get",
        "url": "https://httpbin.org/get",
        "params": {
            "key1": 1,
            "key2": 2
        },
        "headers": {
            "h1": "h1",
            "h2": "h2"
        }
    }
    resp = HttpClient().send_request(request_desc)
    assert resp.status_code == 200
    print(resp.text)


def test_http_client_post_data():
    request_desc = {
        "method": "post",
        "url": "https://httpbin.org/post",
        "params": {
            "v1": "v1"
        },
        "data": {
            "key1": 1,
            "key2": 2
        },
        "headers": {
            "h1": "h1",
            "h2": "h2"
        }
    }
    resp = HttpClient().send_request(request_desc)
    assert resp.status_code == 200
    print(resp.text)
    print(resp.request.body)


def test_http_client_post_json():
    request_desc = {
        "method": "post",
        "url": "https://httpbin.org/post",
        "params": {
            "v1": "v1"
        },
        "json": {
            "key1": 1,
            "key2": 2
        },
        "headers": {
            "h1": "h1",
            "h2": "h2"
        }
    }
    resp = HttpClient().send_request(request_desc)
    assert resp.status_code == 200
    print(resp.text)
    print(resp.request.body)


if __name__ == '__main__':
    # 测试get请求体
    import os
    import pytest

    pytest.main(["-s", "-v", os.path.abspath(__file__)])
