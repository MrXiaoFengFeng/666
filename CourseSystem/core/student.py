"""
学生视图
"""
from lib import common
from interface import student_interface, common_interface



student_info = {
    'user': None,
}


# 学生注册
def register():
    while True:
        username = input('请输入学生注册的用户名：').strip()
        password = input('请输入学生注册的密码：').strip()
        re_password = input('请确认学生注册的密码：').strip()
        if password == re_password:
            flag, msg = student_interface.student_register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致，请重新输入！')



# 学生登录
def login():
    while True:
        username = input('请输入学生登录的用户名：').strip()
        password = input('请输入学生登录的密码：').strip()
        flag, msg = common_interface.login_interface(
            username, password, user_type = 'student')
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要用global
            student_info['user'] = username
            print(student_info)
            break
        else:

            print(msg)



# 学生选择学校
@common.auth('student')
def choice_school():
    while True:
        # 1、获取所有学校，让学生选择
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print(f'编号：{index}  学校名：{school_name}')

        # 2、让学生输入学校编号
        choice = input('请输入选择的学校编号：').strip()
        if not choice.isdigit():
            print('输入有误！')
            continue
        choice = int(choice)

        if choice not in range(len(school_list)):
            print('输入的编号有误！')
            continue

        school_name = school_list[choice]

        # 3、开始调用学生选择学校接口
        flag, msg = student_interface.add_school_interface(
            school_name, student_info.get('user'))

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break




# 学生选择课程
@common.auth('student')
def choice_course():
    while True:
        # 1、先获取当前学生所在学校的课程列表
        flag, course_list = student_interface.get_course_list_interface(
            student_info.get('user')
        )
        if not flag:
            print(course_list)
            break
        # 2、打印课程列表，并让用户选择课程
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}  课程名称：{course_name}')

         # 让学生输入课程编号
        choice = input('请输入你选择的课程编号：').strip()
        if not choice.isdigit():
            print('输入有误！')
            continue
        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入的编号有误！')
            continue
        # 3、获取选择的课程名称
        course_name = course_list[choice]

        # 4、调用学生选择接口，选择课程
        flag, msg = student_interface.add_course_interface(
            course_name, student_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)





    # 2、打印课程列表,并让用户选择课程

# 学生查看分数
@common.auth('student')
def check_score():
    # 1、直接调用查看学生查看分数接口
    score_dict = student_interface.check_score_interface(
        student_info.get('user')
    )
    if not score_dict:
        print('没有选择课程')
    else:
        print(score_dict)

func_dic = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}


def student_view():
    while True:
        print("""
        ============学生============
        - 1.注册
        - 2.登录
        - 3.选择学校
        - 4.选择课程
        - 5.查看分数
        """)
        choice = input('请输入你的选择编号（输入"q/Q":退出）：').strip()
        if choice == 'q' or choice == 'Q':
            break
        if choice not in func_dic:
            print('你输出的编号不存在，请重新输入')
            continue
        func_dic.get(choice)()
