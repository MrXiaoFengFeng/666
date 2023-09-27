# 通过index 页面，进行测试用例的组装
import os
import sys

import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from page.index import Index


class Test_Index:
    # 初始化
    def setup(self):
        self.index = Index()


    def test_login(self):
        self.index.goto_login().login().free()

    def test_free(self):
        self.index.goto_free().free()

    def teardown(self):
        self.index.close()

if __name__ == '__main__':
    pytest.main(["-vs", os.path.abspath(__file__)])
