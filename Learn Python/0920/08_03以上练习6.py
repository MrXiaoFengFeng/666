# 练习6：
# 写函数，检查字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {'k1':'v1v1','k2':[11,22,33,44]}
# PS:字典中的value只能是字符串或列表


def func3(dic):
    d = {}
    for k, v in dic.items():
        if len(v) > 2:
            d[k] = v[0:2]
    return d


print(func3({'k1': 'abcdef', 'k2': [1, 2, 3, 4], 'k3': ('a', 'b', 'c')}))
