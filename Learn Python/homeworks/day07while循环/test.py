'''
作业（必做题）：
#1. 使用while循环输出1 2 3 4 5 6     8 9 10
#2. 求1-100的所有数的和
#3. 输出 1-100 内的所有奇数
#4. 输出 1-100 内的所有偶数
#5. 求1-2+3-4+5 ... 99的所有数的和
#6. 用户登陆（三次机会重试）
#7：猜年龄游戏
    要求：
    允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出

#8：猜年龄游戏升级版（选做题）
要求：
    允许用户最多尝试3次
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
    如何猜对了，就直接退出
'''


#1. 使用while循环输出1 2 3 4 5 6     8 9 10
# number = 1
# while number < 11:
#     if number != 7:
#
#         print(number,end=' ')
#     number += 1

# number = 1
# while number < 11:
#     if number == 7:
#         number += 1
#         continue
#     print(number,end=' ')
#     number += 1


#2. 求1-100的所有数的和

# number = 1
# result = 0
#
# # 先获取1-100之间的数值,然后通过一个新的变量进行累加
#
# while number < 101:
#     # print(number)  #打印1-100
#     result += number
#
#     number += 1
# print(result)  # 5050


#3. 输出 1-100 内的所有奇数
# number = 1
# while number < 101:
#     # 如果number/2 = 0就是偶数，=1则为奇数
#     if number % 2 != 0:
#     # if number % 2 == 1:
#         print(number, end=' ')
#     number += 1
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99


#4. 输出 1-100 内的所有偶数
# number = 1
# while number < 101:
#     # 如果number/2 = 0就是偶数
#     # if number % 2 == 0:
#     if number % 2 != 1:
#         print(number, end=' ')
#     number += 1
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100


#5. 求1-2+3-4+5 ... 99的所有数的和
# number = 1
# result = 0
# while number < 100:
#
#     # print(number,end=' ')
#
#     # 奇数相加
#     if number %2 == 1:
#         result += number
#     else:
#         # 偶数相减
#         result -= number
#     number = number + 1
# print(result)


#6. 用户登陆（三次机会重试）
# init_username = 'tank'
# init_password = '123'
# count = 1
# while count < 4:
#     username = input('请输入你的用户名：》').strip()
#     password = input('请输入你的密码：》').strip()
#     if username == init_username and password == init_password:
#         print('登录成功')
#     else:
#         print('账号密码错误，重新输入！')
#         count += 1

#7：猜年龄游戏
# 要求：
# 允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# count = 1
#
# init_age = 18
#
# while count < 4:
#     input_number = input('请输入你猜测的年龄：》')
#     if input_number.isdigit():
#         input_number = int(input_number)
#         if input_number == init_age:
#             print('猜对了')
#             break
#         else:
#             print(f'猜错啦请重新输入！你还有{3-count}次机会')
#             count += 1
#     else:
#         print('输入有误，请重新输入')


#8：猜年龄游戏升级版（选做题）
# 要求：
# 允许用户最多尝试3次
# 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
# 如何猜对了，就直接退出
# '''

#
# count = 1
#
# init_age = 18
#
# while count < 4:
#     input_number = input('请输入你猜测的年龄：》')
#     if input_number.isdigit():
#         input_number = int(input_number)
#         if input_number == init_age:
#             print('猜对了')
#             break
#         else:
#             print(f'猜错啦请重新输入！你还有{3-count}次机会')
#             count += 1
#
#             if count == 4:
#                 choice = input('请输入Y/y,赠送3次；输入N/n,退出')
#                 if choice in ['Y','y']:
#                     count = 1
#                 elif choice in ['N', 'n']:
#                     break
#
#     else:
#         print('输入有误，请重新输入')
