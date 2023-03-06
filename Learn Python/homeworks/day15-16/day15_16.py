'''
今日作业：
    1、函数对象优化多分支if的代码练熟
    2、编写计数器功能，要求调用一次在原有的基础上加一
        温馨提示：
            I:需要用到的知识点：闭包函数+nonlocal
            II:核心功能如下：
                def counter():
                    x+=1
                    return x


        要求最终效果类似
            print(couter()) # 1
            print(couter()) # 2
            print(couter()) # 3
            print(couter()) # 4
            print(couter()) # 5
'''
# 1、函数对象优化多分支if的代码练熟
# def login():
#     print('运行了登录功能')
#     pass
#
# def register():
#     print('运行了注册功能')
#     pass
#
# func_dic = {
#     '1': ['登录', login],
#     '2': ['注册', register],
# }
# while True:
#     print('''
#     欢迎来到账号系统
#     1、登录功能
#     2、注册功能
#     ''')
#     choice = input('请输入功能编号：').strip()
#     if choice not in func_dic:
#         continue
#
#     func_dic.get(choice)[1]()


# 2、编写计数器功能，要求调用一次在原有的基础上加一
# 温馨提示：
# I: 需要用到的知识点：闭包函数 +
# nonlocal
# II: 核心功能如下：
#
# def counter():
#     x += 1
#     return x
#
#
# 要求最终效果类似
# print(couter())  # 1
# print(couter())  # 2
# print(couter())  # 3
# print(couter())  # 4
# print(couter())  # 5

# # 闭包：函数对象、名称空间、函数对象
# def outter(x):  # outter局部名称空间x
#
#     def inner():
#         # print(x)
#         nonlocal x
#         x += 1
#         return x
#     return inner
#
#
# # inner = outter(0)
# # counter = inner
# counter = outter(0)
# # res = counter()
# # print(res)
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# 结果：
# 1
# 2
# 3
# 4


# ====================周末作业====================
# 编写ATM程序实现下述功能，数据来源于文件db.txt
# 0、注册功能：用户输入账号名、密码、金额，按照固定的格式存入文件db.txt
# 1、登录功能：用户名不存在，要求必须先注册，用户名存在&输错三次锁定，登录成功后记录下登录状态（提示：可以使用全局变量来记录）

# 下述操作，要求登录后才能操作
# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# 4、查询余额功能：输入账号查询余额


# 0、注册功能：用户输入账号名、密码、金额，按照固定的格式存入文件db.txt
# 编写注册功能
# 函数定义
all_user_dict = {}


# 获取所有用户的数据
def get_all_users():
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, pwd, balance = line.strip().split(':')
            all_user_dict[user] = [pwd, balance]


# 调用函数执行代码
get_all_users()


def register():
    # 打开用户数据文件，读取用户的数据

    # 文件关闭后，相当于
    '''
    {
    'tank':['9527','100000']
    'egon':['321','250']
    'alex':['567','100']
    }
    '''

    while True:
        # 1、校验用户是否存在
        # 让用户输入用户名
        username = input('请输入你注册的用户名:').strip()
        if username not in all_user_dict:
            # 2、不存在，则继续输入密码注册
            password = input('请输入注册的密码：').strip()
            re_password = input('请确认注册的密码：').strip()
            # 3、判断两次密码是否一致
            if password == re_password:
                # 4、让用户输入注册金额
                balance = input('请输入注册的金额:').strip()
                if balance.isdigit():
                    # 5、将新用户的数据追加到db.txt中
                    with open('db.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{username}:{password}:{balance}')
                        print(f'{username}注册成功')
                        break
                else:
                    print('请输入数字类型')
            else:

                print('注册失败')
        else:
            # 若存在，则让用户重新输入
            print('当前用户已存在，请重新输入')


# register()


# 1、登录功能：用户名不存在，要求必须先注册，用户名存在&输错三次锁定，
# 登录成功后记录下登录状态（提示：可以使用全局变量来记录）

# 全局变量：用户登录、锁定状态
login_user = None


# # 用于记录用户是否锁定
locked_user = {'jojo': True}


# 定义登录功能
def login():
    while True:

        # 1、请输入用户名，判断用户名是否存在
        username = input('请输入用户名：').strip()

        # 如果用户不存在
        if username not in all_user_dict:
            # 不存在，则调注册函数
            print('你输入的用户不存在，请注册')
            register()
            continue

        # 判断该用户是否被锁定，若锁定就让其退出
        if locked_user.get(username):
            print('当前用户已被锁定')
            break

        count = 0
        while count < 3:

            # 2、若用户存在，则继续输入密码，进行登录校验
            password = input('请输入密码：').strip()
            # all_user_dict.get(username) -->[pwd, balance]
            # password == pwd
            if password == all_user_dict.get(username)[0]:

                # 3、若用户登录成功后，则引用外部传入的全局变量进行修改
                global login_user  # 默认为None
                login_user = username
                print('登录成功！')
                break
            else:
                count += 1
                print('密码错误')
                # 若count == 3时，证明用户输错了三次， 则将该用户锁定
                if count == 3:
                    # print('输错3次，你已经被锁定')
                    locked_user[username] = True
                    print(locked_user)
        break


login()