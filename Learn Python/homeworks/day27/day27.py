"""
选课系统项目中涉及到诸多数据与功能，要求引入面向对象的思想对其进行高度整合
# 1、学校数据与功能整合
# 2、课程数据与功能进行整合
# 3、学生数据与功能进行整合
# 4、讲师数据与功能进行整合
# 5、班级数据与功能进行整合
ps：不会写的同学，可以先用普通的方式，先把数据与功能都给写好，再考虑基于面向对象的思想进行整合

数据部分：
     校区的名字：如"老男孩上海校区"
     校区的地址：如"上海虹桥"

     班级名字
     班级所在校区

     学生的学校
     学生的姓名
     学生的年龄
     学号
     学生的性别

     课程名字
     课程周期
     课程价格

     老师的名字
     老师的年龄
     老师的薪资
     老师的等级


功能部分：
     校区创建完毕后，可以为每个校区关联班级

     班级创建完毕后，可以为每个班级关联课程

     学生创建完毕后，学生可以选择班级

     老师创建完毕后，可以为学生打分
"""


# 整合->解耦合->扩展性增强

class School:
    school_name = 'oldboy'

    def __init__(self, nickname, addr):
        self.nickname = nickname
        self.addr = addr
        self.classes = []

    # def related_class(self, class_name):
    def related_class(self, class_obj):
        # self.classes.append(班级名字)
        # self.classes.append(class_name)
        self.classes.append(class_obj)

    # def tell_class(self):
    #     print(self.nickname)
    #     for class_name in self.classes:
    #         print(f'{self.nickname}{class_name}')
    def tell_class(self):
        # 打印班级的名字
        print(self.nickname.center(60, '='))
        # 打印课程的信息
        for class_obj in self.classes:
            class_obj.tell_course()


# 一：学校
# 1、创建学校
school_obj1 = School('老男孩魔都小区', '上海')
school_obj2 = School('老男孩帝都小区', '北京')
school_obj3 = School('老男孩武汉小区', '武汉')


# 2、为学校开设班级
# 上海校区开了脱产14期
# school_obj1.related_class('脱产14期')

# print(school_obj1.classes)
# 北京开了脱产15期
# school_obj2.related_class('脱产15期')

# print(school_obj2.classes)

# 3、查看每个校区开设的班级
# school_obj1.tell_class()  # 老男孩魔都小区脱产14期
# school_obj2.tell_class()  # 老男孩帝都小区脱产15期

# School.tell_class(school_obj1)  # 老男孩魔都小区脱产14期
# School.related_class(school_obj3, '脱产66期')
# School.tell_class(school_obj3)  # 老男孩武汉小区脱产66期


class Class:
    def __init__(self, name):
        self.name = name
        self.course = None

    # def related_course(self, course_name):
    #     self.course = course_name
    def related_course(self, course_obj):
        self.course = course_obj

    # def tell_course(self):
    #     print(f'班级名:{self.name}课程名:{self.course}')
    def tell_course(self):
        print(f'班级名：{self.name}', end=' ')
        self.course.tell_info()  # 打印课程的详细信息


# 二：班级
# 1、创建班级
class_obj1 = Class('脱产14期')
class_obj2 = Class('脱产15期')
class_obj3 = Class('脱产29期')


# 3、为班级关联一个课程
# class_obj1.related_course('python全栈开发')
# class_obj2.related_course('linux运维')
# class_obj3.related_course('go')

# 3、查看班级开设的课程
# class_obj1.tell_course()
# class_obj2.tell_course()
# class_obj3.tell_course()


# 4、为学校开设班级
# school_obj1.related_class('脱产14期')
school_obj1.related_class(class_obj1)
# class_obj2 = Class('脱产15期')
school_obj2.related_class(class_obj2)
# class_obj3 = Class('脱产29期')
school_obj3.related_class(class_obj3)

# 北京小区开了：脱产29期
# school_obj2.related_class(class_obj3)

# School.tell_class(school_obj1)
# School.tell_class(school_obj2)
# School.tell_class(school_obj3)


class Course:
    def __init__(self, course_name, period, price):
        self.course_name = course_name
        self.period = period
        self.price = price

    def tell_info(self):
        print(f'课程名：{self.course_name}, 周期：{self.period}, 价格：{self.price}')


# 三：课程
# 1、创建课程
course_obj1 = Course('python全栈开发', '6mons', '20000')
course_obj2 = Course('Linux运维', '5mons', '18000')
course_obj3 = Course('Go', '6mons', '10000')

# 2、查看课程的详细信息
# course_obj1.tell_info()
# course_obj2.tell_info()
# course_obj3.tell_info()

# 3、为班级关联课程对象
class_obj1.related_course(course_obj1)
class_obj2.related_course(course_obj2)
class_obj3.related_course(course_obj3)

# 4、查看班级下的课程
# class_obj1.tell_course()
# class_obj2.tell_course()
# class_obj3.tell_course()


school_obj1.tell_class()
school_obj2.tell_class()
school_obj3.tell_class()



class Student:
    pass
