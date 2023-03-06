# 1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作

# 1.定义函数,传入三个形参，文件，被修改的内容，修改后的内容

# def change_file(filepath, old, new):
#     '''
#     :param filepath: 需要修改内容的文件
#     :param old: 被修改的内容
#     :param new: 修改后的内容
#     :return:
#     '''
#     #2. 定义一个空列表，传入文件中读取的文本内容
#     list = []
#     #3.读取文件的内容，将修改后的内容写入空列表
#     with open(filepath, 'r', encoding='utf-8') as f:
#         for line in f:
#             line = line.replace(old, new)
#             list.append(line)
#             print(list)
#     #将新的数据重新写进文件
#     with open(filepath, 'w', encoding='utf-8') as f:
#         for line in list:
#             f.write(line)
#
# change_file('test.txt', 'egon', 'jojo')


# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

# 1.定义函数，传入字符串

# def count_str(str):
#     '''
#
#     :param str:传入的字符串
#     :return:
#     '''
#
#     dict_count = {
#         'numbers': 0,
#         'letters': 0,
#         'blanks': 0,
#         'others': 0,
#     }
#     for i in str:
#         #数字
#         if i.isdigit():
#             dict_count['numbers'] += 1
#         #字母
#         elif i.isalpha():
#             dict_count['letters'] += 1
#         #空格
#         elif i.isspace():
#             dict_count['blanks'] += 1
#         #其他
#         else:
#             dict_count['others'] += 1
#     #将统计完的字典返回
#     return dict_count
# res = count_str('fsdfsdg wee2432sdgsd s34 sdf wq2432 !@!#$@$#52sdf 2#$2\sadf')
# print(res)



# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

#定义函数

# def count_len(obj):
#     if len(obj) <= 5:
#         print('你输入的数据长度小于5')
#     else:
#         print(f'对啦{obj}合格')
# a = [1,2,3,5,6,7]
# # a = (1,2,)
# # a = 'dfsdfd'
# count_len(a)


# 4、写函数，检查传入列表的长度，如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。

# def check_list(list):
#     if len(list) > 2:
#         return list[0:2]
#     else:
#         print('长度不够2')
#
# list = [1,23,4,54,56]
# res = check_list(list)
# print(res)


# 5、写函数，检查获取传入列表或元组对象的
# 所有 "奇数位索引" 对应的元素，并将其作为新列表返回给调用者。
#
# def check(obj):
#     return obj[1::2]
# res = check([2,3,43,5,46,65,7,2])
# print(res)


# 6、写函数，检查字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表

def check_dic(dic):
    for key, value in dic.items():
        print(key,value)
        if len(value) > 2:
            dic[key] = value[:2]
    return dic

dic = {"k1": "v1v1", "k2": [11,22,33,44]}
res = check_dic(dic)
print(res)









