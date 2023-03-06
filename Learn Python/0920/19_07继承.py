# 1、什么是继承
# I：继承是一种创建新类的方式，新建的类可以成为子类或者派生类，父类又可称为基类或超类,子类会遗传父类的属性
# II：需要注意的是：python支持多继承
# 在python中，新建的类可以继承一个或多个父类

# 如果考虑代码兼容python2.7，则可以加上默认的object
class Parent1(object):
    name = 1111


class Parent2(object):
    pass


class Sub1(Parent1):  # 单继承
    pass


class Sub2(Parent1, Parent2):  # 多继承
    pass


# print(Sub1.__bases__)
# print(Sub2.__bases__)
# print(Sub1.name)  # 1111


# ps1:在python2中又经典类与新式类之分
# 新式类：继承了object类的子类，以及该子类的子类子子类。。。
# 经典：没有继承object类的子类，以及该子类的子类子子类。。

# ps2：在python3中没有继承任何类，那么会默认继承object类，所以python3中所有的类都是新式类
# print(Parent1.__bases__)
# print(Parent2.__bases__)

# III：python的多继承
#     优点：子类可以同时遗传多个父类的属性，最大限度的重用代码
#     缺点：
#           1、违背了人的思维习惯：继承表达的是一种什么“是”什么的关系
#           2、代码可读性变差
#             3、不建议直接使用多继承，扩展性变差，如果真的涉及到一个子类
#                 不可避免的要重用多个父类的属性，应该使用Mixins机制


# 2、为何要用继承：用来解决类与类之间代码冗余的问题


# 3、如何实现继承

# 示范2：基于继承解决类与类之间的冗余问题
class OldboyPeople:
    school = 'OLBOY'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(OldboyPeople):
    # school = 'OLDBOY'

    # def __init__(self, name, age, sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex

    def __init__(self, name, age, sex, id):
        OldboyPeople.__init__(self, name, age, sex)
        self.id = id
    def choose_course(self):
        print(f'学生{self.name}正在选课')

stu_obj = Student('lili', 19, 'female', 66)
print(stu_obj.__dict__)
# print(stu_obj.school)
# stu_obj.choose_course()



# class Teacher(OldboyPeople):
#     # school = 'OLDBOY'
#     #   老师的空对象, 'egon',18,'male',3000,10
#     def __init__(self, name, age, sex, salary, level):
#         # self.name = name
#         # self.age = age
#         # self.sex = sex
#
#         # 指名道姓的跟父类OldboyPeople去要__init__
#         OldboyPeople.__init__(self, name, age, sex)
#         self.salary = salary
#         self.level = level
#
#     def score(self):
#         print(f'{self.name}正在打分')
#
# tea_obj = Teacher('egon', 18, 'male', 3000, 10)
# print(tea_obj.__dict__)
# print(tea_obj.school)
# tea_obj.score()
