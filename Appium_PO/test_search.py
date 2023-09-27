import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_SearchPage:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'mark.via'
        desired_caps['appActivity'] = '.Shell'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboad'] = 'True'
        # 更新弹窗，true就是不重置app
        desired_caps['noReset'] = 'True'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(8)
    def teardown(self):
        self.driver.quit()
    def test_search(self):
        print("搜索测试用例")
        """
        1.打开 Via 浏览器 app
        2.点击搜索输入框
        3.输入框输入“天气”
        4.点击搜索按钮
        """
        el = self.driver.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText')
        el.click()
        el.send_keys("天")

        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("天秤座")').click()
        # self.driver.find_element(MobileBy.XPATH, "//*[android.view.View[3]/android.view.View/android.view.View[3]/android.view.View]").click()
        self.driver.find_element(MobileBy.XPATH, "//android.view.View[@text=\'天秤座\']").click()

        # el.click()
        # driver.find_element(MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button').click()
        # driver.find_element(MobileBy.ID, 'mark.via:id/at').send_keys("天气")
        # self.driver.find_element(MobileBy.CLASS_NAME, 'android.widget.Button').click()



if __name__ == '__main__':
    pytest.main()