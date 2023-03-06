"""
if条件判断
1.计算1~100的求和
2.加入分支结构实现1~100之间偶数求和
3，使用python实现1~100之间偶数的求和
"""
# #练习题1：
# result = 0
# for i in range(101):
#     print(i)
#     result = result+i
# print(result)

## 练习题2：
# result = 0
# for i in range(101):
#     if i%2 == 0:
#         result = result+i
# print(result)

# # 练习题3：
# result = 0
# for i in range(2,101,2):
#     result = result+i
# print(result)


# """
# while 循环
# """
# a = 1
# while a == 1:
#     print("a==1")
#     a = a+1
# else:
#     print("a != 1")
#     print(a)

# =============================
# break用法
# i = 0
# for i in range(1,10):
#     if i == 5:
#         break
# print(i)
# #5


# =================================
# whlile用法
# i = 0
# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)


"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示：大一点、小一点、猜对了
"""
# import random
#
# computer_num = random.randint(1,100)
# while True:
#     person_num = int(input("请输入一个数字:"))
#     if person_num > computer_num:
#         print("小一点")
#     elif person_num < computer_num:
#         print("大一点")
#     elif person_num == computer_num:
#         print("猜对了")
#         break
username = 'egon'
password = '123'
#tag条件变为false结束
# tag = True
# while tag:
#     inp_name = input('请输入你的账号：')
#     inp_pwd = input('请输入你的密码：')
#     if inp_name == username and inp_pwd == password:
#         print("登录成功")
#         tag = False
#     else:
#         print("账号或密码错误")

#break结束
# while True:
#     inp_name = input('请输入你的账号：')
#     inp_pwd = input('请输入你的密码：')
#     if inp_name == username and inp_pwd == password:
#         print("登录成功")
#         while True:
#             cmd = input('请输入你的命令')
#             if cmd == 'q':
#                 break
#             print(f'命令{cmd}正在运行')
#         break
#     else:
#         print("账号或密码错误")
##tag改编
# tag = True
# while tag:
#     inp_name = input('请输入你的账号：')
#     inp_pwd = input('请输入你的密码：')
#     if inp_name == username and inp_pwd == password:
#         print("登录成功")
#         while tag:
#             cmd = input('请输入你的命令')
#             if cmd == 'q':
#                 tag = False
#             else:
#                 print(f'命令{cmd}正在运行')
#         break
#     else:
#         print("账号或密码错误")


#while + continue:结束本次循环，直接进入下一次
# count = 0
# while count < 6:
#     if count ==4:
#         continue
#         print("hhahaha") #continue后添加同级代码无意义。不会运行
#
#     count +=1
#     print(count)

count = 0

while count < 3:
    inp_name = input('请输入你的账号：')
    inp_pwd = input('请输入你的密码：')
    if inp_name == username and inp_pwd == password:
        print("登录成功")
        while True:
            cmd = input('请输入命令：')
            if cmd == 'q':
                break
            else:
                print(f'命令{cmd}正在运行')
        break
    else:
        print(inp_name.strip(' '))
        print("账号或密码错误")
        count +=1
else:
    print('输错3次，退出')
