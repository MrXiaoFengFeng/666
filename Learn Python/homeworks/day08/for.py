'''
# 一：for循环
# 1.1 for循环嵌套之打印99乘法表
# 1.2 for循环嵌套之打印10层金字塔
# 1.3 用for+range改写今日早晨默写的代码，作为明天默写内容

# 二：字符串操作
# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
# name = " aleX"
# print(name)
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# 6)    将 name 变量对应的值变大写,并输出结果 
# 7)    将 name 变量对应的值变小写,并输出结果 
# 8)    请输出 name 变量对应的值的第 2 个字符?
# 9)    请输出 name 变量对应的值的前 3 个字符?
# 10)    请输出 name 变量对应的值的后 2 个字符? 
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# 12)    获取子 "序列" ,去掉最后一个字符。如: oldboy 则获取 oldbo。
'''

# 一：for循环
# 1.1 for循环嵌套之打印99乘法表

# for i in range(1,10):
#     # print(i)
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end=' ')
#     print()

# 1.2 for循环嵌套之打印10层金字塔
#金字塔公式：
# 需要打印的空格为 = 最高层数（max_level）- 当前层数(current_levle)
# 需要打印的* = 2 * 当前层数（current） - 1
#先定义一个最高层数

# 树叶层数
# max_level = 10
#
# for current_level in range(1, max_level+1):
#     # 打印每一层空格
#     for i in range(max_level - current_level):
#         print(' ', end='')
#
#     # 打印每一层的*
#     for j in range(2 * current_level -1):
#         print('*',end='')
#
#     # 打印换行
#     print()
#
# # 树干层数
# for x in range(3):
#     print(' '*(max_level-1) + '|')

# 其他方式
# max_level = 5
# for line in range(1, 10, 2):
#     n = '*' * line
    # 字符串的内置方法：center(宽度，'填充的字符')
#     print(n.center(max_level*2, ' '))




# 1.3 用for+range改写今日早晨默写的代码，作为明天默写内容
#用户登陆（三次机会重试）
# init_username = 'tank'
# init_password = '123'
#
# for i in range(3):
#     username = input('请输入用户名：》').strip()
#     password = input('请输入密码：》').strip()
#     if username == init_username and password == init_password:
#         print('登录成功！')
#     else:
#         print(f'用户名密码错误，请重新输入！你还有{2-i}次机会')



# 二：字符串操作
# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
name = " aleX"
print(name)
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip( ))
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
print(name.startswith("al"))
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
print(name.endswith("al"))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
print(name.replace('l', 'p'))
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
print(name.split('l'))
# 6)    将 name 变量对应的值变大写,并输出结果 
print(name.upper())
# 7)    将 name 变量对应的值变小写,并输出结果 
print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 9)    请输出 name 变量对应的值的前 3 个字符?
print(name[0:3])
# 10)    请输出 name 变量对应的值的后 2 个字符? 
print(name[-2:])
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
print(name.index('e'))
# 12)    获取子 "序列" ,去掉最后一个字符。如: oldboy 则获取 oldbo。
print(name[:-1])


