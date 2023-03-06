'''
一：编写函数，（函数执行的时间用time.sleep(n)模拟）
二：编写装饰器，为函数加上统计时间的功能
三：编写装饰器，为函数加上认证的功能

四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录


六：选做题
# 思考题（选做），叠加多个装饰器，加载顺序与运行顺序，可以将上述实现的装饰器叠加起来自己验证一下
# @deco1 # index=deco1(deco2.wrapper的内存地址)
# @deco2 # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
# @deco3 # deco3.wrapper的内存地址=deco3(index)
# def index():
#     pass
'''


# 一：编写函数，（函数执行的时间用time.sleep(n)模拟）
# import time
# def func():
#     time.sleep(1)
# func()

# 二：编写装饰器，为函数加上统计时间的功能
# import time
# # 统计时间装饰器
# def timer(func):  # func-->被装饰对象
#     def inner(*args, **kwargs):
#         # 执行时间开始
#         start_time = time.time()
#         # *args, **kwargs将接收过来的参数，传给调用的被装饰对象，会得到一个返回值
#         res = func(*args, **kwargs)  # 调用被装饰对象，这行代码就是被装饰对象的全过程
#         # 执行时间结束
#         end_time = time.time()
#         # func.__name__会得到函数的名称
#         print(f'当前被装饰的函数:[{func.__name__}]执行时间为:[{end_time-start_time}]秒')
#         return res
#     return inner

# # 方式1语法糖：
# @timer  # timer = inner = timer(func)
# def func():
#     time.sleep(5)
# # # 使用装饰器的目的：
# # # 1、为被装饰对象添加新多功能
# # # 2、前提：不修改被装饰对象的源代码，不修改调用方式
# func()  # 当前被装饰的函数:[func]执行时间为:[5.007017374038696]秒

# 方式2：
# def func2():
#     time.sleep(3)
# inner = timer(func2)
# func2 = inner
# func2()  # 当前被装饰的函数:[func2]执行时间为:[3.0142624378204346]秒


# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

# 全局变量：用户记录是否有用户登录
# login_user = None
#
#
# # 登录功能
# def login():
#     username = input('请输入你的用户名：').strip()
#     password = input('请输入你的密码：').strip()
#     if username == 'tank' and password == '123':
#         print('登录成功')
#         # 登录成功后给全局变量赋值，记录当前用户已登录
#         global login_user
#         login_user = username
#     else:
#         print('登录失败')
#
#
# def login_auth(func):
#     def inner(*args, **kwargs):
#         # 被装饰对象前执行，为其添加新功能
#         if not login_user:
#             print('未登录，无法执行功能')
#             login()
#         # 被装饰对象执行
#         res = func(*args, **kwargs)
#
#         # 被装饰对象执行后，为其添加新功能
#         return res
#
#     return inner
#
#
# @login_auth
# def play():
#     print('play功能运行啦！')
#     pass
#
#
# @login_auth
# def shopping():
#     print('shopping执行啦！')
#     pass
#
#
# login()
#
# play()
#
# shopping()


# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

# 1、打开db.txt文件，读取出用户的数据，转换成字典


def get_userdata():
    with open('db.txt', 'r', encoding='utf-8') as f:
        # 直接读取文件中的数据，得到数据类型str
        userdata = f.read()
        print(userdata, type(userdata))
        # eval(str)-->从str字符串中检测python代码的语法，
        # 如果里面有{key: value},会将该数据生成对应的类型的内存地址
        user_dic = eval(userdata)
        # {"name": "tank", "pwd": "123"}
        # print(user_dic, type(user_dic))
    return user_dic


user_dic = get_userdata()

user_login = None


def login():
    username = input('请输入用户名：').strip()
    if username in user_dic.get('name'):
        password = input('请输入你的密码').strip()
        if password == user_dic.get('pwd'):
            print('登录成功！')
            global user_login
            user_login = {username: password}
        else:
            print('密码错误')
    else:
        print('用户不存在，请重新输入')


# def auth(func):
#     # 定义包内函数
#     def inner(*args, **kwargs):
#         # 被装饰功能运行前
#         if user_login:
#             # 被装饰功能运行
#             res = func(*args, **kwargs)
#             # 被装饰功能运行后
#             return res
#         else:
#             login()
#
#     return inner
#
#
# @auth
# def play():
#     print('正在运行paly功能')
#     pass
#
#
# @auth
# def sing():
#     print('正在运行sing功能')
#     pass
#
#
# if __name__ == '__main__':
#     get_userdata()
#     login()
#     play()
#     sing()


# 五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，
# 在超时时间内无需重复登录，超过了超时时间，则必须重新登录

# 定义装饰器名称：
import time

sum_time = 0


def time_wait(func):
    wait_time = 6

    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        global sum_time
        sum_time += (end_time - start_time)
        print(f'登录后执行的总时长: {sum_time}')
        if sum_time <= wait_time:
            return res
        else:
            login()
            sum_time = 0

    return inner


@time_wait
def func1():
    time.sleep(2)
    print('func1功能运行了')

    pass


@time_wait
def func2():
    time.sleep(3)
    print('func2功能运行了！')
    pass


if __name__ == '__main__':
    func1()
    func2()