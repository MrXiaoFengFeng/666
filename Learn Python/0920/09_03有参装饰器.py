# 一、知识储备：
# 由于语法糖@的限制，outter函数只能有一个参数，并且该参数只用来接收
# 被装饰对象的内存地址


# def outter(func):
#     # func = 函数的内存地址
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res
#
#     return wrapper
#
# @outter # index = outter(index) # index =>wrapper
# def index(x,y):
#     print(x,y)
#
# index(1,2)
# 偷梁换柱之后
# index的参数是什么样子，wrapper的参数应该就是什么样子
# index的返回值是什么样子，wrapper的返回值就应该是是什么样子
# index的属性是什么样子，wrapper的属性应该是什么样子==》from functools import wraps

# 需求：判断用户登录的用户名密码来源
# 方案1：低端玩法
# def auth(func, db_type):
#     def wrapper(*args, **kwargs):
#         name = input('please input you name:>').strip()
#         password = input('please input your password:>').strip()
#
#         if db_type == 'file':
#             print('基于文件的验证')
#             if name == 'egon' and password == '123':
#                 print('login successful')
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('username or password error')
#         elif db_type == 'mysql':
#             print('基于mysql的验证')
#         elif db_type == 'ldap':
#             print('基于ldap的验证')
#         else:
#             print('不支持该数据类型')
#
#     return wrapper
#
#
# # @auth # 账号密码来源于文件
# def index(x, y):
#     print('index-->>%s,%s' % (x, y))
#
#
# # @auth # 账号密码来源于mysql
# def home():
#     print('home')
#
#
# # @auth # 账号密码来源于ldap
# def transfer():
#     print('transfer')
#
#
# index = auth(index, db_type='file')
# home = auth(home, db_type='mysql')
# transfer = auth(transfer, db_type='ldap')
#
# index(1, 2)
# # home('egon')
# # transfer()


# 方案2语法糖：低端玩法2

# def auth(db_type):
#     # db_type = 'file'
#     def deco(func):
#         def wrapper(*args, **kwargs):
#             name = input('please input you name:>').strip()
#             password = input('please input your password:>').strip()
#
#             if db_type == 'file':
#                 print('基于文件的验证')
#                 if name == 'egon' and password == '123':
#                     print('login successful')
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('username or password error')
#             elif db_type == 'mysql':
#                 print('基于mysql的验证')
#             elif db_type == 'ldap':
#                 print('基于ldap的验证')
#             else:
#                 print('不支持该数据类型')
#
#         return wrapper
#     return deco
#
#
# deco = auth(db_type='file')
#
#
# @deco # 账号密码来源于文件
# def index(x, y):
#     print('index-->>%s,%s' % (x, y))
#
#
# @deco # 账号密码来源于mysql
# def home(name):
#     print('home name is %s'%name)
#
# deco = auth(db_type='mysql')
#
# @deco # 账号密码来源于ldap
# def transfer():
#     print('transfer')
#
# deco = auth(db_type='ldap')
#
#
# index(1, 2)
# home('egon')
# transfer()


# 方案3语法糖：
# def auth(db_type,y):  # 如果需要俩参数，就在第三层加一个形参，不影响语法糖限制
def auth(db_type):
    # db_type = 'file'
    def deco(func):
        # func = index
        def wrapper(*args, **kwargs):
            name = input('please input you name:>').strip()
            password = input('please input your password:>').strip()

            if db_type == 'file':
                print('基于文件的验证')
                if name == 'egon' and password == '123':
                    print('login successful')
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('username or password error')
            elif db_type == 'mysql':
                '''从mysql取'''
                print('基于mysql的验证')
            elif db_type == 'ldap':
                '''从ldap取'''
                print('基于ldap的验证')
            else:
                print('不支持该数据类型')

        return wrapper
    return deco


# deco = auth(db_type='file')

# 账号密码来源于文件
#@auth(db_type='file',y)
@auth(db_type='file') # @deco #index=deco(index)
def index(x, y):
    print('index-->>%s,%s' % (x, y))


@auth(db_type='mysql') # 账号密码来源于mysql
def home(name):
    print('home name is %s'%name)

# deco = auth(db_type='mysql')

@auth(db_type='ldap') # 账号密码来源于ldap
def transfer():
    print('transfer')

# deco = auth(db_type='ldap')


index(1, 2)
home('egon')
transfer()








#有参装饰器模板

def 有参装饰器(x,y,z):
    def outter(func):
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            return res
        return wrapper
    return outter

@有装饰器(1,y=2,z=3)
def 被装饰对象():
    pass
被装饰对象()



