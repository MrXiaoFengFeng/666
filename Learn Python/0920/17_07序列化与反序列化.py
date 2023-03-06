#1.什么是序列化
# 序列化知道是吧内存的数据类型转换成一个特定的格式的内容
#
# 该格式的内容可用于存储或者传输给其他平台使用
#
# 内存中的数据类型<--反序列化<--特定的格式（json格式或者pickle格式）

# 土办法：
# {'aaa':111}-->序列化str({'aaa':111})-->"{'aaa':111}"
#
# {'aaa':111}<--反序列化eval({'aaa':111})<--"{'aaa':111}"

#2.为何要序列化
# 序列化得到的结果=》特定的格式的内容有两种用途
# 1、可用于存储 =》用于存档
# 2、传输给其他平台使用=》跨平台数据交互
#
# python                    java
# 列表        特定的格式     数组

# 强调：
#     针对用途1的特定格式：是一种专用的格式=》pickle只有python可以
#     针对用途2的特定格式：应该是一种通用、能够被所有语言识别的格式=》json


# 3、如何序列化与反序列化
import json
# 序列化的结果写入文件的复杂方法：
# dic={'name':'alvin','age':23,'sex':'male'}
# print(type(dic))#<class 'dict'>
#
# j=json.dumps(dic)
# print(j,type(j))  # {"name": "alvin", "age": 23, "sex": "male"} <class 'str'>

# 方式1复杂方法（---------json.dumps()是将一个python数据结构转换为JSON数据）：
# json_res = json.dumps([1,'aaa',True,False,None])
# print(json_res,type(json_res))  # [1, "aaa", true, false, null] <class 'str'>
# with open(r'file/test.json',mode='wt',encoding='utf-8') as f:
#     f.write(json_res)

# 方式2简单方法（----------json.dump()是用来编码JSON数据，用于处理（保存）文件）：
# with open(r'file/test.json',mode='wt',encoding='utf-8') as f:
#     json.dump([1,'aaa','b',True,False,None],f)  #dump使用逻辑：调用dumps序列化数据，然后 要序列化的内容+文件 [1, 'aaa', 'b', True, False, None] <class 'list'>


# 从文件读取json格式的字符串进行反序列化复杂方法1（---------------json.loads()是将一个JSON编码的字符串转换回一个Python数据结构）：
# l = json.loads(json_res)
# print(l,type(l))
# with open(r'file/test.json',mode='rt',encoding='utf-8') as f:
#     json_res = f.read()
#     l = json.loads(json_res)
#     print(l,type(l))


# 从文件读取json格式的字符串进行反序列化简单方法2（------------json.load()是用来解码JSON数据，用于处理（加载）文件）：
# with open(r'file/test.json',mode='rt', encoding='utf-8') as f:
#     l = json.load(f)
#     print(l, type(l))


# json验证：json格式兼容的是所有语言通用的数据类型，不能识别某一语言独有的类型
# json.dumps({1,2,3})  # 不支持集合类型。TypeError: Object of type set is not JSON serializable


# json强调：一定要搞清楚json格式，不要用python混淆
# l = json.loads('[1, "aa", true, false]')
# print(l, type(l))  # [1, 'aa', True, False] <class 'list'>
# print(l[0])  # 1



#pickle 用法同json
# import pickle
#
# pickle.dumps()
# pickle.loads()
#
#
# pickle.dump()
# pickle.load()


# python文件存档用pickle,跨平台数据交互用json






