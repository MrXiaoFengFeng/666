#import导入模块在使用的时候，必须加前缀‘模块.’
# 优点：肯定不会与当前名称空间的名字冲突
# 缺点：加前缀显得麻烦


# from ... import ...导入也发生了三件事
# 1、产生一个模块的名称空间
# 2、运行foo.py将运行过程中产生的名字都丢到模块的名称空间中
# 3、在当前名称空间拿到一个名字，该名字与模块名称空间中的某一个内存地址


# from foo import x # x=模块foo中值0的内存地址
# from foo import get
# from foo import change

# print(x)
# print(get)
# print(change)
# x = 3333
# print(x)  # 3333,取的是当前文件全局的（没有加前缀），的x非foo内的
# get() # 1
# change() # change后的x值为： 0
# get() # 0
#
# print(x) # 1 当前文件调用change只会影响foo本身x对应的内存地址，但不会影响初始imort时拉取x的内存地址
#
# #如果想将变化的值同步成一样，则需要在change后重新导入一次
# from foo import x  # x=新地址
# print(x) #  0



#from ... import ...导入模块在使用时不用加前缀
#优点：代码更精简
#缺点：容易与当前名称空间混淆



#from ... import ...其他知识
#一行导入多个名字(不推荐)
# from foo import x,get,change
# #
# # #*:导入模块中的所有名字
# # from foo import *
# # print(x)
# # print(get)
# # print(change)

#了解：__all__
# 被导入的模块有个默认列表功能,
# 储存名字__all__ =['x','change','get']
#相当于导入模块中的*,若列表中名字缺一个，调用时则会报错

# from foo import *
# print(get)



#起别名
# from foo import get as g # get = g
# print(g) # <function get at 0x000001D461BAAB80>