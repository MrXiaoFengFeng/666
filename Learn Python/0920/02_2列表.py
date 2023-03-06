#1.作用：按位置存放多个值


#类型转换：但凡能够被for循环遍历的类型都可以当做传输传给list()转成列表
# res = list('hello')
# print(res)

# res1 = list({'k1':'a111','k2':222,'k3':333})
#
# print(res1)


# list = [{"name": "推荐食谱", "1": "症状", "name1": "浑身忽冷忽热"}, {"name": "绿豆薏米饭"}, {"name": "芝麻"}]
#
# for item in list:
#     print(item)
#     for k,v in item.items():
#         print(k,v)
#列表中插入值
# l = [111,222,'aaa','333','hello']
# #1.追加
# l.append(666)
# print(l)
# l1 = [1, 2, 3, 4, ['jason']]
# l2 = l1[::]
# print(l2) #[1, 2, 3, 4, ['jason']]
# l1[-1].append(666)
# print(l2) #[1, 2, 3, 4, ['jason', 666]]
# #2.插入值
# l.insert(2,"show")
# print(l)
#
# #3.插入列表
# new_l = [1,2,3]
# l.extend(new_l)
# print(l)


#删除
# l = [111,'egen','hello',666]
# #方式1：del通用的删除方法，只是单纯层删除，没有返回值
# del l[1]
# print(l)
#方式2：l.pop()删除有返回值
# l = [111,'egen','hello',666]
# x = l.pop() #不指定索引就默认删除最后一个
# y = l.pop(2) #删除制定索引
# print(x)
# print(y)
# print(l)

#方式3：l.remove()根据元素删
# l = [111,'egen',[1,2,3],'hello',666]
# l.remove([1,2,3])
# l.remove(666)
# print(l)


# 切片  切片等同于拷贝行为

#循环

#其他操作

# l = [111,'egen',[1,2,3],'hello',666]
# #列表反转
# l.reverse()
# print(l)
#


#l.sort() 排序,默认从小到大,列表中须是同一种类型（常用为数字和字母）
# l = [11,3,-6,3,1]
# l.sort() #[-6, 1, 3, 3, 11]
# l.sort(reverse=True) #[11, 3, 3, 1, -6]
# print(l)
#
# l1 = ['d','c','n','a']
# l1.sort()
# print(l1)


