import os
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.popen('chrome.exe --remote-debugging-port=9222 --user-data-dir="e:\selenium_data"')

# options = Options()
options = Options()
options.debugger_address = '127.0.0.1:9222'
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

driver.get('https://work.weixin.qq.com/wework_admin/frame')

sleep(10)
res = driver.get_cookies()

print(res)
#
cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': 'true'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': ''},
           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': '1688855367453262'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': '1970326646997766'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': '1688855367453262'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': 'direct'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': '1'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': 'a6929334'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': '01629285'},
           {'domain': '.work.weixin.qq.com', 'expiry': 1697646429, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
            'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'en'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'sameSite': 'Lax',
            'secure': False,
            'value': 'HyPwFSB8qw-ixlMhRfbt-zEO_MwRdjnMHzlVAOWfV0TH3HPpJlDzNvmcB0f1s31l8uRRtJ0N_5DdjYjZVLvvtSLJ1JFLScgkCfqk86-2eunhHyBrvc704TmcO2JOwr6oajwY2mWenDHD7LabCVBXs95jD7W5Myf7xVSXd0EoRTzAc2TyG9LnDRc3qcYNN4QdsBqRKX-8hx3MojqRYGossJ-7-58odIO7FPVm6oBBJcySaTz0iXaktl7LJYevqFPHlen_wZptppYf_uQcHRgx7w'},
           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'sameSite': 'Lax',
            'secure': False, 'value': 'C8VHceJU6SLhvOs7m_U1tdt7M-CMJAWlgXNYYFRGA0aXzNyuIgh7nEy_EIWs9lkr'},
           {'domain': '.work.weixin.qq.com', 'expiry': 1726590420, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
            'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0'}]
sleep(5)
# db = shelve.open("cookies")
# cookies = db['cookie']

for cookie in cookies:
    if "expiry" in cookie:
        cookie.pop("expiry")
    driver.add_cookie(cookie)
    sleep(3)
# db.close()
driver.get('https://work.weixin.qq.com/wework_admin/frame')
print("ok")
print(driver.title)
driver.find_element_by_class_name("index_service_cnt_item_title").click()
