import os
import sys
print(os.path.abspath(__file__))    # E:\WorkSpace\temp_study\test_case\test_http_get.py
print(os.path.dirname(os.path.abspath(__file__)))  # E:\WorkSpace\temp_study\test_case
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # E:\WorkSpace\temp_study
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('E:\\WorkSpace\\temp_study')
# print(sys.path)

import pytest
from utils import DataHandler
from utils import HttpClient

ROOT_PATH = "E:\\WorkSpace\\temp_study"
DATA_PAHT = os.path.join(ROOT_PATH, "data")
FILE_PATH = os.path.join(DATA_PAHT, "http_get_desc.yaml")
test_suite = DataHandler.load_yaml_data(FILE_PATH).get("test_suite", [])
if not test_suite:
    raise Exception("用例读取失败，请检查数据文件")

class TestHttpGet():

    @pytest.mark.parametrize("request_desc", test_suite)
    def test_01_http_get_without_params(self, request_desc):
        '''测试get接口'''
        request_desc = request_desc
        resp = HttpClient().send_request(request_desc)
        print(resp.url)
        assert resp.status_code == 200





if __name__ == '__main__':

    pytest.main([
        "-s",
        "-v",
        os.path.abspath(__file__),
    ])
