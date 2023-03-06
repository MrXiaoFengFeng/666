'''
此处存放固定的配置信息
'''

import os

# 获取项目根目录reader_sys根目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# 获取db目录路径
DB_PATH = os.path.join(BASE_PATH, 'db')

# 获取db.txt的根目录
DB_TXT_PATH = os.path.join(DB_PATH, 'db.txt')

# 获取story_class的根目录
STORY_CLASS_PATH = os.path.join(DB_PATH, 'story_class.txt')

# 小说存放目录
FICTIONS_PATH = os.path.join(BASE_PATH, 'fictions')

# 日志文件存放的路径
LOG_PATH = os.path.join(BASE_PATH, 'log', 'log.txt')
