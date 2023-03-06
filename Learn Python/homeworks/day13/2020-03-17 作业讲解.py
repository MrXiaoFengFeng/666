# 1、编写文件修改功能，调用函数时，传入三个参数
# （修改的文件路径，要修改的内容，修改后的内容）既可完成文件的修改

'''  test.txt文件中内容
tank
tank1
tank2
tank3
tank4
tank5
tank6
'''
# 答案:
import os


# 函数定义
def change_file(file_path, old, new):
    '''
    :param file_path: 修改的文件路径
    :param old: 要修改的内容
    :param new: 修改后的内容
    :return:
    '''

    # 1) 先将文件中所有的数据一行一行读取出来
    # 注意: 不要同时操作同一个文件
    # file_path: /python相关/python_files/01 python班级/python14期/作业讲解/day13/test.txt
    # 方式一: 操作系统同时打开了两个文件，同时占用操作系统两个资源
    # with open(file_path, 'r', encoding='utf-8') as f, open('copy.txt', 'w', encoding='utf-8') as w:
    #     # 如果文件比较大的时候，用for循环一行一行读取更好
    #     for line in f:
    #         line = line.replace(old, new)  # old:tank3,  new: egon
    #
    #         # list1.append(line)
    #         w.write(line)
    # 将修改后的数据copy.txt文件，改名为file_path
    # os.rename('copy.txt', file_path)

    # 方式二: 操作系统只开一个文件
    list1 = []
    with open(file_path, 'r', encoding='utf-8') as f:
        # 如果文件比较大的时候，用for循环一行一行读取更好
        for line in f:
            line = line.replace(old, new)  # old:tank3,  new: egon
            list1.append(line)

    # 执行到此处，操作系统已经回收打开文件的资源
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in list1:
            f.write(line)


# 函数调用
# change_file(
#     '/python相关/python_files/01 python班级/python14期/作业讲解/day13/test.txt',
#     'tank3',
#     'egon'
# )


# 2、编写tail工具
# 函数定义
def tail_util(log_path):
    '''
    :param log_path: 用于接收，需要监听的日志文件
    :return:
    '''
    import time

    with open(log_path, 'rb') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                print(line.decode('utf-8'))
            else:
                time.sleep(0.2)


# 函数调用
# tail_util('access.log')


# 3、编写登录功能


# 注意: 用于最后一题
# user_info --> 用于记录当前用户是否登录，
# 若已登录，则给user对应的value值替换成当前用户名
user_info = {'user': None}


# 函数定义
def login():
    username = input('请输入用户名: ').strip()
    password = input('请输入密码: ').strip()
    if username == 'tank' and password == '123':

        user_info['user'] = username

        print('登录成功!')
    else:
        print('登录失败!')


# 函数调用
login()


# 4、编写注册功能
# 函数定义
def register():
    username = input('请输入用户名: ').strip()
    password = input('请输入密码: ').strip()
    re_password = input('请输入密码: ').strip()
    if password == re_password:
        print(f'[{username}]注册成功')

    else:
        print('注册失败!')


# 函数调用
# register()


# 5、编写权限认证功能
# 函数定义
def check_role(username, password, role):
    if username == 'tank' and password == '123':

        if role == 'SVIP':
            print('超级会员，尊享所有服务~')

        elif role == 'VIP':
            print('普通会员，享受部分服务~')

        else:
            print('当前用户没有服务权限~')


# 函数调用
# check_role('tank', '123', 'SVIP')


# 选做题：编写ATM程序实现下述功能，数据来源于文件db.txt
# db.txt
'''
tank:0

'''


# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 函数定义
def pay_money(username):
    '''
    :param username: 充值的用户
    :return:
    '''
    # {'tank': 0}  0 ---> 1000
    # 1) 将db.txt文件中所有的用户数据读取出来存放在一个字典中
    dic = {}  # 用于存放用户名与金额的字典
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic[user] = int(money)

    # 校验用户是否登录
    if not user_info.get('user'):
        # 若果没有用户登录，则调用登录功能
        login()

    # 2) 校验当前传入的username用户是否存在
    if username not in dic:
        print('用户不存在,结束程序!')
        # 若用户不存在，则结束程序
        return

    # 3) 循环让用户输入充值的金额
    while True:
        money = input('请输入充值金额').strip()
        # 若用户输入的不是数字，则让用户重新输入
        if not money.isdigit():
            print('输入的必须是数字!')
            continue

        money = int(money)

        # 4) 给当前用户的金额加钱
        dic[username] += money

        # 5) 将修改后的用户数据重新写入文件中
        with open('db.txt', 'w', encoding='utf-8') as f:
            for user, money in dic.items():
                f.write(f'{user}:{money}\n')
        break


# 函数调用
# pay_money('tank')


# 2、转账功能：用户A向用户B转账1000元，db2.txt中完成用户A账号减钱，用户B账号加钱
'''db2.txt
tank:2000
egon:1001

'''


# 函数定义
def transfer(A_user, B_user, transfer_money):
    '''

    :param A_user: 转账用户
    :param B_user: 收款用户
    :param money: 转账金额
    :return:
    '''
    dic = {}
    with open('db2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic[user] = int(money)

    # 校验用户是否登录
    if not user_info.get('user'):
        # 若果没有用户登录，则调用登录功能
        login()

    # 作业: 判断转账用户与收款用户是否存在
    if A_user not in dic:
        print('转账用户不存在')
        return

    if B_user not in dic:
        print('收款用户不存在')
        return

    print('转账前： ', dic)
    # 1) 判断转账用户的金额是否 大于 等于 转账金额
    if dic.get(A_user) >= transfer_money:

        # 2)转账用户扣钱
        dic[A_user] -= transfer_money

        # 3)收款用户加钱
        dic[B_user] += transfer_money

        print('转账后： ', dic)

        # 4) 此时转账与收款用户的数据都已经修改过了，重新写入文件中
        with open('db2.txt', 'w', encoding='utf-8') as f:
            for user, money in dic.items():
                f.write(f'{user}:{money}\n')


# 函数调用
# transfer('egon', 'tank', 1000)


# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
'''db3.txt
tank:2000
egon:1001

'''


# 函数定义
def withdraw(username, get_money):
    '''
    :param user: 提现用户
    :param money: 提现金额
    :return:
    '''
    # 1）获取所有用户的数据
    dic = {}
    with open('db3.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic[user] = int(money)

    # 校验用户是否登录
    if not user_info.get('user'):
        # 若果没有用户登录，则调用登录功能
        login()

    # 2) 判断当前用户是否存在
    if username not in dic:
        return

    if dic.get(username) >= get_money:
        # 提现用户扣钱
        dic[username] -= get_money

        print(dic)
        with open('db3.txt', 'w', encoding='utf-8') as f:
            for user, money in dic.items():
                f.write(f'{user}:{money}\n')


# 函数调用
withdraw('egon', 1)


# 4、查询余额功能：输入账号查询余额
def check_money(username):
    dic = {}
    with open('db3.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic[user] = int(money)

    # 校验用户是否登录
    if not user_info.get('user'):
        # 若果没有用户登录，则调用登录功能
        login()

    # 2) 判断当前用户是否存在
    if username not in dic:
        return

    # 3) 返回当前用户的金额
    return dic.get(username)

# 调用函数
# money = check_money('tank')
# print(money)


# 选做题中的选做题：登录功能
# 用户登录成功后，内存中记录下该状态，上述功能以当前登录状态为准，必须先登录才能操作
