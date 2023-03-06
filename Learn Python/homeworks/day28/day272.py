import os
import pickle
import uuid

BASE_PATH = os.path.dirname(__file__)

# 父类
class Base:
    # 保存对象方法
    def save(self):
        # 判断类的文件夹是否存在
        user_dir = os.path.join(
            BASE_PATH, 'user_data',
            # 根据类型 + id 号，拼接对象存放的文件路径，更好管理对象
            self.__class__.__name__
        )
        if not os.path.exists(user_dir):
            os.mkdir(user_dir)

        # 文件路径
        user_path = os.path.join(user_dir, self.id)
        # 将对象写入user_path目录中
        with open(user_path, 'wb') as f:
            pickle.dump(self, f)

    # 获取文件中的对象
    def select(self, obj_id):
        # 判断类的文件夹是否存在
        user_dir = os.path.join(
            BASE_PATH, 'user_data',
            # 根据类型 + id 号，拼接对象存放的文件路径，更好管理对象
            self.__class__.__name__
        )
        if not os.path.exists(user_dir):
            os.mkdir(user_dir)

        # 文件路径
        user_path = os.path.join(user_dir, obj_id)
        # 读取文件中的对象
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj


"""
# 保存对象方法
def save_obj(obj):
    user_path = os.path.join(
        'E:/WorkSpace/Learn Python/homeworks/day28/user_data',
        obj.id
    )
    # 将对象写入user_path目录中
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


# 获取文件中的对象
def select(obj_id):
    user_path = os.path.join(
        'E:/WorkSpace/Learn Python/homeworks/day28/user_data',
        obj_id
    )
    # 读取文件中的对象
    with open(user_path, 'rb') as f:
        obj = pickle.load(f)
        return obj

"""


# 学校类
class School(Base):
    # 学校数据的添加
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address  # 一个校区可以存放多个班级，在实例化学校类得到对象时，初始化班级列表
        # 当调用学校类时，等同于创建学校功能，设置了学校id
        # id使用uuid4生成随机字符串
        self.id = str(uuid.uuid4())

        # 班级id
        self.classes_list = []  # [上海14期、北京29期、深圳9期]

        # 保存对象
        # save_obj(self)
        self.save()

    # 学校创建班级，定义一个创建班级的方法
    # def create_classes(self, class_name):
    #     self.classes_list.append(class_name)
    #
    #     # 调用班级类，得到班级对象，并返回给调用者
    #     class_obj = Classes(class_name, self.school_name)  # 上海14期,老男孩上海校区
    #     return class_obj
    def create_classes(self, class_name, school_name):
        class_obj = Classes(class_name, school_name)

        # 将对象的id保存到班级列表id中
        self.classes_list.append(class_obj.id)
        # 刷新学校对象数据
        self.save()

        return class_obj











# 班级类
class Classes(Base):
    def __init__(self, class_name, school_name):
        self.class_name = class_name
        self.school_name = school_name
        # 一个班级可以有多门课程，存放在班级的课程列表中
        self.course_list = []
        self.id = str(uuid.uuid4())
        self.save()

    # 班级创建课程
    def create_course(self, course_name, course_period, course_price):
        # 把创建的课程名称放在班级课程列表中
        self.course_list.append(course_name)  # python

        course_obj = Course(course_name, course_period, course_price)
        return course_obj


# 调用即创建对象
school_obj = School('上海校区', '上海')
'2a3cbd05-35c2-47c6-9829-07b50a0eb409'
# print(school_obj.__class__)  # <class '__main__.School'>
# print(school_obj.__class__.__name__)  # School

# 根据id号，获取对象
# obj = school_obj.select('7552e745-047d-418a-9b84-b2e138721108')
# print(obj.__dict__)

class_obj = school_obj.create_classes('上海14期', school_obj.school_name)
print(class_obj.__dict__)
print(class_obj.id)

# 课程类
class Course:
    def __init__(self, course_name, course_period, course_price):
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price


# 学生类
class Student:
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
    def __init__(self, teacher_name, teacher_age, teacher_salary, teacher_levle):
        self.teacher_name = teacher_name
        self.teacher_age = teacher_age
        self.teacher_salary = teacher_salary
        self.teacher_levle = teacher_levle
        self.__ID_CARD = 'qwertt1111'

    @property
    def teacher_id(self):
        return self.__ID_CARD

    def change_score(self, score, student_obj, course_name):
        student_obj.score_dic[course_name] = score

# # 1、调用类的实例化得到学校对象
# school_obj = School('老男孩上海校区', '中国上海市')
# print(school_obj.__dict__)
#
# # 2、通过学校对象.create_classes方法创建班级
# class_obj = school_obj.create_classes('上海14期')
# print(class_obj.__dict__)
# # 查看学校是否添加了班级
# print(school_obj.__dict__)
#
# # 3、班级对象.create_co
# # urse方法创建课程,传入课程名称，周期，价格
# course_obj = class_obj.create_course('python', 6, 18888)
# print(course_obj.__dict__)
#
# # 4、调用学生类，实例化得到学生对象
# student_obj = Student(school_obj.school_name, 'jojo', 1, '06', 'male')
# # 添加课程前
# print(student_obj.__dict__)
#
# # 5、学生对象调用.choice_course方法选择课程
# student_obj.choice_course(course_obj.course_name)
# # 添加课程后
# print(student_obj.__dict__)
#
# # 6、调用老师类，实例化得老师对象
# teacher_obj = Teacher('tank', 18, 10000, 10)
# teacher_obj.change_score(90, student_obj, 'python')
# print(student_obj.__dict__)
