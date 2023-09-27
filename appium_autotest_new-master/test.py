from appium import webdriver

desired_caps = {
               "platformName": "Android",
               "platformVersion": "11",
               "deviceName": "10.220.47.149:41473",  #真机设备名称  通过adb devices获取
               "noReset": False
              }
driver = webdriver.Remote('http://10.220.73.233:4723/wd/hub', desired_caps)
driver.start_activity('com.xiaomi.shop', '.activity.MainTabActivity')