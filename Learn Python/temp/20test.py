'''
基本需求 90%
1 统计本日志文件的总pv、uv
2 列出全天每小时的pv、uv数
3 列出top 10 uv的IP地址，以及每个ip的pv点击数
4 列出top 10 访问量最多的页面及每个页面的访问量
5 列出访问来源的设备列表及每个设备的访问量
日志格式说明
注意：网络日志文件在课件中，请先下载课件

名词解释：
pv:page visit , 页面访问量，一次请求就是一次pv
uv: user visit, 独立用户，一个ip就算一个独立用户
注意：没有ip的可以认为是异常日志，不用统计！
'''

# 过滤出所有的IP地址
import re
import os

# BASE_DIR = os.path.dirname(__file__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)



FILE_PATH = r'testlog.txt'

# E:\WorkSpace\Learn Python\0920\file\test1\newtestlog.txt
LOG_PATH = os.path.join(BASE_DIR, FILE_PATH)
# NEWLOG_PATH = os.path.join(BASE_DIR, NEWFILE_PATH)
print(LOG_PATH)
#
#
#
# with open(FILE_PATH, mode='rt', encoding='utf-8') as f, \
#         open(NEWFILE_PATH, mode='wt', encoding='utf-8') as f1:
#     def cunt_num():
#         pv_num = 0
#         uv_num = 0
#         pv_key = 'GET'
#         uv_key = 'POST'
#         for line in f:
#             # print(line)
#
#             # 统计文本PV总数
#             if pv_key in line:
#                 pv_num += 1
#
#             # 统计文本UV总数
#             if uv_key in line:
#                 uv_num += 1
#         print(f'统计本日志文件的总PV数为：{pv_num}')
#         print(f'统计本日志文件的总UV数为：{uv_num}')
#
#
#     # cunt_num()
#
#     # def per_hour_num():
#     #     for i in range(0, 24):
#     #         print(f'{i}点到{i + 1}的时间数据为X')
#
#     # 所有iplist
#     # def ip_list():
#     #     for line in f:
#     #         ip = str(re.findall('^[1-6]\d+\.\d*\.\d*\.\d*', line))
#     #         # print(ip)
#     #         # 过滤所有的ip地址
#     #         f1.write(ip + '\n')
#     #
#     # ip_list()
#     # # print('122.71.241.175' in ip_list())
#     # #统计ip计数
#     # ip_cunt = 0
#     # for line1 in f1.readline():
#     #         if ip in line1:
#


