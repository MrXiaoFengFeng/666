"""
管理员视图
"""
from interface import admin_interface, common_interface
from lib import common

admin_info = {
    'user': None,
}


# 管理员注册
def register():
    while True:
        username = input('请输入管理员注册的用户名：').strip()
        password = input('请输入管理员注册的密码：').strip()
        re_password = input('请确认管理员注册的密码：').strip()
        if password == re_password:
            flag, msg = admin_interface.admin_register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致，请重新输入！')


# 管理员登录
def login():
    while True:
        username = input('请输入登录的用户名：').strip()
        password = input('请输入登录的密码：').strip()
        flag, msg = common_interface.login_interface(
            username, password, user_type = 'admin')
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要用global
            admin_info['user'] = username
            print(admin_info)
            break
        else:

            print(msg)


# 管理员创建学校
@common.auth('admin')
def create_school():
    while True:
        # 1、让用户输入学校的名称与地址
        school_name = input('请输入创建的学校名称：').strip()
        school_addr = input('请输入创建的学校地址：').strip()

        # 2、调用接口，保存学校
        flag, msg = admin_interface.create_school_interface(
            school_name, school_addr, admin_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建课程
@common.auth('admin')
def create_course():
    while True:
        # 1、让管理员先选择学校
        # 1.1、调用接口获取所有学校的名称并打印
        flag, school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break

        for index, school_name in enumerate(school_list_or_msg):
            print(f'编号：{index}  学校名：{school_name}')

        choice = input('请输入学校编号：').strip()
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print('请输入正确的数字编号！')
            continue

        # 获取选择后的学校名字
        school_name = school_list_or_msg[choice]

        # 2、选择学校后，再输入课程名称
        course_name = input('请输入需要创建的课程名称：').strip()

        flag, msg = admin_interface.create_course_interface(
            school_name, course_name, admin_info.get('user')
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建老师
@common.auth('admin')
def create_teacher():
    while True:
        # 1、让管理员输入创建老师的名字
        teacher_name = input('请输入老师的名字：').strip()
        # 2、调用接口创建老师
        flag, msg = admin_interface.create_teacher_interface(
            teacher_name, admin_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print("""
        ============管理员============
        - 1.注册
        - 2.登录
        - 3.创建学校
        - 4.创建课程
        - 5.创建老师
        """)
        choice = input('请输入你管理员的选择编号（输入"q/Q":退出）：').strip()
        if choice == 'q' or choice == 'Q':
            break
        if choice not in func_dic:
            print('你输出的编号不存在，请重新输入')
            continue
        func_dic.get(choice)()
