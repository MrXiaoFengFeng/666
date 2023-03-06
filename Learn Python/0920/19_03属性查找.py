class Student:
    # 1、变量的定义
    stu_school = 'oldboy'
    # 统计有多少个同学
    count = 0

    # 空对象,'egon',18,'male'
    def __init__(self, x, y, z):
        Student.count += 1
        self.stu_name = x  # 空对象.stu_name = 'egon
        self.stu_age = y  # 空对象.stu_age = 18
        self.stu_gender = z  # 空对象.stu_gender = 'male'
        print('==================>1')

    # 2、功能的定义
    def tell_stu_info(self):
        print(
            f"学生姓名:{self.stu_name}, 年龄{self.stu_age}, 性别{self.stu_gender}"
        )

    def set_info(self, x, y, z):
        self.stu_name = x
        self.stu_age = y
        self.stu_gender = z

    def choose(self, x):
        print('正在选课')
        self.course = x


stu1_obj = Student('egon', 18, 'male')  # Student.__init__(空对象, x, y, z)
stu2_obj = Student('tom', 19, 'male')
stu3_obj = Student('lili', 21, 'female')

# 类中存放的是对象共有的数据与功能
# 一、类可以访问：
# 1、类的数据属性：
# print(Student.stu_school)  # oldboy

# 2、类的函数属性：
# print(Student.tell_stu_info)  # <function Student.tell_stu_info at 0x000001A6CBE5BAF0>
# print(Student.set_info)  # <function Student.set_info at 0x00000198587ABB80>

# 二、但其实类中的东西是给对象用的：
# 1、类的数据属性是共享给所有对象用的，大家访问的地址都一样
# print(id(Student.stu_school))
# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
'''
1474864390384
1474864390384
1474864390384
'''

# Student.stu_school = 'OLDBOY'
# print(Student.stu_school)
# print(stu1_obj.stu_school)
'''
OLDBOY
OLDBOY
'''

# 改对象中的数据属性，仅对该对象生效
# stu1_obj.stu_school = 'OLDBOY'
# print(stu1_obj.stu_school)  # OLDBOY
# print(stu2_obj.stu_school)  # oldboy
# print(Student.stu_school)  # oldboy

# 统计共有多少个同学。共有方法，所以放在类中
# print(Student.count)  # 3

# 2、类中定义的函数主要是给对象使用的，而且是绑定给对象的，虽然所有对象指向的都是相同的功能
#       但是绑定到不同的对象就是不同的绑定方法，内存地址各不相同

# 类调用自己的函数属性必须严格按照函数的用法来
# print(Student.tell_stu_info)  # <function Student.tell_stu_info at 0x000001708A40B9D0>
# print(Student.set_info)  # <function Student.set_info at 0x000001708A40BAF0>

# Student.tell_stu_info(stu1_obj)  # 学生姓名:egon, 年龄18, 性别male
#
# Student.set_info(stu1_obj, 'EGON', 20, 'MALE')
# Student.tell_stu_info(stu1_obj)  # 学生姓名:EGON, 年龄20, 性别MALE


# 绑定方法的特殊之处在于：谁来调用绑定方法就会将谁当做第一个参数自动传入

# print(Student.tell_stu_info)
# print(stu1_obj.tell_stu_info)
# print(stu2_obj.tell_stu_info)
# print(stu3_obj.tell_stu_info)
'''
<function Student.tell_stu_info at 0x0000024B81A6B550>
<bound method Student.tell_stu_info of <__main__.Student object at 0x0000024B81A87FD0>>
<bound method Student.tell_stu_info of <__main__.Student object at 0x0000024B81A87F10>>
<bound method Student.tell_stu_info of <__main__.Student object at 0x0000024B81A87E20>>
'''

# stu1_obj.tell_stu_info()  # tell_stu1_info(stu1_obj) 学生姓名:egon, 年龄18, 性别male
# stu2_obj.tell_stu_info()  # tell_stu2_info(stu2_obj) 学生姓名:tom, 年龄19, 性别male
# stu3_obj.tell_stu_info()  # tell_stu3_info(stu3_obj) 学生姓名:lili, 年龄21, 性别female

# stu1_obj.choose('python全栈开发')
# print(stu1_obj.course)  # python全栈开发
#
# stu2_obj.choose('linux运维')
# print(stu2_obj.course)  # linux运维
#
# stu3_obj.choose('高级架构师')
# print(stu3_obj.course)  # 高级架构师

