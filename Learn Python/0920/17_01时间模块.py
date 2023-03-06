# 一、time
# import time
# # 时间分为三种格式：
# # 1、时间戳：从1970年到现在经过的秒数
#     #作用：用于时间建个的计算
# time.time()
# print(time.time())  # 1667314918.2217743
#
#
# # 2、按照某种格式显示的时间(格式化时间)：
#     #作用：用于展示时间
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))  # 2022-11-01 23:01:58 PM
#
# print(time.strftime('%Y-%m-%d %X'))  # 2022-11-01 23:09:25
#
# #3、结构化的时间
#     #作用：用户单独获取时间的某一部分
# import time
# res = time.localtime()
# print(res)
# # ime.struct_time(tm_year=2022, tm_mon=11, tm_mday=1,
# # tm_hour=23, tm_min=10, tm_sec=50,
# # tm_wday=1, tm_yday=305, tm_isdst=0)
#
# print(res.tm_year)  # 2022
# print(res.tm_yday) # 305 一年的第几天
# print(res.tm_mday) # 305 本月的的第几天


# 时间模块优先掌握
# 二、datetime
# import datetime
# print(datetime.datetime.now())  # 2022-11-01 23:20:46.108034
#
# print(datetime.datetime.now() + datetime.timedelta(days=3))  # 当前时间3天后
# print(datetime.datetime.now() + datetime.timedelta(days=-3))  # 当前时间3天前
# print(datetime.datetime.now() + datetime.timedelta(weeks=1))  # 当前时间7天后


# 时间模块需要掌握的操作
# 1、时间格式的转换
# struct_time-->时间戳  struct：结构体
import time
# s_time = time.localtime() # 一堆
# print(time.mktime(s_time))  # 1667316856.0
#
# # 时间戳-->struct_time
# tp_time = time.time()
# print(time.localtime(tp_time))  #时间戳转为结构体

# print(time.localtime()) # 北京时间，与世界时间的当前小时时间不一样，差8h tm_hour=23
# print(time.gmtime())  # 世界标准时间 tm_hour=15

# struct_time-->格式化的字符串形式的格式
# s_time = time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S',s_time))  # 2022-11-01 23:45:24

# '1990-09-05 10:10:10' 转成结构时间
# print(time.strptime('1990-09-05 10:10:10','%Y-%m-%d %H:%M:%S'))


#真正需要掌握的就一条：format string<---->timestamp  格式化时间转成时间戳
#'1990-09-05 10:10:10' +7 指定时间7天后

# 1.格式化时间转为结构化时间
# struct_time = time.strptime('1990-09-05 10:10:10','%Y-%m-%d %H:%M:%S')
# # 2.结构化时间转化为时间戳
# timestamp = time.mktime(struct_time) + 7 * 86400
# print(timestamp)
# #3.时间戳转为格式化中国时间
# res = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))
# print(res)


#了解知识
#time.sleep(2)

# import time
# print(time.asctime())  # Wed Nov  2 00:11:43 2022

import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

#时间戳转换为格式化时间
print(datetime.datetime.fromtimestamp(66666))  # 1970-01-02 02:31:06