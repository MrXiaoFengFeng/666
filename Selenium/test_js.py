import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestJs:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()
    @pytest.mark.skip
    def test_js(self):
        self.driver.get("https://baidu.com")
        self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("123456")

        # js获取元素
        # 第一种写法：
        submite_element = self.driver.execute_script("return document.querySelector('#su')")
        # 第二种写法：
        # submite_element = self.driver.execute_script("return document.getElementById('su')")


        submite_element.click()
        sleep(3)
        # 页面滚动到底部方式1：
        self.driver.execute_script("document.documentElement.scrollTop=100000")
        # 页面滚动到底部方式2：
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        # 页面滚动到顶部方式1：
        self.driver.execute_script("document.documentElement.scrollTop=0")
        # 页面滚动到顶部方式2：
        # self.driver.execute_script("window.scrollTo(0, 0);")


        # 循环执行js代码(获取js执行后的数据需加return)
        # document.title--》获取页面标题 JSON.stringify(performance.timing)--》获取页面加载性能数据
        for code in [
            "return document.title", "return JSON.stringify(performance.timing)"
        ]:
            print(self.driver.execute_script(code))

        # 第二种写法：
        # print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))

    # 时间模块选择不可修改时处理。readonly="readonly"
    @pytest.mark.skip
    def test_change_time(self):
        self.driver.get("https://trains.tieyou.com/")
        self.driver.find_element(By.XPATH,"//*[@id='home-page-less']/div[2]/div/div[1]/form/div/div[1]/input").send_keys("北京")
        self.driver.find_element(By.XPATH,"//*[@id='home-page-less']/div[2]/div/div[1]/form/div/div[2]/input").send_keys("北京")
        self.driver.find_element(By.XPATH,"//*[@id='divAppBanner']").click()


        # 定位到元素，然后取消只读属性

        self.driver.execute_script(
            "return a=document.getElementsByClassName('calendar-input input_txt270');a.removeAttribute(readonly)"
        )

        sleep(5)



        # 修改value值
        self.driver.execute_script(
            "a=document.getElementsByClassName('calendar-input input_txt270').value='2023-04-15'")
        sleep(5)
        print(self.driver.execute_script(
            "return a=document.getElementsByClassName('calendar-input input_txt270').value"))
        sleep(5)
        self.driver.execute_script("window.alert('hhh')")
        sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#searchbtn").click()
        sleep(5)

    @pytest.mark.skip
    def test_change_time1(self):
        # self.driver.get("https://www.12306.cn/index/")
        # # self.driver.find_element(By.XPATH,'//*[@id="fromStationText"]').send_keys("北京")
        # # self.driver.find_element(By.XPATH,'//*[@id="toStationText"]').send_keys("北京")
        # # document.getElementById('train_date')
        # sleep(3)
        # self.driver.execute_script(
        #     "return a=document.getElementById('train_date');a.Node('aria-label').value='2023-04-06'"
        # )
        #
        # self.driver.find_element(By.XPATH, '//*[@id="search_one"]').click()
        self.driver.get("http://jqueryui.com/resources/demos/datepicker/other-months.html")
        self.driver.find_element_by_id('datepicker').send_keys("10/16/2022")
        sleep(5)



    def test_change_time2(self):
        self.driver.get("https://trains.tieyou.com/")
        self.driver.find_element(By.XPATH,"//*[@id='home-page-less']/div[2]/div/div[1]/form/div/div[1]/input").send_keys("北京")
        self.driver.find_element(By.XPATH,"//*[@id='home-page-less']/div[2]/div/div[1]/form/div/div[2]/input").send_keys("北京")
        self.driver.find_element(By.XPATH,"//*[@id='divAppBanner']").click()



        # js = "$('document.getElementsByClassName('calendar-input input_txt270')').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        self.driver.execute_script("a=document.getElementsByClassName('calendar-input input_txt270');a.removeAttribute('readonly')")
        sleep(5)
        self.driver.execute_script("window.alert('oooo')")
        self.driver.execute_script(
            "document.getElementsByClassName('calendar-input input_txt270').value='2023-04-15'")
        sleep(5)
        print(self.driver.execute_script(
            "return document.getElementsByClassName('calendar-input input_txt270').value"))
        sleep(5)
        self.driver.execute_script("window.alert('hhh')")
        sleep(10)









if __name__ == '__main__':
    pytest.main(["-v", "-s", os.path.abspath(__file__)])