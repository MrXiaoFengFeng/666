'''
postman:
import requests

url = "https://httpbin.org/get?key1=1&key2=2"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
'''

import requests

base_url = 'https://httpbin.org'
path = '/get'
url = f"{base_url}{path}"  # 字符串格式化
params = {
    'key1': 'v1',
    'key2': 'v2'
}
# 方式一： 用于开发数据驱动，我们的数据驱动要把数据直接剥离代码，实现工具与数据的分离
# response = requests.request("GET", url,  params=params)   方式一相对方式二抽象，把请求方法作为参数传进去
# 方式二：
response = requests.get(url, params=params)
# 为什么不用这个方法来执行get请求 下面的这个方法更加具体，方便学习，但是越具体的
# 方法，越不抽象
'''
很多培训班为了教学的方便，去封装更具体的方法，让更具体的方法再次变成抽象，后果：让看过底层的人，觉得封装过度
'''

print(response.text)


''''
1、写简历的时候，把你项目技术变化，表现出来
例如：2019 用 unittest + ddt + htmlreport  + 发邮件， 硬编码+部分数据剥离，数据放在json里面
2020 用pytest+pytest插件（参数化，用例重跑，测试报告，前后置脚本） + allure报告，比2019年功能强了一点，换了更强大的pytest,熟练使用
里面的api（pytest的方法）和插件
3、2021 开发数据驱动，实现数据和代码的完全剥离  requests 封装更抽象的请求驱动




'''