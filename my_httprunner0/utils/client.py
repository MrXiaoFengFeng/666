import requests
from pprint import pprint
# import yaml


class RequesetHandler:

    def send_http_v1(self, request_data):
        resp = requests.request(**request_data)
        print(resp.text) # json() 是将响应体进行反序列化

    def run_datas(self, requests_data):
        test_case_suite = requests_data['test_case']
        for case in test_case_suite:
            print(f'case_name:{case["case_name"]}')
            print(f'interface_name:{case["interface_name"]}')
            request_data = case['request']
            self.send_http_v1(request_data)
            print(f'\n'
                  '分割线----\n'
                  '\n')


if __name__ == '__main__':
    requests_data = {
        'test_case': [{
            'case_name': '测试GET请求发送成功',
            'interface_name': 'GET请求的测试路由',
            'request': {
                'method': 'GET',
                'url': 'http://httpbin.org/get',
                'params': {
                    'k1': 'v1',
                    'k2': 'v2'
                }
            }
        }, {
            'case_name': '测试post请求发送成功',
            'interface_name': 'post请求的测试路由',
            'request': {
                'method': 'post',
                'url': 'http://httpbin.org/post',
                'params': {
                    'k3': 'v3',
                    'k4': 'v4'
                }
            }
        }]
    }

    requests_handler = RequesetHandler()
    # requests_handler.send_http_v1(requests_data['test_case'][0]['request'])
    requests_handler.run_datas(requests_data)