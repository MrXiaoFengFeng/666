import os
import sys
import time
from logging import Logger

import allure
import yaml

from Base_Page import BasePage


class IndexPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        o_path = os.getcwd()
        conf = os.path.join(o_path, 'Config', 'IndexPage_conf.yml')
        file = open(conf, 'r', encoding="UTF-8")
        self.indexpage_conf = yaml.load(file)

    def reset(self):
        self.mishoop_open()
        time.sleep(1)

    @allure.step("进入分类页")
    def to_category(self):
        self.get_element(self.elements['IndexPage']
                         ['main_bottom_category']).click()

    @allure.step("进入发现页")
    def to_discovery(self):
        self.get_element(self.elements['IndexPage']
                         ['main_bottom_discovery']).click()

    @allure.step("进入购物车页")
    def to_cart(self):
        self.get_element(self.elements['IndexPage']
                         ['main_bottom_cart']).click()

    @allure.step("进入个人页")
    def to_mine(self):
        self.get_element(self.elements['IndexPage']
                         ['main_bottom_mine']).click()

    @allure.step("进入首页")
    def to_home(self):
        self.get_element(self.elements['IndexPage']
                         ['main_bottom_home']).click()

    @allure.step("进入搜索页")
    def to_search(self):
        self.get_element(self.elements['IndexPage']['switcher']).click()
