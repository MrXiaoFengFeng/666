'''
postman

import requests

url = "https://httpbin.org/post"

payload = 'key1=v1&key2=v2'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}  # 可以不传，默认   'Content-Type': 'application/x-www-form-urlencoded'

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

'''
import requests

base_url = 'https://httpbin.org'
path = '/post'
url = f"{base_url}{path}"  # 字符串格式化
data = {   # 如果post请求是一个字典格式，框架底层会帮你转换成 key=value&key2=value2
    'key1': 'v1',
    'key2': 'v2'
}

# requests里面使用post请求，header不传，默认表单
# 'Content-Type': 'application/x-www-form-urlencoded'
# 表单请求体放在data里面
resp = requests.request('POST', url, data=data)
print(resp.text)


