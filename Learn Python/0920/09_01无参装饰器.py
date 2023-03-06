# **********************一、装饰器知识储备复习*********************
# 1、*args,**kwargs
# 场景：wrapper参数需要原封不动的传给index
# def index(x, y):
#     print(x, y)
#
#
# def wrapper(*args, **kwargs):  # args=(1,2,3,4,5) kwargs={'a':1,'b':2}
#     index(*args, **kwargs)  # index(*(1,2,3,4,5),**{'a':1,'b':2})
#                             #index(1,2,3,4,5,a=1,b=2)
#                             # index(y=222,x=111)
# # wrapper(1,2,3,4,5,a=1,b=2)  # wrapper传的参数原封不动的传给index，传入参数的格式需参照index
# wrapper(y=222,x=111)  #结果111 222


# 2、名称空间与作用域：名称空间的“嵌套”关系是在函数定义阶段，即检测语法的时候确定的


# 3、函数对象：
# 可以把函数当做参数传入
# 可以吧函数当做返回值返回

# def index():
#     pass
#
# def foo(func):
#     return func
#
# foo(index)


# 4、函数的嵌套定义：
#
# def outter(func):
#     def wrapper():
#         pass
#     return wrapper


# 5、闭包函数
# def outter():
#     x = 111
#     def wrapper():
#         print(x)
#     return wrapper
#
# f = outter()
# f()  #111

# 6、传值方式：
# 方式一：通过参数的形式为函数体传值

# def wrapper(x):
#     print(x)
#
# wrapper(1)
# wrapper(2)
# wrapper(32)

# 方式二：通过闭包的方式为函数体传值
# def outter():
#     x = 1
#     def wrapper():
#         print(x)
#     return wrapper
#
# f = outter()
# f() #1

# def outter(x):
#     def wrapper():
#         print(x)
#     return wrapper
#
# f1 = outter(3333)
# f1() #333
# f2 = outter(444)
# f2() #444


# **********************二、装饰器*********************
# 1、什么是装饰器
# 器指的是工具，可以定义成函数
# 装饰指的是为其他事物添加额外的东西点缀
# 合到一起的解释：装饰器指的定义一个函数，该函数是用来为其他函数添加额外的功能

# 2、为何要用装饰器
# 开放封闭原则
# 开放：指的是对拓展功能是开放的
# 封闭：指的是对修改源代码是封闭的
# 装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下，为被装饰对象添加新功能

# 3、如何用
# 需求：在不修改被装饰器对象源代码以及调用方式的前提下，为其添加运行时间的功能

# 原程序
# import time
# def index(x, y):
#     time.sleep(3)
#     print('index内容为： %s %s' % (x, y))
#
# index(1, 2)

# 解决方式1: 失败，问题：没有修改调用方式，但是修改了源代码
# import time
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print('index内容为： %s %s' % (x, y))
#     stop = time.time()
#     print(stop-start)
#
# index(1, 2)

# 解决方案2：失败，多处调用。没改源代码及调用方式，但代码冗余
# import time
# def index(x, y):
#     time.sleep(3)
#     print('index内容为： %s %s' % (x, y))

# start = time.time()
# index(1, 2)
# stop = time.time()
# print(stop-start)
#
#
# start = time.time()
# index(33, 44)
# stop = time.time()
# print(stop-start)

# 解决方案3：失败，解决重复代码，但是改变了函数调用方式
# import time
# def index(x, y):
#     time.sleep(3)
#     print('index内容为： %s %s' % (x, y))
# def wrapper():
#     start = time.time()
#     index(1, 2)
#     stop = time.time()
#     print(stop-start)
#
# wrapper()

# 方案3优化1：index值写死了，将参数写活
#
# import time
# def index(x, y, z):
#     time.sleep(3)
#     print('index内容为:x值为%s，y值为%s，z值为%s' % (x, y,z))
#
#
# def wrapper(*args,**kwargs):
#     start = time.time()
#     index(*args,**kwargs) #index(111,222)
#     stop = time.time()
#     print(stop-start)
#
# wrapper(222,z=111,y=333)


# 方案3优化2.1再优化思路：index写死了，给其他函数调用时又得重复写wrapper

# import time
# def index(x, y, z):
#     time.sleep(3)
#     print('index内容为:x值为%s，y值为%s，z值为%s' % (x, y,z))
#
#
# def wrapper(*args,**kwargs):
#     start = time.time()
#     index(*args,**kwargs) #index(111,222)
#     stop = time.time()
#     print(stop-start)
#
# wrapper(222,z=111,y=333)


# #方案3优化2.2：在方案3的基础上不改变函数的调用方式，将index作为投石传入
# #将装饰器outter给其他函数做装饰器
# import time
# def index(x, y, z):
#     time.sleep(3)
#     print('index内容为:x值为%s，y值为%s，z值为%s' % (x, y,z))
# # print(index) #<function index at 0x0000015316ADF160>
#
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to homepage'%name)
#
# def outter(func):
#     # func = index #func=index的内存地址
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs) # index 的内存地址(1,2,z=4)
#         stop = time.time()
#         print(stop-start)
#     return wrapper
#
#
# index = outter(index) # f=outter(index内存地址) ,f也可以取名为index。但是内存地址已经变了
# # print(index) 实际调用的是wrapper<function outter.<locals>.wrapper at 0x000002BC90D7A9D0>
# index(1,2,z=4) #内存地址变了，只是看起来调用方式一样
#
# home = outter(home)
# home('jojo')


# 方案3优化3：将wrapper做的跟被装饰对象一模一样，以假乱真

# import time
#
#
# def index(x, y, z):
#     time.sleep(3)
#     print('index内容为:x值为%s，y值为%s，z值为%s' % (x, y, z))
#     return 1234
#
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to homepage' % name)
#     return 666
#
#
# def outter(func):
#     # func = index #func=index的内存地址
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)  # index 的内存地址(1,2,z=4)
#         stop = time.time()
#         print(stop - start)
#         return res  # 返回被调函数的返回
#
#     return wrapper
#
#
# index = outter(index)
# print('index的返回值-》', index)
# res1 = index(1, 2, z=4)
# print('index的返回值-》', res1)
#
# home = outter(home)
# print('home的返回值-》', home)
# res2 = home('jojo')
# print('home的返回值-》', res2)


# 语法糖:让你开心的语法
#
# import time
#
# #装饰器
# def timmer(func):
#     # func = index #func=index的内存地址
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)  # index 的内存地址(1,2,z=4)
#         stop = time.time()
#         print(stop - start)
#         return res  # 返回被调函数的返回
#
#     return wrapper
#
# #在被装饰对象正上方的单独一行写@装饰器名字
# @timmer # index = timmer(index)
# def index(x, y, z):
#     time.sleep(3)
#     print('index内容为:x值为%s，y值为%s，z值为%s' % (x, y, z))
#     return 1234
#
# @timmer # home = timmer(home)
# def home(name):
#     time.sleep(2)
#     print('welcome %s to homepage' % name)
#     return 666
#
#
# index(1, 2, z=4)
#
# home('jojo')


# 思考题：叠加多个装饰器,加载顺序与运行顺序，挨着越近先运行
#
#
# @deco1 # index的内存地址=deco1(deco2.wrapperd的内存地址)
# @deco2 # deco2.wrapperd的内存地址=deco2(deco3.wrapper的内存地址)
# @deco3 # deco3.wrapper的内存地址=deco3(index)
# def index():
#     pass
#
# def deco3():
#     pass
# def deco2():
#     pass
# def deco1():
#     pass


# 总结无参装饰器模板


# def outter(func):
#     def wrapper(*args,**kwargs):
#         #装饰器的功能：
#         #1.调用原函数
#         #2.为其增加新功能
#         res = func(*args,**kwargs)
#         return res
#     return wrapper
#
# @outter
# def index(x):
#     print('from index')
#
# index(1)


# 案例：在运行index函数前，需要先判断账号密码


# def auth(func):
#     def wrapper(*args, **kwargs):
#         name = 'egon'
#         password = '123'
#         input_name = input('请输入的账号-》').strip()
#         input_password = input('请输入的密码-》').strip()
#         if input_name == name and input_password == password:
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print('账号密码错误')
#
#     return wrapper
#
#
# @auth # index = auth(index) #index = wrapper的内存地址
# def index():
#     print('welcome to index')
#
#
# index()

# ===================================================
# 无参装饰器补充
#装饰器：偷梁换柱，及将原函数名指向的内存地址偷梁换柱称wrapper
#所以应该将wrapper做的跟原函数一样才行

from functools import wraps


def outter(func):
    @wraps(func) # wraps()相当于帮忙处理了所有原函数的属性赋值给wrapper函数
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    #手动将原函数的属性赋值给wrapper函数
    #1、函数wrapper.__name__ = 原函数.__name__
    #2、函数wrapper.__doc__ = 原函数.__doc__
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

@outter # index = outter(index)
def index(x, y):
    '''这是index的说明'''
    print(x, y)

index(111, 222)
print(index.__name__)
print(index.__doc__)
#伪装前返回：wrapper、None
#伪装后返回：index、这是index的说明


