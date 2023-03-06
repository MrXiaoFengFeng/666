# 一、引入：
# 一切都源于一句话：一切皆为对象

# 二、什么是元类？
# 元类就是用来实例化产生类的类
# 关系：元类----实例化---》类

# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def say(self):
#         print(f'{self.name}{self.age}')


# 如何得到对象
# obj = 调用类()
# obj = People('egon', 18)

# 如果说类也是对象
# People = 调用类(。。。)

# 查看内置的元类：
# 1、type是内置的元类
# 2、我们用class关键字定义了所有的类以及内置的类都是有内置的元类type实现的
# print(type(People))  # <class 'type'>  定义类
#
# print(type(int))  # <class 'type'>  内置类

# 三、class关键字创造类People的步骤
# 类有三大特征:
# 1、类名：
class_name = "People"

# 2、类的基类
class_bases = (object,)

# 3、执行类体代码拿到类的名称空间,类体就是一堆字符串
class_dic = {}
class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age


def say(self):
        print(f'{self.name}{self.age}')
"""

exec(class_body, {}, class_dic)

print(class_dic)  # 内置的class造的类属性更全面，自建的只有基本属性
"""
{'__init__': <function __init__ at 0x0000017BD03EF160>, 'say': <function say at 0x0000017BD0490AF0>}
"""

# 4、调用内置的元类（type）     class People: -->People只是个变量名，对应的值才是类
People = type(class_name, class_bases, class_dic)
print(People)  # <class '__main__.People'>

