"""
面向过程：
    核心是"过程"二字

    过程的终极奥义就是将程序流程化
    过程是"流水线"，用来分步骤解决问题的

面向对象：
    核心是"对象"二字
    对象的终极奥义就是将程序“整合”
    对象是“容器”，用来盛放数据与功能的

    类也是“容器”，该容器用来存放同类对象共有的数据和功能


python这门语言到底提供了什么语法来允许我们将数据与功能很好的整合到一起？？


"""

# 程序=数据+功能
'''
# 学生的数据
stu_name = 'egon'
stu_age = 18
stu_gender = 'male'


# 学生功能
def tell_stu_nfo():
    print(
        f'名字{stu_name} 年龄{stu_age} 性别{stu_gender}'
    )


# 修改学生数据
def set_info(x, y, z):
    global stu_name
    global stu_age
    global stu_gender

    stu_name = x
    stu_age = y
    stu_gender = z


# 课程的数据
course_period = '6months'
course_score = 10


def tell_coure_info():
    print(
        f'课程名{course_name} 学习周期{course_period} 学分{course_score}'
    )
'''


# 学生的容器 = 学生的数据 + 学生的功能

# 课程的容器 = 课程的数据 + 课程的功能




