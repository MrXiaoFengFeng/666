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

    print(json_yam_data)
    print(type(json_yam_data))
    extract_data = jmespath.search("test_suite[0].extract.session", json_yam_data)
    pprint(extract_data)


if __name__ == '__main__':
    import pytest
    import os
    pytest.main(['-s', '-v', os.path.abspath(__file__)])


