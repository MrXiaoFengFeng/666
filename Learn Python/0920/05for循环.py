'''
#for 变量名 in 可迭代对象：#可迭代的对象可以是：列表、字典、字符串、元组、集合
    代码1
    代码2
'''
# 案例1：列表循环取值
# 简单版
# l = ['a','b','c']
# for x in l:
#     print(x)

# 复杂版：
# l = ['a','b','c']
# i = 0
# while i < 3:
#     print(l[i])
#     i +=1

# 案例2：字典循环取值
# 简单版
# dic = {'k1': 111, 'k2':222,'k3':333}
# for x in dic:
#     print(x,dic[x])

# 复杂版：while循环可以遍历字典，比较麻烦

# 案例3：字符串循环取值
# 简单版
# msg = 'hello python'
# for x in msg:
#     print(x)


# 二：总结for循环与while循环的异同
# 1.相同之处：都是循环，for循环可以干的事，while循环也可以干
# 2.不同之处：
#     while循环为条件循环，循环次数取决于条件何时变为假
#     for循环称之为'取值循环'，循环次数取决于in后包含值的个数

# 三：for循环控制循环次数：range()

# username= 'egon'
# password = '123'
# for i in range(3):
#     inp_name = input('请输入你的账号：')
#     inp_pwd = input('请输入你的密码：')
#
#     if inp_name == username and inp_pwd == password:
#         print('登录成功')
#         break
# else:
#     print('输入密码错误次数过多')
# 终止for循环只有break一种方案

# 四：range补充知识

# l = ['a','b','c']
# for i in range(len(l)):
#     print(i,l[i])

# 五.for + continue
# for i in range(6):
#     if i == 4:
#         continue
#     print(i)

# print('hello','word')
# print('hello',end='*')
# print('word')

# 六.for循环嵌套:外层循环循环一次，内层循环需要完整的循环完毕
# for i in range(3):
#     print('外层循环--》', i)
#     for j in range(5):
#         print('内层--》', j)
#     break
