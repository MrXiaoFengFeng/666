"""
老师视图
"""
from lib import common
from interface import common_interface, teacher_interface

teacher_info = {
    'user': None,
}


# 老师登录
def login():
    while True:
        username = input('请输入登录的用户名：').strip()
        password = input('请输入登录的密码：').strip()
        flag, msg = common_interface.login_interface(
            username, password, user_type='teacher')
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要用global
            teacher_info['user'] = username
            print(teacher_info)
            break
        else:

            print(msg)


# #查看授课课程
@common.auth('teacher')
def check_course():
    flag, course_list = teacher_interface.check_course_interface(
        teacher_info.get('user')
    )
    if flag:
        print(course_list)
    else:
        print(course_list)


# 选择授课课程
@common.auth('teacher')
def choose_course():
    while True:
        # 1、先打印所有学校，并选择
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
        # 获取选择的学校名称
        school_name = school_list[choice]

        # 2、从选择的学校中，获取所有的课程
        flag2, course_list = common_interface.get_course_in_school_inerface(
            school_name
        )

        if not flag2:
            print(course_list)
            break


        for index2, course_name in enumerate(course_list):
            print(f'编号：{index2}  课程名：{course_name}')

        # 让老师输入学校编号
        choice2 = input('请输入选择的课程编号：').strip()
        if not choice2.isdigit():
            print('输入有误！')
            continue
        choice2 = int(choice2)

        if choice2 not in range(len(course_list)):
            print('输入的编号有误！')
            continue
        # 获取选择的课程名称
        course_name = course_list[choice2]

        # 调用选择教授课程接口，将该课程添加到老师选择课程列表中
        flag3, msg = teacher_interface.add_course_interface(
            course_name, teacher_info.get('user')
        )
        if flag3:
            print(msg)
            break
        else:
            print(msg)




# 查看课程下学生
@common.auth('teacher')
def check_stu_from_course():
    while True:
        # 1、获取当前老师下所有的课程接口
        flag, course_list = teacher_interface.check_course_interface(
            teacher_info.get('user')
        )
        if not flag:
            print(course_list)
            break

        # 2、打印所有课程，并让老师选择
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}  课程名：{course_name}')

        # 让老师输入学校编号
        choice = input('请输入选择的课程编号：').strip()
        if not choice.isdigit():
            print('输入有误！')
            continue
        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入的编号有误！')
            continue
        # 3、获取选择的课程名称
        course_name = course_list[choice]

        # 4、利用当前课程获取所有学生
        flag2, student_list = teacher_interface.get_student_interface(
            course_name, teacher_info.get('user')
        )
        if flag2:
            print(student_list)
            break
        else:
            print(student_list)
            break




# 修改学生分数
@common.auth('teacher')
def change_score_from_student():
    """
    # 1、先获取老师下所有的课程，并选择
    # 2、获取选择的课程下所有的学生，并选择修改的学生
    # 3、调用修改学生分数接口修改分数
    """
    while True:
        # 1、获取当前老师下所有的课程接口
        flag, course_list = teacher_interface.check_course_interface(
            teacher_info.get('user')
        )
        if not flag:
            print(course_list)
            break

        # 2、打印所有课程，并让老师选择
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}  课程名：{course_name}')

        # 让老师输入学校编号
        choice = input('请输入选择的课程编号：').strip()
        if not choice.isdigit():
            print('输入有误！')
            continue
        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入的编号有误！')
            continue
        # 3、获取选择的课程名称
        course_name = course_list[choice]

        # 4、利用当前课程获取所有学生
        flag2, student_list = teacher_interface.get_student_interface(
            course_name, teacher_info.get('user')
        )

        if not flag2:
            print(student_list)
            break

        # 5、打印所有学生让老师选择
        for index2, student_name in enumerate(student_list):
            print(f'学生编号：{index2}  学生姓名：{student_name}')

        choice2 = input('请输入选择的课程编号：').strip()
        if not choice2.isdigit():
            print('输入有误！')
            continue
        choice2 = int(choice2)

        if choice2 not in range(len(student_list)):
            print('输入的编号有误！')
            continue
        # 获取选择的课程名称
        student_name = student_list[choice2]

        # 老师输入需要修改的分数
        score = input('请输入需要修改的成绩：').strip()
        if not score.isdigit():
            print('请输入数字！')
            continue
        score = int(score)

        # 5、调用修改学生分数接口，修改分数
        flag3, msg = teacher_interface.change_score_interface(
            course_name, student_name, score, teacher_info.get('user')
        )

        if flag3:
            print(msg)
            break






func_dic = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_student,
}


def teacher_view():
    while True:
        print("""
        ============老师============
        - 1、登录
        - 2、查看授课课程
        - 3、选择授课课程
        - 4、查看课程下学生
        - 5、修改学生分数
        """)
        choice = input('请输入你的选择编号（输入"q/Q":退出）：').strip()
        if choice == 'q' or choice == 'Q':
            break
        if choice not in func_dic:
            print('你输出的编号不存在，请重新输入')
            continue
        func_dic.get(choice)()
