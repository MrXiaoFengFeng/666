'''
post json demo
import requests
import json

url = "https://httpbin.org/post"

payload = json.dumps({
  "key1": "v1",
  "key2": "v2"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

requests.post  data参数传的是字典  或者  是key=value的字符串
json是一个字符串，所有可以用data, 用的时候，json.dumps('字典') ==》 json字符串
'''

import requests

data = {
    "key1": "v1",
    "key2": "v2"
}
url = "https://httpbin.org/post"

# json这个关键字参数，当你传你一个字典的时候，会把你的这个字典，序列化成json字符串（框架底层实现）
response = requests.request("POST", url, json=data)
print(response.text)
