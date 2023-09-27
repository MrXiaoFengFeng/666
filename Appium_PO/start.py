from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0.1.0'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.baidu.searchbox'
desired_caps['appActivity'] = '.MainActivity'
desired_caps['automationName'] = 'Uiautomator2'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboad'] = 'True'
# 更新弹窗，true就是不重置app
desired_caps['noReset'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
#
driver.find_element(AppiumBy.ID, 'com.baidu.searchbox:id/obfuscated').click()

driver.find_element(AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element(AppiumBy.ID, 'com.baidu.searchbox:id/obfuscated').click()

