name = " alegonxX"
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# 6)    将 name 变量对应的值变大写,并输出结果
# 7)    将 name 变量对应的值变小写,并输出结果
# 8)    请输出 name 变量对应的值的第 2 个字符?
# 9)    请输出 name 变量对应的值的前 3 个字符?
# 10)    请输出 name 变量对应的值的后 2 个字符?
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置?
# 12)    获取子序列,去掉最后一个字符。如: egonlin 则获取egonli

'''
# 答案
name = ' alegonxX'

1) print(name.strip())
2) print(name.startswith('al'))
3) print(name.endswith('X'))
4) print(name.replace('l', 'p'))
5) print(name.split('l'))
6) print(name.upper())
7) print(name.lower())
8) print(name[1])
9) print(name[0:3])
10) print(name[-1:-3:-1])
11) print(name.find('e'))
12) name = 'egonlin'
print(name[:-1])
'''