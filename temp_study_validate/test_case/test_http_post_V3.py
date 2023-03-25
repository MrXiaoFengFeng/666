import os
import sys

import pytest
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from utils import DataHandler
from utils.http_client_V3 import HttpClient

ROOT_PATH = "E:\\WorkSpace\\temp_study_validate"
DATA_PAHT = os.path.join(ROOT_PATH, "data")
FILE_PATH = os.path.join(DATA_PAHT, "02_http_post_desc.yaml")
test_suite = DataHandler.load_yaml_data(FILE_PATH).get("test_suite", [])
if not test_suite:
    raise Exception("用例读取失败，请检查数据文件")



class TestHttpPost():

    @pytest.mark.parametrize("request_desc", test_suite)
    def test_01_http_post_with_json_success(self, request_desc):
        request_desc = request_desc
        HttpClient(request_desc)


        # print(resp.url)
        # assert resp.status_code == 200




if __name__ == '__main__':
    import os

    pytest.main([
        "-s",
        "-v",
        os.path.abspath(__file__),
    ])
