"""
面向对象编程是编程思想。
核心是“对象”二字，对象是“数据与功能”的结合体

抽象讲法：把时间万物都比喻成一个对象，每个对象都是“特征与技能”的结合体

class People：
    # 属于tank这个人的特征，名字---》数据
    name = 'tank'

    # tank 的技能，跑步---》功能
    def run(self):
        pass

===============================================================
用面向对象编程思想编写程序：
    1.先找到对象
    2.通过对象总结出类
        - 学校类
            - 数据
                - 校区的名字
                - 校区的地址
            - 功能
                - 校区创建班级


        - 班级类
            - 数据
             - 班级名字
             - 班级所在校区
            - 功能
                - 班级创建课程

        - 学生类
            - 数据
             - 学生的学校
             - 学生的姓名
             - 学生的年龄
             - 学号
             - 学生的性别
            - 功能
                - 学生选择班级

        - 课程类
            - 数据
             - 课程名字
             - 课程周期
             - 课程价格
            - 功能


        - 讲师类
            - 数据
             - 老师的名字
             - 老师的年龄
             - 老师的薪资
             - 老师的等级
            - 功能
                - 老师给学生打分

    3.定义类
    4.调用类实例化得到的对象


选课系统项目中涉及到诸多数据与功能，要求引入面向对象的思想对其进行高度整合
# 1、学校数据与功能整合      ----》学校类
# 2、课程数据与功能进行整合  ----》课程类
# 3、学生数据与功能进行整合  ----》学生类
# 4、讲师数据与功能进行整合  ----》讲师类
# 5、班级数据与功能进行整合  ----》班级类
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
        上海小区--》School() --> school_obj(创建班级的功能)
     校区创建完毕后，可以为每个校区创建班级


     班级创建完毕后，可以为每个班级创建课程

     学生创建完毕后，学生可以选择班级

     老师创建完毕后，可以为学生打分
"""


# 学校类
class School:
    """
    - 学校类
    - 数据
        - 校区的名字
        - 校区的地址

    - 功能
        - 校区创建班级
    """

    # 学校数据的添加
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address
        # 一个校区可以存放多个班级，在实例化学校类得到对象时，初始化班级列表
        self.classes_list = []  # [上海14期、北京29期、深圳9期]

    # 学校创建班级，定义一个创建班级的方法
    def create_classes(self, class_name):
        self.classes_list.append(class_name)

        # 调用班级类，得到班级对象，并返回给调用者
        class_obj = Classes(class_name, self.school_name)  # 上海14期,老男孩上海校区
        return class_obj


# 班级类
class Classes:
    """
    - 班级类
        - 数据
         - 班级名字
         - 班级所在校区
        - 功能
            - 班级创建课程
    """

    def __init__(self, class_name, school_name):
        self.class_name = class_name
        self.school_name = school_name
        # 一个班级可以有多门课程，存放在班级的课程列表中
        self.course_list = []

    # 班级创建课程
    def create_course(self, course_name, course_period, course_price):
        # 把创建的课程名称放在班级课程列表中
        self.course_list.append(course_name)  # python
        # 调用课程类，实例化得到课程对象
        # course_obj = Course('python', 6, 18888)
        course_obj = Course(course_name, course_period, course_price)
        return course_obj


# 课程类
class Course:
    """
    - 课程类
        - 数据
         - 课程名字
         - 课程周期
         - 课程价格
"""

    def __init__(self, course_name, course_period, course_price):
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price


# 学生类
class Student:
    """
    - 学生类
        - 数据
            - 学生的学校
            - 学生的姓名
            - 学生的年龄
            - 学号
            - 学生的性别
        - 功能
            - 学生选择课程
    """

    def __init__(self, school_name, student_name, student_age, student_number, student_sex):
        self.school_name = school_name
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.student_sex = student_sex
        # 学生的课程列表，学生每次添加课程成功后往该列表中添加课程名称
        self.student_course_list = []
        # 学生分数列表
        '''
        score_dic = {
            'python':0,
            'go':0,
            
        }
        '''
        self.score_dic = {}

    # 学生选择课程的功能
    def choice_course(self, course_name):
        self.student_course_list.append(course_name)
        # 设置默认分数为0
        self.score_dic[course_name] = 0


# 老师类
class Teacher:
    """
    - 讲师类
        - 数据
            - 老师的名字
            - 老师的年龄
            - 老师的薪资
            - 老师的等级
        - 功能
            - 老师给学生打分
    """

    def __init__(self, teacher_name, teacher_age, teacher_salary, teacher_levle):
        self.teacher_name = teacher_name
        self.teacher_age = teacher_age
        self.teacher_salary = teacher_salary
        self.teacher_levle = teacher_levle

    def change_score(self, score, student_obj, course_name):
        student_obj.score_dic[course_name] = score


# 1、调用类的实例化得到学校对象
school_obj = School('老男孩上海校区', '中国上海市')
print(school_obj.__dict__)

# 2、通过学校对象.create_classes方法创建班级
class_obj = school_obj.create_classes('上海14期')
print(class_obj.__dict__)
# 查看学校是否添加了班级
print(school_obj.__dict__)

# 3、班级对象.create_co
# urse方法创建课程,传入课程名称，周期，价格
course_obj = class_obj.create_course('python', 6, 18888)
print(course_obj.__dict__)

# 4、调用学生类，实例化得到学生对象
student_obj = Student(school_obj.school_name, 'jojo', 1, '06', 'male')
# 添加课程前
print(student_obj.__dict__)

# 5、学生对象调用.choice_course方法选择课程
student_obj.choice_course(course_obj.course_name)
# 添加课程后
print(student_obj.__dict__)

# 6、调用老师类，实例化得老师对象
teacher_obj = Teacher('tank', 18, 10000, 10)
teacher_obj.change_score(90, student_obj, 'python')
print(student_obj.__dict__)