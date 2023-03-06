"""
上节课复习：
    1、编程范式/思想
        面向过程
            介绍：
                核心是“过程”二字
                过程就是流水线
                过程终结奥义是将程序流程化

            优点：

                1、将程序流程化，进而程序的设计会变得简单化

            缺点：
                1、可拓展性差


        面向对象
            介绍：
                核心是“对象”二字
                对象就是“容器”，用来盛放数据与功能
                对象终结奥义是将程序进行高度整合

            优点：

                1、提升程序的解耦合程度，进而增强程序的可拓展性

            缺点：
                1、设计复杂

    2、面向对象编程
        现实生活中：
            1、先找出现实生活中的对象
            2、然后归纳总结出类
        1、先定义类
        2、后调用类产生对象（调用类的过程又称之为实例化）


        对象

        stu_school = 'oldboy'
        stu_id = 111
        stu_name = 'egon'
        stu_age = 18

        def study():
            pass


"""


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 打印学生信息
    def tell_info(self):
        print(self.name, self.age, self.gender)

    def choose(self):
        print(f'{self.name} is choosing a course')


# 对象单独调用
stu1 = Student('egon', 18, 'male')
stu1.tell_info()  # egon 18 male
stu1.choose()  # egon is choosing a course
# print(stu1.name, stu1.age, stu1.gender)

stu2 = Student('jojo', 1, 'male')

# 类的调用
Student.tell_info(stu1)  # egon 18 male
Student.choose(stu1)  # egon is choosing a course
Student.choose(stu2)  # jojo is choosing a course
