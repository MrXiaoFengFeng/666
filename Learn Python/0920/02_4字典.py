# dic = {'age':18,"hobbies":['game','ball'],'name':'xxx'}
# # dic.items([('name','xxx'),('age',18),('hobbies',['game','ball'])])
# print(dic.items())
# print(dic)
# res = dic.get("age1",99)
# print(res)


# v = dic.pop('age')
# print(dic)
# print(v)

# v = dic.popitem()
# print(dic)
# print(v)


# 类型转换：
#转换1：
# info = dict([['name','tom'],('age',18)])
# print(info) #{'name': 'tom', 'age': 18}

#转换2：formkeys 会从元组中取出每个值当做key，然后与None组成key:value放到字典中
# # 例1：
# dic = {}.fromkeys(('name','age','sex'),None)
# print(dic)

# 例2：
# keys = ['name','age','gender']
# d = {}.fromkeys(keys , None)
# print(d) #{'name': None, 'age': None, 'gender': None}
# #对于赋值操作，如果key原先不存在于字典，则会新增key:value
# d['name'] = 'tom'
# print(d) #{'name': 'tom', 'age': None, 'gender': None}
# # 对于赋值操作，如果key原先存在于字典，则会修改对应value的值
# d['name'] = 'joy'
# print(d) #{'name': 'joy', 'age': None, 'gender': None}
# d.setdefault('name',"99")
# print(d) #{'name': 'tom', 'age': None, 'gender': None}
# d.setdefault('name111',"kate")
# print(d) #{'name': 'tom', 'age': None, 'gender': None, 'name111': 'kate'}

# 数据类型转换例三：
# info = [
#     ['name','egon'],
#     ('age',18),
#     ['gender','male']
# ]
# #第一种方式：
# d = {}
# for x,y in info:
#     print(x,y)
#     d[x] = y
# print(d) #{'name': 'egon', 'age': 18, 'gender': 'male'}
# # 第二种内置方式：
# d = dict(info)
# print(d) #{'name': 'egon', 'age': 18, 'gender': 'male'}

#循环遍历
dic = {'name': 'xxx',
       'age': 18,
       'hobbies': ['play game', 'basketball']
}
# 默认遍历的是字典的key
# for key in dic:
#     print(key) #name age hobbies
# -----------------------------
for key in dic:
    print(key,dic[key])

#结果：
# name xxx
# age 18
# hobbies ['play game', 'basketball']



# #只遍历key
# for key in dic.keys():
#     print(key) ##name age hobbies
# #只遍历value
# for key in dic.values():
#     print(key)
# xxx
# 18
# ['play game', 'basketball']

#遍历key和value
# for key in dic.items():
#     print(key)
#
# ('name', 'xxx')
# ('age', 18)
# ('hobbies', ['play game', 'basketball'])

#数据操作
# dic = {'k1':'tom','k2':'kate','k3':'jerry'}
# #get()
# # res = dic.get('k2')
# # print(res)
# res = dic.get("k4",555) # key不存在时，可以设置默认返回的值
# print(res)  #555

#pop()
# res = dic.pop("k2") # 删除指定的key对应的键值对,并返回值
# print(res)
# print(dic)

#popitem()
# item = dic.popitem() # 随机删除一组键值对,并将删除的键值放到元组内返回
# print(item)
# print(dic)

# #update()
# dic.update({'k1': 'jone','k4':'jojo'}) # 用新字典更新旧字典，有则修改，无则添加
# print(dic)

#造字典的方式
# keys = ['name','age','gender']
#第一种方式
# d = {}
# for k in keys:
#     d[k] = None
# print(d) #{'name': None, 'age': None, 'gender': None}

# #第二种方式.快速初始化一个字典
# d= {}.fromkeys(keys,None)
# print(d) #{'name': None, 'age': None, 'gender': None}

#判断是否存在于字典中：
# dic = {'k1':'tom','k2':'kate','k3':'jerry'}
# print('2' in dic) #False
# print('k3' in dic) #True

#键keys(),值values()，键值对items() ==》py3中取得的是老母鸡
# d ={'k1':111,'k2':222}
# print(d.keys()) #dict_keys(['k1', 'k2'])
# print(d.values()) #dict_values([111, 222])
# print(d.items()) #dict_items([('k1', 111), ('k2', 222)])


# # 字典转列表：
# l =list(d.items())
# print(l)


# #d.setdefault()
# d ={'k1':111,'k2':222}
# # key不存在则新增键值对，并将新增的value返回
# d.setdefault('k1','jojo')
# print(d) #{'k1': 111, 'k2': 222}
# # key存在则不做任何修改，并返回已存在key对应的value值
# d.setdefault('k3','hh')
# print(d) #{'k1': 111, 'k2': 222, 'k3': 'hh'}
