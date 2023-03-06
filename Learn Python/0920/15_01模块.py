'''
1、什么是模块
    模块就是一系列功能的集合体，分为三大类：
    I:内置的模块
    II:第三方的模块
    III:自定义的模块
        一个python文件本身就是一个模块，文件名m.py,模块名叫m

        PS：模块分为4种形式：
        1.使用python编写的.py文件
        2.已被编译为共享库或DLL的C或者C++拓展
        3.把一些列模块组织到一起的文件夹（注：文件夹下有一个__init__.py文件，该文件加称之为包）
        4.使用C编写并连接到python解释器的内置模块

2、为何要用模块
    I：内置与第三方的模块拿来就用，无需定义，这种拿来主义，可以极大的提升自己的开发效率
    II:自定义的模块
        可以将程序的各部分功能提取出来放到一个模块中为大家共享使用
        好处：减少了代码的冗余，程序组织结构更加清晰


'''
# 1.首次导入模块会发生3件事


#文件名：15_01模块foo.py
# print('模块foo==》》')
# x=1
# def get():
#     print(x)
# def change():
#     global x
#     x=0
# class Foo:
#     def func(self):
#        print('from the func')

# 当前文件为05.py，被导入的文件为foo.py
# 导入：
# import foo #模块foo==》》
# import foo # 之后的导入，都是直接引用首次导入产生的foo.py名称空间，不会重复执行代码
# import foo
# import foo
# 05[首次]导入模块会发生3件事
# 1、执行foo.py
# 2、产生foo.py的名称空间，将foo.py运行过程中产生的名字都丢到foo的名称空间中
# 3、在当前文件中产生的有一个名字foo，改名字指向2中产生的名称空间，若要引用模块名称
#       空间中的名字，需要加上该前缀，如下：



# 2.引用:指名道姓的问某一个模块要名字对应的值
# import foo   #模块foo==》》
# print(foo.x) #1
# print(foo.get) #<function get at 0x000001790C52A8B0>
# print(foo.change) #<function change at 0x000001790C52A9D0>
#强调1：模块名.名字，是指名道姓的问某一个模块要名字的对应值，不会与当前
#               名称空间中的名字发生冲突

# x = 11111
# print(x) #11111
# print(foo.x) #1


#强调2：无论是查看还是修改都是以原模块为基准的，与调用位置无关
# import foo
# x = 3333
# foo.get() #1
#
# foo.change() #将foo中的x值改为0
# foo.get() #0
# print(foo.x) #0










#3.可以以逗号为分隔符在一行导入多个模块
#建议如下所示导入多个模块
import time
import functools

#不建议在同一行同时导入多个模块，但不建议
import time, functools



#4.导入模块的规范
# I:python内置模块
# II：第三方模块
# III：程序员自定义的模块
#
# import time
# import sys
#
# import 第三方
#
# import 自定义模块

#5.imort .... as ....
# import foo as f   # f=foo
#
# f.get()



#6.模块是第一类对象
# import foo #模块当对象，可以传值或者定义
# f = foo

#7.自定义模块当命名应该采用纯小写+下划线的风格



#8.可以在函数内导入模块

# def func():
#     import foo