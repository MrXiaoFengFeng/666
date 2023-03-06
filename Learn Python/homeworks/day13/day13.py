# 1、编写文件修改功能，调用函数时，传入三个参数
# （修改的文件路径，要修改的内容，修改后的内容）既可完成文件的修改
# 函数定义
# 方式一：
# def change_file(file_path, old, new):
#     '''
#     :param file_path: 修改的文件路径
#     :param old: 要修改的内容
#     :param new: 修改后的内容
#     :return:
#     '''
#     # 1.先将文件中所有的数据一行一行读取出来
#     list1 = []
#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             line = line.replace(old, new)
#             list1.append(line)
#
#     # print(list1)
#     with open(file_path, 'w', encoding='utf-8') as f1:
#         for line in list1:
#             f1.write(line)
# change_file(
#     'E:/WorkSpace/Learn Python/homeworks/day13/test.txt',
#     'tank3',
#     'egon'
# )

# 方式二：
# import os
#
#
# def change_file(file_path, old, new):
#     with open(file_path, 'r', encoding='utf-8') as f1, \
#             open('copy.txt', 'w', encoding='utf-8') as f2:
#         for line in f1:
#             line = line.replace(old, new)
#             f2.write(line)
#
#     os.remove(file_path)
#     os.rename('copy.txt', file_path)
#
#
# change_file(
#     'E:/WorkSpace/Learn Python/homeworks/day13/test1.txt',
#     'tank2',
#     'e66'
# )


# 2.编写tail工具
# 函数定义
# def tail_util(log_path):
#     '''
#
#     :param log_path: 用于接收，需要监听的日志
#     :return:
#     '''
#     import time
#     with open('access.log', 'rb') as f:
#         f.seek(0, 2)
#         while True:
#             line = f.readline()
#             if line:
#                 print(line.decode('utf-8'))
#             else:
#                 time.sleep(0.2)
# #函数调用
# tail_util('access.log')


# 3.编写登录功能：登录、注册、权限认证
# 注意: 用于最后一题
# user_info --> 用于记录当前用户是否登录，
# 若已登录，则给user对应的value值替换成当前用户名

# 3.1 登录

user_info = {'user': None}


def login():
    username = input('请输入你的用户名：').strip()
    password = input('请输入你的密码：').strip()
    if username == 'jojo' and password == '123':
        user_info['user'] = username
        print('登录成功')
        print(user_info)  # {'user': 'jojo'}
    else:
        print('账号或密码错误，登录失败')


# login()


# 3.2 注册

def register():
    username = input('请输入你的用户名：').strip()
    password = input('请输入你的密码：').strip()
    re_password = input('请确认你的密码：').strip()
    if password == re_password:
        print(f'用户{username}注册成功')
    else:
        print('两次输入的密码不一致，注册失败')


# register()


# 3.3 权限认证

def check_role(username, password, role):
    '''

    :param username: 用户登录的账号
    :param password: 用户登录的密码
    :param role: 用户对应的角色
    :return:
    '''
    if username == 'jojo' and password == '123':

        if role == 'vip':
            print('你享受的是vip服务')
        elif role == 'svip':
            print('你享受的是svip服务')
        else:
            print('你还不是会员')
    else:
        print('账号或密码错误')


# check_role('jojo', '123', 'svip')


# 4、选做题：编写ATM程序实现下述功能，数据来源于文件db.txt
# # db.txt
# '''
# tank:0
#
# '''
#
#
# # 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 1、定义函数
def charge_money(username):
    '''

    :param username: 给存在的用户重值
    :return:
    '''
    # 2.定义一个空字典，存放文件中读取的用户信息及金额
    dic = {}  # {tank:0}
    # 3.打开文件，读取为本中用户及金额信息
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic[user] = int(money)
    print(dic)
    # 4.检验用户是否登录
    if not user_info.get('user'):
        print('用户未登录')
        login()
    # 5.判断传入的用户名是否在字典中
    if username not in dic:
        print('用户不存在，结束程序')
        return
    # 6.如果用户已登录且存在，则让用户充值
    while True:
        money = input('请输入你想充值的金额：').strip()
        if not money.isdigit():
            print('必须输入数字')
            continue
        money = int(money)
        # 7.给当前的用户加钱
        dic[username] += money
        print(dic)
    # 8.将最终累加完的金额写进文件
        with open('db.txt', 'w', encoding='utf-8') as f:
            for user, money in dic.items():
                f.write(f'{user}:{money}\n')
            break
# charge_money('jojo')

#2.提现功能

def withdraw(username, get_money):
    '''
    :param username:
    :param get_money:
    :return:
    '''
    # 用一个字典存放文件读取出来的用户信息
    dic1 = {}
    # 打开文件读取到用户现有的信息
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic1[user] = int(money)
    print(dic1)
    #判断用户是否登录
    if not user_info.get('user'):
        print('用户未登录')
        login()
    # 判断字典内是否有该传入的用户
    if username not in dic1:
        print('用户不存在，退出程序')
        return

    # 输入取出的金额
    get_money = int(get_money)
    if get_money < dic1[username]:
        return

    else:
        dic1[user] -= money

# withdraw('jojo','100')


#3.转账功能

def transfer(A_user, B_user, transfer_money):
    '''
    :param A_user: 转账用户
    :param B_user: 收款账户
    :param transfer_money: 转账金额
    :return:
    '''
    dic = {}
    with open('db2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic[user] = int(money)
    print(dic)
    #1.判断转账用户的金额是否大于等于转账金额
    if dic.get(A_user) >= transfer_money:


        #转账用户扣钱
        dic[A_user] -= transfer_money

        #收款账户加钱
        dic[B_user] += transfer_money
        print('转账后：', dic)

        with open('db2.txt', 'w', encoding='utf-8') as f:
            for user, money in dic.items():
                f.write(f'{user}:{money}\n')

transfer('tank', 'egon',10)



