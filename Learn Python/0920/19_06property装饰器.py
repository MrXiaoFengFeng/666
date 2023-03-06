
# 装饰器是在不修改被装饰对象源码及调用方式的前提下为被装饰对象添加新功能
# 新功能的可调用对象

# print(property)  # <class 'property'>

# property是一个装饰器，是用来将绑定给对象的方法伪装成一个数据属性

"""
BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86
"""
# 案例一：
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     # 定义函数的原因1：
#     # 1、从bmi的公式看，bmi是应该是触发功能计算得到的
#     # 2、bmi是随着身高、体重的变化而动态的变化的，不是一个固定的值，
#     #     说白了，每次是需要临时计算得到的
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# obj1 = People('egon', 74, 1.73)
# # print(obj1.bmi())  # 24.725182932941294
#
# print(obj1.bmi)  # 24.725182932941294


# # 案例二：
# class People:
#     def __init__(self, name):
#         self.__name = name
#
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, val):
#         if type(val) is not str:
#             print('必须传入str类型')
#             return
#         self.__name = val
#
#     def del_name(self):
#         print('不许删除')
#
#     name123 = property(get_name, set_name, del_name)
#
# obj1 = People('egon')
# print(obj1.get_name())
# obj1.set_name('jojo')
# print(obj1.get_name())
# obj1.del_name()
# print(obj1.get_name())
# """
# egon
# jojo
# 不许删除
# jojo
# """


# 人类正常思维
# print(obj1.name123)
# obj1.name123 = 18
# del obj1.name123



# 案例三：
class People:
    def __init__(self, name):
        self.__name = name

    @property  # name = property
    def name123(self):  # obj1.name123
        return self.__name

    @name123.setter
    def name123(self, val):  # obj1.name123 = 'EGON'
        if type(val) is not str:
            print('必须传入str类型')
            return
        self.__name = val

    @name123.deleter
    def name123(self):  # del obj1.name123
        print('不许删除')



obj1 = People('egon')
print(obj1.name123)
obj1.name123 = 18
del obj1.name123