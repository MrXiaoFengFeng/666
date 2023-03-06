# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
# egon male 18 3000
# alex male 38 30000
# wupeiqi female 28 20000
# yuanhao female 28 10000
#
# 要求:
# 从文件中取出每一条记录放入列表中,
# 列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
# 方式一：
def add_data():
    user_list = []
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            name, sex, age, salary = line.strip().split(' ')
            user_list.append(
                {'name': name, 'sex': sex, 'age': age, 'salary': salary}
            )

    return user_list


user_list = add_data()
# print(user_list)

# 方式2：用一行代码实现
# def add_data():
#     with open('db.txt', 'r', encoding='utf-8') as f:
#         user_list = [
#             [{'name': line2[0], 'sex': line2[1], 'age': line2[2], 'salary': line2[3]}
#              for line2 in
#              [line.strip().split(' ') for line in f]]
#         ]
#
#     return user_list
#
#
# res = add_data()
# print(res)


# 2 根据1得到的列表,取出所有人的薪资之和
# print(sum(int(user.get('salary')) for user in user_list))  # 63000

# 3 根据1得到的列表,取出所有的男人的名字
# res = filter(lambda user_name: user_name.get('sex') == 'male', user_list)
#
# print(list(res))
# #[{'name': 'egon', 'sex': 'male', 'age': '98', 'salary': '3000'},
# # {'name': 'wupeiqi', 'sex': 'male', 'age': '68', 'salary': '20000'}]


# 4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式

# res = map(lambda x:
#           {'name': x.get('name').capitalize(), 'sex': x.get('sex'), 'age': x.get('age'), 'salary': x.get('salary')}, user_list)
# print(list(res))
# [{'name': 'Egon', 'sex': 'male', 'age': '98', 'salary': '3000'}, {'name': 'Alex', 'sex': 'female', 'age': '78', 'salary': '30000'}, {'name': 'Wupeiqi', 'sex': 'male', 'age': '68', 'salary': '20000'}, {'name': 'Yuanhao', 'sex': 'female', 'age': '88', 'salary': '10000'}]



# 5 根据1得到的列表,过滤掉名字以a开头的人的信息

# res = filter(lambda user_name: not user_name.get('name').startswith('a'), user_list)
# print(list(res))
# [{'name': 'egon', 'sex': 'male', 'age': '98', 'salary': '3000'}, {'name': 'wupeiqi', 'sex': 'male', 'age': '68', 'salary': '20000'}, {'name': 'yuanhao', 'sex': 'female', 'age': '88', 'salary': '10000'}]


# 6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 5 8 13...)
# 0 1 1 2 3 5 8 13...
# 普通版
# a = 0
# b = 1
#循环取a 的值
# while a < 100:
#     print(a, end=' ')
#     a, b = b, a+b

#0 1 1 2 3 5 8 13 21 34 55 89


# 递归版
# def func(a, b, stop):
#     '''
#     :param a:初始值0
#     :param b:初始值1
#     :param stop:斐波那契数列最大值
#     :return:
#     '''
#     if a > stop:
#         return
#     print(a, end=' ')
#     func(b, a + b, stop)
#
#
# func(0, 1, 100)

# 0 1 1 2 3 5 8 13 21 34 55 89



# 7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值

l=[1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]

def get_value(l):
    # 循环列表
    for i in l:
        if type(i) is list:
            get_value(i)
        else:
            print(i,end=' ')

get_value(l)