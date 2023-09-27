import os
import sys
import time
from logging import Logger

import allure
import yaml

from Base_Page import BasePage


class GoodPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        o_path = os.getcwd()
        conf = os.path.join(o_path, 'Config', 'GoodPage_conf.yml')
        file = open(conf, 'r', encoding="UTF-8")
        self.goodpage_conf = yaml.load(file)

    def add_cart(self):
        try:
            self.get_element(
                self.elements['GoodPage']['action_text_org']).click()
            return True
        except Exception as e:
            Logger.error(e)
            return False

    @allure.step("还原状态")
    def reset(self):
        self.mishoop_open()
        time.sleep(1)
        self.go_page(self.goodpage_conf["path"])

    @allure.step("检查价格是否显示正常")
    def check_value(self, lst):
        try:
            for ls in lst:
                if ls not in self.elements['GoodPage']:
                    raise KeyError
                if self.get_element(self.elements['GoodPage'][ls]).text[1:] != str(self.goodpage_conf[ls]):
                    raise ValueError
        except KeyError:
            Logger.error("没有id为"+ls+"的数据！")
            return False
        except ValueError:
            Logger.error(ls+"的数据出错")
            return False
        return True
    
    @allure.step("滑动轮播图")
    def swipe_pic(self):
        try:
            num_id = self.get_element(
                    self.elements['GoodPage']['imageNum'])
            pic_id = self.get_element(
                self.elements['GoodPage']['gallery_viewpager'])
            pic_num = num_id.text
            pic_num = list(map(int, pic_num.split("/")))
            while pic_num[0] < pic_num[1]:
                self.mswipe("right", element=pic_id)
                pic_num = num_id.text
                pic_num = list(map(int, pic_num.split("/")))
            return True
        except Exception as e:
            Logger.error(e)
            return False