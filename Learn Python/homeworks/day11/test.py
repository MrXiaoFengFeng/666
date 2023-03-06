'''
#一：今日作业：
#1、编写文件copy工具

#2、编写登录程序，账号密码来自于文件

#3、编写注册程序，账号密码来存入文件

#二：周末综合作业：
# 2.1：编写用户登录接口
#1、输入账号密码完成验证，验证通过后输出"登录成功"
#2、可以登录不同的用户
#3、同一账号输错三次锁定，（提示：锁定的用户存入文件中，这样才能保证程序关闭后，该用户仍然被锁定）


# 2.2：编写程序实现用户注册后，可以登录
'''

# 一：今日作业：
# 1、编写文件copy工具
#
# with open(r'.\a.txt', mode='rt', encoding='utf-8') as f1, \
#         open(r'.\b.txt', mode='wt', encoding='utf-8') as f2:
#     for line in f1:
#         f2.write(line)

# 2、编写登录程序，账号密码来自于文件

# with open(r'user.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read().split(':')
#     print(res)
#     # username = user[0]
#     # password = user[1]
#     for i in res:
#         print(i)
#     username, password = res
    # print(username)
    # print(password)

    # input_name = input('请输入用户名：》').strip()
    # input_pasword = input('请输入密码：》').strip()
    # if input_name == username and input_pasword == password:
    #     print('登录成功')
    # else:
    #     print('登录失败')



# 3、编写注册程序，账号密码来存入文件

# username = input('输入用户名：》').strip()
# password = input('输入密码:》').strip()
# with open(r'./userdb.txt', mode='at', encoding='utf-8') as f:
#     f.write(f'用户名:{username}\n密码{password}')

#二：周末综合作业：
# 2.1：编写用户登录接口
#1、输入账号密码完成验证，验证通过后输出"登录成功"
#2、可以登录不同的用户
#3、同一账号输错三次锁定，（提示：锁定的用户存入文件中，
# 这样才能保证程序关闭后，该用户仍然被锁定）

## 2.2：编写程序实现用户注册后，可以登录




tag = True
while tag:
    dic = {
        '0': '退出',
        '1': '登录',
        '2': '注册',
    }
    # 向用户展示功能列表。让用户选择
    for choice_num in dic:
        print(choice_num, dic[choice_num])



    user_choice = input('请输入你的命令：》').strip()
    if not dic.get(user_choice):
        print('不存在你输入的命令，请重新输入')

    # else:
    if user_choice == '0':
        break
    elif user_choice == '1':
        # user_choice = int(user_choice)

        while tag:
            username = input('请输入你的用户名：》').strip()
            # 打开储存用户信息文件，切分出用户名和密码以及计数
            with open(r'./userdb.txt', mode='rt', encoding='utf-8') as f1, \
                    open(r'./userdb_copy.txt', mode='wt', encoding='utf-8') as f2:
                for line in f1:
                    res = line.strip('\n').split(':')
                    name, password, count = res
                    # print(f'文件中存放的账号与密码是: {name} {password}')
                    count = int(count)
                    # print(res)
                    # print('jojo' in res)


                    if username == name:
                        while count < 3:
                            userpassword = input('请输入你的密码：》').strip()
                            if userpassword == password:
                                print('登录成功！')
                                tag = False
                                break
                            else:
                                print('登录失败')
                                count += 1
                        if count == 3:
                            print('当前用户已被锁定')

                    f2.write(f'{name}:{password}:{count}\n')

        import os
        os.remove(r'./userdb.txt')
        os.rename(r'./userdb_copy.txt',r'./userdb.txt')
    elif user_choice == '2':
        username = input('输入用户名：》').strip()
        password = input('输入密码:》').strip()
        with open(r'./userdb.txt', mode='at', encoding='utf-8') as f:
            f.write(f'{username}:{password}')



#     #
#     #
#     #
#     # break
# 具体化功能，如果存在用户则直接让输入密码，如果不存在用户则引导注册流程

# 密码正确则通知登录成功，不正确则让用户尝试3次，超过3次锁定






