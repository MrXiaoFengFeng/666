import os
import sys
import pytest
import yaml
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(sys.path)
from utils import DataHandler
from utils import HttpClient

# ROOT_PATH = "E:\\WorkSpace\\request_demo"
ROOT_PATH = "/Users/dengjiajie/Desktop/request_demo"
DATA_PATH = os.path.join(ROOT_PATH, 'data')
FILE_PATH = os.path.join(DATA_PATH, 'http_get_testsuit.yaml')
print(FILE_PATH)
test_suite = DataHandler.load_yaml_data(FILE_PATH).get("test_suite", [])
print(type(test_suite))

if not test_suite:
    raise Exception('用例读取失败请检查数据')


class TestHttpSuccess:

    @pytest.mark.parametrize("request_desc", test_suite)
    def test_01_post_get(self, request_desc):
        request_desc = request_desc
        HttpClient(request_desc)
        # print(res.url)
        # assert res.status_code == 200


if __name__ == '__main__':
    pytest.main(["-s", "-v", os.path.abspath(__file__)])
    # print(f"返回header为{response.headers}")