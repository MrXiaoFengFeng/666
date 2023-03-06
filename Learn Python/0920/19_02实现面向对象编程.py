# 一、 先定义类
# 类是对象相似数据与功能的集合体
# 所以类中最常见的是变量与函数的定义，但是类体中其实是可以包含任意其他代码的
# 注意：类体代码是在定义阶段就会立即执行，会产生类的名称空间
# class Student:
#     # 1、变量的定义
#     stu_school = 'oldboy'
#
#     # 功能的定义
#     def tell_stu_info(stu_obj):
#         print(
#             f"学生姓名:{stu_obj['stu_name']}, 年龄{stu_obj['stu_age']}, 性别{stu_obj['stu_gender']}"
#         )
#
#     def set_info(stu_obj, x, y, z):
#         stu_obj['stu_name'] = x
#         stu_obj['stu_age'] = y
#         stu_obj['stu_gender'] = z


# print('=============>')

# Student 名称空间存放的名字
# print(Student.__dict__)
'''
{'__module__': '__main__', 'stu_school': 'oldboy', 'tell_stu_info': <function Student.tell_stu_info at 0x00000217D143B550>, 'set_info': <function Student.set_info at 0x00000217D143B9D0>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}

'''
# print(Student.__dict__['stu_school'])  # oldboy
# print(Student.__dict__['tell_stu_info'])  # <function Student.tell_stu_info at 0x000001DAFE07B550>

# 属性的访问语法
# 1、访问数据属性
# print(Student.stu_school)  # oldboy
# 2、访问函数属性
# print(Student.tell_stu_info)  # <function Student.tell_stu_info at 0x000001E4E801B550>


# 二、再调用类产生对象
# stu1_obj = Student()
# stu2_obj = Student()
# stu3_obj = Student()


# print(stu1_obj.__dict__)
# print(stu2_obj.__dict__)
# print(stu3_obj.__dict__)
'''
{}
{}
{}
'''


# 为对象定制自己独有的属性
# 类是存放对象相似的数据和功能，往类产生的对象中塞不同对象的独有的其他数据
# 问题1：代码重复
# 问题2：属性的查找顺序

# 写法1：
# stu1_obj.__dict__['stu_name'] = 'egon'
# stu1_obj.__dict__['stu_age'] = 18
# stu1_obj.__dict__['stu_gender'] = 'male'
# print(stu1_obj.__dict__)  # {'stu_name': 'egon', 'stu_age': 18, 'stu_gender': 'male'}

# 写法2：
# stu1_obj.stu_name = 'egon'
# stu1_obj.stu_age = 19
# stu1_obj.stu_gender = 'male'
# print(stu1_obj.__dict__)  # {'stu_name': 'egon', 'stu_age': 19, 'stu_gender': 'male'}
#
# stu2_obj.stu_name = 'tom'
# stu2_obj.stu_age = 20
# stu2_obj.stu_gender = 'male'
# print(stu2_obj.__dict__)
#
# stu3_obj.stu_name = 'lili'
# stu3_obj.stu_age = 21
# stu3_obj.stu_gender = 'female'
# print(stu3_obj.__dict__)


# 解决问题1：
#
# 解决方案1：

# def init(obj, x, y, z):
#     obj.stu_name = x
#     obj.stu_age = y
#     obj.stu_gender = z
#
# init(stu1_obj, 'egon', 18, 'male')
# init(stu2_obj, 'tom', 19, 'male')
# init(stu3_obj, 'lili', 21, 'female')
#
# print(stu1_obj.__dict__)  # {'stu_name': 'egon', 'stu_age': 18, 'stu_gender': 'male'}


# ====================================================================
# 解决方案2：
# 一、先定义类


class Student:
    # 1、变量的定义
    stu_school = 'oldboy'

    # 空对象,'egon',18,'male'
    def __init__(obj, x, y, z):
        obj.stu_name = x  # 空对象.stu_name = 'egon
        obj.stu_age = y  # 空对象.stu_age = 18
        obj.stu_gender = z  # 空对象.stu_gender = 'male'
        print('==================>1')

    # 2、功能的定义
    def tell_stu_info(stu_obj):
        print(
            f"学生姓名:{stu_obj['stu_name']}, 年龄{stu_obj['stu_age']}, 性别{stu_obj['stu_gender']}"
        )

    def set_info(stu_obj, x, y, z):
        stu_obj['stu_name'] = x
        stu_obj['stu_age'] = y
        stu_obj['stu_gender'] = z


# 二、再调用类产生的对象
# 调用类的过程又称之为实例化，发生了三件事：
# 1.先产生一个空对象
# 2、python会自动调用类中的__init__方法，
#       然后将空对象以及调用类时括号内传入的参数一同传给ini方法
# 3、返回初始化好的对象
stu1_obj = Student('egon', 18, 'male')  # Student.__init__(空对象, x, y, z)
stu2_obj = Student('tom', 19, 'male')
stu3_obj = Student('lili', 21, 'female')

# print(stu1_obj.__dict__)
# print(stu2_obj.__dict__)
# print(stu3_obj.__dict__)
'''
{'stu_name': 'egon', 'stu_age': 18, 'stu_gender': 'male'}
{'stu_name': 'tom', 'stu_age': 19, 'stu_gender': 'male'}
{'stu_name': 'lili', 'stu_age': 21, 'stu_gender': 'female'}
'''
#
# print(stu1_obj.stu_name)
# print(stu1_obj.stu_school)
# print(Student.tell_stu_info)

# 总结__init__方法
# 1、会在调用类时自动触发执行，用来为对象初始化自己独有的数据
# 2、__init__内应该存放是为对象初始化属性的功能，但是可以存放任意代码
#       类调用时就立刻执行的代码都可以放到该方法内
# 3、__init__方法必须返回None



