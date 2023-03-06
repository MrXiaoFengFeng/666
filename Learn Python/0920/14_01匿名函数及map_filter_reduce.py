# 1.def用于定义有名函数
# func = 函数的内存地址
# def func(x, y):
#     return x + y
# print(func)
#
# #2.lambda用于定义匿名函数------------------------------lambda
# lambda x,y:x+y
# print(lambda x,y:x+y) # 内存地址


# 3.调用匿名函数
# 方式1：
# res = (lambda x, y: x + y)(1, 2)
# print(res)
#
# 方式2：
# func = lambda x, y: x + y
# res = func(1, 2)
# print(res)

# 4.匿名用于临时调用一次的场景：更多的是将匿名与其他函数配合使用
# lambda x, y: x + y


salaries = {
    'siry': 3000,
    'tom': 7000,
    'lili': 10000,
    'jack': 2000
}
# 需求1：选出工资最高的那个人
# res = max([2,300,15,66,100])
# print(res)  # 300
# # 方式1：
# def func(k):
#     return salaries[k]
# res = max(salaries, key=func)
# print(res)
#
# # 方式2(优选)：---------------------max的应用
# res = max(salaries, key=lambda k: salaries[k])
# print(res)

# 需求2：选出工资最低的那个人---------------min
# res = min(salaries, key=lambda k: salaries[k])
# print(res)

# 需求3：工资从低到高排序------------------sorted排序(默认从小到大)
# res = sorted(salaries, key=lambda k: salaries[k]) # 从小到大
res = sorted(salaries, key=lambda k: salaries[k],reverse=True) ## 从大到小
print(res)

# ---------------------map的应用
# 案例：列表名称映射别的名字

# l = ['alex', 'lili', 'wxx', 'jojo']

# 方式1.1(数据较少可以用列表生成式)：
# new_l = [name + '_dsb' for name in l]
# print(new_l)

# 方式1.2（数据较多可以用生成器）：
# new_l = (name + '_dsb' for name in l)
# print(new_l) # 生成器 <generator object <genexpr> at 0x00000262C4D28DD0>

# 方式1.3-----------------------------------------------map(映射)
# res = map(lambda name: name + '_dsb',l)
# print(res) # 生成器 <map object at 0x000001C1AA74F2B0>

# ----------------------------------------------------filter(过滤器)
# 需求过滤名字中含有"dsb"的名字
# l = ['alex_dsb', 'lili', 'wxx_dsb', 'jojo']
# res = (name for name in l if name.endswith('dsb'))
# print(res) # 生成器<generator object <genexpr> at 0x000002B5480C7DD0>
# v = next(res)
# print(v) #alex_dsb


# res = filter(lambda name: name.endswith('dsb'), l)
# print(res)
# v=next(res)
# print(v)


# ----------------------------------reduce(复位)
# from functools import reduce
#
# res = reduce(lambda x, y: x + y, [1, 2, 3], 10)  # 10为y初始值（不写为None），
#                                                     # 与1相加=11变为初始值
#                                                     # 与2相加=13变为初始值与3相加=16
# print(res)  # 16
#
# res1 = reduce(lambda x, y: x + y, ['a', 'b', 'c'], 'hello')
# print(res1)  # helloabc
