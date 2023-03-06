# 一、封装介绍
# 封装是面向对象三大特性最核心的一个特性
# 封装<->整合


# 二、将封装的属性进行隐藏操作
# 1、如何隐藏：在属性名前家__前缀，就会实现一个对外隐藏属性效果
# 该隐藏需要注意的问题：
# I：在类外部无法直接访问下划线开头的属性，但知道了类名和属性名就可以拼出名字：_类名__属性，然后就可以访问了
# ，如Foo._A_N，所以说这种操作并没有严格意义上的限制外部访问，仅仅知识一种语法意义上的变形。
# class Foo:
#     __x = 1  # _Foo__x
#
#     def __f1(self):  # _Foo__f1
#         print('from f1')


# print(Foo.__x)  # AttributeError: type object 'Foo' has no attribute '__x'
# print(Foo.__f1)  # AttributeError: type object 'Foo' has no attribute '__f1'

# print(Foo.__dict__)  #  '_Foo__x': 1
# print(Foo._Foo__x)  # 1


# II：这种隐藏对外不对内,因为__开头的属性会在类定义阶段&检查语法时统一发生变形
# class Foo:
#     __x = 1  # _Foo__x
#
#     def __f1(self):  # _Foo__f1
#         print('from f1')
#
#     def f2(self):
#         print(self.__x)
#
# obj = Foo()
# obj.f2()

# III:这种变形操作只在检查类体语法的时候发生一次，之后定义的__开头的属性

# class Foo:
#     __x = 1  # _Foo__x
#
#     def __f1(self):  # _Foo__f1
#         print('from f1')
#
#     def f2(self):
#         print(self.__x)
#         print(self.__f1)
#
#
# obj = Foo()
# obj.f2()


# 2、为何要隐藏
# I、隐藏数据属性
# 设计者：egon
class People:
    def __init__(self, name):
        self.__name = name

    # 访问名字
    def get_name(self):
        # 通过该接口就可以间接的访问到名字属性
        print(self.__name)

    # 修改名字
    def set_name(self, val):
        if type(val) is not str:
            print('输入错误，必须传字符串')
            return
        self.__name = val


# 使用者：其他人
obj = People('1egon')
obj.get_name()
obj.set_name(1234)
obj.set_name('haha')
obj.get_name()


# II、隐藏函数/方法属性:目的是为了隔离复杂度















