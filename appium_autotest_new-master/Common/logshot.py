import logging
import time
import os
import allure
proj_path = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(proj_path, 'log')
logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d--%H_%M_%S')))


class Log:
    def __printconsole(self, level, message):
        """创建一个logger"""
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        """创建一个handler，用于写入日志文件"""
        fh = logging.FileHandler(logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        """再创建一个handler，用于输出到控制台"""
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        """定义handler的输出格式"""
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        """给logger添加handler"""
        logger.addHandler(fh)
        logger.addHandler(ch)

        """记录一条日志"""
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        """关闭打开的文件"""
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)


shot_path = os.path.join(proj_path,'shot')


class Shotter:
    picdict = format(time.strftime('%Y-%m-%d--%H_%M_%S'))
    error_number = 1
    pic_number = 1
    def __init__(self):
        if not os.path.exists(os.path.join(shot_path, self.picdict)):
            os.makedirs(os.path.join(shot_path, self.picdict))
    @allure.step("获取截图")
    def shot(self, driver, name=None):
        if name is not None:
            file_name = str(name)+'.png'
        else:
            file_name = 'SHOT'+str(self.pic_number)+'.png'
            self.pic_number = self.pic_number + 1
        try:
            time.sleep(0.5)
            driver.get_screenshot_as_file(os.path.join(shot_path, self.picdict, file_name))
            with open(os.path.join(shot_path, self.picdict, file_name), mode='rb') as f:
                file = f.read()
                allure.attach(file, '屏幕截图', allure.attachment_type.PNG)
        except Exception as e:
            logger.error(str(e)+'截图保存失败！')

    @allure.step("错误截图")
    def error(self,driver):
        file_name = "ERROR"+str(self.error_number)+'.png'
        picdir = os.path.join(shot_path, self.picdict,file_name)
        driver.get_screenshot_as_file(picdir)
        logger.error("截图保存为："+picdir)
        with open(os.path.join(shot_path, self.picdict,file_name), mode='rb') as f:
            file = f.read()
            allure.attach(file,'截图', allure.attachment_type.PNG)


shotter = Shotter()
logger = Log()

