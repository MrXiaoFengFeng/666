import yaml



class DataHandler:

    @classmethod
    def load_yaml_data(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            return yaml_data


def test_load_yaml_data():
    file_name = 'E:/WorkSpace/request_demo/data/http_get_testsuit.yaml'
    yam_data = DataHandler.load_yaml_data(file_name)
    print(yam_data)







if __name__ == '__main__':
    import pytest
    import os
    pytest.main(['-s', '-v', os.path.abspath(__file__)])
