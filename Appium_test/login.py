import time

from appium import webdriver
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

#apk_file = os.path.join(os.path.dirname(__file__), 'app/腾讯会议.apk')

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0.1',
    'deviceName': '127.0.0.1:7555',
    'appPackage': 'com.xueqiu.android',
    'appActivity': '.view.WelcomeActivityAlias',
    'automationName': 'UiAutomator2',
    'unicodeKeyboard': True,
    'resetKeyboad': True,

    'noReset': False,
    'autoAcceptAlerts': True,
    #'app': apk_file

}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

# driver.find_element(AppiumBy.ID,'com.tencent.wemeet.app:id/fn').click()
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("同意")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.tencent.wemeet.app:id/fn").text("同意")').click()
# driver.wait_activity('com.tencent.wemeet.module.splash.activity.NewUserGuideActivity',13,1)

WebDriverWait(driver, 3, 1).until(lambda x: x.find_element(AppiumBy.ID, 'com.tencent.wemeet.app:id/axb')).click()
# e = WebDriverWait(driver,2,0.5,).until(EC.presence_of_element_located(loc))
# # d.xpath('//android.widget.FrameLayout[2]')
# # time.sleep(20)
# print(2222)
# window_size = driver.get_window_size()
# x = window_size['width']
# y = window_size['height']
# print(33)
# time.sleep(15)
# # 左滑4次
# for i in range(0, 6):
#     driver.swipe(start_x=x * 0.9,
#                  start_y=y * 0.5,
#                  end_x=x * 0.3,
#                  end_y=y * 0.5,
#                  duration=3000)
#

time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//*[@text = "微信登录"]').click()
time.sleep(1)
# driver.find_element(AppiumBy.XPATH,'//*[@id = "com.tencent.wemeet.app:id/fw" and @class = "android.widget.CheckBox"]').click()
tip = driver.find_element(AppiumBy.XPATH, '//android.widget.Toast')
print(tip.text)
# time.sleep(1)
# driver.find_element(AppiumBy.XPATH,'//*[@id = "com.tencent.wemeet.app:id/iw"]').click()
# driver.find_element(AppiumBy.XPATH,'//*[@id = "com.tencent.wemeet.app:id/fw"]').click()
# time.sleep(1)
# driver.find_element(AppiumBy.XPATH,'//*[@text = "使用帐号密码登录"]').click()
