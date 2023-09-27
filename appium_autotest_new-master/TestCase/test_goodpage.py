from Pages.Good_Page import GoodPage
from Common.logshot import Shotter, logger
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
def goodpage(base_driver):
    goodpage = GoodPage(base_driver)
    return goodpage

@pytest.fixture(scope = 'function', autouse=True)
def before(goodpage):
    goodpage.reset()

class TestOP:

    @allure.title("检查价格数据")
    def test_price(self, goodpage):
        assert goodpage.check_value(["price", "market_price"])

    @allure.title("检查轮播图情况")
    def test_pic(self, goodpage):
        if goodpage.goodpage_conf['hasvideo']:
            pic = goodpage.get_element(goodpage.elements['GoodPage']['text'])
            pic.click()
        assert goodpage.swipe_pic()

    @allure.title("版本价格显示测试")
    def test_detail_price(self, goodpage):
        goodpage.add_cart()
        time.sleep(1)
        for i in range(1, len(goodpage.goodpage_conf['detailprice'])+1):
            model = goodpage.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView")
            model.click()
            detail = model.text
            page_price = goodpage.get_element(
                goodpage.elements['GoodPage']['goods_price']).text
            page_marketprice = goodpage.get_element(
                goodpage.elements['GoodPage']['market_price']).text
            assert page_price[1:] == str(
                goodpage.goodpage_conf['detailprice'][detail][0])
            assert page_marketprice[1:] == str(
                goodpage.goodpage_conf['detailprice'][detail][1])
