#列表生成式

# l = [表达式 for x in 可迭代对象 if 条件]

#案例，将结尾是dsb的名字存入新列表
l = ['tom_dsb','jack_dsb','jerry_dsb','jojo_dsb','egon']
# new_l = []

# for name in l:
#     if name.endswith('dsb'):
#         new_l.append(name)
# print(new_l) # ['tom_dsb', 'jack_dsb', 'jerry_dsb', 'jojo_dsb']


#条件判断,条件成立，取值
new_l = [name for name in l if name.endswith('dsb')]
print(new_l)  # ['tom_dsb', 'jack_dsb', 'jerry_dsb', 'jojo_dsb']

#条件判断，意思是条件都为真，取所有
new_2 = [name for name in l if 3>2]
print(new_2)  # ['tom_dsb', 'jack_dsb', 'jerry_dsb', 'jojo_dsb', 'egon']


#不加条件判断，则意思是条件都为真，取所有
new_3 = [name for name in l]
print(new_3) # ['tom_dsb', 'jack_dsb', 'jerry_dsb', 'jojo_dsb', 'egon']


# 练习：
#把所有小写字母变成大写
res = [name.upper() for name in l]
print(res)

#把所有名字去掉后置_dsb
res1 = [name.strip('_dsb') for name in l]
# res1 = [name.split('_')[0] for name in l]
# res1 = [name.replace('_dsb','') for name in l]
print(res1)