
#1.字典生成式

# dic = {键：值 for k,v in 可迭代对象 if 条件}

# keys = ['name','age','gender']
# dic = {key:None for key in keys}
# print(dic) # {'name': None, 'age': None, 'gender': None}
#


# items = [('name','egon'),('age',19),('gender','male')]
#
# res = {k:v for k,v in items if k != 'gender'}
# print(res)


#2.集合生成式

# set1 = {元素 for k in 可迭代对象 if 条件}

# keys = ['name','age','gender']
# set1 = {key for key in keys}
# print(set1,type(set1)) # {'name', 'age', 'gender'} <class 'set'>


# 3.生成器表达式

# g = (表达式 for x in 可迭代对象 if 条件)

# g = (i for i in range(10) if i >3)
# #!!!!!!!!!!重要！！！！！！！！！
# #此刻g内部一个值也没有
# print(g) #生成器 <generator object <genexpr> at 0x000001B7FC488DD0>
# print(next(g)) #4
# print(next(g)) #5
# print(next(g)) #6


# 统计有多少个字符(生成器表达式)

# with open('file/a.txt',mode='rt',encoding='utf-8') as f:
#     '''方式1：'''
#     # res = 0
#     # for line in f:
#     #     res += len(line)
#     # print(res) # 10
#
#     '''方式2'''
#     # res = sum([len(line) for line in f])
#     # print(res) # 10
#
#     '''方式3'''
#     res = sum(len(line) for line in f)
#     print(res) # 10
#


#带括号指生成一个生成器
# g = (表达式 for x in 可迭代对象 if 条件)
# sum(表达式 for x in 可迭代对象 if 条件)
# list(表达式 for x in 可迭代对象 if 条件)
#
#