# 在子类派生的新方法中如何重用父类的功能
# 方式一：指名道姓调用某一个类下的函数=》不依赖与继承关系
#
#
# class OldboyPeople:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def f1(self):
#         print(f'{self.name} say hello')
#
#
# class Teacher(OldboyPeople):
#     def __init__(self, name, age, sex, salary, level):
#         OldboyPeople.__init__(self, name, age, sex)
#         self.salary = salary
#         self.level = level
#
#     def f2(self):
#         print(f'{self.name} 的年龄是：{self.age} 性别是：{self.sex} 工资是：{self.salary} 级别是：{self.level}')
#
#
# tea_obj = Teacher('egon', 18, 'male', 3000, 10)
# print(tea_obj.__dict__)
# tea_obj.f2()




# 方式二：super()调用父类提供给自己的方法=》严格依赖继承关系
#         调用super()会得到一个特殊的对象，该对象会参照发起属性查找的类的mro，去当前类的父类中找属性
# class OldboyPeople:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def f1(self):
#         print(f'{self.name} say hello')
#
#
# class Teacher(OldboyPeople):
#     def __init__(self, name, age, sex, salary, level):
#         super().__init__(name, age, sex)
#         self.salary = salary
#         self.level = level
#
#     def f2(self):
#         print(f'{self.name} 的年龄是：{self.age} 性别是：{self.sex} 工资是：{self.salary} 级别是：{self.level}')
#
# # 从第二个开始找，即父类
# print(Teacher.mro())  # [<class '__main__.Teacher'>, <class '__main__.OldboyPeople'>, <class 'object'>]
# tea_obj = Teacher('egon', 18, 'male', 3000, 10)
# print(tea_obj.__dict__)
# tea_obj.f2()


# super()案例

class A:
    def test(self):
        print('from A')
        super().test()


class B:
    def test(self):
        print('from B')

class C(A, B):
    pass


obj = C()
print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
obj.test()
# from A
# from B