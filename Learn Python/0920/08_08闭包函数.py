# 一：大前提：
# 闭包函数=名称空间与作用域+函数嵌套+函数对象
#     核心点：名字的查找关系是以函数定义阶段为准
#
# 二：什么是闭包函数
# '闭'函数指的是该函数是内嵌函数
# '包'函数值的是该函数包含对外层函数作用域名字的引用（不是对全局作用域）

#闭包函数：名称空间与作用域+函数嵌套
# def f1():
#     x = 33333
#
#     def f2():
#         print(x)  # 33333
#
#     f2()
#
# x = 1111
#
# def bar():
#     x = 4444
#     f1()
#
# def foo():
#     x = 222
#     bar()
#
# foo()


#闭包函数：函数对象
# def f1():
#     x = 33333
#
#     def f2():
#         print(x)
#
#     return f2 # 返回f2的内存地址
#
# f = f1()
# # print(f) # 拿到f2的内存地址<function f1.<locals>.f2 at 0x000001F5DEA5A8B0>
# # f()   # 33333
#
# def foo():
#     x = 555
#     f()
# foo() # 33333


# 三、为何要有闭包函数=》闭包函数的应用
#两种为函数体传参的方式
#方式1：直接吧函数体需要的参数定义为形参

# def f2():
#     print(x)
#
# f2(1)
# f2(2)

#方式2：
# def f1(x):
#     # x = 3
#     def f2():
#         print(x) # 3
#     return f2
# f = f1(3)
# f() # 3




#需求：获取指定网址页面返回
import requests
# 传参方式1：通过传参的方式
# def get(url):
#     res = requests.get(url)
#     print(len(res.text))
#
# get('https://www.baidu.com')
# get('https://www.bilibili.com')

#
# #传参方式2：
# def outter(url):
#     # url = 'https://www.baidu.com'
#     def get():
#         res = requests.get(url)
#         print(len(res.text))
#     return get
#
# baidu = outter('https://www.baidu.com')
# baidu()
#
# bilibili = outter('https://www.bilibili.com')
# bilibili()



