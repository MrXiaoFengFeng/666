import logging

# 默认级别为warning，默认打印到终端，warning以上都会打印
# logging.debug('调试debug')  # 默认级别10
# logging.info('消息info')  # 默认级别20
# logging.warning('警告warning')  # 默认级别30
# logging.error('错误error')  # 默认级别40
# logging.critical('严重critical')  # 默认级别50
# 输出结果
# WARNING:root:警告warning
# ERROR:root:错误error
# CRITICAL:root:严重critical

# file = open(r'file/access1.log', mode='w', encoding='utf-8')
logging.basicConfig(
    #1.日志输出位置：1、终端 2.文件
    filename=r'file/access1.log',  # 不定义此项会默认输出到终端窗口。定义了此项后会输出到文件。遗留问题：中文乱码
    # stream=file,  # 输出流
    #日志格式
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
    #时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p',
    #日志级别
    level=logging.DEBUG
    #等同于：level=10
)

logging.debug('调试bug')
logging.info('消息info')
logging.warning('警告warning')
logging.error('错误error')
logging.critical('严重critical')
