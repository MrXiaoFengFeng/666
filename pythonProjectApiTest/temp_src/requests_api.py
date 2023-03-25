import requests

url = "http://127.0.0.1:5000/api/books"
# headers = {
#     "Cookie": "user_id=654321"
# }
cookies = {
    "user_id": "654321"
}

resp = requests.get(url, cookies=cookies)
print(resp.text)
print(resp.headers)

# 需求1：拿到发送的cookies 和 响应的cookies做对比
# 需求2：拿到发送的body的数据 和 响应的body中的数据做对比
from pprint import pprint
print("======")
pprint(resp.__dict__)



pprint(resp.request.__dict__)
print(resp.request.__dict__.get("headers"))
print(dict(resp.request.__dict__.get("_cookies")))
print(resp.request.__dict__.get)




