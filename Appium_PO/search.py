from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

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

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
sleep(3)
el = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText').send_keys("天气")
el.click()
# driver.find_element(MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button').click()
# driver.find_element(MobileBy.ID, 'mark.via:id/at').send_keys("天气")
driver.find_element(MobileBy.CLASS_NAME, 'android.widget.Button').click()



