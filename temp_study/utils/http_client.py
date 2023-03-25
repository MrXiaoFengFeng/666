import requests




class HttpClient():

    # 根据requests关键字参数定义数据模板
    def send_request(self, request_desc):

        resp = requests.request(**request_desc)
        # print(resp.text)
        return resp


def test_http_client_get():
    """测试get请求"""
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
    '''测试Post请求'''
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


def test_http_client_post_data1():
    '''测试Post请求'''
    request_desc = {
        "method": "post",
        "url": "https://api.apiopen.top/api/login",
        "data": {
            "account": "309324904@qq.com",
            "password": "123456"
        },
    }
    resp = HttpClient().send_request(request_desc)
    assert resp.status_code == 200
    print(resp.text)
    print(resp.request.body)

def test_http_client_post_json():
    """测试Post Json请求"""
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
    # print(resp.text)
    # print(resp.request.body)

if __name__ == '__main__':
    # 测试get请求体
    import os
    import pytest
    pytest.main(["-s", "-v", os.path.abspath(__file__)])
