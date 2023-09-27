import json
from pprint import pprint

import jmespath
import yaml



class DataHandler:

    @classmethod
    def load_yaml_data(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            return yaml_data


def test_load_yaml_data():
    file_name = 'E:\\WorkSpace\\request_demo\\data\\http_get_testsuit1.yaml'
    yam_data = DataHandler.load_yaml_data(file_name)
    print(type(yam_data))
    json_yam_data = json.dumps(yam_data)

    # print(json_yam_data)
    # print(type(json_yam_data))
    json_yam_data = json.loads(json_yam_data)
    # json_yam_data = {"test_suite": [{"case_desc": "\u53d1\u9001\u5feb\u9012100\u8bf7\u6c42\u6210\u529f", "request": {"method": "post", "url": "http://www.kuaidi100.com/query", "params": "None", "data": {"type": "shunfeng", "postid": "SF1631643020688"}}, "extract": {"session": "cookies.Session"}, "validate": [{"key_word": "eq", "actual_data": "json.status", "expect_data": "200", "msg": "POST\u8bf7\u6c42\u76f8\u5e94\u7684\u72b6\u6001\u7801\u5931\u8d25"}]}]}
    extract_data = jmespath.search("test_suite[0].extract", json_yam_data)

    pprint(extract_data)
    # pprint(json_yam_data)


if __name__ == '__main__':
    import pytest
    import os
    pytest.main(['-s', '-v', os.path.abspath(__file__)])


