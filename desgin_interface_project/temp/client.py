'''
选择 http驱动
requests 只能测试http1.1
httpx api的适应方法和requests 类似  http2.0
'''

import requests


class RequestHandler():

    def __init__(self):
        pass

    def send_http(self, request_data):
        '''

        :param request_data: 传入的数据类型是一个字典，里面有请求所需要的所有数据
        :return:
        '''
        # 请求方法
        # method = request_data.get('method')  # 复制的快捷键，ctrl + D 复制多一行
        # url = request_data.get('url')  # get方法，获取不到参数，默认为None
        # params = request_data.get('params')
        # data = request_data.get('data')
        # json = request_data.get('json')
        # 请求url/path

        # 请求参数 params / body form / json
        # response = requests.request(method=method, url=url, params=params, data=data, json=json)
        response = requests.request(**request_data)
        return response


if __name__ == '__main__':
    request_data = {
        "method": 'GET',
        "url": 'http://httpbin.org/get',
        "params": {
            "key1": 'v1',
            "key2": 'v2'
        },
    }
    request_data = {
        "method": 'GET',
        "url": 'http://httpbin.org/get',
        "params": {
            "key1": 'v3',
            "key2": 'v4'
        },
    }
    # 相同的数据结构，放在列表
    # 正常情况下：
    '''
    post url是不带参数，理论可以带
    http://httpbin.org/123/ # restful风格
    http://httpbin.org?orderNo=123 # 老项目
    '''
    # 接口定义
    reqeust_list = [
        {
            "method": 'GET',
            "url": 'http://httpbin.org/get',
            "params": {
                "key1": 'v1',
                "key2": 'v2'
            },
        },
        {
            "method": 'POST',
            "url": 'http://httpbin.org/post',
            "data": {
                "key1": 'v3',
                "key2": 'v4'
            },
        }
    ]
    for request_data in reqeust_list:
        http_client = RequestHandler()
        resp = http_client.send_http(request_data)
        print(resp.text)
