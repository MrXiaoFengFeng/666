# 1、什么是多态：同一种事物有多重形态
# class Animal:
#     pass
#
#
# class People(Animal):
#     pass
#
#
# class Dog(Animal):
#     pass
#
#
# class Pig(Animal):
#     pass


# 2、为何要有多态=》多态会带来什么样的特性，多态性
#         多态性指的是可以在不考虑对象具体类型的情况下而直接使用对象

# I：父类规范子类形式1：
# class Animal:
#     def say(self):
#         print('动物基本的发声...', end='')
#
#
# class People(Animal):
#     def say(self):
#         # super(People, self).say()
#         super().say()
#         print('嘤嘤嘤')
#
#
# class Dog(Animal):
#     def say(self):
#         super().say()
#         print('汪汪汪')
#
#
# class Pig(Animal):
#     def say(self):
#         super().say()
#         print('哼哼哼')
#
#
# obj1 = People()
# obj2 = Dog()
# obj3 = Pig()
#
# # obj1.say()  # 动物基本的发声...嘤嘤嘤
# # obj2.say()  # 动物基本的发声...汪汪汪
# # obj3.say()  # 动物基本的发声...哼哼哼
#
# # 定义统一的接口，接收传入的动物对象
# def animal_say(animal):
#     animal.say()
#
#
# animal_say(obj1)
# animal_say(obj2)
# animal_say(obj3)
# # 动物基本的发声...嘤嘤嘤
# # 动物基本的发声...汪汪汪
# # 动物基本的发声...哼哼哼



# ====================================================================
# II、python推崇的是鸭子类型

# class Animal:
#     def say(self):
#         print('动物基本的发声...', end='')
#
#
# class People:
#     def say(self):
#         # super(People, self).say()
#         super().say()
#         print('嘤嘤嘤')
#
#
# class Dog:
#     def say(self):
#         super().say()
#         print('汪汪汪')
#
#
# class Pig:
#     def say(self):
#         super().say()
#         print('哼哼哼')
#
#
# obj1 = People()
# obj2 = Dog()
# obj3 = Pig()


# 鸭子类型案例
# class Cpu:
#     def read(self):
#         print('cpu read')
#
#     def write(self):
#         print('cpu write')
#
#
# class Mem:
#     def read(self):
#         print('mem read')
#
#     def write(self):
#         print('mem write')
#
#
# class Disk:
#     def read(self):
#         print('disk read')
#
#     def write(self):
#         print('disk write')
#
#
# class Txt:
#     def read(self):
#         print('txt read')
#
#     def write(self):
#         print('txt write')
#
#
# obj1 = Cpu()
# obj2 = Mem()
# obj3 = Disk()
# obj3 = Txt()
#
# obj1.read()
# obj1.write()
#
# obj2.read()
# obj2.write()
#
# obj3.read()
# obj3.write()



# I.2：了解父类规范子类形式2
import abc

class Animal(metaclass=abc.ABCMeta):  # 统一所有子类的标准
    @abc.abstractclassmethod
    def say(self):
        print('动物基本的发声...', end='')
# obj = Animal()  # 不能实例化抽象类自己

class People(Animal):
    def say(self):  # 子类必须有与父类一样的say方法
        # super(People, self).say()
        super().say()
        print('嘤嘤嘤')


class Dog(Animal):
    def say(self):
        super().say()
        print('汪汪汪')


class Pig(Animal):
    def say(self):
        super().say()
        print('哼哼哼')


obj1 = People()
obj2 = Dog()
obj3 = Pig()

obj1.say()  # 动物基本的发声...嘤嘤嘤
# obj2.say()  # 动物基本的发声...汪汪汪
# obj3.say()  # 动物基本的发声...哼哼哼