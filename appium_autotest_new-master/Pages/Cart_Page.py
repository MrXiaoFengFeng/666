import os
import sys
import time
from logging import Logger
from typing import ClassVar

import allure
import yaml

from Base_Page import BasePage


class CartPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        o_path = os.getcwd()
        conf = os.path.join(o_path, 'Config', 'CartPage_conf.yml')
        file = open(conf, 'r', encoding="UTF-8")
        self.cartpage_conf = yaml.load(file)


    @allure.step("清空购物车")
    def cleanup_cart(self):
        self.mclick(self.get_element(self.elements['CartPage']['title_bar_editer_btn']))
        self.mclick(self.get_element(self.elements['CartPage']['check_allgoods_btn']))
        self.mclick(self.get_element(self.elements['CartPage']['delete']))
        self.mclick(self.get_element(self.elements['CartPage']['pos_text']))
