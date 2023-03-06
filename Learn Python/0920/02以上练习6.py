# 去重
#
# 　　 1.
# 有列表l = ['a', 'b', 1, 'a', 'a']，列表元素均为可hash类型，去重，得到新列表, 且新列表无需保持列表原来的顺序
#
# 　　 2.
# 在上题的基础上，保存列表原来的顺序
#
# 　　 3.
# 去除文件中重复的行，肯定要保持文件内容的顺序不变
# 　　 4.
# 有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序

l = [
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'alex', 'age': 73, 'sex': 'male'},
    {'name': 'egon', 'age': 20, 'sex': 'female'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
]

# 答案
# 去重,无需保持原来的顺序
l = ['a', 'b', 1, 'a', 'a']
print(set(l))

# 去重,并保持原来的顺序
# 方法一:不用集合
l = [1, 'a', 'b', 1, 'a']

l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
# 方法二:借助集合
l1 = []
s = set()
for i in l:
    if i not in s:
        s.add(i)
        l1.append(i)

print(l1)

# 同上方法二,去除文件中重复的行
import os

with open('db.txt', 'r', encoding='utf-8') as read_f, \
        open('.db.txt.swap', 'w', encoding='utf-8') as write_f:
    s = set()
    for line in read_f:
        if line not in s:
            s.add(line)
            write_f.write(line)
os.remove('db.txt')
os.rename('.db.txt.swap', 'db.txt')

# 列表中元素为可变类型时,去重,并且保持原来顺序
l = [
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'alex', 'age': 73, 'sex': 'male'},
    {'name': 'egon', 'age': 20, 'sex': 'female'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
]
# print(set(l)) #报错:unhashable type: 'dict'
s = set()
l1 = []
for item in l:
    val = (item['name'], item['age'], item['sex'])
    if val not in s:
        s.add(val)
        l1.append(item)

print(l1)


# 定义函数,既可以针对可以hash类型又可以针对不可hash类型
def func(items, key=None):
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item


print(list(func(l, key=lambda dic: (dic['name'], dic['age'], dic['sex']))))