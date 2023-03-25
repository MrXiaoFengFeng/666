import logging

import jmespath
import requests

# curl - X
# 'POST' \
# 'https://api.apiopen.top/api/login' \
# - H
# 'accept: application/json' \
# - H
# 'Content-Type: application/json' \
# - d
# '{
# "account": "309324904@qq.com",
# "password": "123456"
# }'

# body = {
#     "account": "309324904@qq.com",
#     "password": "123456"
# }
# url = "https://api.apiopen.top/api/login"
# headers = {
#     "accept": "application/json",
#     "Content-Type": "application/json"
# }
#
# resp = requests.post(
#     url="https://api.apiopen.top/api/login",
#     headers=headers,
#     json=body
# )


url = "http://127.0.0.1:5000/api/books"

resp = requests.get(url)
"""
两个电脑要通过代码通信，要有共同的数据类型传输 --> 字符串
A电脑用python, 组装了一个字典类型的数据 --> 字符串 --> 序列化
B电脑用JAVA，接受A电脑的字符串数据，识别到是一个JSON格式的字符串
--> 反序列化 --> java的对象（类是python字典）
"""

# print(type(resp.text), resp.text)  # 原始字符串，网络中传输用字符串，每个电脑语言都有字符串类型
# print(type(resp.json()), resp.json())  # .json() 是把json字符串 反序列化到代码对象 python dict
# print(type(resp.cookies), type(dict(resp.cookies.items())), dict(resp.cookies.items()))
print(type(resp.headers), type(dict(resp.headers)), dict(resp.headers))
"""
resp.json() --> json
dict(resp.cookies.items()) -- > cookies.items 这种写法对用户有友好吗？ 找大家都认识的关键字 --> cookies
dict(resp.headers) --> headers
为什么用反射去取不好处理？
因为反射拿到的对象 数据类型不能统一处理，不能抽象化
"""
# json.books[0].author
# headers.
# key_word = input("key_word: ")
_jmespath = input("jmespath: ")
try:
    key_word, path = _jmespath.split(".", 1)  # json  .   books[0]['author']
except Exception as msg:
    logging.warning(msg)
    key_word = _jmespath
    path = dict()

if key_word == "json":  # --> json.
    print(type(resp.json()))
    print(resp.json())
    data = jmespath.search(path, resp.json())
    print("===data===")
    print(data)

elif key_word == "cookies":  # --> cookies.xx
    print(type(dict(resp.cookies.items())))
    print(dict(resp.cookies.items()))
    data = jmespath.search(path, dict(resp.cookies.items()))
    print("===data===")
    print(data)
elif key_word == "headers":  # --> headers.xx
    print(type(dict(resp.headers)))
    print(dict(resp.headers))
    data = jmespath.search(path, dict(resp.headers))
    print("===data===")
    print(data)

elif key_word == "status_code":
    print(resp.status_code)
