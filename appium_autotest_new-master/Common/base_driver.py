from appium import webdriver
import yaml, os
import socket



class BaseDriver:



    def __init__(self, device_info):
        self.device_info = device_info
        cmd = "appium -p {0} -bp {1} -U {2}".format(self.device_info["server_port"], self.device_info["server_port"]+1, self.device_info["deviceName"])
        port = device_info["server_port"]
        if not self.check_port_in_use(int(port)):
            os.system(cmd)

    def check_port_in_use(self, port):
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect(('127.0.0.1', int(port)))
            return True
        except socket.error:
            return False
        finally:
            if s:
                s.close()

    def get_base_driver(self, noRest=False):
        o_path = os.getcwd()
        conf = os.path.join(o_path, 'Config', 'Appium_Caps.yml')
        fs = open(conf, encoding="utf-8")
        desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
        desired_caps["platformVersion"] = self.device_info["platform_version"]
        desired_caps["deviceName"] = self.device_info["deviceName"]
        desired_caps["systemPort"] = self.device_info["system_port"]
        desired_caps["automationName"] = "UiAutomator2"
        if noRest == True:
            desired_caps["noReset"] == True

        driver = webdriver.Remote("http://127.0.0.1:{0}/wd/hub".format(self.device_info["server_port"]), desired_caps)
        return driver
