# 拿到日志的产生者，即loggers
# 第一个日志的产生者：kkk
# 第一个日志的产生者：bbb

# 但是需要先导入日志配置字典：LOGGING_DIC

import settings # 运行时18_02settings更名为setting
# import 18_02settings
from logging import config,getLogger

# import logging.config
# logging.config.dictConfig(settings.LOGGING_DIC)
# print(logging.getLogger())

config.dictConfig(settings.LOGGING_DIC)
# logger1 = getLogger('标准日志')  #终端和文件都展示'handlers': ['default', 'console']
#
# logger1.info('这是一条logger1的info信息')

# logger2 = getLogger('bbb')  #只展示到文件'handlers': ['other',]
# logger2.debug('这是一条logger2的debug信息')

# logger3 = getLogger('ccc')  # 'handlers': ['console',] 仅屏幕打印
# logger3.info('这是一条logger3的info信息')

#setting字典中保留一个空日志名，若取的名称不在字典中，则传取的名称[task_id:默认日志]
logger4 = getLogger('默认日志1')  # 'handlers': ['default',]
logger4.info('这是一条logger4的info信息')




# 补充两个重要额外知识
#1.日志名的命名
# 日志名是区别日志业务归属的一种非常重要的标识


# 2.日志轮转
# 日志中记录着程序员运行过程中的关键信息
# 'class': 'logging.handlers.RotatingFileHandler'
# 新增的内容默认存在配置指定的a1.log文件中，超出字节的部分存在a1.log.1自动生成的备份中
# 'maxBytes': 5,  # 日志大小 5M
# 'backupCount': 5  #超出备份数目，有新增默认删除最早的那个