import json
from pprint import pprint

import jmespath
import yaml

file_name = 'E:\\WorkSpace\\request_demo\\data\\http_get_testsuit1.yaml'
def test_load_yaml_data():
    with open(file_name, 'r', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)

        print(type(yaml_data))
        json_yaml_data = json.dumps(yaml_data)

        print(json_yaml_data)
        print(type(json_yaml_data))
        # json_yaml_data = {"test_suite": [{"case_desc": "\u53d1\u9001\u5feb\u9012100\u8bf7\u6c42\u6210\u529f", "request": {"method": "post", "url": "http://www.kuaidi100.com/query", "params": "None", "data": {"type": "shunfeng", "postid": "SF1631643020688"}}, "extract": {"session": "cookies.Session"}, "validate": [{"key_word": "eq", "actual_data": "json.status", "expect_data": "200", "msg": "POST\u8bf7\u6c42\u76f8\u5e94\u7684\u72b6\u6001\u7801\u5931\u8d25"}]}]}
        extract_data = jmespath.search("test_suite[].extract", json_yaml_data)

        pprint(extract_data)

test_load_yaml_data()