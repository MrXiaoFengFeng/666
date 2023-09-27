
from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.baidu.searchbox'
desired_caps['appActivity'] = '.MainActivity'
desired_caps['automationName'] = 'Uiautomator2'
# desired_caps['skipServerInstallation'] = 'true'

# desired_caps['appium:unicodeKeyboard'] = 'True'
# desired_caps['appium:resetKeyboad'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.quit()

# from appium import webdriver
# from appium.options.common import AppiumOptions
#
# option = AppiumOptions()
# option.set_capability('platformName','android')
# driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
#                           options=option)
# from appium import webdriver

# # 配置Appium服务器的地址和端口
# appium_server = "http://127.0.0.1:4723/wd/hub"

# # 配置移动设备或模拟器的Desired Capabilities
# capabilities = {
#     "platformName": "Android",  # 平台名称：Android 或 iOS
#     "deviceName": "127.0.0.1:62001",  # 设备名称
#     "appPackage": "com.baidu.searchbox",  # 应用程序的包名
#     "appActivity": ".MainActivity"  # 应用程序的启动活动
# }

# # 创建WebDriver对象，并连接到Appium服务器
# driver = webdriver.Remote(appium_server, capabilities)

# # 启动应用程序
# driver.launch_app()


# import unittest
# from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy

# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='Android',
#     appPackage='com.android.settings',
#     appActivity='.Settings',
#     language='en',
#     locale='US'
# )

# appium_server_url = 'http://localhost:4723'
# driver = webdriver.Remote(appium_server_url, capabilities)

# class TestAppium(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Remote(appium_server_url, capabilities)

#     def tearDown(self) -> None:
#         if self.driver:
#             self.driver.quit()

#     def test_find_battery(self) -> None:
#         el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
#         el.click()

# if __name__ == '__main__':
#     unittest.main()