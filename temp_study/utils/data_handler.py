import yaml


class DataHandler:

    @classmethod
    def load_yaml_data(cls, file_name):
        """
        读取yaml文件
        :param file_name: 文件路径
        :return: dict or list
        """
        with open(file_name, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data


def test_load_yaml_data():
    file_name = "E:/WorkSpace/temp_study/data/http_get_desc.yaml"
    yaml_data = DataHandler.load_yaml_data(file_name)
    print(yaml_data)


if __name__ == '__main__':
    import os
    import pytest

    pytest.main(["-s", "-v", os.path.abspath(__file__)])
