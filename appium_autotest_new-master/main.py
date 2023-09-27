import pytest
import os
import time
import re
from multiprocessing import Pool


def get_infos(devices):
    server_port = 4723
    system_port = 8211
    infos = []
    for i in devices:
        caps = {}
        caps["deviceName"] = i[0]
        caps["platform_version"] = i[1]
        caps["server_port"] = server_port
        caps["system_port"] = system_port
        server_port = server_port + 2
        system_port = system_port + 2
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


device_infos = get_infos(get_devices())


def run_parallel(device_info):
    name = device_info["deviceName"]
    pytest.main([f"--cmdopt={device_info}",
                 "--alluredir", "allure-results"])


if __name__ == "__main__":
    n = len(device_infos)
    with Pool(n) as pool:
        pool.map(run_parallel, device_infos)
        pool.close()
        pool.join()
