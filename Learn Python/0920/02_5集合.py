"""
集合
定义：在{}内用逗号分隔开多个元素，集合具备以下三个特点：
     1：每个元素必须是不可变类型
     2：集合内没有重复的元素
     3：集合内元素无序
"""
# s = {1,2,3,4}  # 本质 s = set({1,2,3,4})
# d= {} #默认是空字典
# d = set() #这是定义空集合

# 类型转换
# s = set([1,2,3,4])
# s1 = set((1,2,3,4))
# s2 = set({'name':'tom',})
# s3 = set('egon')
# print(s,s1,s2,s3)
#{1, 2, 3, 4} {1, 2, 3, 4} {'name'} {'n', 'g', 'e', 'o'}
#
# # 关系运算
# pythons = {'jason','egon','keven','rick','bubu','gaga'}
# linuxs = {'rick','bubu','tony'}
# #1.交集&：共同的数据
# s1 = pythons & linuxs
# print(s1) #{'bubu', 'rick'}
#
# #2.合集| ：求两组数据加在一起的数据（重复数据只留一个）
# s2 = pythons | linuxs
# print(s2) #{'keven', 'egon', 'bubu', 'gaga', 'rick', 'jason', 'tony'}
#
# #3.差集-：s3=数据1独有的  s3_1=数据2独有的
# s3 = pythons - linuxs
# print(s3) #{'keven', 'gaga', 'jason', 'egon'}
# s3_1 = linuxs - pythons
# print(s3_1)  #{'tony'}
#
# #4.对称差集^:去掉共同的数据
# s4 = pythons ^ linuxs
# print(s4) #{'tony', 'egon', 'keven', 'gaga', 'jason'}
#
# #5.值是否相等
# print(pythons == linuxs) #False

# 6.父集：一个集合是否包含另外一个集合
# 6.1 包含则返回True
# >>> {1,2,3} > {1,2}
# True
# >>> {1,2,3} >= {1,2}
# True
# # 6.2 不存在包含关系，则返回True
# >>> {1,2,3} > {1,3,4,5}
# False
# >>> {1,2,3} >= {1,3,4,5}
# False
#
#
# # 7.子集
# >>> {1,2} < {1,2,3}
# True
# >>> {1,2} <= {1,2,3}
# True

#==============================================
#去重
#例如需求为列表中排重排序
# l=['a','b',1,'a','a']
# s = set(l) #{1, 'a', 'b'}列表转化为集合，集合排重，但集合为乱序
# print(s)
# l_new = list(s) #集合转换回列表
# print(l_new) #['a', 'b', 1] #乱序
# 针对排重+排序实现：
# l=[
#     {'name':'lili','age':18,'sex':'male'},
#     {'name':'jack','age':73,'sex':'male'},
#     {'name':'tom','age':20,'sex':'female'},
#     {'name':'lili','age':18,'sex':'male'},
#     {'name':'lili','age':18,'sex':'male'},
# ]
#
# new_l = []
# for dic in l:
#     if dic not in new_l:
#         new_l.append(dic)
# print(new_l) #[{'name': 'lili', 'age': 18, 'sex': 'male'}, {'name': 'jack', 'age': 73, 'sex': 'male'}, {'name': 'tom', 'age': 20, 'sex': 'female'}]
#


#=======集合去重局限性===============
# 1.只能针对不可变类型去重
#
# 2.无法保证原来的顺序


#其他内置方法：
s = {1,2,3}
s.discard(2) #删除元素。若元素不存在就什么都不做
print(s) #{1, 3}
s.discard(5)
print(s) #{1, 3}













# list = ['a','b','c','d',1]
# list.append('e')
# print(list)
# list.extend(['e','f','g',10])
# print(list)

#
# l = ['a','b',1,'a','a']
# s = set(l)
# print(s)