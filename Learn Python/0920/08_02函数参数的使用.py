# 一.**************形参与实参介绍*************
# 形参：在定义函数阶段定义的参数称之为形式参数，简称为形参，相当于变量名
# def func(x,y): #x=1 ,y=2
#     print(x,y)
#
# #实参：在调用函数阶段传入的值称之为实际参数，简称为实参，相当于变量值
# func(1,2)

#形参与实参的关系：
#1、在调用阶段，实参（变量值）会绑定形参（变量名）
#2、这种绑定关系只能在函数体内使用
#3、实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定

#实参是传入值，可以是以下形式:
# 形式1：
# func(1,2)

# 形式2：
# a = 1
# b = 2
# func(a,b)
#
# #形式3：
# func(int('1'),2)
# func(func1(1,2),func2(3,4))

# ===============================================
# 二、*************形参与实参的具体使用*****************
#2.1位置参数：按照从左到右的顺序一次定义的参数称之为位置参数
# 位置形参：在函数定义阶段，按照从左到右的顺序直接定义的'变量名'
# 位置形参的特点：必须被传值，多一个少一个都不行
# def func(x,y):
#     print(x,y)

#位置实参:在函数调用阶段，按照从左到右的顺序依次传入的值
# 位置实参的特点：按照顺序与形参一一对应
# func(1,2)
# func(2,1)


#2.2关键字参数
# 关键字实参：在函数调用阶段，按照key=value的形式传入值
# 关键字实参特点：指名道姓给某个形参传值，可以完全不参照顺序
# def func(x,y):
#     print(x,y)
# func(y=3,x=2)

#混合使用，强调
# 1.位置实参必须放在关键字实参的前面
# func(1,y=2)
# func(y=2,1) #-->报错
#2.不能为同一个形参重复传值
# func(1,y=2,x=3) #-》报错
# func(1,2,x=3,y=4) #-》报错
# func(1,x=2) #-》报错

#2.3默认参数
#默认形参：在定义函数阶段，就已经被赋值的形参，称之为默认参数
# 默认形参特点：在定义阶段就已经被赋值，意味着在调用阶段可赋值也可不赋值
# def func(x,y=3):
#     print(x,y)
# func(x=1) #-->1 3
# func(2) #-->2 3
# func(x=1,y=444) #-->1 444
# func(1,2) #-->1 2

#默认参数示例：
# def student(name,age,gender='男'):
#     print(name,age,gender)
# student('张三',15)
# student('李四',16)
# student('小李',18,'女')
# '''
# 张三 15 男
# 李四 16 男
# 小李 18 女
# '''

# 位置形参与默认形参混用，强调：
# 1.位置形参必须在默认形参的左边
# def func(x,y=2): #x必须在y左边
#     pass
# 2.默认参数的值是在函数定义阶段被赋值的，准确的说是被赋予的值的内存地址
# 示范1：
# m = 2
# def func(x,y=m): #y=>2的内存地址
#     print(x,y)
# m = 33333  #y跟3333没关系
# func(1) #-->1 2

# 示范2：
# m = [1111, ]
# def func(x,y=m): #y=>[1111, ]的内存地址，列表为可变类型
#     print(x,y)
# m.append(3333)
# func(1) #->1 [1111, 3333]

# 3.虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
# 函数最理想的状态：函数的调用只跟函数本身有关系，不收外界代码的影响

# def func(x,y,z,l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     l.append(y)
#     l.append(z)
#     print(l)
# new_l = [666,777]
# func(1,2,3) #->[1, 2, 3]
# func(1,2,3,new_l) #->[666, 777, 1, 2, 3]
# ======
# num_list = [1,2,3]
# def foo(a): #a为位置形参
#     a.append(4)
# foo(num_list) #num_list为a形参对应的实参
# print(num_list) #[1, 2, 3, 4]


#2.4可变长度的参数(*与**的用法)
#可变长度值的是在调用函数时，传入的值（实参）的个数不固定
# 而实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接收

#2.4.1 可变长度的位置参数
# 形参带*格式：*形参命名  用来接收溢出的位置实参，溢出的位置实参会被*保存称【元组】的格式，
# 然后赋值紧跟其后的形参名
#*后跟的可以是任意名字，但是约定俗称应该是args
# def func(x,y,*z):
#     print(x,y,z)
# func(1,2,3,4,5,6) #1 2 (3, 4, 5, 6)
# 使用案例：
#计算一个不知道多少个数的和
# def my_sum(*args):
#     res = 0
#     for item in args:
#         res += item #->相当于res = res+item
#     return res
# res = my_sum(1,2,3,4,5) #元组元组元组
# print(res) #15
#


#2.4.2 可变长度的关键字参数
# 形参格式:**形参名 用来接收溢出的关键字实参，**会将溢出的关键字实参保存成【字典】格式，
# 然后赋值紧跟其后的形参名
#**后跟的可以是任意名字，但是约定俗称应该是kwargs
# def func(x,y,**kwargs):
#     print(x,y,kwargs) #1 2 {'a': 1, 'b': 2, 'c': 3}
#
# func(1,y=2,a=1,b=2,c=3)

#2.4.3 *可以用在实参中，实参中带*，先将*后的值拆分成位置实参

# def func(x,y,z):
#     print(x,y,z)
# # func(*[11,22,33]) #相当于func(11,22,33)
# # func(*[11,22]) #报错 TypeError: func() missing 1 required positional argument: 'z'
# l = [11,22,33]
# func(*l) #11 22 33

# 2.4.4 **可以用在实参中（**后只能是字典），实参中带**，先将**后的值拆分成关键字实参
# def func(x,y,z):
#     print(x,y,z)
# func(*{'x':1,'y':2,'z':3})  #func('x','y','z' ) ->for循环字典，只能渠道key值
# # # 结果：x y z
# func(**{'x':1,'y':2,'z':3}) #->func('x'=1,'y'=2,'z'=3)
# # #结果：1 2 3
# 错误示例：
# func(*{'x':1,'y':2}) #->func('x'=1,'y'=2) 报错TypeError: func() missing 1 required positional argument: 'z'
# func(**{'x':1,'a':2,'z':3}) #->func('x'=1,'a'=2,'z'=3) TypeError: func() got an unexpected keyword argument 'a'




#C.形参和实参带*
#
# def func(x,y,*args):
#     print(x,y,args)
# func(1,2,[3,4,5,6]) #1 2 ([3, 4, 5, 6],)
# func(1,2,*[3,4,5,6])
#第一步，将*后的值打散成位置实参：func(1,2,3,4,5,6)
#第二步，多出来的实参会分配给args形参：1 2 (3, 4, 5, 6)
# *例2
# func(*'hello')
# 第一步：func('h','e','l','l','o')
# 第二步 func(h,e,('l','l','o'))  #h e ('l', 'l', 'o')

# 例3：形参同时存在*和**：
# def func(a,*args,**kwargs):
#     print(args) #(2, 3, 4, 5)
#     print(kwargs) #{'x': 1, 'y': 2, 'z': 3}
#
# func(1,2,3,4,5,x=1,y=2,z=3)

# def func(*args,**kwargs):
#     print(args) #(1,2, 3, 4, 5) 全部接收
#     print(kwargs) #{'x': 1, 'y': 2, 'z': 3}
#
# func(1,2,3,4,5,x=1,y=2,z=3)

# 例4：形参和实参中都带**
# def func(x,y,**kwargs):
#     print(x,y,kwargs)
# func(**{'y':222,'x':111,'a':333,'b':444}) #111 222 {'a': 333, 'b': 444}


# 混用*与**: *args 必须在**kwargs之前，否则会报错

# def func(*args,**kwargs):
#     print(args) #(1,2, 3, 4, 5) 全部接收
#     print(kwargs) #{'x': 1, 'y': 2, 'z': 3}
#
# func(1,2,3,4,5,x=1,y=2,z=3)


# def index(x,y,z):
#     print('from index>>:',x,y,z)
#
# def wrapper(a,b,c): #a=1 b=2 c=3
#     index(a,b,c) #index(1,2,3)
# wrapper(1,2,3) #为wrapper传递的参数是给index用的

#如果index新增了一个形参，wrapperd 的传参受制于index，
# index如果变化，wrapper就也需要同步变化
# def index(x,y,z,bbb):
#     print('from index>>:',x,y,z,bbb)
#
# def wrapper(a,b,c,d):
#     index(a,b,c,d)
# wrapper(1,2,3,4)  #from index>>: 1 2 3 4


# 示例解析：
# def index(x,y,z):
#     print(x,y,z)  #结果1 2 3
# def wrapper(*args,**kwargs): #args = (1,),kwargs={'z':3,'y':2}
#     index(*args,**kwargs)
#     #index(*(1,),**{'z':3,'y':3})
#     #index(1,z=3,y=2)
#     #数据变化
# #【知识点】（重要）：
# # 形参带*为溢出元组聚合，形参带**为溢出字典聚合；
# # 实参带*打散为位置实参，实参带**打散为关键字实参
# wrapper(1,z=3,y=2)