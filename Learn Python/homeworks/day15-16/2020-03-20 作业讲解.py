# 今日作业：
#     1、函数对象优化多分支if的代码练熟
# def login():
#     pass
#
#
# def register():
#     pass
#
#
# # func_dic = {
# #     '1': ['登录', login],
# #     '2': ['注册', register],
# # }
# func_dic = {
#     '1': login,
#     '2': register
# }
#
# while True:
#     print('''
#     欢迎来到Tank系统
#     1、登录功能
#     2、注册功能
#     ''')
#
#     choice = input('请输入功能编号: ').strip()
#
#     if choice not in func_dic:
#
#         continue
#
#     func_dic.get(choice)()  # func_dic.get('1') ---> ['登录', login][1] ---> login()


#     2、编写计数器功能，要求调用一次在原有的基础上加一
#         温馨提示：
#             I:需要用到的知识点：闭包函数+nonlocal
#             II:核心功能如下：
#                 def counter():
#                     x+=1
#                     return x
#
#
#         要求最终效果类似
#             print(couter()) # 1
#             print(couter()) # 2
#             print(couter()) # 3
#             print(couter()) # 4
#             print(couter()) # 5

# 闭包: 函数对象、名称空间、函数嵌套
# def outer(x):  # outer局部名称空间: x ---> 0
#
#     def inner():
#         # print(x)
#         nonlocal x
#         x += 1
#         return x
#
#     return inner
#
#
# counter = outer(0)  # inner ---> counter
# # res = counter()  # ---> inner()
# # print(res)  # 1
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())



# # ====================周末作业====================
# # 编写ATM程序实现下述功能，数据来源于文件db.txt
# # 0、注册功能：用户输入账号名、密码、金额，按照固定的格式存入文件db.txt
all_user_dict = {

}
# 获取所有用户的数据
def get_all_users():
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user, pwd, balance = line.strip().split(':')
            # tank:9527:100000 ---> all_user_dict ---> {'tank': ["9527", 100000]}
            all_user_dict[user] = [pwd, balance]

# 调用函数执行函数体代码
get_all_users()

# 注册功能
def register():

    # 打开文件，获取文件中所有用户的数据
    # with open('db.txt', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         user, pwd, balance = line.strip().split(':')
    #         # tank:9527:100000 ---> all_user_dict ---> {'tank': ["9527", 100000]}
    #         all_user_dict[user] = [pwd, balance]

    # 文件关闭后，相当于字典中有了所有的用户
    '''
    all_user_dict
    {
    'tank': ['9527','100000']
    'egon': ['321','250']
    'alex': ['567','100']
    }
    '''
    while True:
        # 让用户输入用户名  ---> tank
        username = input('请输入用户名: ').strip()
        # 1、校验用户是否存在 in
        # if tank in ['tank', 'egon', 'alex']:
        if username not in all_user_dict:

            # 2、若用户不存在，则继续让用户输入密码，进行注册
            password = input('请输入密码: ').strip()
            re_password = input('请输入密码: ').strip()

            # 3、判断两次密码是否一致
            if password == re_password:

                # 4、可以让用户输入注册的金额
                balance = input('请输入注册金额：').strip()
                if balance.isdigit():

                    # 5、将新的用户数据追加到db.txt文件中
                    with open('db.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{username}:{password}:{balance}')

                    print(f'[{username}]注册成功')
                    break

                else:
                    print('请输入数字类型')

            else:
                print('注册失败!')

        else:
            # 若存在，则让用户重新输入
            print('当前用户已存在，请重新输入!')

# 测试功能
# register()

# # 1、登录功能：用户名不存在，要求必须先注册，用户名存在&
# 输错三次锁定，登录成功后记录下登录状态（提示：可以使用全局变量来记录）

# 全局变量
login_user = None

# 用于记录用户是否锁定，
# locked_users = {}

# 登录功能
def login():
    # with open('db.txt', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         user, pwd, balance = line.strip().split(':')
    #         # tank:9527:100000 ---> all_user_dict ---> {'tank': ["9527", 100000]}
    #         all_user_dict[user] = [pwd, balance]

    while True:

        # 1、请输入用户名，判断用户名是否存在
        username = input('请输入用户名: ').strip()

        # 若用户不存在
        if username not in all_user_dict:
            # 不存在，则调用注册函数
            register()
            continue

        # 判断该用户是否被锁定，若锁定则让其退出登录
        if all_user_dict.get(username)[2]:  # True
            print('当前用户已被锁定!')
            break

        count = 0
        while count < 3:
            # 2、若用户存在，则继续输入密码，进行登录校验
            password = input('请输入密码: ').strip()
            # all_user_dict.get(username) --> [pwd, balance]
            # passsword == pwd
            if password == all_user_dict.get(username)[0]:

                # 3、若用户登录成功后，则引用外部传入的全局变量进行修改，
                # 将当前登录的用户名存放在全局变量login_user中，用于证明已经有用户登录了
                global login_user  # 默认为 None
                login_user = username
                print('登录成功!')
                break

            else:
                count += 1
                print('密码错误!')

                # 若count == 3时，证明用户输错三次了，则将该用户锁定
                if count == 3:
                    # {tank: True}
                    # locked_users[username] = True

                    # {'tank': ["9527", 100000]}
                    # ["9527", 100000]  -----> ["9527", 100000, True]
                    all_user_dict[username][2] = True
        break

login()

# 下述操作，要求登录后才能操作
# # 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# # 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# # 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# # 4、查询余额功能：输入账号查询余额

'''
答案: 借鉴2020-03-17选做题
'''


