import pytest
import os
import time
import re
import yaml
from selenium.webdriver.remote.errorhandler import ErrorCode
from appium import webdriver


def get_infos(devices):
    server_port = 5023
    system_port = 8211
    infos = []
    index = 0
    for i in devices:
        caps = {}
        caps["index"] = index
        caps["deviceName"] = i[0]
        caps["platform_version"] = i[1]
        index = index + 1
        infos.append(caps)
    return infos


def get_devices():
    str_init = ' '
    all_info = os.popen('adb devices').readlines()
    for i in range(len(all_info)):
        str_init += all_info[i]
    devices_name = re.findall('\n(.+?)\t', str_init, re.S)
    devices = []
    for i in devices_name:
        devices_platform = os.popen(
            'adb -s '+i+' shell getprop ro.build.version.release').read().split('\n')[0]
        devices.append((i, devices_platform))
    return devices



def read_yml():
    o_path = os.getcwd()
    conf = os.path.join(o_path, 'Config', 'PluginsId.yml')
    file = open(conf, 'r', encoding="UTF-8")
    conf = yaml.load(file, Loader=yaml.FullLoader)
    return conf



def write_yml(conf):
    o_path = os.getcwd()
    file = os.path.join(o_path, 'Config', 'PluginsId.yml')
    with open(file, "w", encoding="utf-8") as f:
        yaml.dump(conf, f, allow_unicode=True, sort_keys=False)

def get_driver(device_info, port):
    caps = {}
    caps['deviceName'] = device_info['deviceName']
    caps['platform_version'] = device_info['platform_version']
    caps['platformName'] = 'Android'
    caps["noReset"] = True
    caps["automationName"] = "UiAutomator2"
    cmd = "start appium -p {0} -bp {1} -U {2}".format(
        port, port+1, device_info["deviceName"])
    os.system(cmd)
    driver = webdriver.Remote("http://127.0.0.1:{0}/wd/hub".format(port), caps)
    return driver


conf = read_yml()
device_infos = get_infos(get_devices())
for device in device_infos:
    print(device)
choose = int(input("choose a device(input the index):"))
if choose >= len(device_infos) or choose < 0:
    print("Error Index!! Already choose the first device instead!")
    choose = 0
port = input("Set appium port:(defult:4723):")
if not isinstance(port, int):
    port = 4723
driver = get_driver(device_infos[choose], port)
print('Device connected successfully!')
id = int(input("Input start id:"))
next = True
while True:
    os.popen("adb -s {0} shell am force-stop com.xiaomi.shop".format(device_infos[choose]['deviceName']))
    time.sleep(1)
    os.popen("adb -s {0} shell am start -n com.xiaomi.shop/com.xiaomi.shop2.plugin.PluginRootActivity --es pluginId {1}".format(device_infos[choose]['deviceName'], str(id)))
    time.sleep(1)
    try:
        e = driver.find_element_by_id("com.xiaomi.shop:id/loadingview_txterror")   
        if e:
            print ('pass id {0}'.format(id))
            id = id + 1
            continue
    except:
        text= input("Input:")
        if text == '':
            id = id + 1
            continue
        conf[id] = text
        id = id + 1
        write_yml(conf)
