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
pv: page visit , 页面访问量，一次请求就是一次pv
uv: user visit, 独立用户，一个ip就算一个独立用户
注意：没有ip的可以认为是异常日志，不用统计！
'''
import calendar
import re
import time


# 请求打开记载文件方法
def load_log_file(file_path):
    with open(file_path, mode='rt', encoding='utf-8') as f:
        return f.readlines()


# 过滤出所有的ip方法
def re_group_ip(regx, line):
    data_list = re.findall(regx, line)
    return data_list


# 统计计数方法
def count_data(data):
    # ip正则
    regx_for_ip = "(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) - -"  # 122.71.241.175
    # 创建一个空的uv列表
    # uv = list()
    # get请求正则
    regx_for_get = "GET (\S+)"  # GET /api/v1/affiches/
    # post请求正则
    regx_for_post = "POST (\S+)"  # POST /api/v1/affiches/
    # 时间正则
    # regx_for_time = "\[(\S+)"  # 15/Apr/2019:00:00:01
    # pv：请求200成功+域名正则
    regx_for_pv = '200 \d+ "(\w+://\S+)"'  # 200 24 'https://m.luffycity.com/home'
    # 创建一个空的pv列表
    # pv = list()
    # 创建一个字典，存放需要统计的数据信息
    count_data = {}

    # for line in data:
    #     # 拿到每一条数据
    #     # 定义一个容器类型来接手
    #
    #     # 处理不兼容的时间格式，转换为正常时间格式
    #     str_time = re.findall(regx_for_time, line)[0]  # 取出读出的一条log中时间部分的字母月份（Apr）
    #     str_time = str_time.split("/")  # 将时间用'/'切分
    #     str_time[1] = list(calendar.month_abbr).index(str_time[1])  # 将切分后的时间数组取出字母月份转换为数字
    #     my_time_str = '-'.join(
    #         [str(v) for v in str_time])  # 用三元表达式将获取到的时间都取出来，然后转成字符串，重新用'-'拼接时间格式为15-Apr-2019:00:00:01
    #     time_obj = time.strptime(my_time_str, "%d-%m-%Y:%H:%M:%S")  # 将时间格式转成原数据对应的时间格式
    #     str_time = time.strftime("%Y-%m-%d-%H", time_obj)  # 将自定义的时间格式转换为标准时间格式
    #     # print(str_time)

        # 初始化读取文件数据的pv、uv计数
    #     if str_time not in count_data:
    #         count_data[str_time] = {
    #             "pv": 0,
    #             "uv": 0
    #         }
    #
    #     # 找到当前行的ip地址
    #     uv_data = re.findall(regx_for_ip, line)  # 找不到数据 会返回一个， if 可判断为False的数据结构或类型
    #     # 如果没有找到uv_data,继续执行
    #     if not uv_data:
    #         continue
    #
    #     # 取出列表内的ip数据
    #     uv_data = uv_data[0]
    #     # print(uv_data)
    #     # 初始化get请求数据，判断当前行的ip地址是否存在，如果不存在一个ip就算一个uv
    #     if not count_data[str_time].get(uv_data):
    #         count_data[str_time][uv_data] = 1
    #         # pass
    #     else:
    #         # 如果不重复 uv+1
    #         count_data[str_time][uv_data] += 1
    #         count_data[str_time]["uv"] += 1
    #
    #     # 找到当前行中的pv数据
    #     pv_data = re.findall(regx_for_pv, line)
    #     # 如果匹配到了空就继续执行
    #     if not pv_data:
    #         continue
    #     # 取出列表中的网址数据
    #     pv_data = pv_data[0]
    #     # print(pv_data)
    #     # 初始化get请求，
    #     if not count_data[str_time].get(pv_data):
    #         count_data[str_time][pv_data] = 1
    #         # pass
    #
    #     else:
    #         count_data[str_time][pv_data] += 1
    #         count_data[str_time]['pv'] += 1
    #     #
    # from pprint import pprint
    # pprint(count_data)


# 1 计算文件的pv和uv
def count_pv_uv(data):
    # ip正则
    regx_for_ip = "(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) - -"  # 122.71.241.175
    # 创建一个空的uv列表
    count_data = {
        "pv": 0,
        "uv": 0,
        "ips": {},
    }
    # pv：请求200成功+域名正则
    regx_for_pv = '200 \d+ "(\w+://\S+)"'  # 200 24 'https://m.luffycity.com/home'
    # 创建一个空的pv列表
    for line in data:
        # 获取文件中uv的数据
        uv = re.findall(regx_for_ip, line)
        # uv = [] 如果取到uv数据，则读取出列表中的第一条数据，即IP地址
        if uv:
            uv = uv[0]
        # 如果找到一个uv且该uv不在count_data['ips']字典里,则ips字典里的uv值等于1，日志文件中的uv值
        if uv and (uv not in count_data["ips"]):
            count_data["ips"][uv] = 1  # 或者None
            count_data["uv"] += 1

        # 获取文件中pv数据
        pv = re.findall(regx_for_pv, line)
        #如果pv存在则
        if pv:
            count_data["pv"] += 1

    return count_data["pv"], count_data["uv"]

# 2 列出全天每小时的pv、uv数
def count_pv_perhour(data):
    # 创建一个空的统计每小时pv的字典
    pv_perhour = {}
    # 正则取出时间，然后转化成正常的时间格式
    regx_for_time = "\[(\S+)"  # 15/Apr/2019:00:00:01
    for line in data:
        # 处理不兼容的时间格式，转换为正常时间格式
        str_time = re.findall(regx_for_time, line)[0]  # 取出读出的一条log中时间部分的字母月份（Apr）
        str_time = str_time.split("/")  # 将时间用'/'切分
        str_time[1] = list(calendar.month_abbr).index(str_time[1])  # 将切分后的时间数组取出字母月份转换为数字
        my_time_str = '-'.join(
            [str(v) for v in str_time])  # 用三元表达式将获取到的时间都取出来，然后转成字符串，重新用'-'拼接时间格式为15-Apr-2019:00:00:01
        time_obj = time.strptime(my_time_str, "%d-%m-%Y:%H:%M:%S")  # 将时间格式转成原数据对应的时间格式
        str_time = time.strftime("%Y-%m-%d-%H", time_obj)  # 将自定义的时间格式转换为标准时间格式
        # print(str_time)

        # 初始化读取文件数据的pv、uv计数
        if str_time not in pv_perhour:
            pv_perhour[str_time] = {
                "pv": 0,
            }
        # pv：请求200成功+域名正则
        regx_for_pv = '200 \d+ "(\w+://\S+)"'  # 200 24 'https://m.luffycity.com/home'

        pv_data = re.findall(regx_for_pv, line)

        if not pv_data:
            continue
        pv_data = pv_data[0]
        if pv_perhour[str_time].get(pv_data):
            pv_perhour[str_time]['pv'] += 1
        #
        #
        #     pv_perhour[str_time][pv_data] = 1
        #
        # else:
        #     pv_perhour[str_time][pv_data] += 1
        #     pv_perhour[str_time]['pv'] += 1

        # print(pv_perhour)

    return pv_perhour[str_time]










def main(file_path):
    # 打开文件，拿到数据
    data = load_log_file(file_path)
    # print(data)

    # 1 统计本日志文件的总pv、uv
    # count_pv, count_uv = count_pv_uv(data)
    # print(f"count_pv:{count_pv}, count_uv: {count_uv}")
    # 2 列出全天每小时的pv、uv数
    pv_perhour = count_pv_perhour(data)
    print(f"pv_perhour:{pv_perhour}")
    # 3 列出top 10 uv的IP地址，以及每个ip的pv点击数

    # 4 列出top 10 访问量最多的页面及每个页面的访问量

    # 5 列出访问来源的设备列表及每个设备的访问量


if __name__ == '__main__':
    file_path = "E:/WorkSpace/Learn Python/temp/testlog.txt"
    # file_path = "/Users/dengjiajie/myCode/myCodeNote/temp/testlog.txt"
    main(file_path)
