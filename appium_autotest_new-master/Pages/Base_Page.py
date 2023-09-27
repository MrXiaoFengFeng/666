import os
import re
import sys

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy as By
from Common.logshot import logger, shotter
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o_path = os.getcwd()
sys.path.append(o_path)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.package = 'com.xiaomi.shop'
        self.main_activity = '.activity.MainTabActivity'
        self.welcome_activity = '.activity.MainActivity'
        o_path = os.getcwd()
        conf = os.path.join(o_path, 'Config', 'Page_Elements.yml')
        file = open(conf, 'r', encoding="UTF-8")
        self.elements = yaml.load(file)

    @allure.step("从本地字典获取元素信息")
    def get_element(self, ele_conf):
        shotter.shot(self.driver)
        ele_id = ele_conf['id']
        ele_text = ele_conf['text']
        ids = WebDriverWait(self.driver, 2).until(
            lambda x: x.find_elements_by_id(ele_id))
        try:
            if len(ids) > 1 and ele_text != '':
                texts = WebDriverWait(self.driver, 2).until(
                    lambda x: x.find_elements_by_xpath('//*[@text="' + ele_text + '"]'))
                if len(ids) > len(texts):
                    return texts[0]
                else:
                    return ids[0]
            elif len(ids) == 1:
                return ids[0]
            else:
                texts = WebDriverWait(self.driver, 2).until(
                    lambda x: x.find_elements_by_xpath('//*[@text="' + ele_text + '"]'))
                return texts[0]
        except Exception as e:
            logger.error(e)
            return None

    @allure.step("获取屏幕尺寸")
    def get_phone_size(self):
        try:
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
        except Exception as e:
            logger.error(e)
            return
        return x, y

    @allure.step("向{direction}滑动屏幕")
    def mswipe(self, direction, element=None, n=1):
        MAX_EDGE_LIMIT = 80
        if element is None:     # 屏幕中心点击
            screen_size = self.get_phone_size()
            x_middle = int(screen_size[0] * 0.5)
            y_middle = int(screen_size[1] * 0.5)
            x_left = int(screen_size[0] * 0.25)
            x_right = int(screen_size[0] * 0.75)
            y_up = int(screen_size[1] * 0.25)
            y_down = int(screen_size[1] * 0.75)
            from_x = x_middle
            from_y = y_middle
            if direction == "up":
                to_x = x_middle
                from_y = y_down
                to_y = y_up
            elif direction == "down":
                from_y = y_up
                to_x = x_middle
                to_y = y_down
            elif direction == "left":
                from_x = x_right
                to_x = x_left
                to_y = y_middle
            elif direction == "right":
                from_x = x_left
                to_x = x_right
                to_y = y_middle
            else:
                logger.error("滑动函数方向设置错误！")
                return False
        else:
            right_limit = self.get_phone_size()[0] - MAX_EDGE_LIMIT
            left_limit = MAX_EDGE_LIMIT  # 防止误触返回手势
            x_left_up = int(element.location['x'] * 1.1)
            if x_left_up < left_limit:
                x_left_up = left_limit
            y_left_up = int(element.location['y'] * 1.1)
            x_right_down = int(
                (element.location['x'] + element.size['width']) * 0.9)
            if x_right_down > right_limit:
                x_right_down = right_limit
            y_right_down = int(
                (element.location['y'] + element.size['height']) * 0.9)
            x_middle = int((x_left_up + x_right_down) / 2)
            y_middle = int((y_left_up + y_right_down) / 2)
            if direction == "up":
                from_x = x_left_up
                to_x = x_right_down
                from_y = y_left_up
                to_y = y_right_down
            elif direction == "down":
                from_x = x_right_down
                to_x = x_left_up
                from_y = y_right_down
                to_y = y_left_up
            elif direction == "left":
                from_x = x_left_up
                to_x = x_right_down
                from_y = y_middle
                to_y = y_middle
            elif direction == "right":
                from_x = x_right_down
                to_x = x_left_up
                from_y = y_middle
                to_y = y_middle
            else:
                logger.error("滑动函数方向设置错误！")
                return False
        try:
            for i in range(n):
                self.driver.swipe(from_x, from_y, to_x, to_y)
        except Exception as e:
            logger.error(e)

    @allure.step("滑动屏幕，从{start_x}{start_y}到{end_x}{end_y}")
    def start_end_slide(self, start_x, start_y, end_x, end_y):
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y)
        except Exception as e:
            logger.error(e)

    @allure.step("获取{id}位置")
    def get_id_pos(self, id):
        e = None
        shotter.shot(self.driver)
        try:
            e = WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_id(id))
        except Exception as error:
            logger.error(str(error) + "没有找到id为" + id + "的元素!")
            e = None
        return e

    @allure.step("点击元素{e}")
    def mclick(e):
        try:
            e.click()
            return True
        except Exception as error:
            logger.error(str(error) + "点击空元素！")
            return False

    @allure.step("查找文本信息为{keyword}的元素")
    def find_text(self, keyword):
        shotter.shot(self.driver)
        try:
            pos = WebDriverWait(self.driver, 2).until(
                lambda x: x.find_elements_by_xpath('//*[@text="' + keyword + '"]'))
            return pos
        except Exception as e:
            logger.error(str(e))
            return None

    @allure.step("点击文本信息为{keyword}的元素")
    def touch_text(self, text):
        try:
            element = self.find_text(text)
            if len(element) > 1:
                logger.debug("此页面关于" + text + "的文本有多个，默认选择第一个进行点击")
            element[0].click()
            return True
        except Exception as error:
            logger.error(error)
            return False

    @allure.step("返回上级")
    def send_back_key(self):
        try:
            self.driver.press_keycode(4)
        except Exception as e:
            logger.error(str(e) + "发送返回失败，请参考错误信息！")

    @allure.step("在当前界面滑动屏幕向{direction}寻找文字信息为{text}的元素")
    def swipe_find(self, text, direction="up", MAX_TRY_TIME=10):
        shotter.shot(self.driver)
        try:
            while self.find_text(text) is None:
                self.mswipe(direction)
                MAX_TRY_TIME = MAX_TRY_TIME - 1
                if MAX_TRY_TIME < 0:
                    raise ValueError
        except ValueError:
            logger.error("没有找到" + text)
            shotter.error(self.driver)
        finally:
            element = self.find_text(text)
            return element

    @allure.step("获取元素{element}的信息")
    def get_text(element):
        try:
            return element.text
        except Exception as e:
            logger.error(str(e)+"获取不到该元素的文本信息")
            return False

    @allure.step("执行ADB shell{shell}")
    def adb_shell(self, shell):
        device = self.driver.session['deviceName']
        msg = os.popen("adb -s "+device+" shell "+shell).read().split('\n')
        return msg

    @allure.step("打开小米商城app")
    def mishoop_open(self):
        self.driver.start_activity(self.package, self.main_activity)

    @allure.step("前往目标页面")
    def go_page(self, pth):
        try:
            for p in pth:
                nxt = self.find_text(p)
                nxt[0].click()
            return True
        except Exception as e:
            logger.error(e)
            shotter.error(self.driver)
            return False

    @allure.step("点击目标id")
    def click_id(self, id):
        pos = self.get_id_pos(id)
        try:
            pos.click()
            return True
        except:
            return False
