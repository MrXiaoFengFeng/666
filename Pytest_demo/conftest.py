import sys

import pytest

# 默认是function
@pytest.fixture(scope='module')
def login():
    print('登录方法')
    pass


def pytest_configure(config):
    marker_list = ['search', 'login']
    for markers in marker_list:
        config.addinalue_line(
            'markers', markers
        )
