from Pages.Index_Page import IndexPage
from Common.logshot import shotter, logger
from conftest import base_driver
import time
import pytest
import allure
import os
import sys
o_path = os.getcwd()
pg_path = os.path.join(o_path, "Pages")
cm_path = os.path.join(o_path, "Common")
sys.path.append(o_path)
sys.path.append(pg_path)
sys.path.append(cm_path)


@pytest.fixture()
def indexpage(base_driver):
    indexpage = IndexPage(base_driver)
    return indexpage


@pytest.fixture(scope = 'function', autouse=True)
def before(indexpage):
    indexpage.reset()

class TestOP:

    @allure.title("检查切换1")
    def test_switch11(self, indexpage):
        indexpage.to_cart()
        shotter.shot(indexpage.driver)


    @allure.title("检查切换2")
    def test_switch22(self, indexpage):
        indexpage.to_category()
        shotter.shot(indexpage.driver)

    @allure.title("检查切换3")
    def test_switch33(self, indexpage):
        indexpage.to_mine()
        shotter.shot(indexpage.driver)