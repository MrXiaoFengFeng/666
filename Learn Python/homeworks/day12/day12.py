# 1、通用文件copy工具实现

# 2、基于seek控制指针移动，测试r+、w+、a+模式下的读写内容

# 3、tail -f access.log程序实现

# 4、周末作业参考在老师讲解完毕后（下午17：30开始讲解），练习熟练，明早日考就靠他俩
# 4.1：编写用户登录接口
# 4.2：编写程序实现用户注册后（注册到文件中），可以登录（登录信息来自于文件


# 1、通用文件copy工具实现
# import os
# while True:
#     # 接收用户需要拷贝的源文件
#     source_file = input('请输入源文件路径：').strip()
#     # 判断源文件是否存在,不存在则重新输入源文件路径
#     if not os.path.exists(source_file):
#         print('当前源文件路径不存在，请重新输入')
#         continue
#     # 让用户输入拷贝后的文件路径
#     dst_file = input('请输入拷贝后的文件路径：').strip()
#     with open(source_file,'rb') as f_r,\
#             open(dst_file,'wb') as f_w:
#         for line in f_r:
#             f_w.write(line)
#     break


# 2、基于seek控制指针移动，测试r+、w+、a+模式下的读写内容
# r+ ：可读可写
# with open(r'test.txt','r+',encoding='utf-8') as f:
#     # 光标从文件文本开头，从做到右移动6个字节
#     f.seek(6)
#     # 读取四个字符
#     # res = f.read(4)
#     # print(res)  # alex
#     # 写入7777
#     f.write("7777")

# w+ :可读可写，每次打开都会覆盖原来的内容，无法读取文件的内容
# with open(r'test.txt','w+',encoding='utf-8') as f:
#     res = f.read()
#     print(res)  # 返回空

# a+ ：可读可写，无论是a或者是a+模式，追加时都会从末尾开始追加，指针移动无效
# with open(r'test.txt','a+',encoding='utf-8') as f:
#     # 指针移动后
#     f.seek(6)
#     # 读取4个字节
#     res = f.read(4)
#     print(res)
#     # 文本后追加
#     f.write('haha')


# 3、tail -f access.log程序实现
# def tail_util(log_path):
#     import time
#     # 1.读取文件的内容，循环监听
#     # with open('access.log','rb') as f:
#     with open(log_path, 'rb') as f:
#         # 将指针移动到文件的最后一行开头
#         f.seek(0, 2)
#         while True:
#             # 读取一行
#             line = f.readline()
#             # 如果最后一行有数据则打印
#             if line:
#                 print(line.decode('utf-8'))
#             else:
#                 # 否则等待，监听。
#                 time.sleep(0.2)
#
#
# tail_util('access.log')


# 4、周末作业参考在老师讲解完毕后（下午17：30开始讲解），练习熟练，明早日考就靠他俩
# 4.1：编写用户登录接口
# user_info = {}
# with open('user_info.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         user, pwd = line.strip().split(':')
#         user_info[user] = pwd  # {'tank': '123'}
# print(user_info)  # {'tank': '123', 'egon': '321', 'tank2': '321', '张全蛋': '123'}
#
# while True:
#     username = input('请输入用户名：').strip()
#     # 校验用户明是否存在
#     if username not in user_info:
#         print('当前用户不存在，请重新输入')
#         continue
#     password = input('请输入密码：').strip()
#     if password == user_info.get(username):
#         print('登录成功！')
#         break
#     else:
#         print('登录失败！')






# 4.2：编写程序实现用户注册后（注册到文件中），可以登录
#1、读取文件中所有的用户数据
user_info = {}
with open('user_info.txt', 'r', encoding='utf-8') as f:
    for line in f:
        user, pwd = line.strip().split(':')
        user_info[user] = pwd
print('用户数据为：',user_info)
while True:
    #2.让用户输入用户名密码进行注册
    username = input('请输入你的用户名：').strip()
    #3.判断用户是否存在，若存在则让用户重新输入
    if username in user_info:
        print('用户已存在，请重新输入')
        continue
    #4.如果不存在则继续输入密码
    password = input('请输入你的密码：').strip()
    re_password = input('请确认你的密码：').strip()
    #5.确认两次输入的密码是否一致
    if password == re_password:
        print('注册成功')

        #6.将注册成功的用户数据，追加到user_info.txt文件中
        with open('user_info.txt', 'a', encoding='utf-8') as f1:
            f1.write(f'{username}:{password}\n')
        break
    else:
        print('两次输入不一致!')