

import requests

# def test_a():
#     a = "1213324"
#     print(a)


url = 'http://japi.juhe.cn/qqevaluate/qq'
parm = {
    "qq" : "12345678",
    "key" : "8dbee1fcd8627fb6699bce7b986adc45"}

r = requests.post(url=url, params=parm)
print(r.text)
