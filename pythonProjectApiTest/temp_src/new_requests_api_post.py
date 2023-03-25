import json

import requests

url = "http://www.kuaidi100.com/query"
# headers = {
#     "Cookie": "user_id=654321"
# }
body = {
    "type": "shunfeng",
    "postid": "SF1631643020688"
}
resp = requests.post(url, data=body)
# resp = requests.request("POST", url=url, data = body)
print(resp.text)
print(resp.headers)

# 需求1：拿到发送的cookies 和 响应的cookies做对比
# 需求2：拿到发送的body的数据 和 响应的body中的数据做对比
from pprint import pprint

print("======")
pprint(resp.__dict__)
print('________________________')
pprint(resp.request.__dict__)
# print(resp.request.__dict__.get("headers"))
print("0000000000000000000000000000")
print(dict(resp.request.__dict__.get("_cookies")))
print("555555555")
pprint(resp.__dict__.get("cookies"))
# print(resp.request.__dict__.get)
# print(resp.request.__dict__.get("body").decode("utf-8"))
# requests_body = resp.request.__dict__.get("body").decode("utf-8")
# print(json.loads(requests_body))
# assert body.get("title") == json.loads(requests_body).get("title")
# print("===断言成功===")