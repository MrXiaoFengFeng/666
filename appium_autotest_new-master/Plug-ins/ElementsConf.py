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


def read_yml():
    o_path = os.getcwd()
    conf = os.path.join(o_path, 'Config', 'Page_Elements.yml')
    file = open(conf, 'r', encoding="UTF-8")
    conf = yaml.load(file, Loader=yaml.FullLoader)
    return conf


def conf_reload(page, conf, driver):
    elements = driver.find_elements_by_xpath("//*")
    changenum = 0
    elenumber = 0
    if page not in conf:
        conf[page] = {}
    for e in elements:
        try:
            if e.get_attribute("resourceId") != None:
                elenumber = elenumber + 1
                id = e.get_attribute("resourceId")
                name = e.get_attribute("resourceId").split('/')[1]
                text = e.get_attribute("text")
                if name in conf[page]:
                    if conf[page][name]['id'] == id:
                        continue
                    else:
                        conf[page][name]['id'] = id
                        changenum = changenum + 1
                else:
                    edict = {'id': id, 'text': text}
                    conf[page][name] = edict
                    changenum = changenum = 1
                print('id = '+id)
                print('name = '+name)
                print('text = '+text)
                print('--------------------')
        except:
            print("!!!!!!!AppiumError!!!!!!!")
            print("!!Problem element has been skipped!!")
    print("{0} elements reloaded successfully,{1} elements has been collected,{2} dictionary updated,{3} elements in yaml".format(
        page, elenumber, changenum, len(conf[page])))
    return conf


def write_yml(conf):
    o_path = os.getcwd()
    file = os.path.join(o_path, 'Config', 'Page_Elements.yml')
    with open(file, "w", encoding="utf-8") as f:
        yaml.dump(conf, f, allow_unicode=True, sort_keys=False)


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

conf = read_yml()
print("Congfig yml file loaded successfully!")
keys = []
keynumber = 0
for key in conf:
    keys.append(key)
    print("{0}) {1}".format(keynumber, key))
    keynumber = keynumber + 1
page = input("Choose a page below to reload or input here a NEW PAGE NAME:")
newpage = False
try:
    page = keys[int(page)]
except:
    newpage = True
ctn = True
while ctn:
    conf = conf_reload(page, conf, driver)
    write_yml(conf)
    print("Elements on this screen has been loaded successfully")
    print("Please swipe this page and press enter to continue")
    question = input("Or type anything here to FINISH THIS RELOAD")
    if question != '':
        ctn = False
write_yml(conf)
