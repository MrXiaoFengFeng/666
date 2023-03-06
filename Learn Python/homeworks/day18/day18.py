'''
作业：
1、编写课上讲解的有参装饰器准备明天默写
2：还记得我们用函数对象的概念，制作一个函数字典的操作吗，
    来来来，我们有更高大上的做法，在文件开头声明一个空字典，
    然后在每个函数前加上装饰器，完成自动添加到字典的操作
3、 编写日志装饰器，实现功能如：一旦函数f1执行，
则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
注意：时间格式的获取
import time
time.strftime('%Y-%m-%d %X')
4、基于迭代器的方式，用while循环迭代取值字符串、列表、元组、字典、集合、文件对象
5、自定义迭代器实现range功能
'''


# 1、编写课上讲解的有参装饰器准备明天默写
# from functools import wraps
#
#
# def deco(x):
#     def outter(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if x == 'jojo':
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('x值不对')
#
#         return wrapper
#
#     return outter
#
#
# @deco('jojo')
# def index():
#     print('哈哈哈哈')
#
#
# index()


# 2：每个函数前加上装饰器，完成自动添加到字典的操作
# from functools import wraps
# # 定义一个空字典
# dic = {}
#
# # 定义一个有参装饰器
#
# def add_info(x):  # x='1'
#
#     def wrapper(func):  # func = 被装饰的函数地址login、register
#         dic[x] = func
#
#         @wraps(func)
#         def inner(*args, **kwargs):
#
#             res = func(*args, **kwargs)
#
#             return res
#         return inner
#     return wrapper
#
#
# @add_info('1')
# def login():
#     pass
#
# @add_info('2')
# def register():
#     pass
#
# print(dic)  # {'1': <function login at 0x000002522F9BE820>, '2': <function register at 0x000002522F9BED30>}


# 3、 编写日志装饰器，实现功能如：一旦函数f1执行，
# 则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取
# import time
# time.strftime('%Y-%m-%d %X')
# 导包
# from functools import wraps
# import time
#
# # 编写装饰器
#
# def add_log(func):
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#
#         res = func(*args, **kwargs)
#         # 函数运行后
#         with open('add_log.txt', 'a', encoding='utf-8') as f:
#             run_time = time.strftime('%Y-%m-%d %H:%M:%S')
#             func_name = func.__name__
#             log = f'{run_time} {func_name}函数 run\n'
#             f.write(log)
#
#         return res
#
#     return wrapper
#
#
# # 定义函数f1
# @add_log
# def f1():
#     print('f1运行了')
#     pass
#
#
# f1()



# 4、基于迭代器的方式，用while循环迭代取值字符串、列表、元组、字典、集合、文件对象

# def my_iter(obj):
#     iter_obj = obj.__iter__()
#     while True:
#         try:
#             print(iter_obj.__next__())
#         except StopIteration:
#             break
#
#
# my_iter('tank')


# 5、自定义迭代器实现range功能
# res = range(1, 10 , 2)


def my_range(start, end, step=1):
    while start < end:
        print(start)  # 1,3,5,7,9

        yield start

        start += step

res1 = range(1, 10 , 2)
# __str__:range(1, 10, 2)
print(res1)

res2 = my_range(1, 10, 2)
print(res2)  # <generator object my_range at 0x000002CE0595E350>  生成器

for i in res2:
    print(i)





